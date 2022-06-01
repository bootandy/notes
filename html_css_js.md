# JavaScript  
### Debugger:                
    add 'debugger' to code - will drop you into debugger in console in browser.
#### Prefer !== over !=
        Use an extra '=' for stict type check mode
####  Try to use .find instead of loops:
        This pulls profileKey out of each entry in 'list' looking for a match
        const profile = this.list.find( ({profileKey}) => profileKey == targetKey);    

# HTML:                     
## FxFlx:              
    Must have imported FlexLayoutModule to work.
    This will do what you expect:
     fxFlex="" # Fills the right gap
     fxFlex="none"         
     fxFlex="grow"         
     fxLayoutAlign="stretch stretch"
    fxFlex="grow shrink default" <- put numbers in
    Use: fxFlex="1 0 100px" <- the growth is ratio '1'. important: keep shrink at 0. default is 100px
[Demo of layouts](https://tburleson-layouts-demos.firebaseapp.com/#/docs)
                           
## fxLayout:       
     fxLayoutGap="10px"
                           
## Touch actions in HTML
    https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action


# CSS:
### [CSS grid](https://cssgridgarden.com/)
  
