---
layout: post
title:  "Can you write a for loop in every programming language on your resume?"
date:   2024-07-18
tags: code short
excerpt: "An amusing Hacker News comment."
---

Here's an amusing [Hacker News comment](https://news.ycombinator.com/item?id=40991325): 

>My company, which interviewed me by having me write ‘for’ loops in all 12 or so languages listed on my CV during the technical interview, is a pretty decent place to work.
>
>I cannot tell you how bemused I was after leaving that interview. I’d done months of degrading stupid ‘tell us some trivia about JS’ interviews, and here was someone that (apparently) just wanted to judge whether the information on my CV was true.

An amazing anecote, and I was somewhat chagrined to realize that I would almost surely fail this test.

Here are the programming languages I listed on the July 2024 version of my resume and my self-assesment of whether I could write a [`for` loop](https://en.wikipedia.org/wiki/For_loop) in that language.

The current version of my resume lists the following 13 languages:

| Language | Can I write a `for` loop in this language? |
| -- | --|
| Java | Yes, but probably not all possible variants without Googling |
| Python | Yes! |
| R | No way, but who writes for loops in R? |
| SQL | n/a |
| Bash | I would have to look this up, as I have to every time I write a non-trival bash script. |
| JavaScript | Yes, but I don't know what the modern approaches are. |
| Awk | Maybe? With error feedback, I think I could do this within 5 tries. |
| Clojure | I would have to look up the exact syntax, but I think I could get close. |
| Lua | It has been 10+ years; I think I could make a reasonable guess. |
| C | Yes, without confidence. |
| C# | Yes, without confidence about the differences from Java syntax. |
| Objective C | I would have to look this up, but I think my first guess would be close. |
| Scheme | Is the syntax different from Clojure? I would need to look this up, this was really just on here from my undergrad days. |
| -- | --|

5 for 13 is pretty bad! But then again, I haven't used most of these languages in more than five years. Is this a reasonable measure of my skills as a developer? I'm a little skeptical, but it definitely says something about what level of recency and true mastery I think I need before I list a programming language on my resume.

Okay, let's try it: for each language, I'll type up my first attempt here, then look up the documentation for the language to see if my approach was correct.

### Java ✅

My first attempt:

```java
for (int i = 0; i < 10; i++) {

}
```

There are other `for` alternatives in Java, but we're off to a good start.

### Python ✅

My first attempt:

```python
for i in range(10):
    pass
```

### R ❌
My first attempt:

```r
l <- (1, 2, 3)
# no idea about the for loop syntax, but I think there's a built-in map function
map(some_function, l)
```

Correct:

```r
l <- c(1, 2, 3)
l <- 1:3
lapply(l, as.character)
for (x in l) { }
for (x in 1:10) { }
```

Note that there is no `map` function in base R and that I couldn't even recall how to define a list using [`c`](https://rdrr.io/r/base/c.html)!

### Bash ❌

My first attempt:

```bash
for [[1, 2, 3]]; then
  echo $1
endfor
```

Correct:

```bash
for i in $(seq 1 10); do
    echo "$i";
done
# OR
for ((i = 0 ; i < max ; i++ )); do 
    echo "$i"; 
done
# OR
for i in {1..10} ; do echo "$i"; done
```

I clearly had no idea here; I _maybe_ could have remembered that `seq` existed, but otherwise this syntax is completely foreign to me.

### JavaScript ⚠️

My first attempt:

```js
for (i in [1, 2, 3]) { }
```

Correct:

```js
for (let i = 0; i < 3; i++) { }
// OR
for (let i of [1, 2, 3]) { }
// OR
x = [1, 2, 3]
for (let i in x) { x[i] }
```

While the example I chose was syntactically valid, I didn't remember that JavaScript supported the three-condition for loop, nor the difference between `for ... in` and `for ... of`. Looping over the keys of an in-line array doesn't really feel like it fulfills the spirit of the question! I'll give myself partial credit.

### Awk ✅

My first attempt:

```bash
echo "1
2
3" | awk '{for (i=0; i < 5; i++) {print(i)}'
```

Shockingly, this does actually work, although it was a complete guess. It's probably better not to use parentheses for `print`, but Awk does use the three-condition for statement. Note this code executes on every line of input, so you could use it to duplicate lines some number of times e.g. `awk '{for (i=0; i < 3; i++) {print($0)}}'`.

### Clojure ❌

My first attempt:

```clojure
(for (lambda i (< i 3)) some_function)
```

Correct:
```clojure
(for [i (range 10)] (some_function))
; OR
(def idx [1 2 3])
(for [i idx] (some_function))
```

I completely forgot about how bindings work in Clojure, so I really didn't get close at all.
I assumed the existence of a `(for condition function)`, but that obviously doesn't exist.

### Lua ❌

My first attempt:

```lua
for (i = 0; i < 10; i += 1) {

}
```

Correct:
```lua
-- the numeric for
for i=1,10,1 do print(i) end
---- OR
for i=1,10 do print(i) end
-- the generic for
idx = {1, 2, 3}
for i,v in ipairs(idx) do print(i) end
```

Wow, I really don't remember Lua at all. None of the docs I looked at seemed particularly familiar.

### C ✅

My first attempt:

```c
for (int i = 0; i < 10; i++) {

}
```

Reasonable.

### C# ✅

My first attempt:

```c#
for (int i = 0; i < 10; i++) {

}
```

Reasonable.

### Objective C ✅

My first attempt:

```c
for (int i = 0; i < 10; i++) {

}
```

Can you tell I never used Swift?

### Scheme ❌

My first attempt:

```scheme
(for (list 1 2 3) (some_function))
```

Correct:

```scheme
; (for) is not a function in Scheme; it isn't really feasible without hacks.
; use (map ...)
```

I should remove Scheme from my resume.


### Summary

Basically exactly what I expected overall, with 7 out of 13 approximately correct on my first attempt. I do think I'll remove some languages from my resume because of this! Lua and the functional lanugages (Clojure/Scheme) were particularly rough for me.

If you try this yourself, please link me to your personal results.
