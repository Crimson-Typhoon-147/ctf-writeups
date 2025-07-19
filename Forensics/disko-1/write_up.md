# picoCTF - disko-1

**Category:** Forensics  
**Points:** 100  
**Platform:** picoCTF  
**Author:** Darkraicg492

---

## 🧩 Challenge Description

> Can you find the flag in this disk image?

We're given a compressed disk image file: `disko-1.dd.gz`. Our task is to extract the flag hidden within this image.

---

## 🛠️ Tools & Commands Used

- `gzip` – to decompress `.gz` files  
- `strings` – to extract printable characters from a binary  
- `grep` – to search for flag patterns  
- `file`, `ls`, `binwalk`, `mount` (considered but not required)

---

## 🪜 Step-by-Step Walkthrough

### 1. 🔽 Download & Navigate

Place the challenge file (`disko-1.dd.gz`) into a working folder.

```bash
mkdir -p ~/Desktop/ctf-writeups/Forensics/disko-1
cd ~/Desktop/ctf-writeups/Forensics/disko-1
mv ~/Downloads/disko-1.dd.gz .

2. 📦 Decompress the File
Unzip the .gz file to get the raw disk image.
gzip -d disko-1.dd.gz

This produces the file disko-1.dd.

3. 🔍 Analyze with strings
Since .dd is a disk image, it might contain readable strings. Let’s search for anything that looks like a flag.

strings disko-1.dd | grep -i pico
This outputs:
picoCTF{th1s_w4s_ju5t_a_fl4g}
📘 What I Learned
Always try simple techniques first before jumping to complex analysis.

.dd files (raw disk images) can often be searched using just strings.

If strings doesn’t work, then tools like mount, binwalk, or autopsy can be explored.
