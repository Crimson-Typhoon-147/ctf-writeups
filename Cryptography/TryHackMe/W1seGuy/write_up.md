# 🧠 Challenge Name: W1seGuy (TryHackMe)

## 🧩 Category
Cryptography

## 📝 Description
A basic XOR encryption challenge where the user must extract the flag by analyzing encoded text and understanding the underlying encryption mechanism.

---

## 🔍 Challenge Overview

- The server provides an **XOR-encoded hex string**.
- The encoded data contains the flag.
- The encryption key is 5 characters long.
- The flag format is predictable (e.g., starts with `THM{`).

---

## 🧠 Concepts Used

- XOR encryption
- Known plaintext attack
- Brute-forcing short keyspace
- CyberChef for analysis
- Hex decoding
- Pattern recognition in CTF flags

---

## 🧪 Approach & Solution Steps

1. **Connect to the server** (e.g., via `nc <IP> 1337`) and get the XOR-encoded hex string.
2. **Note the flag format** — e.g., `THM{...}` — so you can apply a known-plaintext attack.
3. Convert the XORed hex string to bytes using CyberChef or Python.
4. Use the known plaintext `"THM{"` and XOR it against the first 4 bytes to get part of the key.
5. Brute force the 5th character of the key manually using CyberChef or a script.
6. Once the full 5-character key is recovered, use CyberChef:
   - Operation: `From Hex` → `XOR with key`
   - Encoding: UTF-8
7. The output will be the full decrypted flag.

---

## 🧪 Sample Python Script (if needed)

```python
import string
from pwn import xor

xored_hex = "..."  # Paste your hex here
xored_bytes = bytes.fromhex(xored_hex)

known = b"THM{"  # Known prefix of the flag
partial_key = xor(xored_bytes, known)[:4]

charset = string.ascii_letters + string.digits

for char in charset:
    key = partial_key + char.encode()
    try:
        decrypted = xor(xored_bytes, key)
        flag = decrypted.decode()
        if flag.startswith("THM{") and flag.endswith("}"):
            print("Key:", key.decode())
            print("Flag:", flag)
            break
    except:
        continue
