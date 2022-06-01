# Notes on Angular

## Style:
#### Pull out a variable for re-use in template with:
        (someVar | async) as toUse
        <tr *ngIf="(observableDto | async) as realDto">
#### Unsubscribe after subscribing
        Needed for DOM input/mouse/key listener events,
        Not required for other kinds of subscription but arguably neat.
        Remember to add all subscribers to Subscribe object
        Prefer subscribe in ngOnInit over constructor.
#### Naming:
 * Private methods at bottom in alphabetical                            
 * Methods that react when clicked on: should have the prefix 'on'
 * Observables should end name with '$'


## Code Samples:
#### Do thing after n subscriptions have returned:
        this.first$ = this.store$.pipe(select(Selectors.getThing));
        this.second$ = this.store$.pipe(select(Selectors.getOther));
        this.combined$ = combineLatest([this.first$, this.second$]).pipe(
          map(([first, second]) => this.dothing(first, second))
        );
#### Set An observable [Fake subscription]:
        this.first$ = new Observable(ob => {ob.next('new value'); })
#### switchMap vs mergeMap
        switch cancels old http requests in flight.
#### Using tap:
      .pipe(
        switchMap(c => this.service.queryThing(c?.key)),
        tap(c => {console.log('hi '); console.log(c)})
      );
#### Wait until value changed:
        this.subscription.add(
          this.store$
            .pipe(
              select(Selectors.getIsSaved),
              distinctUntilChanged(),
              filter((isSaved: boolean) => isSaved)
            )
            .subscribe((_) => { /*stuff*/}

#### The 'Nothing' tag of angular /Empty tag
        <ng-container />
#### Angular doesn't recognise certain attrs: 'X isnt a known property of Y':
        Here we set 'list' which angular doesnt know about
        [attr.list]="thing" 
        
## NGRXJS:                   
 * Action - point to do a thing
 * Reducer - Pure functions for moving state
 * Effect - Impure functions, calls to services etc.
                            
