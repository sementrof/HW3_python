spi = list(map(int, input().split())) 
num = len(spi) 
count = 0 
for i in range(num):
    for j in range(i+1, num): # перебираем все элементы списка, начиная с индекса 1
        if spi[i] == spi[j]:
            count += 1 # увеличиваем счетчик пар
print(count)