stroka = input() 
if stroka.count('f') == 1: # если буква f встречается только один раз
    print(stroka.index('f'))
elif stroka.count('f') >= 2: # если буква f встречается два и более раз
    print(stroka.index('f'), stroka.rindex('f')) # выводим индексы 