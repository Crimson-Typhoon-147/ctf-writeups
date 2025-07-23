# Open and read the encoded file
with open("enc", "r", encoding="utf-8") as f:
    data = f.read()

# Decode the data
flag = ''
for c in data:
    val = ord(c)            # this is (char1 << 8) + char2
    ch1 = chr(val >> 8)     # upper byte
    ch2 = chr(val & 0xff)   # lower byte
    flag += ch1 + ch2

print("Decoded Flag:", flag)
