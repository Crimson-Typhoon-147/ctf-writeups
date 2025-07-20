# 🔓 Password Hash Cracking Challenge – MD5

## 🧩 Challenge
We are given the following MD5 hash and need to determine the original plaintext password:

```
482c811da5d5b4bc6d497ffa98491e38
```

---

## 🔍 Step 1: Identify the Hash Type

We identified the hash using a hash identifier tool:

- **Hash**: `482c811da5d5b4bc6d497ffa98491e38`
- **Type**: MD5

---

## 🛠️ Method 1: Cracking with John the Ripper

### 🔧 Prepare the Hash

John requires the hash to be in a specific format. Save the hash in a file named `hash.txt`:

```
482c811da5d5b4bc6d497ffa98491e38
```

### ▶️ Run John

Use the built-in `rockyou.txt` wordlist to crack the hash:

```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

> 💡 Make sure `rockyou.txt` is unzipped:
>
> ```bash
> gunzip /usr/share/wordlists/rockyou.txt.gz
> ```

### ✅ View the Result

After cracking:

```bash
john --show hash.txt
```

**Output**:
```
482c811da5d5b4bc6d497ffa98491e38:password123
```

---

## 🛠️ Method 2: Cracking with Hashcat

### 🔧 Prepare the Hash

Same as before, save the hash to `hash.txt`:

```
482c811da5d5b4bc6d497ffa98491e38
```

### ▶️ Run Hashcat

Use mode `0` for MD5 and attack mode `0` for dictionary attack:

```bash
hashcat -m 0 -a 0 -o found.txt hash.txt /usr/share/wordlists/rockyou.txt
```

- `-m 0`: MD5 hash mode
- `-a 0`: Dictionary attack
- `-o found.txt`: Save result to file

### ✅ View the Result

After the run completes, check the output:

```bash
cat found.txt
```

**Output**:
```
482c811da5d5b4bc6d497ffa98491e38:password123
```

You can also confirm with:

```bash
hashcat -m 0 --show hash.txt
```

---

## 📌 Summary

| Tool           | Command Used                                                                 | Result         |
|----------------|-------------------------------------------------------------------------------|----------------|
| John the Ripper| `john --format=raw-md5 --wordlist=rockyou.txt hash.txt`                     | `password123`  |
| Hashcat        | `hashcat -m 0 -a 0 -o found.txt hash.txt rockyou.txt`                       | `password123`  |

---

## 🧠 Learning Points

- Always identify the hash type before choosing a tool.
- Use optimized wordlists like `rockyou.txt` for fast cracking.
- Both tools support multiple hash formats and cracking strategies.
- `john` is simple and quick to use; `hashcat` provides more fine-grained control and GPU acceleration.

---

## ✅ Cracked Password

```
password123
```

---
