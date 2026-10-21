import re
from pwn import remote

HOST = '130.192.5.212'
PORT = 8766

io = remote(HOST, PORT)

for _ in range(3):
	question = io.recvuntil(b"= ")
	print(question.decode(errors="replace"), end="")
	numbers = re.findall(rb"-?\d+", question)
	a, b = map(int, numbers[-2:])
	io.sendline(str(a + b).encode())

io.interactive()

