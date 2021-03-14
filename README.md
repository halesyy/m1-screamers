### 🧪 Testing Tools

| Code-name | Hardware                        | Estimate CPU Cost    |
|-----------|---------------------------------|----------------------------|
| M1        | Apple M1 MacBook Air, 8gb 256gb, 8 raw cores in Terminal | US$280 [(Intel)](https://ark.intel.com/content/www/us/en/ark/products/88195/intel-core-i7-6700k-processor-8m-cache-up-to-4-20-ghz.html) |
| PC        | Windows 10, i7-6700K @ 4.00 GHz (4 cores, 4 hyperthreaded) in Powershell | US$45 [(Google)](https://www.google.com/search?q=estimate+cost+for+apple+m1+chip) |

From here down, the Python versions are the same (PC: 3.8.5, M1: 3.9.2) unless specified otherwise.

### 🔥 1-one-to-million.py

* M1: 1.78s
* M1 Python 2: 0.98s
* PC: 39.89

### 🔥 2-threaded-scraping.py

In the below test, there are two variables that can be changed: threads and how many are done at-once. If we choose to run 50 threads, this means we'll make 50 requests in total. If we do 10 at-once, it will perform these in 10-chunk batches. The at-once metric is important since it's a key value contributing to scrape performance for cloud-based systems or locally.

* M1, 50 threads, 50 at-once: 0.53s
* M1, 500 threads, 500 at-once: 3.14s
* M1, 1000 threads, 1000 at-once: 22.19s
* M1, 1000 threads, 100 at-once: 6.8s

* PC, 50 threads, 50 at-once: 0.53s
* PC, 500 threads, 500 at-once: 3.49s
* PC, 1000 threads, 1000 at-once: 7.12s
* PC, 1000 threads, 100 at-once: 6.9s

With these results, we 10x'd our required responses with only a 6x increase in time-to-serve. This says Apple's M1 threads are efficient with their thread-switching (something Python naturally struggles with).

But, there seems to be a max to this curve (of course). When we approach 1,000 threads and 1,000 at-once, we've stuffed the threads, causing a Pythonic ms-feedback loop where the threads forcibly keep switching without completing the whole request (my guess). But, when switching 1,000 threads to 100 at-once, we return to our agile speeds with 6.8 seconds.

### 🤔 The takeaway from this test...

Don't stuff your threads. They DO enjoy their space. But, don't give them too much credit - they are M1's... don't need to be boring and go as low as your core count 😉

### 🔥 3-beautiful-soups-per-second.py

A simple compute single-threaded test to observe how many soups a single thread can parse per-second. Important for engineers who are looking for an efficient machine to scrape from. Times the loading of the page (`screamers/sources/3-page.html`), removing unicode (by removing `ord < 128`) then doing 5,000 soup parses.

Test run on a 6,053 length page.

* M1: untested
* PC: 475 per-second average

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
