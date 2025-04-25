```text
py vol.py -f ../../ctf/fcsc-2025/challfiles/analyse-memoire.dmp windows.pstree --pid 1800
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	Audit	Cmd	Path

656	544	wininit.exe	0xa50a26073080	1	-	0	False	2025-04-01 22:10:43.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\System32\wininit.exe	wininit.exe	C:\Windows\system32\wininit.exe
* 800	656	services.exe	0xa50a20ade080	5	-	0	False	2025-04-01 22:10:43.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\System32\services.exe	C:\Windows\system32\services.exe	C:\Windows\system32\services.exe
** 936	800	svchost.exe	0xa50a26148240	10	-	0	False	2025-04-01 22:10:44.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\System32\svchost.exe	C:\Windows\system32\svchost.exe -k DcomLaunch -p	C:\Windows\system32\svchost.exe
*** 1800	936	rundll32.exe	0xa50a270b9200	4	-	0	False	2025-04-01 22:10:45.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\System32\rundll32.exe	rundll32.exe	C:\Windows\system32\rundll32.exe
```

```
FCSC{svchost.exe:rundll32.exe}