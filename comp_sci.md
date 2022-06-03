# Data Structures etc:
#### LSM Tree and SSTables
* Sorted String Table: A file which contains a set of arbitrary, sorted key-value pairs inside. Append only log
* Log Structured Merge Trees: Collapse several SSTs into a tree like structure
* Used in DB as a write buffer.
* [more detail](https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/)

#### Mutual Exclusion Semaphores Mutex VS Binary semaphore
A Mutex semaphore is "owned" by the task that takes it. If Task B attempts to semGive a mutex currently held by Task A, Task B's call will return an error and fail.

# Other:
## Rest Standards
 * [Pragmatic REST](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)
 * [Choose the Correct HTTP error code](https://racksburg.com/choosing-an-http-status-code/)
 * 

## Latency in TCP/IP
By default TCP/IP connections will wait 40ms when they get data before forwarding it on. This is to optimise data transmission (maximise amount of data sent in each packet).
* [Nagle's Algorithm](https://en.wikipedia.org/wiki/Nagle%27s_algorithm)

# Programming Concepts:
## Covariance & Contravariance

Easy def:
* Covariance = Inheritance for collection generics `func(List<Car>: cars)  func(new List<Prius>())`
* Contravariance = Inheritance the wrong way round for collection generics. `func(Action<Prius>: action) func(new Action<Car>())`
* [Full MS Definition](https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance#:~:text=Covariance%20and%20contravariance%20are%20terms,assigning%20and%20using%20generic%20types)
* [Full SO Definition](https://stackoverflow.com/questions/2662369/covariance-and-contravariance-real-world-example)  
