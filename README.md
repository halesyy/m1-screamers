### 🧪 Testing Tools

| Code-name | Hardware                                                                                   | Estimate CPU Cost                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| M1        | Apple M1 MacBook Air, 8gb 256gb, 8 raw cores in Terminal                                   | US$45[(Google)](https://www.google.com/search?q=estimate+cost+for+apple+m1+chip)                                                       |
| PC        | Windows 10, i7-6700K @ 4.00 GHz (4 cores, 4 hyperthreaded) in Powershell                   | US$280[(Intel)](https://ark.intel.com/content/www/us/en/ark/products/88195/intel-core-i7-6700k-processor-8m-cache-up-to-4-20-ghz.html) |
| M2        | Apple M2 Mac Mini, 24gb 1TB, 8 raw cores in Terminal<br />Using Python3.11                 |                                                                                                                                     |
| LX        | The above PC target, on a Linux distro, specifically ElementaryOS.                        |                                                                                                                                     |
| LX2       | My friend**[@harvmaster](https://github.com/harvmaster)** PC running Linux - 12700h, 3.10.12 |                                                                                                                                     |

LX = same stats of PC, but ran on a Linux distro (ElementaryOS).

From here down, the Python versions are the same (PC: 3.8.5, M1: 3.9.2) unless specified otherwise.

### 🔥 1-one-to-million.py

* M1: 1.78s
* M1 Python 2: 0.98s
* M2: 1.27s
* PC: 39.89s
* LX: 2.71s
* LX2: 1.148s

### 🔥 2-threaded-scraping.py

In the below test, there are two variables that can be changed: threads and how many are done at-once. If we choose to run 50 threads, this means we'll make 50 requests in total. If we do 10 at-once, it will perform these in 10-chunk batches. The at-once metric is important since it's a key value contributing to scrape performance for cloud-based systems or locally.

* M1, 50 threads, 50 at-once: 0.53s
* M2, 50 threads, 50 at-once: 0.34s
* PC, 50 threads, 50 at-once: 0.53s
* LX, 50 threads, 50 at-once: 0.45s
* LX2, 50 threads, 50 at-once: 4.52s

With these results, we 10x'd our required responses with only a 6x increase in time-to-serve. This says Apple's M1 threads are efficient with their thread-switching (something Python naturally struggles with).

But, there seems to be a max to this curve (of course). When we approach 1,000 threads and 1,000 at-once, we've stuffed the threads, causing a Pythonic ms-feedback loop where the threads forcibly keep switching without completing the whole request (my guess). But, when switching 1,000 threads to 100 at-once, we return to our agile speeds with 6.8 seconds.

### 🤔 The takeaway from this test...

Don't stuff your threads. They DO enjoy their space. But, don't give them too much credit - they are M1's... don't need to be boring and go as low as your core count 😉

### 🔥 3-beautiful-soups-per-second.py

A simple compute single-threaded test to observe how many soups a single thread can parse per-second. Important for engineers who are looking for an efficient machine to scrape from. Times the loading of the page (`screamers/sources/3-page.html`), removing unicode (by removing `ord < 128`) then doing 5,000 soup parses.

Test run on a 6,053 length page.

* M1: 530 per-second (550 max)
* M2: 1,035 per-second (used max)
* PC: 485 per-second (489 max)
* LX: 473 per-second
* LX2: 867 per-second

**M1 out-performs by 9.2%**. M1 out-performs my personal scrape workspace in a single-core approach.

### 🔥 4-sha256.py

Perform 1,000,000 iterations of a sha256 hash digest + generate a random string of 10 to use as the to-hash.

* M1: 4.95 seconds
* M2: 1.95 seconds
* PC: 4.42 seconds
* LX: 5.29 seconds
* LX2: 2.20 seconds

### 🔥 5-jacobian.py

Performs 1,000,000 Jacobian computations. I'm not too familiar with this branch of mathematics, but I have seen many implementations of Bitcoin wallet generation using Jacobian mathematics. 1,000 total iterations where `t` spans 1->1,000, and `a, b` both span 1->1,000 in each `t` iteration. Lower the better.

* M1: 17.25 seconds
* M2: 7.08 seconds
* PC: 20.81 seconds
* LX: 19.76 seconds
* LX2: 7.28 seconds

### 🔥 6-threaded-compute.py

Just 50 threads filled with heavy compute. Store the first 10,000,000 integers in a list, then divide them by a float (`5.2125`) and return the length of the list.

* M1: 255.48 seconds (~4 minutes) - 50 threads, 50 at-once
* M1: 97.5 seconds - 50 threads, 8 at-once
* M1: 49.87 seconds - 50 threads, 4 at-once
* M1: 48.76 seconds - 50 threads, 1 at-once
* M2: 21.45 seconds - 50 threads, 4 at-once
* PC: untested
* LX: 42.13 seconds - 50 threads, 4 at-once
* LX2: 25.68 seconds - 50 threads, 4 at-once

This test was interesting, since the M1 used a lot of "virtual memory" during this test. "Memory Used" displayed 28GB on my 8GB model as "Virtual Memory". Further, this reinforces the idea to not stuff threads in M1 Python.

In reality I just realised this is because of GIL and Python and compute, so what's happening is nothing is happening in 3/4 threads when 1 is working. So, I'll re-write this in the future using multiprocessing or another measure to steer from this.

### ❓ The M1 Screamers

Pushing to the border: multiprocessing, threading, scraping, and compute tests with Apple M1 Silicon & their Windows/Linux counterparts.

### 📝 Future Screamer Test Ideas:

* Print the first million numbers
* Threading a scrape and BeautifulSoup parse with adjustable threads
* Complex Jacobian mathematics, generating ecliptics, etc
* Million-iteration cryptography (SHA256, 512, XMR's algo, etc...)
* Video cut-and-render using moviepy (copy + hard encode)
* My personal y12 heavy-compute smart art functions (requires seperate project link, won't publish source here)
* My personal image re-interpretation functions
