// Procedural variants after Adolph Gottlieb, "Under and Over".
// renderGottlieb(canvas, seed, knobs) draws a 1:2 portrait at canvas.width x canvas.height.
// knobs (optional) overrides any of renderGottlieb.KNOBS by key; all random draws still happen in the same
// order, so changing one knob leaves the rest of the seed's painting where it was.
(function (global) {
  "use strict";

  // Scratch canvases are reused across renders (renders never overlap): making fresh ones on every render churns
  // canvas memory, which iOS Safari caps and only gives back on garbage collection. Setting the size clears and resets.
  const scratch = {};
  function scratchCanvas(name, w, h) {
    const c = scratch[name] || (scratch[name] = document.createElement("canvas"));
    c.width = w; c.height = h;
    return c;
  }

  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function makeNoise(rand) {
    const N = 256, g = new Float32Array(N * N);
    for (let i = 0; i < g.length; i++) g[i] = rand();
    const s = (t) => t * t * (3 - 2 * t);
    return function (x, y) {
      const xi = Math.floor(x), yi = Math.floor(y);
      const u = s(x - xi), v = s(y - yi);
      const at = (i, j) => g[(i & 255) * N + (j & 255)];
      const a = at(xi, yi), b = at(xi + 1, yi), c = at(xi, yi + 1), d = at(xi + 1, yi + 1);
      return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
    };
  }

  // Explorable parameters. [min, max] is the slider range; [vmin, vmax] the range the variants actually use
  // (vmin === vmax: the variants never touch it). Units: W/H fractions or plain multipliers.
  const KNOBS = [
    { key: "sunY", group: "over", label: "Height of the sun", min: 0.08, max: 0.5, vmin: 0.235, vmax: 0.252, flip: true },
    { key: "haloR", group: "over", label: "Halo size", min: 0.12, max: 0.5, vmin: 0.333, vmax: 0.358 },
    { key: "sunR", group: "over", label: "Sun size", min: 0.05, max: 0.5, vmin: 0.25, vmax: 0.268 },
    { key: "sunDx", group: "over", label: "Sun off-center", min: -0.2, max: 0.2, vmin: -0.005, vmax: 0.015 },
    { key: "haloAsp", group: "over", label: "Halo shape", min: 0.6, max: 1.2, vmin: 0.86, vmax: 0.92 },
    { key: "warmth", group: "over", label: "Halo warmth", min: 0, max: 1.6, vmin: 0.25, vmax: 1 },
    { key: "blobUp", group: "under", label: "Height of the mass", min: -0.1, max: 0.4, vmin: 0, vmax: 0 },
    { key: "blobW", group: "under", label: "Width", min: 0.35, max: 1.3, vmin: 1, vmax: 1 },
    { key: "blobH", group: "under", label: "Depth", min: 0.3, max: 1.8, vmin: 1, vmax: 1 },
    { key: "towers", group: "under", label: "Tower height", min: 0, max: 3, vmin: 1, vmax: 1 },
    { key: "rag", group: "under", label: "Raggedness", min: 0, max: 3, vmin: 1, vmax: 1 },
    { key: "blobV", group: "under", label: "Lightness", min: 0.5, max: 3.5, vmin: 0.94, vmax: 1.06 },
    { key: "groundV", group: "ground", label: "Lightness of the ground", min: 0.35, max: 2.4, vmin: 0.96, vmax: 1.04 },
  ];

  function renderGottlieb(canvas, seed, knobs) {
    const K = knobs || {};
    const kv = (key, own) => (K[key] != null ? K[key] : own);
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const S = W / 600; // all hand-tuned sizes assume W = 600
    const rand = mulberry32(seed >>> 0);
    const noise = makeNoise(rand);
    const R = (a, b) => a + (b - a) * rand();
    const J = (c, j) => c.map((v) => v + (rand() - 0.5) * 2 * j);
    const L = (c, j) => { const k = 1 + (rand() - 0.5) * 2 * j; return c.map((v) => v * k); }; // luminance-only jitter
    const rgba = (c, a) => `rgba(${c[0] | 0},${c[1] | 0},${c[2] | 0},${a})`;
    const mix = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
    const fbm = (x, y) => 0.55 * noise(x, y) + 0.3 * noise(x * 2.1 + 17, y * 2.1) + 0.15 * noise(x * 4.3, y * 4.3 + 9);

    // ---- primitives -------------------------------------------------------

    // Fill a path with a blurred edge, via the off-canvas shadow trick (works everywhere).
    function softFill(pathFn, color, blur) {
      const off = 4 * W;
      ctx.save();
      ctx.shadowColor = color;
      ctx.shadowBlur = blur * S;
      shadowShift(off);
      ctx.translate(-off, 0);
      ctx.fillStyle = "#000";
      ctx.beginPath(); pathFn(); ctx.fill();
      ctx.restore();
    }

    // Shadows are offset in device pixels, so match the current transform's scale.
    function shadowShift(off) { const t = ctx.getTransform(); ctx.shadowOffsetX = off * t.a; ctx.shadowOffsetY = off * t.b; }

    // Closed wobbly ellipse.
    function wobblyEllipse(cx, cy, rx, ry, amp, freq, phase, rot) {
      const cr = Math.cos(rot || 0), sr = Math.sin(rot || 0);
      return function () {
        const n = 90;
        for (let i = 0; i <= n; i++) {
          const th = (i / n) * Math.PI * 2;
          const k = 1 + amp * (noise(phase + Math.cos(th) * freq, phase + Math.sin(th) * freq) - 0.5) * 2;
          const ex = Math.cos(th) * rx * k, ey = Math.sin(th) * ry * k;
          const x = cx + ex * cr - ey * sr, y = cy + ex * sr + ey * cr;
          i ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
        }
        ctx.closePath();
      };
    }

    // Random-walk path.
    function walk(x, y, ang, len, curl, steps) {
      steps = steps || Math.max(6, Math.round(len / (4 * S)));
      const pts = [[x, y]], step = len / steps;
      for (let i = 0; i < steps; i++) {
        ang += (rand() - 0.5) * curl;
        x += Math.cos(ang) * step; y += Math.sin(ang) * step;
        pts.push([x, y]);
      }
      return pts;
    }

    // Dry-brush stroke: many bristles, each dropping out where paint runs thin.
    function dryStroke(pts, o) {
      const width = o.width, K = Math.max(3, Math.min(60, Math.round(width / (1.2 * S))));
      const n = pts.length;
      const norms = pts.map((p, i) => {
        const a = pts[Math.max(0, i - 1)], b = pts[Math.min(n - 1, i + 1)];
        const dx = b[0] - a[0], dy = b[1] - a[1], l = Math.hypot(dx, dy) || 1;
        return [-dy / l, dx / l];
      });
      const taperIn = o.taperIn == null ? 0.15 : o.taperIn;
      const taperOut = o.taperOut == null ? 0.3 : o.taperOut;
      ctx.lineCap = "round";
      for (let k = 0; k < K; k++) {
        const off = (K === 1 ? 0 : k / (K - 1) - 0.5) + (rand() - 0.5) * 0.6 / K;
        const edge = Math.abs(off) * 2;
        const ph = rand() * 200;
        ctx.strokeStyle = rgba(J(o.color, o.jit || 6), o.alpha * R(0.55, 1.1));
        ctx.lineWidth = Math.max(0.6 * S, (width / K) * R(1.3, 1.9));
        ctx.beginPath();
        let pen = false;
        for (let i = 0; i < n; i++) {
          const t = i / (n - 1);
          let prof = 1;
          if (t < taperIn) prof = Math.sqrt(t / taperIn);
          if (t > 1 - taperOut) prof = Math.min(prof, Math.sqrt((1 - t) / taperOut));
          if (edge > prof + 0.02) { pen = false; continue; }
          const load = 1 - (o.dry || 0) * t;
          const thresh = (o.cover == null ? 0.9 : o.cover) * load - 0.35 * edge * edge;
          const on = noise(ph + i * (o.grain || 0.4), k * 1.7) < thresh;
          const x = pts[i][0] + norms[i][0] * off * width, y = pts[i][1] + norms[i][1] * off * width;
          if (on) { pen ? ctx.lineTo(x, y) : ctx.moveTo(x, y); pen = true; }
          else pen = false;
        }
        ctx.stroke();
      }
    }

    // Ribbon: a solid soft-edged band along a path whose width wobbles and frays toward the end.
    function ribbon(pts, width, color, blur) {
      const n = pts.length, ph = rand() * 99, L = [], Rr = [];
      for (let i = 0; i < n; i++) {
        const a = pts[Math.max(0, i - 1)], b = pts[Math.min(n - 1, i + 1)];
        const dx = b[0] - a[0], dy = b[1] - a[1], l = Math.hypot(dx, dy) || 1, nx = -dy / l, ny = dx / l;
        const t = i / (n - 1), end = t > 0.7 ? 1 - (t - 0.7) / 0.3 * 0.6 : 1;
        const wl = width / 2 * end * (0.75 + 0.5 * noise(ph + i * 0.5, 1)), wr = width / 2 * end * (0.75 + 0.5 * noise(ph + i * 0.5, 7));
        L.push([pts[i][0] + nx * wl, pts[i][1] + ny * wl]); Rr.push([pts[i][0] - nx * wr, pts[i][1] - ny * wr]);
      }
      softFill(() => {
        L.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1])));
        for (let i = n - 1; i >= 0; i--) ctx.lineTo(Rr[i][0], Rr[i][1]);
        ctx.closePath();
      }, color, blur);
    }

    // ---- parameters (tight jitter around the original) ---------------------
    const P = {
      ground: J([80, 56, 41], 3), // between the three scans' consensus and the primary crop
      hx: W * R(0.495, 0.53), hy: H * R(0.235, 0.252),
      hr: W * R(0.333, 0.358), hAsp: R(0.86, 0.92),
      hSq: R(0, 0.015), hSqTop: R(0.01, 0.03), // squarer shoulders, mostly at the top (as in the scans)
      redDx: W * R(-0.005, 0.015), redDy: W * R(-0.015, 0.005), // scans: sun nearly concentric, a hair high
      redR: W * R(0.25, 0.268), redAsp: R(0.9, 0.97),
      redAng: R(-1.15, -0.55), // direction of scumbled red strokes
      redLight: [R(-0.4, 0.4), R(-0.4, 0.4)], // where the red is brightest (fraction of radius)
      ghostAng: R(-0.6, 0.6) + (rand() < 0.5 ? Math.PI : 0), // side where the crescent shows a doubled edge
      pale: J([188, 130, 100], 5),
      cream: J([232, 208, 180], 5), // the luminous highlight seen in person
      // lit photos (installation shots, catalogue cover) show the brightest strokes going buttery yellow; how far varies per seed
      butter: J([248, 210, 150], 5), warmth: R(0.25, 1),
      glowAng: R(0, Math.PI * 2), // side of the ring that glows brightest
      edgeGlow: Math.PI * R(0.72, 1.05), // lower-left/left: where the ring's outer edge bleeds softly into the ground
      red: J([110, 32, 25], 4),
      blob: L([34, 25, 20], 0.06), // neutral, a little cooler than the ground
    };
    const own = { sunY: P.hy / H, haloR: P.hr / W, sunR: P.redR / W, sunDx: P.redDx / W, haloAsp: P.hAsp, warmth: P.warmth,
      blobUp: 0, blobW: 1, blobH: 1, towers: 1, rag: 1, blobV: 1, groundV: 1 };
    P.hy = kv("sunY", own.sunY) * H; P.hr = kv("haloR", own.haloR) * W; P.redR = kv("sunR", own.sunR) * W;
    P.redDx = kv("sunDx", own.sunDx) * W; P.hAsp = kv("haloAsp", own.haloAsp); P.warmth = kv("warmth", own.warmth);
    const gk = kv("groundV", 1), bk = kv("blobV", 1), rag = kv("rag", 1);
    P.ground = P.ground.map((v) => v * gk); P.blob = P.blob.map((v) => v * bk);
    const OLIVE = [72, 66, 56].map((v) => v * gk);

    // ---- ground ------------------------------------------------------------
    const g0 = P.ground;
    ctx.fillStyle = rgba(g0, 1);
    ctx.fillRect(0, 0, W, H);
    let gr = ctx.createLinearGradient(0, 0, 0, H);
    gr.addColorStop(0, rgba([g0[0] - 3, g0[1] - 1, g0[2] + 2], 0.5));
    gr.addColorStop(0.5, rgba(g0, 0));
    gr.addColorStop(1, rgba([g0[0] * 0.82, g0[1] * 0.82, g0[2] * 0.8], 0.9)); // scans: ground darkens toward the foot
    ctx.fillStyle = gr; ctx.fillRect(0, 0, W, H);
    // vertical brushing in the ground
    for (let i = 0; i < 260; i++) {
      const x = R(-0.05, 1.05) * W, y = R(-0.2, 1) * H;
      dryStroke(walk(x, y, Math.PI / 2 + R(-0.08, 0.08), R(0.1, 0.45) * H, 0.05), {
        // about a third of the ground strokes are a cool grey-olive (the in-person colour), the rest warm
        width: R(8, 40) * S, color: rand() < 0.35 ? J(OLIVE, 5) : J(g0, 9), alpha: R(0.04, 0.1), jit: 5, cover: 0.75, dry: 0.5, grain: 0.15,
      });
    }
    // ---- the pale crescent (halo) --------------------------------------------
    // Layering, as painted: cream ring first, then the ground brushed back over its outer edge
    // (so the brown defines the boundary and bites in), then the red over its inner edge.
    const hrx = P.hr, hry = P.hr * P.hAsp, hph = R(0, 50);
    const haloK = (th) => 1 + 0.03 * (noise(hph + Math.cos(th) * 1.8, hph + Math.sin(th) * 1.8) - 0.5) * 2
      + (P.hSq + P.hSqTop * Math.max(0, -Math.sin(th))) * (1 - Math.cos(4 * th)) / 2;
    const haloPt = (th, f) => { const k = haloK(th) * f; return [P.hx + Math.cos(th) * hrx * k, P.hy + Math.sin(th) * hry * k]; };
    const haloPath = (f) => () => {
      for (let i = 0; i <= 120; i++) { const p = haloPt((i / 120) * Math.PI * 2, f); i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]); }
      ctx.closePath();
    };
    const halo = haloPath(1);
    // snapshot of the bare ground, to sample local colour for the overpainting strokes
    const gH = Math.ceil(H * 0.6), gImg = ctx.getImageData(0, 0, W, gH).data;
    const groundAt = (x, y) => {
      const c = [0, 0, 0];
      for (const [dx, dy] of [[-4, -4], [4, -4], [-4, 4], [4, 4], [0, 0]]) {
        const xi = Math.min(W - 1, Math.max(0, Math.round(x + dx * S))), yi = Math.min(gH - 1, Math.max(0, Math.round(y + dy * S)));
        const k = (yi * W + xi) * 4; c[0] += gImg[k] / 5; c[1] += gImg[k + 1] / 5; c[2] += gImg[k + 2] / 5;
      }
      return c;
    };
    const glowW = (th) => Math.pow(0.5 + 0.5 * Math.cos(th - P.edgeGlow), 2); // 1 on the glowing side, 0 opposite
    // a soft warm glow just outside the ring, mostly on one side (seen in the scans and in person)
    {
      const gc = scratchCanvas("glow", W, gH);
      const g = gc.getContext("2d");
      g.translate(P.hx, P.hy); g.scale(1, hry / hrx);
      let rg = g.createRadialGradient(0, 0, hrx * 0.96, 0, 0, hrx * 1.13);
      rg.addColorStop(0, "rgba(176,122,72,0.6)"); rg.addColorStop(0.35, "rgba(150,100,60,0.3)"); rg.addColorStop(1, "rgba(130,85,52,0)");
      g.fillStyle = rg; g.fillRect(-hrx * 1.3, -hrx * 1.3, hrx * 2.6, hrx * 2.6);
      g.setTransform(1, 0, 0, 1, 0, 0);
      g.globalCompositeOperation = "destination-in";
      const dx = Math.cos(P.edgeGlow) * hrx, dy = Math.sin(P.edgeGlow) * hry;
      rg = g.createLinearGradient(P.hx - dx, P.hy - dy, P.hx + dx, P.hy + dy);
      rg.addColorStop(0, "rgba(0,0,0,0.12)"); rg.addColorStop(0.55, "rgba(0,0,0,0.35)"); rg.addColorStop(1, "rgba(0,0,0,1)");
      g.fillStyle = rg; g.fillRect(0, 0, W, gH);
      ctx.save(); ctx.globalAlpha = R(0.6, 0.85); ctx.drawImage(gc, 0, 0); ctx.restore();
    }
    softFill(halo, rgba(P.pale, 0.92), 3);
    ctx.save();
    ctx.beginPath(); halo(); ctx.clip();
    // tangential strokes give the ring its brushed texture
    for (let i = 0; i < 700; i++) {
      const th = R(0, Math.PI * 2), rr = Math.sqrt(R(0.3, 1.0));
      const x = P.hx + Math.cos(th) * hrx * rr, y = P.hy + Math.sin(th) * hry * rr;
      const dir = th + Math.PI / 2 + R(-0.25, 0.25);
      const tone = R(0, 1);
      const c = [P.pale[0] + 20 - tone * 44, P.pale[1] + 18 - tone * 44, P.pale[2] + 14 - tone * 42];
      dryStroke(walk(x, y, dir, R(15, 60) * S, 0.15), {
        width: R(3, 10) * S, color: c, alpha: R(0.07, 0.18), cover: 0.8, dry: 0.4, grain: 0.5,
      });
    }
    // luminous cream band through the middle of the ring, brightest toward glowAng
    ctx.save();
    ctx.translate(P.hx, P.hy); ctx.scale(1, hry / hrx);
    gr = ctx.createRadialGradient(0, 0, hrx * 0.72, 0, 0, hrx * 1.02);
    const band = mix(P.cream, P.butter, 0.45 * P.warmth); // warmer seeds lean buttery, cooler ones stay pink-cream
    gr.addColorStop(0, rgba(band, 0));
    gr.addColorStop(0.55, rgba(band, 0.5));
    gr.addColorStop(0.85, rgba(band, 0.28));
    gr.addColorStop(1, rgba(band, 0.1));
    ctx.fillStyle = gr; ctx.fillRect(-hrx * 1.1, -hrx * 1.1, 2.2 * hrx, 2.2 * hrx);
    ctx.restore();
    for (let i = 0; i < 450; i++) {
      const th = R(0, Math.PI * 2), lit = 0.5 + 0.5 * Math.cos(th - P.glowAng);
      if (rand() > 0.25 + 0.75 * lit) continue;
      const rr = R(0.76, 0.95);
      const x = P.hx + Math.cos(th) * hrx * rr, y = P.hy + Math.sin(th) * hry * rr;
      dryStroke(walk(x, y, th + Math.PI / 2 + R(-0.15, 0.15), R(20, 70) * S, 0.1), {
        width: R(4, 12) * S, color: J(mix(P.cream, P.butter, rand() * P.warmth), 8), alpha: R(0.06, 0.2) * (0.5 + 0.5 * lit), cover: 0.85, dry: 0.4, grain: 0.45,
      });
    }
    // a few loaded highlight strokes on the lit side, and a peach/orange zone toward the red (both seen in lit photos)
    for (let i = 0; i < 260; i++) {
      const th = R(0, Math.PI * 2), lit = 0.5 + 0.5 * Math.cos(th - P.glowAng), hi = rand() < 0.6;
      if (hi && rand() > lit * lit) continue;
      const rr = hi ? R(0.8, 0.94) : R(0.7, 0.8);
      const x = P.hx + Math.cos(th) * hrx * rr, y = P.hy + Math.sin(th) * hry * rr;
      dryStroke(walk(x, y, th + Math.PI / 2 + R(-0.12, 0.12), R(18, 55) * S, 0.1), {
        width: R(3, 9) * S, color: hi ? J(mix(P.cream, P.butter, 0.4 + 0.6 * P.warmth), 6) : J([212, 132, 88], 8),
        alpha: hi ? R(0.22, 0.5) : R(0.08, 0.2), cover: 0.85, dry: 0.45, grain: 0.45,
      });
    }
    // warm tan where the ring meets the ground (stronger on the glowing side)
    gr = ctx.createRadialGradient(P.hx, P.hy, hrx * 0.88, P.hx, P.hy, hrx * 1.04);
    gr.addColorStop(0, "rgba(190,120,75,0)");
    gr.addColorStop(1, "rgba(175,110,65,0.22)");
    ctx.fillStyle = gr; ctx.fillRect(0, 0, W, H * 0.6);
    ctx.restore();
    // ghost edge: a sliver of cream left showing just outside the edge on one side
    {
      const ghostSpan = R(0.5, 1.0), gk = R(1.01, 1.025), pts = [];
      for (let i = 0; i <= 30; i++) pts.push(haloPt(P.ghostAng - ghostSpan / 2 + (ghostSpan * i) / 30, gk));
      dryStroke(pts, { width: R(2, 3.5) * S, color: [200, 158, 122], alpha: R(0.35, 0.55), jit: 6, cover: 0.7, dry: 0.3, grain: 0.35, taperIn: 0.25, taperOut: 0.25 });
    }
    // the ground brushed back over the ring: tangential bands that start outside and bite inward
    for (let i = 0; i < 80; i++) {
      const th = R(0, Math.PI * 2), span = R(0.12, 0.38), w = R(9, 22) * S, gl = glowW(th);
      const bite = R(-1, 6) * S * (1 - 0.7 * gl), dirn = rand() < 0.5 ? 1 : -1, drift = R(-2, 8) * S, pts = [];
      for (let j = 0; j <= 30; j++) {
        const u = j / 30, t = th + dirn * span * (u - 0.5), p = haloPt(t, 1);
        const nx = Math.cos(t) * hry, ny = Math.sin(t) * hrx, nl = Math.hypot(nx, ny); // outward normal of the ellipse
        const off = w / 2 - bite + drift * u * u; // the stroke lifts off (or digs into) the edge as it ends
        pts.push([p[0] + (nx / nl) * off, p[1] + (ny / nl) * off]);
      }
      const m = pts[15], nx = m[0] - P.hx, ny = m[1] - P.hy, nl = Math.hypot(nx, ny);
      let c = groundAt(m[0] + (nx / nl) * (w * 0.8 + 6 * S), m[1] + (ny / nl) * (w * 0.8 + 6 * S));
      if (rand() < 0.3) c = c.map((v, k) => v * 0.65 + OLIVE[k] * 0.35); // some grey-olive
      ribbon(pts, w, rgba(L(c, 0.03), R(0.6, 0.92) * (1 - 0.55 * gl)), R(2, 3.5));
    }
    // dry-brush hairlines of ground colour dragged into the cream just inside the edge
    for (let i = 0; i < 24; i++) {
      const th = R(0, Math.PI * 2), span = R(0.1, 0.3), f = R(0.95, 0.99), pts = [];
      for (let j = 0; j <= 14; j++) pts.push(haloPt(th + span * (j / 14 - 0.5), f + R(-0.002, 0.002)));
      const p = haloPt(th, 1.12), c = groundAt(p[0], p[1]);
      dryStroke(pts, { width: R(2, 6) * S, color: c, alpha: R(0.1, 0.25) * (1 - 0.5 * glowW(th)), jit: 4, cover: 0.6, dry: 0.5, grain: 0.5 });
    }

    // ---- the red sun -----------------------------------------------------------
    const rx = P.hx + P.redDx, ry = P.hy + P.redDy, rrx = P.redR, rry = P.redR * P.redAsp;
    const redShape = wobblyEllipse(rx, ry, rrx, rry, 0.02, 1.1, R(0, 50));
    softFill(wobblyEllipse(rx, ry, rrx * 1.05, rry * 1.05, 0.03, 1.1, R(0, 50)), "rgba(205,135,105,0.4)", 14); // soft cream-to-red fringe
    softFill(redShape, rgba(P.red, 1), 24); // wide feather into the ring (scans: ~0.05 W from red to cream)
    softFill(wobblyEllipse(rx, ry, rrx * 0.9, rry * 0.9, 0.03, 1.1, 7), rgba(P.red, 0.8), 12);
    ctx.save();
    ctx.beginPath(); wobblyEllipse(rx, ry, rrx * 0.97, rry * 0.97, 0.02, 1.1, 3)(); ctx.clip();
    gr = ctx.createRadialGradient(rx + P.redLight[0] * rrx, ry + P.redLight[1] * rry, 0, rx, ry, rrx * 1.05);
    gr.addColorStop(0, rgba([P.red[0] + 18, P.red[1] + 4, P.red[2] + 2], 0.5));
    gr.addColorStop(0.6, rgba(P.red, 0));
    gr.addColorStop(0.75, rgba([P.red[0] - 20, P.red[1] - 8, P.red[2] - 4], 0.2)); // only a faint darkening: the scans show no dark rim
    gr.addColorStop(0.92, rgba([P.red[0] - 20, P.red[1] - 8, P.red[2] - 4], 0)); // fades out before the clip, so no hard edge
    ctx.fillStyle = gr; ctx.fillRect(rx - rrx * 1.2, ry - rry * 1.2, rrx * 2.4, rry * 2.4);
    // a few coral passages and dark blotches widen the red's range (seen in person)
    for (let i = 0; i < 24; i++) {
      const th = R(0, Math.PI * 2), rr = Math.sqrt(rand()) * 0.8, coral = rand() < 0.6;
      softFill(wobblyEllipse(rx + Math.cos(th) * rrx * rr, ry + Math.sin(th) * rry * rr, R(12, 40) * S, R(8, 22) * S, 0.4, 2, R(0, 50), P.redAng),
        coral ? rgba(rand() < 0.4 ? [165, 58, 46] : [196, 62, 40], R(0.1, 0.22)) : rgba([78, 18, 16], R(0.12, 0.25)), 10);
    }
    // mottled shading
    for (let i = 0; i < 45; i++) {
      const th = R(0, Math.PI * 2), rr = Math.sqrt(rand());
      const tone = R(-1, 1);
      softFill(wobblyEllipse(rx + Math.cos(th) * rrx * rr, ry + Math.sin(th) * rry * rr, R(10, 35) * S, R(8, 25) * S, 0.3, 2, R(0, 50), P.redAng),
        rgba([P.red[0] + tone * 25, P.red[1] + tone * 6, P.red[2] + tone * 4], 0.18), 12);
    }
    ctx.restore();
    for (let i = 0; i < 900; i++) {
      const th = R(0, Math.PI * 2), rr = Math.sqrt(rand()) * 0.95;
      const x = rx + Math.cos(th) * rrx * rr, y = ry + Math.sin(th) * rry * rr;
      const tone = R(-1, 1);
      // brights lean vermilion (lit photos), darks toward oxblood: a wider spread than the scan's flat red
      const c = tone > 0 ? [P.red[0] + tone * 62, P.red[1] + tone * 18, P.red[2] + tone * 10] : [P.red[0] + tone * 34, P.red[1] + tone * 10, P.red[2] + tone * 6];
      dryStroke(walk(x, y, P.redAng + R(-0.3, 0.3) + (rand() < 0.5 ? Math.PI : 0), R(12, 45) * S, 0.2), {
        width: R(2, 7) * S, color: c, alpha: R(0.05, 0.13) * (tone > 0 ? 1.6 : 1) * (1 - Math.pow(rr, 6)), cover: 0.75, dry: 0.5, grain: 0.6,
      });
    }

    // ---- the dark mass ("under") ---------------------------------------------
    // Knobs move/scale the whole mass with a canvas transform: width about the centre, depth about its foot.
    ctx.save();
    {
      const sx = kv("blobW", 1), sy = kv("blobH", 1), foot = 0.95 * H, up = kv("blobUp", 0) * H;
      ctx.translate(W / 2, foot - up); ctx.scale(sx, sy); ctx.translate(-W / 2, -foot);
    }
    // The silhouette is defined by four noisy profiles (top/bottom edge as a function of x,
    // left/right edge as a function of y), each built from a few named features.
    const B = P.blob;
    const bump = (d, hw, p) => Math.exp(-Math.pow(Math.abs(d / hw), p || 4));
    const wig = (ph, t, sc) => fbm(ph + t / sc, ph * 0.37) - 0.5;
    const ph = [R(0, 99), R(0, 99), R(0, 99), R(0, 99)];
    const tw = [
      { x: R(0.22, 0.32) * W, hw: R(0.11, 0.15) * W, top: R(0.565, 0.585) * H },
      { x: R(0.76, 0.83) * W, hw: R(0.07, 0.1) * W, top: R(0.585, 0.605) * H },
    ];
    if (rand() < 0.6) tw.push({ x: R(0.5, 0.62) * W, hw: R(0.03, 0.05) * W, top: R(0.615, 0.635) * H });
    const topBase = R(0.65, 0.675) * H; // the bay between the towers
    for (const t of tw) t.top = topBase - (topBase - t.top) * kv("towers", 1);
    const legs = [0, 1, 2].map(() => ({ x: R(0.15, 0.85) * W, hw: R(0.03, 0.07) * W, d: R(0.01, 0.035) * H }));
    const botBase = R(0.935, 0.955) * H; // scans: the mass reaches ~0.95-0.98 H
    const botRound = R(0.02, 0.05) * H, botMid = R(0.42, 0.52) * W;
    const leftBase = R(0.1, 0.14) * W, rightBase = R(0.86, 0.9) * W;
    const lw = [{ y: R(0.64, 0.72) * H, hh: R(0.03, 0.06) * H, d: R(0.05, 0.09) * W }, { y: R(0.77, 0.88) * H, hh: R(0.03, 0.05) * H, d: R(0.02, 0.06) * W }];
    const rw = [{ y: R(0.62, 0.7) * H, hh: R(0.03, 0.05) * H, d: R(0.01, 0.04) * W }];
    const notches = [{ side: 1, y: R(0.74, 0.82) * H, hh: R(0.012, 0.022) * H, d: R(0.05, 0.1) * W }];
    // flat-ended fingers: horizontal on the sides, vertical spikes on top
    const sideFingers = { "-1": [], "1": [] };
    for (const side of [-1, 1]) {
      const n = 3 + Math.floor(rand() * 3);
      for (let i = 0; i < n; i++) sideFingers[side].push({ y: R(0.6, 0.9) * H, hh: R(0.01, 0.025) * H, d: R(0.03, side < 0 ? 0.1 : 0.07) * W });
    }
    const spikes = [];
    for (let i = 0, n = 1 + Math.floor(rand() * 3); i < n; i++) spikes.push({ x: R(0.15, 0.88) * W, hw: R(0.012, 0.03) * W, d: R(0.015, 0.045) * H });
    if (rand() < 0.5) notches.push({ side: -1, y: R(0.84, 0.9) * H, hh: R(0.01, 0.02) * H, d: R(0.03, 0.06) * W });
    for (const f of [...legs, ...lw, ...rw, ...notches, ...sideFingers["-1"], ...sideFingers["1"], ...spikes]) f.d *= rag;

    const topY = (x) => {
      let y = topBase;
      for (const t of tw) y -= (topBase - t.top) * bump(x - t.x, t.hw);
      for (const k of spikes) y -= k.d * bump(x - k.x, k.hw, 2.5);
      return y + rag * (wig(ph[0], x, 0.12 * W) * 0.04 * H + wig(ph[0] + 5, x, 0.03 * W) * 0.012 * H);
    };
    const botY = (x) => {
      let y = botBase;
      for (const l of legs) y += l.d * bump(x - l.x, l.hw, 2);
      y -= botRound * Math.pow(Math.abs(x - botMid) / (0.42 * W), 4); // the foot rounds off toward the corners (scans)
      return y + rag * (wig(ph[1], x, 0.1 * W) * 0.04 * H + wig(ph[1] + 5, x, 0.03 * W) * 0.015 * H);
    };
    const sideX = (y, side) => {
      let x = side < 0 ? leftBase : rightBase;
      for (const w of side < 0 ? lw : rw) x += side * w.d * bump(y - w.y, w.hh, 2);
      for (const n of notches) if (n.side === side) x -= side * n.d * bump(y - n.y, n.hh, 2);
      for (const f of sideFingers[side]) x += side * f.d * bump(y - f.y, f.hh, 3);
      const q = ph[side < 0 ? 2 : 3];
      return x + rag * (wig(q, y, 0.07 * H) * 0.035 * W + wig(q + 5, y, 0.015 * H) * 0.015 * W);
    };
    const inside = (x, y) => y > topY(x) && y < botY(x) && x > sideX(y, -1) && x < sideX(y, 1);

    // rasterize the mask at low resolution; upscaling softens the edge
    const cell = 3 * S, mw = Math.ceil(W / cell), mh = Math.ceil(H / cell);
    const mask = scratchCanvas("mask", mw, mh);
    const mctx = mask.getContext("2d"), mimg = mctx.createImageData(mw, mh);
    const edges = [];
    const inGrid = new Uint8Array(mw * mh);
    for (let j = Math.floor(0.2 * mh); j < mh; j++) { // towers can be pulled up a long way
      for (let i = 0; i < mw; i++) {
        if (inside((i + 0.5) * cell, (j + 0.5) * cell)) inGrid[j * mw + i] = 1;
      }
    }
    for (let j = 1; j < mh - 1; j++) {
      for (let i = 1; i < mw - 1; i++) {
        const k = j * mw + i;
        if (!inGrid[k]) continue;
        mimg.data[k * 4] = B[0]; mimg.data[k * 4 + 1] = B[1]; mimg.data[k * 4 + 2] = B[2]; mimg.data[k * 4 + 3] = 255;
        const gx = inGrid[k + 1] - inGrid[k - 1], gy = inGrid[k + mw] - inGrid[k - mw];
        if (gx || gy) edges.push([(i + 0.5) * cell, (j + 0.5) * cell, gx, gy]);
      }
    }
    mctx.putImageData(mimg, 0, 0);

    // stain halo, then the solid mass
    const drawMask = (alpha, blur) => {
      const off = 4 * W;
      ctx.save();
      ctx.globalAlpha = alpha;
      ctx.shadowColor = "#000"; // shadow color alpha multiplies with the image alpha
      ctx.shadowColor = rgba(B, 1);
      ctx.shadowBlur = blur * S; shadowShift(off);
      ctx.imageSmoothingEnabled = true;
      ctx.drawImage(mask, -off, 0, W, H);
      ctx.restore();
    };
    drawMask(0.12, 30);
    drawMask(0.95, 5);

    // interior value variation: some denser, some thinner dabs
    const dab = (x, y, rx, ry, rot, a, blur, c) =>
      softFill(wobblyEllipse(x, y, rx, ry, 0.35, 1.6, R(0, 99), rot), rgba(c || L(B, 0.15), a), blur == null ? 4 : blur);
    const nearVert = () => Math.PI / 2 + R(-0.35, 0.35);
    const nearHorz = () => R(-0.3, 0.3);
    for (let i = 0; i < 70; i++) {
      const x = R(0.15, 0.85) * W, y = R(0.6, 0.93) * H;
      if (!inside(x, y)) continue;
      // thin passages only near the edge (and more often toward the top)
      const nearEdge = y - topY(x) < 0.05 * H || x - sideX(y, -1) < 0.06 * W || sideX(y, 1) - x < 0.06 * W;
      const thin = nearEdge && rand() < 0.8 - (y / H - 0.6) * 1.5;
      dab(x, y, R(0.04, 0.1) * W, R(0.02, 0.04) * W, rand() < 0.5 ? nearVert() : nearHorz(), thin ? R(0.1, 0.22) : R(0.25, 0.5), R(5, 12),
        thin ? [g0[0] - 10, g0[1] - 10, g0[2] - 8] : L([B[0] - 6, B[1] - 5, B[2] - 4], 0.1));
    }

    // ---- contrast within the mass: two blacks, streaks, a scraped highlight ----
    // (in person the blob ranges from near-black to a cool matte grey; the web scan flattens this)
    const DEEP = L([20, 14, 11], 0.08).map((v) => v * bk), MATTE = J([60, 53, 48], 3).map((v) => v * Math.sqrt(bk));
    const edgeDist = (x, y) => Math.min(y - topY(x), botY(x) - y, x - sideX(y, -1), sideX(y, 1) - x);
    // deep black: one continuous core, inset from the edge and starting below the towers
    {
      const dph = R(0, 99), deepTop = R(0.68, 0.72) * H;
      const deep = scratchCanvas("deep", mw, mh);
      const dctx = deep.getContext("2d"), dimg = dctx.createImageData(mw, mh);
      for (let j = Math.floor(0.6 * mh); j < mh; j++) {
        for (let i = 0; i < mw; i++) {
          const x = (i + 0.5) * cell, y = (j + 0.5) * cell;
          if (!inGrid[j * mw + i]) continue;
          const inset = (0.06 * fbm(dph + x / (0.08 * W), y / (0.08 * W)) - 0.015) * W; // can be <0: reaches the edge
          if (y < deepTop + wig(dph, x, 0.1 * W) * 0.1 * H + wig(dph + 3, x, 0.03 * W) * 0.05 * H || edgeDist(x, y) < inset) continue;
          const k = (j * mw + i) * 4;
          dimg.data[k] = DEEP[0]; dimg.data[k + 1] = DEEP[1]; dimg.data[k + 2] = DEEP[2]; dimg.data[k + 3] = 255;
        }
      }
      dctx.putImageData(dimg, 0, 0);
      const off = 4 * W;
      ctx.save();
      ctx.globalAlpha = R(0.7, 0.85);
      ctx.shadowColor = rgba(DEEP, 1); ctx.shadowBlur = 6 * S; shadowShift(off);
      ctx.drawImage(deep, -off, 0, W, H);
      ctx.restore();
      // black tongues pushing up into the grey, so the core's top isn't a seam
      for (let i = 0; i < 12; i++) {
        const x = R(0.18, 0.82) * W, y = deepTop + R(0.01, 0.05) * H;
        if (!inside(x, y)) continue;
        ribbon(walk(x, y, -Math.PI / 2 + R(-0.35, 0.35), R(0.04, 0.1) * H, 0.2), R(16, 34) * S, rgba(DEEP, R(0.45, 0.7)), 4);
      }
      // brushy deep strokes so the core's edge isn't a smooth contour
      for (let i = 0; i < 30; i++) {
        const x = R(0.2, 0.8) * W, y = R(deepTop, 0.92 * H);
        if (!inside(x, y) || edgeDist(x, y) < 0.03 * W) continue;
        ribbon(walk(x, y, nearVert() + (rand() < 0.5 ? Math.PI : 0), R(0.05, 0.12) * W, 0.15), R(14, 30) * S, rgba(DEEP, R(0.3, 0.55)), 4);
      }
    }
    // matte grey-black zones: gritty dry-brush where the canvas weave shows through
    const zones = [
      { x: tw[0].x + R(-0.3, 0.3) * tw[0].hw, y: tw[0].top + R(0.03, 0.06) * H, r: R(0.07, 0.11) * W },
      { x: tw[1].x, y: tw[1].top + R(0.04, 0.07) * H, r: R(0.06, 0.09) * W },
    ];
    if (rand() < 0.7) zones.push({ x: R(0.4, 0.6) * W, y: topBase + R(0.01, 0.04) * H, r: R(0.05, 0.08) * W });
    for (const z of zones) {
      ctx.save();
      ctx.beginPath(); // keep the grey inside the silhouette
      for (let i = 0; i <= 60; i++) { const x = z.x - 1.5 * z.r + (3 * z.r * i) / 60; i ? ctx.lineTo(x, topY(x) + 0.004 * H) : ctx.moveTo(x, topY(x) + 0.004 * H); }
      ctx.lineTo(z.x + 1.5 * z.r, H); ctx.lineTo(z.x - 1.5 * z.r, H); ctx.closePath(); ctx.clip();
      dab(z.x, z.y, z.r, z.r * 1.1, nearVert(), R(0.15, 0.25), 10, MATTE);
      for (let i = 0; i < 22; i++) {
        const x = z.x + R(-1, 1) * z.r, y = z.y + R(-1, 1) * z.r * 1.2;
        if (!inside(x, y)) continue;
        dryStroke(walk(x, y, nearVert() + (rand() < 0.5 ? Math.PI : 0), R(0.04, 0.1) * W, 0.2), {
          width: R(16, 36) * S, color: J(MATTE, 4), alpha: R(0.12, 0.24), jit: 5, cover: 0.85, dry: 0.6, grain: 0.6,
        });
      }
      ctx.restore();
    }
    // faint vertical streaks and drips through the core
    for (let i = 0; i < 26; i++) {
      const x = R(0.2, 0.8) * W, y = R(0.7, 0.9) * H;
      if (!inside(x, y)) continue;
      dryStroke(walk(x, y, Math.PI / 2 + R(-0.08, 0.08), R(0.04, 0.12) * H, 0.08), {
        width: R(4, 10) * S, color: MATTE, alpha: R(0.07, 0.14), cover: 0.8, dry: 0.5, grain: 0.4,
      });
    }
    // a pale scraped passage in the right-hand notch
    {
      const n = notches[0], x = sideX(n.y, 1) - R(0.01, 0.04) * W;
      const pts = walk(x, n.y + R(-0.005, 0.005) * H, Math.PI + R(-0.2, 0.2), R(0.05, 0.09) * W, 0.2);
      ribbon(pts, R(18, 30) * S, rgba([g0[0] + 22, g0[1] + 18, g0[2] + 14], R(0.25, 0.4)), 5);
      dryStroke(pts, { width: R(16, 26) * S, color: [g0[0] + 40, g0[1] + 32, g0[2] + 26], alpha: R(0.12, 0.22), cover: 0.7, dry: 0.6, grain: 0.35, taperIn: 0.2, taperOut: 0.4 });
    }

    // edge scrubs: broad, flat strokes dragged across the outline (not fur)
    const snapAng = (e) => {
      let nx = e[2], ny = e[3];
      const nl = Math.hypot(nx, ny); nx /= -nl; ny /= -nl; // outward
      return Math.abs(ny) > Math.abs(nx) ? Math.sign(ny) * Math.PI / 2 : nx > 0 ? 0 : Math.PI;
    };
    for (let i = 0; i < 30; i++) {
      const e = edges[Math.floor(rand() * edges.length)];
      if (!e) break;
      const ang = snapAng(e);
      // mostly drag along the edge, sometimes push out of it
      const a = (rand() < 0.6 ? ang + Math.PI / 2 * (rand() < 0.5 ? 1 : -1) : ang) + R(-0.15, 0.15);
      const len = R(0.08, 0.18) * W, w = R(16, 34) * S;
      const x = e[0] - Math.cos(ang) * w * 0.3 - Math.cos(a) * len * 0.3, y = e[1] - Math.sin(ang) * w * 0.3 - Math.sin(a) * len * 0.3;
      const pts = walk(x, y, a, len, 0.1);
      ribbon(pts, w, rgba(L(B, 0.08), R(0.5, 0.8)), R(2, 4));
      dryStroke(pts, { width: w * 0.9, color: L(B, 0.1), alpha: R(0.1, 0.2), jit: 3, cover: 0.9, dry: 0.5, grain: 0.3, taperIn: 0.03, taperOut: 0.3 });
    }
    // translucent dragged smears reaching past the solid edge
    for (let i = 0; i < 14; i++) {
      const e = edges[Math.floor(rand() * edges.length)];
      if (!e) break;
      const ang = snapAng(e), a = ang + R(-0.4, 0.4);
      dryStroke(walk(e[0] - Math.cos(a) * 0.03 * W, e[1] - Math.sin(a) * 0.03 * W, a, R(0.06, 0.14) * W, 0.15), {
        width: R(40, 80) * S, color: [B[0] + 10, B[1] + 6, B[2] + 5], alpha: R(0.08, 0.18), jit: 4, cover: 0.85, dry: 0.8, grain: 0.2, taperIn: 0.05, taperOut: 0.4,
      });
    }

    // arms: thick tapering strokes with a blunt rounded end
    const leftT = tw[0];
    const arms = [{ x: leftT.x + leftT.hw * R(0.1, 0.35), y: leftT.top + 0.012 * H, ang: R(-0.45, -0.1), len: W * R(0.12, 0.19), w: R(24, 32) }];
    if (rand() < 0.8) arms.push({ x: leftT.x - leftT.hw * R(0.2, 0.5), y: leftT.top + 0.015 * H, ang: -Math.PI / 2 - R(0.1, 0.5), len: W * R(0.04, 0.07), w: R(12, 18) });
    if (rand() < 0.5) arms.push({ x: tw[1].x + R(-0.3, 0.3) * tw[1].hw, y: tw[1].top + 0.01 * H, ang: -Math.PI / 2 + R(-0.4, 0.4), len: W * R(0.03, 0.06), w: R(12, 18) });
    for (const a of arms) {
      const pts = walk(a.x, a.y, a.ang, a.len, 0.12), w = a.w * S;
      for (let i = 0; i < pts.length; i += 2) {
        const t = i / (pts.length - 1);
        softFill(() => ctx.arc(pts[i][0], pts[i][1], (w / 2) * (1 - 0.25 * t), 0, Math.PI * 2), rgba(B, 0.7), 3);
        softFill(() => ctx.arc(pts[i][0], pts[i][1], (w / 2.6) * (1 - 0.25 * t), 0, Math.PI * 2), rgba([20, 14, 11], 0.35), 4);
      }
      const end = pts[pts.length - 1];
      softFill(() => ctx.arc(end[0], end[1], w * 0.45, 0, Math.PI * 2), rgba(B, 0.75), 3);
    }

    // isolated dabs floating above
    const nd = 1 + (rand() < 0.35 ? 1 : 0);
    for (let i = 0; i < nd; i++) {
      const r = W * R(0.02, 0.03);
      dab(W * R(0.52, 0.64), H * R(0.515, 0.54), r * 1.3, r, R(-0.4, 0.4), 0.85, 3, [26, 18, 14]);
    }
    for (let i = 0; i < 5; i++) {
      softFill(() => ctx.arc(W * R(0.35, 0.7), H * R(0.545, 0.6), R(1, 3) * S, 0, Math.PI * 2), rgba(B, R(0.3, 0.6)), 2);
    }

    // scratchy thin marks around the edges
    for (let i = 0; i < 40; i++) {
      const e = edges[Math.floor(rand() * edges.length)];
      if (!e) break;
      const pts = walk(e[0] + R(-0.03, 0.03) * W, e[1] + R(-0.02, 0.02) * H, Math.PI / 2 + R(-0.15, 0.15) + (rand() < 0.4 ? Math.PI : 0), R(0.02, 0.12) * H, 0.25, 16);
      dryStroke(pts, { width: R(1.2, 3) * S, color: B, alpha: R(0.2, 0.45), cover: 0.85, dry: 0.4, grain: 0.7 });
    }
    // drips below
    for (let i = 0; i < 6; i++) {
      const x = R(0.2, 0.8) * W, y = botY(x) - 0.01 * H;
      ctx.strokeStyle = rgba(B, R(0.3, 0.6)); ctx.lineWidth = R(1, 2) * S;
      ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + R(-1, 1) * S, y + R(0.01, 0.04) * H); ctx.stroke();
    }

    ctx.restore(); // end of the mass's transform

    // ---- canvas grain + vignette ----------------------------------------------
    gr = ctx.createRadialGradient(W / 2, H * 0.45, H * 0.3, W / 2, H * 0.5, H * 0.75);
    gr.addColorStop(0, "rgba(20,10,5,0)");
    gr.addColorStop(1, "rgba(20,10,5,0.15)");
    ctx.fillStyle = gr; ctx.fillRect(0, 0, W, H);
    const img = ctx.getImageData(0, 0, W, H), d = img.data;
    for (let i = 0; i < d.length; i += 4) {
      const p = i >> 2, x = p % W, y = (p / W) | 0;
      const weave = ((x & 1) ^ (y & 1)) ? 2 : -2;
      const n = (rand() - 0.5) * 10 + weave;
      d[i] += n; d[i + 1] += n * 0.9; d[i + 2] += n * 0.8;
    }
    ctx.putImageData(img, 0, 0);
    // geometry as fractions of the canvas, for hit-testing
    return { red: { x: rx / W, y: ry / H, rx: rrx / W, ry: rry / H }, knobs: own };
  }

  renderGottlieb.KNOBS = KNOBS;
  global.renderGottlieb = renderGottlieb;
})(typeof window !== "undefined" ? window : globalThis);
