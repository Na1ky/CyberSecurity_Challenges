import re

from pwn import remote

HOST = "130.192.5.212"
PORT = 8767

r = remote(HOST, PORT)

r.recvuntil(b"Go!")

for _ in range(100):
    question = r.recvuntil(b".").decode()

    question = question.split()

    a, b = int(question[2]), int(question[4])
    print(a,b, a+b)

    r.sendline(str(a+b).encode())
    
r.interactive()