import requests
from pwn import *

context.log_level = "debug"
HOST = "chall.fcsc.fr"
PORT = 2052

r = remote(HOST, PORT)
r.recvline()
r.sendline(b"getfingerprint flag.opus")
fingerprint = r.recvlines(1)[0].split()[1].strip().decode()
r.sendline(b"lsinfo flag.opus")
duration = int(r.recvlines(7)[4].decode().split(":")[1])


API = "https://api.acoustid.org/v2/lookup"
KEY = "..."

r = requests.get(API,
                 params={
                        "client" : KEY,
                        "duration" : duration,
                        "fingerprint" : fingerprint,
                        "meta" : "artist recordings"
                 })
print(r.text)