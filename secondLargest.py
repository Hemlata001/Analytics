l = [12,14,100,45,123,9]
largest = l[0]
second_largest = l[0]
index = 0
for i in l:
    if i > largest:
        second_largest = largest
        largest = i
print(second_largest,largest)
