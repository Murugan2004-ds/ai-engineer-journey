def greet(name):
    return f"Hello, {name}!"

def add(a, b=0):
    return a + b

def is_even(n):
    return n % 2 == 0

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(greet("Murugan"))
print(add(5, 3))
print(add(5))
print(is_even(10))
print(factorial(5))

# Challenge : Write a function count_vowels(word) that returns the number of vowels, reusing your logic from Topic 3.
def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count