import torch
import timeit
import json
import sys
from tqdm import tqdm

MAX_THREADS = 10 * 2

intraop_threads_list = [1] + [t for t in range(2, MAX_THREADS, 2)]
interop_threads_list = [1] + [t for t in range(2, MAX_THREADS, 2)]
n_interop_threads = int(sys.argv[-1])
torch.set_num_interop_threads(n_interop_threads)
with open("runtimes.ndjson", "a") as outfile:
    for n_intraop_threads in tqdm(intraop_threads_list):
        torch.set_num_threads(n_intraop_threads)
        for mat_size in [1024, 2048]:
            # for n_interop_threads in interop_threads_list:
            r = timeit.timeit(
                setup=f"import torch; x = torch.randn({mat_size}, {mat_size}); y = torch.randn({mat_size}, {mat_size})",
                stmt="torch.mm(x, y)",
                number=100,
            )
            line = json.dumps(
                {
                    "num_interop_threads": n_interop_threads,
                    "num_intraop_threads": n_intraop_threads,
                    "mat_size": mat_size,
                    "runtime": r,
                }
            )
            outfile.write(line + "\n")
