

#### Shell IO:
* ` > `   Is write stdout and overwrite
* ` >> `  Is append stdout
* ` | `   Is stdout -> stdin
* `2> `   Is write stderr
* `ls badtext > out 2>&1` Redirecting stderr to the same file as stdout.


#### Overview of Root *nix Directories:
 ```
 Core:
/bin - compiled ready to run programs
/dev - Devices files (disks)
/etc - System configuration files
/home - Personal directories
/lib -  Library - hold library files used by executables. (note: /usr/lib also exists)
/proc - System stats, information about running processes.
/sys - Similar to proc (TODO: Update)
/sbin - System executables. Users should NOT have /sbin in their PATH.
/tmp
/usr - Not user files! File layout is similar to '/'. Historic, meant to minimise space for root user.
/var - 'Variables' Programs record runtime info. System logging, caches, user tracking etc.

Other:
/boot - kernal boot loader
/media - Removable drives
/opt - Third party software, often not used.

/usr/:
/usr/ - The same as above
/usr/include - Header files for C compiler
/usr/info - GNU manuals
/usr/local - For admins to install stuff here
/usr/man - man pages
/usr/share - historical from the days of low disk space
```
