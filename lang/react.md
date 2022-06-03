
#### Overview of core:
this.state = stuff you can change
this.props = constants that come from the hierarchy.

#### Build / Flow locally:

    yarn flow src

Lost / Where is that function from:
look for: conectRedux at the bottom of the file. - go to the class mentioned there.
Generally go to the bottom of the react file.

#### Mistakes:

* Dont use alert use window.sendError
* Link tag: use 'to' not 'a'
* Every list li ul element needs a key property key={uuid} NOT key="{uuid}"
* Use button not a if it is a button.
    (Get icons from)[https://material.io/resources/icons/?style=baseline]
* Don't use Maps just use raw Objects instead:
    * If you do use maps: [Don't use [] use .set and .get](https://javascript.info/map-set#object-fromentries-object-from-map)
        * Map arrow functions inside html don't seem to work. Use a loop.
* If no state in a react component just use an arrow function.
* Make react handle the loading case instead of blindly defaulting to empty list:
    * if (!teamsFetch || teamsFetch.pending) return <Loading />
    * if (teamsFetch.rejected) return <Error />
    * const rawTeams = (teamsFetch && teamsFetch.fulfilled && teamsFetch.value) || []
* Use useMemo:
    * const memoisedValue = React.useMemo(() => doHeavyComputation(a, b), [a, b])
    * Must go before any returns. 

* Don't modify this.props - instead call onChange and have the parent update it.  [...this.props.mylist, new_element]

#### Tests yarn add --dev jest

    yarn jest
    Jest test design: We don't tend to test the API is hit. Normally test the modals are called.

JS yarn prettify

yarn prettier --write find src | egrep jsx\\\\?$ --exclude passfort-types | grep -v passfort-types


#### Flow
Ignore JS Flow check add this on line before:

    // $FlowFixMe
    {/* $FlowFixMe */}

