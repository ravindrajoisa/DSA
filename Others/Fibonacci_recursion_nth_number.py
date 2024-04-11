# To find the nth Fibonacci number we can write code based on the mathematic formula for Fibonacci number n: F(n)=F(n−1)+F(n−2)

def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
    
print(F(19))