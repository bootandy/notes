## Data Structures etc:
#### LSM Tree and SSTables
* Sorted String Table: A file which contains a set of arbitrary, sorted key-value pairs inside. Append only log
* Log Structured Merge Trees: Collapse several SSTs into a tree like structure
* Used in DB as a write buffer.
* [more detail](https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/)

#### Mutual Exclusion Semaphores Mutex VS Binary semaphore
* A Mutex semaphore is "owned" by the task that takes it. If Task B attempts to semGive a mutex currently held by Task A, Task B's call will return an error and fail.

## Other:
#### Standards
 * [Pragmatic REST](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
 * [Choose the Correct HTTP error code](https://racksburg.com/choosing-an-http-status-code/)
 

#### Latency in TCP/IP
By default TCP/IP connections will wait 40ms when they get data before forwarding it on. This is to optimise data transmission (maximise amount of data sent in each packet).
* [Nagle's Algorithm](https://en.wikipedia.org/wiki/Nagle%27s_algorithm)

## Programming Concepts:
#### Covariance & Contravariance

Easy def:
* Covariance = Inheritance for collection generics `func(List<Car>: cars)  func(new List<Prius>())`
* Contravariance = Inheritance the wrong way round for collection generics. `func(Action<Prius>: action) func(new Action<Car>())`
* [Full MS Definition](https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance#:~:text=Covariance%20and%20contravariance%20are%20terms,assigning%20and%20using%20generic%20types)
* [Full SO Definition](https://stackoverflow.com/questions/2662369/covariance-and-contravariance-real-world-example)  

#### Factory Patterns
* [SO Post](https://stackoverflow.com/questions/4209791/design-patterns-abstract-factory-vs-factory-method)

#### Unicode:
* You always decode everything you read
* You always encode everything you write
* UTF-8 is a superset of ASCII which means all valid ASCII byte strings are valid UTF-8 byte strings but only some UTF-8 byte strings are valid ASCII byte strings

## Algo:
#### Which greater asymptotic complexity and why?
* f1(n) = n^sqrt(n)
* f3(n) = n^10 · 2^(n/2)

Proof:
Another way to prove this is to rewrite f3 as f3  = n^10 · 2^(n/2) = n^10 * (2^(sqrt(n)/2)^(sqrt(n)). This works since (a^b)^c = a^(bc). This has a similar form to f1 except it has the n^10 at the beginning and 2^(sqrt(n)/2) instead of n in the second part. If we can show 2^(sqrt(n)/2) grows faster than n, that shows f3 grows faster than f1. This is the case since 2^log2(n) = n(that's log base 2) and sqrt(n)/2 grows faster than log2(n) so 2^(sqrt(n)/2) grows faster than n.
