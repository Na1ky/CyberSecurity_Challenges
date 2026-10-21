from pwn import remote
import sys

sys.set_int_max_str_digits(0)

HOST = '130.192.5.212'
PORT = 8769

r = remote(HOST, PORT)

r.recvuntil(b"Go!")

for _ in range(1000):
    question = r.recvuntil(b"= ")
    print("Domanda: ", question)
    question = question.decode().split(' ')

    a = int(question[2])
    b = int(question[4])

    response = 0

    match question[3]:
        case '+':
            response = a + b
        case '-':
            response = a - b
        case '/':
            response = a//b
        case '*':
            response = a*b
        case '**':
            response = a**b

    r.sendline(str(response).encode())
    
r.interactive()