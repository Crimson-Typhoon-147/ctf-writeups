🧩 Challenge Topic: Reverse Engineering
🎯 Challenge Name: Flag Hunters
📚 Concepts Used: Python static analysis, Reverse engineering logic flow, Control flow manipulation, Understanding command interpretation and user input, Hidden function revealing flag (using label jumping)

💡 Breakthrough Step:
Realizing that the crowd input line accepts user input that gets evaluated line-by-line as code instructions in the song reader logic. By entering:

some_string;RETURN 0

We trigger a return to the very first line of the song, which includes the hidden flag in the secret_intro.

🛠️ How I Solved It:
Downloaded and read the Python source code:

A song lyric parser is implemented using splitlines() and label-based jumps like [REFRAIN], RETURN, etc.

The secret_intro (which contains the flag) is defined above the [REFRAIN] section, but never printed by default.

Observed the control logic:

User input is accepted at lines that match CROWD, and the user input is processed line-by-line using a for loop.

If we inject a special keyword like RETURN, it changes where the program continues reading from.

Key Insight:

Normally if we enter RETURN 0 alone, it's treated as a string, not code.

But if we enter something like:
some_string;RETURN 0
the parser splits the line by semicolon (;) and processes each as a separate instruction.

This makes RETURN 0 get treated as a control instruction, effectively jumping to line 0, which prints the hidden secret_intro that includes the flag.

Ran the exploit using:
nc verbal-sleep.picoctf.net 60855

When prompted at Crowd:, I entered:
some_string;RETURN 0

Got the flag.
