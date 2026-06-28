nums = [1,2,3,4,5,6,7,8,9,0]

for num in nums:
    print(num)

for num in nums:
    if num == 4:
        print("Found")
        break
    print(num)

for num in nums:
    if num == 4:
        print("Found")
        continue
    print(num)

for num in nums:
    for letter in 'abcd':
        print(num, letter)

for i in range(1, 11):
    print(i)

x = 0

while x < 10:
    print(x)
    x += 1