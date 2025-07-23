Challenge name- Transformation

Overview


This report documents the solution to a reverse engineering challenge from picoCTF, involving decoding a specially encoded file named `enc`. The challenge required understanding the encoding scheme and reversing it to recover the original flag (secret message).

Challenge Description

We were provided with:  
- A downloadable encoded file: [`enc`](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc)  
- A snippet of Python code that explained the encoding method:  
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

This means that the original flag string was encoded by taking pairs of characters, converting each to their ASCII value, shifting the first character’s value 8 bits to the left (essentially multiplying by 256), and then adding the second character’s ASCII value. The result was converted back to a character and concatenated into the encoded string.

---

## Objective

- Decode the `enc` file using the provided encoding logic reversed.
- Recover the original flag.
- Document the process comprehensively.

---

## Understanding the Encoding

The encoding process performs the following for every two characters in the flag:  

1. Converts the first character to its ASCII code (`ord(flag[i])`).
2. Shifts this value left by 8 bits (`<< 8`), which creates space for the second character in the lower 8 bits.
3. Converts the second character to ASCII (`ord(flag[i+1])`).
4. Adds them together: `(ord(flag[i]) << 8) + ord(flag[i+1])`.
5. Converts this combined number back to a Unicode character (`chr(...)`).

This effectively **packs two 8-bit characters into a single 16-bit character**.

---

## Reversing the Encoding (Decoding Strategy)

To decode the data:

- Read each character of the encoded file.
- Convert it to an integer using `ord()`.
- Extract the original two characters by splitting the integer into high and low bytes:  
  - High byte (first character) = `val >> 8` (integer shifted right 8 bits)  
  - Low byte (second character) = `val & 0xff` (bitwise AND with 255)  
- Convert the high and low bytes back to characters with `chr()`.
- Concatenate these original characters to reconstruct the flag.

---

## Decoding Code

Below is the Python code used for decoding:
Open and read the encoded file
with open("enc", "r", encoding="utf-8") as f:
data = f.read()

Initialize empty string to store decoded flag
flag = ''

Iterate over each encoded character
for c in data:
val = ord(c) # Get integer Unicode code of encoded char
ch1 = chr(val >> 8) # Extract high byte (original first char)
ch2 = chr(val & 0xff) # Extract low byte (original second char)
flag += ch1 + ch2 # Append decoded characters

Output the decoded flag
print("Decoded Flag:", flag)


## Execution and Result

- Upon running the above script with the `enc` file, it successfully outputs the original flag string.
- This confirms that the encoding was correctly reversed and decoding logic is sound.

---

## Conclusion

This challenge demonstrated a simple but clever use of bit manipulation to encode ASCII characters by packing two bytes into one character. Understanding the use of bit shifting and masking helped us reverse typical byte-pair encoding. Such techniques are common in low-level data encoding and give valuable insight into bitwise operations and encoding/decoding problems in cybersecurity.
