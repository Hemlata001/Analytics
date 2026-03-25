n = 5873
num = n
count = 0

while n > 0:
    n = n // 10   # last digit remove
    count = count + 1

print(count)
