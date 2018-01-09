plugin for CudaText.
small commands to work with binary/hex numbers, etc.

Binary Sum
==========
for any decimal or hex number (64 bit currently, use "0x" prefix for hex), it decomposes number to the sum of 2^N for some indexes N.
for example:
  112 (0x70)
  = 16 + 32 + 64
  bits 4 5 6


Convert base-2 to hex
=====================
stackoverflow.com
E.g. I have a file with the following lines:
00000000000000000000000000001000, 00000000000000000000000000000000, 00000000000000000000000000010000, 00000000000000000000000000111000, 00000000000000000000000000110000, 00000000000000000000000001000000,
And I want to see them in hex representation:
0000_0008, 0000_0000, 0000_0010, 0000_0038, 0000_0030, 0000_0040,

Command reads current text as a list of base-2 nums (separators: , ; space tab newline),
converts them to list of hex NNNN_NNNN, writes result to a new tab.


Sort lines by length
====================
Sorts all lines in the current editor. First go short lines, then longer. Same len lines sorted by text.


author: Alexey (CudaText)
license: MIT
