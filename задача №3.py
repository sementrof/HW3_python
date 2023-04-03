spisok = list(map(int, input().split()))
last_spisok = spisok.pop() # удаляем  элемент и сохраняем его в переменную
spisok.insert(0, last_spisok) # добавляем последний элемент в начало списка
print(spisok) 