picoCTF Forensics Challenge: Ph4nt0m 1ntrud3r
Challenge
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to analyze the provided PCAP file, uncover how the attacker infiltrated the system, and retrieve the hidden flag. [PCAP File Download]

Solution Writeup
1. Initial Analysis
Opened myNetworkTraffic.pcap in Wireshark.

Protocol Hierarchy: Only Frame > IPv4 > TCP (no HTTP/FTP/other protocols).

Noted: No high-level protocol, which means any transferred data is likely hidden within raw TCP payloads.

2. Suspicious Observations
Repeated TCP SYN packets with retransmissions between 192.168.0.2 and 192.168.1.2.

Some packets carried tiny payloads (length 12 or 4 bytes).

No normal application-layer traffic was observed—just TCP anomalies.

This suggested a covert channel attack via base64-encoded chunks hidden in TCP payloads, possibly sent out of order.

3. Extracting the Flag: Step-by-Step
A. Tried to Dump All TCP Data (Messy!)

tshark -r myNetworkTraffic.pcap -Y "tcp" -T fields -e tcp.segment_data | xxd -p -r | base64 -d
Result: Produced mostly junk; lots of irrelevant or noisy packets.

B. Filtered by Likely Packet Size

tshark -r myNetworkTraffic.pcap -Y "tcp.len==12" -T fields -e tcp.segment_data | xxd -p -r | base64 -d
Result: Only 12-byte TCP packets extracted; better, but the chunks were still out of sequence.

C. Restored Order by Timestamps
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data \
| sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
Explanation of pipeline:

Extracted packets matching key sizes (12 or 4 bytes).

Grabbed timestamp and payload.

Sorted output by packet/time (crucial! PCAP order was scrambled).

Used awk, xxd, and base64 to reconstruct, decode, and reveal the flag in human-readable order.

4. Why Not Wireshark Alone?
The attacker split the flag into tiny, base64-encoded pieces, embedded out-of-order in TCP packets.

Wireshark’s GUI can’t easily:

Extract only certain payload lengths across thousands of packets.

Automatically restore/collate out-of-order data fragments by timestamp.

Batch process, reassemble, and decode payloads at scale.

Automation with tshark and shell scripting was essential for this type of post-exploitation forensic analysis.

Key Commands Cheat Sheet
Command	Purpose
`tshark -r myNetworkTraffic.pcap -Y "tcp" -T fields -e tcp.segment_data	xxd -p -r
`tshark -r myNetworkTraffic.pcap -Y "tcp.len==12" -T fields -e tcp.segment_data	xxd -p -r
`tshark -r myNetworkTraffic.pcap -Y "tcp.len==12	
💡 Core Learnings
PCAP challenges can hide data in specially-crafted, out-of-order segments—automation and sorting are key.

tshark is a must-have for professional and CTF forensics: allows surgical, scriptable traffic analysis at field-level.

Know your UNIX text-processing tools (awk, sort, xxd, base64)—perfect combo for real-world and competition forensics.
