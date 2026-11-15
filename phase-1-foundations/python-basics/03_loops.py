# 1. Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# 2. Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 3. Sum of numbers 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

# 4. While loop: keep asking until the user enters a positive number
value = int(input("Enter a positive number: "))
while value <= 0:
    value = int(input("Try again, enter a positive number: "))
print("Thanks!")

# 5. Count vowels in a word
word = input("Enter a word: ")
count = 0
for letter in word.lower():
    if letter in "aeiou":
        count += 1
print("Vowels:", count)