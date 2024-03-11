## React ideas
* const func = useSetAtom(someAtom) # This calls a function from global state
* const [field, func] = useAtom(someAtom) # This calls a function & stores the value from global state

### Rule of thumb:
Functions should never read fields. 
A function may only 'read' a field if it is in a ` = React.useCallback((` - and then the fields are listed at the end in the callback list.

