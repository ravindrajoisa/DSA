# Fibonacci Numbers - Implementation Using a For Loop
#Notes: https://www.w3schools.com/dsa/dsa_algo_simple.php
#Problem:  Create the 20 first Fibonacci numbers

# How it works:
"""
Start with the two first Fibonacci numbers 0 and 1.
Add the two previous numbers together to create a new Fibonacci number.
Update the value of the two previous numbers.
Do point a and b above 18 times. 
"""
#Steps:
""" 
1. Two variables to hold the previous two Fibonacci numbers
2. A for loop that runs 18 times
3. Create new Fibonacci numbers by adding the two previous ones
4. Print the new Fibonacci number
5. Update the variables that hold the previous two fibonacci numbers 
"""

#Code:

prev2 = 0
prev1 = 1
print(prev2)
print(prev1)
for fibo in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo