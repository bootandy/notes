## JavaScript  
#### Debugger:                
    add 'debugger' to code - will drop you into debugger in console in browser.
#### Prefer !== over !=
        Use an extra '=' for stict type check mode
####  Try to use .find instead of loops:
        This pulls profileKey out of each entry in 'list' looking for a match
        const profile = this.list.find( ({profileKey}) => profileKey == targetKey);    

## HTML:                     
#### FxFlex:              
    Must have imported FlexLayoutModule to work.
    This will do what you expect:
     fxFlex="" # Fills the right gap
     fxFlex="none"         
     fxFlex="grow"         
     fxLayoutAlign="stretch stretch"
    fxFlex="grow shrink default" <- put numbers in
    Use: fxFlex="1 0 100px" <- the growth is ratio '1'. important: keep shrink at 0. default is 100px
[Demo of layouts](https://tburleson-layouts-demos.firebaseapp.com/#/docs)
                           
#### fxLayout:       
     fxLayoutGap="10px"
                           
#### Touch actions in HTML
    https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action


## CSS:
#### [CSS grid](https://cssgridgarden.com/)
#### [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#align-items)
Css to use:
* display: flex;

Vertical align bottom:
* align-items: flex-end;

Horizontal align middle:  
* justify-content: center;





## JavaScript oddities in RegEx:
Short version: JavaScript incorrectly assumes unicode characters are always 2 bytes, they may be 4. It's regex handler cant deal with the modern 4 byte unicode characters.

 Get a JS console and try this
/./.exec('a')
>["a"]

^ This regex '.' will match the single character 'a'.
Now try with a complex unicode char like an emoji:
/./.exec('😂')
> ["�"]
The JS regex matches half of the unicode character. 
What is interesting is if you specify a 2 letter match JS finds the character:

/../.exec('😂')
>["😂"]

'😂'.length
>2

In other unrelated regex bugs: \w can not understand accents:
/\w/.exec('Ä')
> Null

Reading more about crazy Unicode in Javascript. Note that some accents can be displayed as letter followed by accent (2 characters) and that the same character can be letter_with_accent (1 character). Ofcourse if this happens the string length is different and they don't match.

## Drawing on GoogleMaps:
Demo code:
```
              const coordinates = // array of lat, lng
              const flightPath = new google.maps.Polyline({
                path: coordinates,
                geodesic: true,
                strokeColor: '#73B9FF',
                strokeOpacity: 1.0,
                strokeWeight: 4,
                 icons: [{
                    icon:  {
      path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
    },
                    offset: '100%'
                  }],
                map: this.theMap,
```
Useful links

* [Google maps doc on custom symbols](https://developers.google.com/maps/documentation/javascript/symbols)

* [Custom google maps markers](https://levelup.gitconnected.com/how-to-create-custom-html-markers-on-google-maps-9ff21be90e4b)

* [Demo for how to do many things in google maps](https://ngmap.github.io/#/!control-simple.html)
