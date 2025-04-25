```txt
$ py vol.py -f ../../ctf/fcsc-2025/challfiles/analyse-memoire.dmp windows.malfind
...
1800	rundll32.exe	0x2244dde0000	0x2244dde0fff	VadS	PAGE_EXECUTE_READWRITE	1	1	Disabled	N/A	
```

```txt
$ py vol.py -f ../../ctf/fcsc-2025/challfiles/analyse-memoire.dmp windows.malfind
...
0xa50a29eaea60	TCPv4	10.0.2.15	49709	100.68.20.103	443	ESTABLISHED	1800	rundll32.exe	2025-04-01 22:11:15.000000 UTC
```

```text
FCSC{rundll32.exe:1800:100.68.20.103:443:TCP}
```