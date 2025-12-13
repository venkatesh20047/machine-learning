#TASK 1
for i in range(1,6):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

#TASK 2
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#TASK 3
def factorial(n):
    if n<0:
        return None
    result = 1
    for i in range(1,n+1):
        result = result*i
    
    return result
print(factorial(7))

#TASK 4
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

fibonacci(7)


#TASK 5

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for i in range(10,51):
    if is_prime(i):
        print(i,end="")

