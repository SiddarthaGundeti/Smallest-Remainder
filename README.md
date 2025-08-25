# Smallest-Remainder

Input: 3  7

Output: 1

Question Explanation:

This program calculates the remainders of two different divisions involving two numbers A and B, and then identifies the smaller of the two remainders. The two key operations are:

Calculating the remainder when A is divided by B (A % B).
Calculating the remainder when B is divided by A (B % A).
The smallest of these two remainders is then printed as the output.

Logical Approach:

Read Inputs:
Read two numbers A and B from the user input.

Calculate Remainder of A % B:
Use the modulus operator (%) to find the remainder when A is divided by B. Store this value in reminder_AB.

Calculate Remainder of B % A:
Similarly, find the remainder when B is divided by A and store this value in reminder_BA.

Find and Print Smallest Remainder:
Compare reminder_AB and reminder_BA.
Print the smaller value among the two. If both are equal, either of them can be printed as they are the same.

Example for Clarity:

If A is 3 and B is 7:
A % B (3 % 7) is 3 as 3 divided by 7 gives a remainder of 3.
B % A (7 % 3) is 1 as 7 divided by 3 gives a remainder of 1.
The smaller remainder between 1 and 3 is 1.
The output will be:

