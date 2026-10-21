import re

from pwn import remote

HOST = '130.192.5.212'
PORT = 8770

io = remote(HOST, PORT)

prompt = io.recvuntil(b"): ").decode()

for _ in range(20):
    match = re.search(r"between (\d+) and (\d+)", prompt)

    if match is None:
        print(prompt)
        break

    lower, upper = map(int, match.groups())
    for _ in range(30):
        guess = (lower + upper) // 2
        print(f"{prompt.strip()} {guess}")
        io.sendline(str(guess).encode())

        try:
            prompt = io.recvuntil(b"): ").decode()
        except EOFError:
            print(io.recvall(timeout=1).decode(errors="replace"))
            raise SystemExit

        if "Higher!" in prompt:
            lower = guess + 1
        elif "Lower!" in prompt:
            upper = guess - 1
        elif "between" in prompt:
            break
        else:
            print(prompt)
            raise SystemExit

print(io.recvall(timeout=2).decode(errors="replace"))