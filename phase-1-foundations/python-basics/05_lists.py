nums = [10,25,3,47,18]

print(nums[0])
print(nums[-1])
print(nums[1:4])

nums.append(99)
nums.remove(3)
print(nums)

print(len(nums),sum(nums),max(nums),min(nums))
print(sorted(nums))

for n in nums:
    print(n*2)


# List of squares using a loop
squares = []
for n in range(1,6):
    squares.append(n**2)
print(squares)        