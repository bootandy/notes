#### VSCode:
[Trouble with CAPS-LOCK mapped to ESCAPE in VSCode](https://stackoverflow.com/questions/37777417/how-to-use-vim-key-bindings-with-visual-studio-code-vim-extension)
Search in settings, for 
keyboard.dispatch - change to keyCode
Basic settings.json:

    "keyboard.dispatch": "keyCode",
    "vim.handleKeys": {
        "<C-p>": false,
        "<C-d>": true
    }
    

#### Cron:
[From SO](https://stackoverflow.com/questions/12786410/run-cron-job-every-n-minutes-plus-offset)

Note the number after / must exactly divide by 60 or jobs will not run at the same time each hour.

*  5-59/20 * * * *     -  Run a task every 20 minutes starting at 5 past the hour:
* 10-59/25 * * * *     -  Run at 10 minutes after and 35 minutes after:

#### TcpDump notes:
0. Try tracert:
* tracert www.google.com
 
1. To monitor HTTP traffic including request and response headers and message body:
* tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
2. To monitor HTTP traffic including request and response headers and message body from a particular source:
* tcpdump -A -s 0 'src example.com and tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
3. To monitor HTTP traffic including request and response headers and message body from local host to local host:
* tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -i lo
4) To listen to https traffic limited to the interface ethernet 0: (Obviously this is encrypted so not legible)
* /usr/sbin/tcpdump  -i eth0 port 433


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
