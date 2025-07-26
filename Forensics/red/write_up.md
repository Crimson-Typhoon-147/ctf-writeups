picoCTF Forensics Challenge: "RED, RED, RED, RED" (red.png)
Challenge Description
RED, RED, RED, RED
Download the image: red.png

Solution Walkthrough
1. Initial Inspection
Downloaded red.png (a 128x128, completely red PNG).

[exiftool red.png] revealed a custom "Poem" in the metadata:
Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.
No flag directly found here.

2. Strings Analysis
Ran:

strings red.png
Results: Displayed the PNG’s poem and structure, but no flag.

3. Steganalysis with zsteg
Installation:

sudo apt install ruby
sudo gem install zsteg
Usage:

zsteg red.png
Discovery:
zsteg output included:

b1,rgba,lsb,xy .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==..."
This is a base64-encoded string, detected in the least significant bit plane of all RGBA channels.

4. Flag Extraction
Took one sequence:

cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==
Decoded with Cyberchef by bring From  base64 to receipe.
Output:

picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

The Flag
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

Key Takeaways
The visible poem was a creative misdirection.

zsteg is essential for uncovering LSB steganography in images.

Always try base64 decoding on extracted bit-level strings during CTF forensics!

Toolbox Summary
Tool	Purpose	Example Command
exiftool	Metadata extraction	exiftool red.png
strings	Strings inside files	strings red.png
zsteg	PNG/BMP steg analysis	zsteg red.png
Python	Base64 decode	base64.b64decode().decode()
References
zsteg GitHub for installation and usage examples.

Usage
Add this example to your forensics/CTF study notes for quick reference when tackling similar steganography challenges in the future!
