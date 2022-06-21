# Examples
## Collatz Sequence
This simple 2-tag system is adapted from [De Mol, 2008]. It uses no halting symbol, but halts on any word of length less than 2, and computes a slightly modified version of the Collatz sequence.

In the original Collatz sequence, the successor of n is either n/2 (for even n) or 3n + 1 (for odd n). The value 3n + 1 is clearly even for odd n, hence the next term after 3n + 1 is surely 
(3n + 1)/2 . In the sequence computed by the tag system below we skip this intermediate step, hence the successor of n is (3n + 1)/2 for odd n.

In this tag system, a positive integer n is represented by the word aa...a with n a's.

SOURCE: https://en.wikipedia.org/wiki/Tag_system

## Fill Neighbour Task
This computation stems from an exercise that lead to the creation of the m-Tag RPM system to more easily communicate spatially without having to change the parity of the tape length as in usual m-Tag systems.

It's a good example to demonstrate the use of the RPM system. 

Challenge: Feel free to give the same task a try using only an m-Tag system.


