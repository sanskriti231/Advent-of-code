#part 1

arr1 = list()
arr2 = list()
with open("input.txt", 'r') as f:
    s = f.read().split()
    for i in range(2000):
        if i % 2 == 0:
            arr1.append(s[i])
        else:
            arr2.append(s[i])
            
arr1 = sorted(arr1)
arr2 = sorted(arr2)
sum = 0
for i in range(1000):
    diff = int(arr1[i]) - int(arr2[i])
    sum += abs(diff)
    
print(sum)

#part 2

similarity_score = 0
for i in arr1:
    similarity_score += int(i) * arr2.count(i)

print(similarity_score)