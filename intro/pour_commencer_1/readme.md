
```txt
$ py vol.py -f ../../ctf/fcsc-2025/challfiles/analyse-memoire.dmp windows.registry.hashdump
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished                                
User	rid	lmhash	nthash

Administrateur	500	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
Invité	501	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
DefaultAccount	503	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
WDAGUtilityAccount	504	aad3b435b51404eeaad3b435b51404ee	f3ae0fa4a6f8774079f9316acc07eaee
userfcsc-10	1001	aad3b435b51404eeaad3b435b51404ee	3f2360db87910bf0120f8de2b2a0807b
```

```text
$ py vol.py -f ../../ctf/fcsc-2025/challfiles/analyse-memoire.dmp windows.envars
DESKTOP-JV996VQ
```

```text
$ py vol.py -f ../../ctf/fcsc-2025/challfiles/analyse-memoire.dmp windows.registry.printkey --offset 0xb88510266000 --key "ControlSet001\Services\Tcpip\Parameters\Interfaces\{3661d890-d311-4d36-b861-54aef2c9adcc}"
10.0.2.15
```

FCSC{userfcsc-10:DESKTOP-JV996VQ:10.0.2.15}