
# Notes on C#

## Layout:
* WebApps put Logic in Service not controller
*  CommandQuerySeparation:
      * Can be read as Don't use chaining/trainwrecking.
      * Queries: Return a result and do not change the observable state of the system (are free of side effects).
      * Commands: Change the state of a system but do not return a value.
        
        
## Naming:
### Method names:
* PascalCase not camelCase
* Dont use Get* unless a Get HTTP or a property
### Constants:
  * ConstantNamesLikeThis. NOT_LIKE_THIS
### Async:
 Async suffix is a naming convention in C#. It has to do with the return type, not the [async] modifier.
        Types that return Task/Task<T> are typically named XXXAsync

  
## Tests:
* Don't cast directly use:
    Assert.IsAssignableFrom<NotFoundResult>(getAsync);

## LinQ samples:
* Get single one or raise if more, else default?:
  
    var orgKey = entity.Select(js => js.OrganisationKey).Distinct().SingleOrDefault();
  
    // return value if no: ObjectId.Empty                                                                                     
     
* Returns the only element of a sequence, and throws an exception if there is not exactly one element in the sequence.
  
    var orgKey = entity.Select(js => js.OrganisationKey).Distinct().Single();

## Secrets:
* right click cs proj file
* Tools -> Open project secrets
       
