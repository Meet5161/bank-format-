def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

a = int(input(" Enter the number: "))
print(factorial(a))
