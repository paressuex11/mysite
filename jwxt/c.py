flag = True

sum = 0
total = 0

while True:
    temp = input()
    if (temp == ''):
        break
    sum += int(temp)
    total += 1
    avg = sum/total
    if total > 200:
        break
print(avg)