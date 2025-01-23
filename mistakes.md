
[Gist of python mistakes](https://gist.github.com/bootandy/6fee9cf5f6e1cfc4484b0205464fee4f)


## Mistakes:
#### Read docs on new API before using
* Could have saved money with the google maps & places API 

#### Async
* Not awaiting a call:

  Here if task occassionally takes longer than 10 seconds, we run 2 tasks at once. If task takes out a lock we fail confusingly:
```
  While !cancelled:
     nursery.start_soon(task)
     sleep(10)
```
  
#### Units in names
* No: timeout
* Yes: [timeout_seconds](https://ruudvanasseldonk.com/2022/03/20/please-put-units-in-names)
        
 
## Things to do better
* When asked when & why 'x':
  * Search the git history, search PR history
 
* Writing docs:
  * Imagine counter argument then search for it. Include links.

    
