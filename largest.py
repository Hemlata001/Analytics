l = [12, 14, 100, 45, 123, 9]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"your largest number is {largest} and its index is {index}")
