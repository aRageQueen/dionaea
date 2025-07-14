RESPONSES = {
    "ls": "Documents  Downloads  Music  Pictures",
    "ls -la": (
        "drwxr-xr-x 6 root root 4096 Jul 13 10:00 .\r\n"
        "drwxr-xr-x 3 root root 4096 Jul 13 09:59 ..\r\n"
        "-rw-r--r-- 1 root root  220 Jul 13 10:00 .bash_logout\r\n"
        "-rw-r--r-- 1 root root 3771 Jul 13 10:00 .bashrc\r\n"
        "-rw-r--r-- 1 root root  807 Jul 13 10:00 .profile"
    ),
    "pwd": "/root",
    "whoami": "root",
    "uname -a": "Linux 5.15.0-75-generic #1 SMP x86_64 GNU/Linux",
    "cat /etc/passwd": (
        "root:x:0:0:root:/root:/bin/bash\r\n"
        "daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\r\n"
        "user:x:1000:1000:Fake User,,,:/home/user:/bin/bash"
    ),
    "netstat -tuln": (
        "Proto Recv-Q Send-Q Local Address           Foreign Address         State\r\n"
        "tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN\r\n"
        "tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN"
    ),
    "ps aux": (
        "USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\r\n"
        "root         1  0.0  0.1  22560  3264 ?        Ss   10:00   0:01 /sbin/init\r\n"
        "root       531  0.0  0.3  72356  8064 ?        Ss   10:01   0:00 /usr/sbin/sshd"
    ),
    "top": (
        "top - 10:05:43 up 10 min,  1 user,  load average: 0.00, 0.01, 0.05\r\n"
        "Tasks:  92 total,   1 running, 91 sleeping,   0 stopped,   0 zombie\r\n"
        "%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.4 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st\r\n"
        "KiB Mem :  2048000 total,   256000 free,  1024000 used,   768000 buff/cache"
    ),
    "who": "root     pts/0        2025-07-13 14:00 (192.168.0.5)"
}
