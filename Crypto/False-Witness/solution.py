from pwn import remote, log
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST, PORT = "target", "port"

io = remote(HOST, PORT)
io.recvuntil(b"Here is something for you:\n")
ct = bytes.fromhex(io.recvline().strip().decode())

P = 0xCD4A96D3B7FA7251A1BB765933FB676FCAE8C9026682E34F779122DFD66915BB
G = P - 1
io.sendlineafter(b"generator: ", str(G).encode())

bits = []
for i in range(256):
    io.recvuntil(b"> ")
    io.sendline(b"1")
    io.recvuntil(b"Enter offset: ")
    io.sendline(str(i).encode())
    line = io.recvline().decode()
    val = int(line.split(":")[1].strip())
    bit = 1 if val in (1, P - 1) else 0
    bits.append(bit)
    log.info(f"bit[{i}] = {bit}")

io.sendlineafter(b"> ", b"2")

key_int = int("".join(map(str, bits)), 2)
key = key_int.to_bytes(32, "big")
print("Recovered KEY:", key.hex())

flag = unpad(AES.new(key, AES.MODE_ECB).decrypt(ct), 16)
print("FLAG:", flag)