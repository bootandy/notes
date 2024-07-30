#### Reverts:
* git reset --hard HEAD

* git reset --hard origin/master

* git reset --hard master@{"10 minutes ago"}   

* git clean -fd (Removes untracked local changes)

#### Find old deleted commits

* git reflog

#### Undo commits but keep the changes on my local area:
* git reset --soft HEAD^

#### Delete remote branch
* git push origin --delete 

#### Pull someone else's branch to local files:
*  `git remote add <username> https://github.com/username/projectname.git  `(in github click code -> copy git link)
*  `git fetch <username>`
*  git pull <username> <branch>

#### Master has gone to hell. My current branch should be master instead
* git merge --strategy=ours master
* git checkout master
* git merge GOOD_BRANCH


#### Search thru git logs:
* git log --all-match --grep=search_string --author=andy

##### Git logs with follow [Follow change thru file moves]:
* git log --follow

##### Search for component:
* git log -p -S SEARCH_FOR optional_limit_by_dir

##### History of a file:
* git log --full-history -- dir/myfile.py

### Blame:
##### Look at lines 400->410. 
  * git blame -L 400,+10 basic.py
##### '-C' is smartly ignore renames, up to 3 are allowed. Compute heavy.
  * git blame -C -C -C basic.py


#### Edit commit order:
* git rebase -i

[Learn git game](https://learngitbranching.js.org/)
