

## Grep
#### Count occurrences in a file:
* grep -c RuntimeError 2015-10-* 

#### Find files containg the word 'jsp'
* find . | xargs grep -i jsp

#### Only keep part that matches
 grep -o 'x' = only keep the string 'x' not the whole line 'x' is on. (Alternate to -v)
* grep 'fish' my_food.log | grep -o 'fish' | wc -l

#### Grep, count:
* grep 'fish' my_food.log |sort | uniq
 
#### Grepping with RegEx:
Returns the last word in each line.
\w doesn't work

* grep -oG '[a-z0-9A-Z\-\_\-]'*$ products

Note: add -P for more regex terms allowing you to use \d & \s [Search for 50X errors in http logs]

* grep -P '\s50\d\s' 2014-05-20.log

 #### I want to grep for all these values in `file.txt` in 1 go:

* grep -v -f file.txt test.txt

#### Nice grep example:
   cat -n: print line number.
   use of -B and -A to look at lines 'near' the problem line
* cat -n 2014-02-01.log | grep -i rball |grep -B10 -A50 1680071

 
## Awk:

#### Sum numbers in file
```
cat ab2.txt
a=1
bbbb=2
cc=4
awk '{  split($1, ar, "="); sum += ar[2]; } END { print sum; }' < ab2.txt
```


#### Awk:
* $0 = the whole line
* $1..n = the line after a split by space
* END must be in capitals

#### .. Awk in a shell script using strings not files:
This takes the string s1 and splits it (by space) and stores the first 2 columns.
(to split by something other than space use -F) see here
* ``` col1=`echo $s1 | awk  '{print $1}'` ```
* ``` col2=`echo $s1 | awk  '{print $2}' ` ```

#### Awk with ls
Split by underscore, only show unique names
List files -> Keep part of the filename before '_' -> only keeps unique names

* ls | awk '{ split($1, ar, "_"); print ar[1] }' | uniq

#### Awk for http logs
Find all 400 errors in this todays log:
* head -100 2014-02-13.log | awk -v FS='\t' '{ print $6,$0 }' | grep ^40* 

Alternate way of finding 500 errors: 
* cat /log/nginx_access/current | awk '$9 == "500" { print $0 }' | less


## Other:
#### Sort files then Diff in one:
bash -c 'diff <(sort file1) <(sort file2)'

#### Cut:
Split filename by '_' show first part of filename:
* ls * | cut -f1 -d '_'

#### Remove space from string in script:
* ``` nospace=`echo "hello there hi" | tr -d " "` ```

#### Shell IO:
* ` > `   Is write stdout and overwrite
* ` >> `  Is append stdout
* ` | `   Is stdout -> stdin
* `2> `   Is write stderr
* `ls badtext > out 2>&1` Redirecting stderr to the same file as stdout.

#### Zip with ignore:
Zip a dir ignoring .git and tmp files:
* zip  -r output.zip  mydir/ -x *.git* *tmp*~

#### Local Networking:
List of open files &amp; ports used by process:
* lsof -n -P -p 

List open ports:
* netstat -a

Find which port mongo process uses:
* netstat -tapn | grep mongo

Like Ping but lower, works on level 2:
* arping IP/MAC_ADDR

#### Script samples:
How to if:
```
#!/bin/sh
FULLHOSTNAME=`hostname -f`
if [ "$FULLHOSTNAME" = "5jane" ]; then
        echo "hi"
fi

case $PWD/ in
    (*/remote/*) COLOR_DIR=$BLUE;;
    (*/local/*) COLOR_DIR=$CYAN;;
    (*) COLOR_DIR=$WHITE;;
esac

```
You need a space after '[' and before ']' 
You need a ';' Use `-gt' for greater than.

How to RegEx:
```
if [[ "los" =~ lo.* ]]; then
```
' will not evaluate vars, " will evaluate vars
```
fish=haddock
echo 'Hello $fish'=== Hello $fish
echo "Hello $fish" === Hello haddoc
```

#### Replace:
Use ^old^new to run the previous command but swap out value with new one:
```
$ ls fille
$ ^fille^file
```
#### Mass Rename
* find . -name "*.php" -print | xargs sed -i 's/foo/bar/g'

#### Find tool to do X or similar to X: (searches man pages)
* apropos X
