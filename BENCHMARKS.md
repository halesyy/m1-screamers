## Testing Tools

| Code-name | Hardware                        |
|-----------|---------------------------------|
| M1        | Apple M1 MacBook Air, 8gb 256gb |
| PC        |                                 |
|           |                                 |

### 1-one-to-million.py

* M1 Python 3: 1.78s
* M1 Python 2: 0.98s

### 2-threaded-scraping.py

In the below test, there are two variables that can be changed: threads and how many are done at-once. If we choose to run 50 threads, this means we'll make 50 requests in total. If we do 10 at-once, it will perform these in 10-chunk batches. The at-once metric is important since it's a key value contributing to scrape performance for cloud-based systems or locally.

* M1 Python 3, 50 threads, 50 at-once: 0.53s
* M1 Python 3, 500 threads, 500 at-once: 3.14s

With these results, we 10x'd our required responses with only a 6x increase in time-to-serve. This says Apple's M1 threads are efficient with their thread-switching (something Python naturally struggles with).
