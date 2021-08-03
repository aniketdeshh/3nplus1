# The 3N+1 Problem
This small python project is meant to simulate the Collatz Conjecture, or the 3N+1 problem. This is a problem in mathematics that many mathematicans have attempted to solve. Experienced mathematicans advise younger students to not attempt to find a reason for why this problem exists, because it has been tested thoroughly and a solution still has not been found. 

## The problem
Pick any positive integer. If the integer is odd, multiply it by 3 and add 1. If it is even, divide by 2. After you've done the corresponding operation, this new number is now your current number. If you repeat this process forever, you will _always_ end up with 1. Once you're at 1, you have to multiply by 3 and add 1, which results in 4, then 2, then 1 again. The Collatz Conjecture always ends in the 4-2-1 loop. Mathematicans have been trying to find a number that breaks this loop. In fact, they have tested all numbers up to 2^68 on a Turing Machine, and none have broken it.

## This project
This isn't an attempt to solve the 3N+1 problem, but it does visualize it. I found that it is a very nice algorithm for generating mountains in a virtual setting. You see that the plot will essentially move randomly until it hits the 4-2-1 loop and the plot ends. 

