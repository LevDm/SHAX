# -*- coding: utf-8 -*-
def MATRIX(): #создание шахматной доски
    A = []
    for i in range(10):
        B = []
        for j in range(10): B.append('#')
        A.append(B)
        
    name_pole = ['a','b','c','d','e','f','g','h']
    
    for i in range(10):
        for j in range(10):
            if i == 0 and j == 0: continue
            if i == 0 and j == 9: continue
            if i == 9 and j == 0: continue
            if i == 9 and j == 9: continue
        
            if i == 0 or i == 9: A[i][j] = name_pole[j-1]
            if j == 0 or j == 9: A[i][j] = str(9-i)
            
            if A[i][j] == '#':
                if int(i % 2) == 1 and int(j % 2) == 1 or int(i % 2) == 0 and int(j % 2) == 0 : A[i][j] = 'Б'
                if int(i % 2) == 1 and int(j % 2) == 0 or int(i % 2) == 0 and int(j % 2) == 1: A[i][j] = 'ч'        
    return A


A = MATRIX()


def PRINT_MATRIX(A): #вывод доски
    for i in range(len(A)):
        LINE = ''
        for j in range(len(A)):    
            LINE = LINE + str(A[i][j]) + ' '
        print(LINE)
    

def ZNAHENIE(KAKOE): #запрос значения
    i = True
    
    while i == True:    
        otvet = input('** Значение '+str(KAKOE) + ':')
            
        if  otvet.isdigit() == True:
            otvet = int(otvet)
            if 1 <= otvet <= 8: break
            else:
                print('\n*** Число не попадает в диапазон действий!')
                continue
        else:
            print('\n*** Необходимо целое число!')
            continue
        
    return otvet


def POLE(KAKOE):  #создание поля
    print('\n-----')
    print('\n* '+str(KAKOE)+' поле')
    
    pole = [] 
    
    znah_1 = ZNAHENIE(1)
    znah_2 = ZNAHENIE(2)
    
    pole.append(znah_1)
    pole.append(znah_2)
    
    print('\n**** Получено поле '+str(KAKOE)+ ': '+ str(pole))
    print('\n-----')
    return pole


def FERS(pole_1,pole_2):  #создание шахматной доски с ферзём
    global D
    D[9 - pole_1[0]][pole_1[1]] = 'F'
    D[9 - pole_2[0]][pole_2[1]] = '@'
    
    cnisy = 8 - (9 - pole_1[0])
    cverhy = (9 - pole_1[0]) - 1

    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9: continue
            
            if i == (9 - pole_1[0]): 
                if j != pole_1[1]: 
                    if D[i][j] == '*' or D[i][j] == '|' or D[i][j] == '-': D[i][j] = '&'
                    else: D[i][j] = '-'
                
            if j == (pole_1[1]): 
                if i != (9 - pole_1[0]):
                    if D[i][j] == '*' or D[i][j] == '|' or D[i][j] == '-': D[i][j] = '&'
                    else: D[i][j] = '|'
                
            if i < (9-pole_1[0]):
                if j < pole_1[1]:
                    if j == (pole_1[1] - cverhy + (i-1)): 
                        if D[i][j] == '*' or D[i][j] == '|' or D[i][j] == '-': D[i][j] = '&'
                        else: D[i][j] = '*'
                else:
                    if j == (pole_1[1] + cverhy - (i-1)):
                        if D[i][j] == '*' or D[i][j] == '|' or D[i][j] == '-': D[i][j] = '&'
                        else: D[i][j] = '*'
            else:
                if j > pole_1[1]:
                    if j == (pole_1[1] + cnisy - (8-i)):
                        if D[i][j] == '*' or D[i][j] == '|' or D[i][j] == '-': D[i][j] = '&'
                        else: D[i][j] = '*'
                else:
                    if j == (pole_1[1] - cnisy + (8-i)):
                        if D[i][j] == '*' or D[i][j] == '|' or D[i][j] == '-': D[i][j] = '&'
                        else: D[i][j] = '*'
                    
                    
    if D[9 - pole_2[0]][pole_2[1]] != '@':
        value = True
        D[9 - pole_2[0]][pole_2[1]] = '@'
    else: value = False
    
    D[9 - pole_1[0]][pole_1[1]] = 'F'
    
    return value


def KON(pole_1,pole_2):  #создание шахматной доски с конем
    C = MATRIX()
    C[9 - pole_1[0]][pole_1[1]] = 'K'
    C[9 - pole_2[0]][pole_2[1]] = '@'

    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9: continue
            
            if i == ((9 - pole_1[0])-1) or i == ((9 - pole_1[0])+1):
                if j ==(pole_1[1]-2) or j == (pole_1[1]+2): C[i][j] = '*'
                
            if i == ((9 - pole_1[0])-2) or i == ((9 - pole_1[0])+2):
                if j ==(pole_1[1]-1) or j == (pole_1[1]+1): C[i][j] = '*'
                
    if C[9 - pole_2[0]][pole_2[1]] != '@':
        value = True
        C[9 - pole_2[0]][pole_2[1]] = '@'
    else: value = False
    C[9 - pole_1[0]][pole_1[1]] = 'K'
    PRINT_MATRIX(C) 
    return value


def LAD(pole_1,pole_2):  #создание шахматной доски с ладьей
    global E
    E[9 - pole_1[0]][pole_1[1]] = 'L'
    E[9 - pole_2[0]][pole_2[1]] = '@'

    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9: continue
        
            if i == (9 - pole_1[0]): 
                if j != pole_1[1]:
                    if E[i][j] != '|': E[i][j] = '-'
                    else: E[i][j] = '&'
                
            if j == (pole_1[1]): 
                if i != (9 - pole_1[0]):
                    if E[i][j] != '-': E[i][j] = '|'
                    else: E[i][j] = '&'
            
    if E[9 - pole_2[0]][pole_2[1]] != '@':
        value = True
        E[9 - pole_2[0]][pole_2[1]] = '@'
    else: value = False
    E[9 - pole_1[0]][pole_1[1]] = 'L'
     
    return value
    

def LADI(pole_1,pole_2):  #создание шахматной доски с двойным ходом ладьи
    global E
    E = MATRIX()
    
    lv_1 = LAD(pole_1,pole_2)
    
    if lv_1 != True:
        E = MATRIX()
        
        varianti = []
        
        LAD(pole_2,pole_1)
        LAD(pole_1,pole_2)
        
        for i in range(10):
            for j in range(10):
                if i == 0 or i == 9 or j == 0 or j == 9: continue
            
                if E[i][j] == '&':
                    var = []
                    var.append(9-i)
                    var.append(j)
                    varianti.append(var)
            
        PRINT_MATRIX(E)
        print('** Вариантов 1ого хода: '+str(len(varianti)))
        print('*** Варианты для 1ого хода: ' + str(varianti[0]) + '  и ' + str(varianti[1]))
    else:
        PRINT_MATRIX(E)
        print('** Решается 1м ходом')
    
    
def FERSI(pole_1,pole_2): #создание шахматной доски с двойным ходом ферзя
    global D
    D = MATRIX()
    
    lv_1 = FERS(pole_1,pole_2)
    
    if lv_1 != True:
        D = MATRIX()
        
        varianti = []
        
        FERS(pole_2,pole_1)
        FERS(pole_1,pole_2)
        
        for i in range(10):
            for j in range(10):
                if i == 0 or i == 9 or j == 0 or j == 9: continue
            
                if D[i][j] == '&':
                    var = []
                    var.append(9-i)
                    var.append(j)
                    varianti.append(var)
            
        PRINT_MATRIX(D)
        print('** Вариантов 1ого хода: '+str(len(varianti)))
        print('*** Варианты для 1ого хода: ')
        for i in range(len(varianti)):
            print('**** '+str(varianti[i]))
    else:
        PRINT_MATRIX(D)
        print('** Решается 1м ходом')


def SLON(pole_1,pole_2): #создание шахматной доски со слоном
    global F
    F[9 - pole_1[0]][pole_1[1]] = 'S'
    F[9 - pole_2[0]][pole_2[1]] = '@'
    
    cnisy = 8 - (9 - pole_1[0])
    cverhy = (9 - pole_1[0]) - 1

    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9 or j == 0 or j == 9: continue
            
                
            if i < (9-pole_1[0]):
                if j < pole_1[1]:
                    if j == (pole_1[1] - cverhy + (i-1)): 
                        if F[i][j] == '*': F[i][j] = '&'
                        else: D[i][j] = '*'
                else:
                    if j == (pole_1[1] + cverhy - (i-1)):
                        if F[i][j] == '*': F[i][j] = '&'
                        else: D[i][j] = '*'
            else:
                if j > pole_1[1]:
                    if j == (pole_1[1] + cnisy - (8-i)):
                        if F[i][j] == '*': F[i][j] = '&'
                        else: F[i][j] = '*'
                else:
                    if j == (pole_1[1] - cnisy + (8-i)):
                        if F[i][j] == '*': F[i][j] = '&'
                        else: F[i][j] = '*'
                    
                    
    if F[9 - pole_2[0]][pole_2[1]] != '@':
        value = True
        F[9 - pole_2[0]][pole_2[1]] = '@'
    else: value = False
    
    F[9 - pole_1[0]][pole_1[1]] = 'S'
    
    return value


def SLONI(pole_1,pole_2): #создание шахматной доски с двойным ходом слона
    global F
    F = MATRIX()
    
    lv_1 = SLON(pole_1,pole_2)
    
    if lv_1 != True:
        F = MATRIX()
        
        varianti = []
        
        SLON(pole_2,pole_1)
        SLON(pole_1,pole_2)
        
        for i in range(10):
            for j in range(10):
                if i == 0 or i == 9 or j == 0 or j == 9: continue
            
                if F[i][j] == '&':
                    var = []
                    var.append(9-i)
                    var.append(j)
                    varianti.append(var)
            
        PRINT_MATRIX(F)
        if len(varianti) != 0:
            print('** Вариантов 1ого хода: '+str(len(varianti)))
            print('*** Варианты для 1ого хода: ')
            for i in range(len(varianti)):
                print('**** '+str(varianti[i]))
        else:
            print('** Невозможно, так как слоны стоят на полях разного цвета')
    else:
        PRINT_MATRIX(F)
        print('** Решается 1м ходом')

               
def ABWGDE(): #выполнение задания а)-е)
    pole_1 = POLE(1)
    pole_2 = POLE(2)
    
    if pole_1 == pole_2: 
        print('\n***** Эти поля совпадают')
        return False
    
    print('\n* a) Являются ли поля 1 и 2 полями одного цвета?')
    zp_1 = A[9 - pole_1[0]][pole_1[1]]
    zp_2 = A[9 - pole_2[0]][pole_2[1]]
    if zp_1 == zp_2: print('** 1 и 2 поля одного цвета - ' + zp_1)
    else:  print('** 1 и 2 поля разного цвета:' + zp_1 + ' и ' + zp_2 )

    
    print('\n* б) На поле 1 расположен ферзь. Угрожает ли он полю 2?')
    global D
    D = MATRIX()
    fv = FERS(pole_1,pole_2) 
    PRINT_MATRIX(D) 
    if fv == True: print('** угрожает')
    else: print('** не угрожает')
    
    
    print('\n* в) На поле 1 расположен конь. Угрожает ли он полю 2?')
    kv = KON(pole_1,pole_2)
    if kv == True: print('** угрожает')
    else: print('** не угрожает')
    
    
    print('\n* г) Можно ли с поля 1 одним ходом ладьи попасть на поле 2. Если нет, то выяснить, как это можно сделать за два хода.')
    LADI(pole_1,pole_2)

    print('\n* д) Можно ли с поля 1 одним ходом ферзя попасть на поле 2. Если нет, то выяснить, как это можно сделать за два хода.')
    FERSI(pole_1,pole_2)
    
    print('\n* е) Можно ли с поля 1 одним ходом слона попасть на поле 2. Если нет, то выяснить, как это можно сделать за два хода.')
    SLONI(pole_1,pole_2)
    
    
def OTVET(): #запрос дейсвия
    i = True
    while i == True:
        print('\n-----')
        otvet = input('* Действие: ')
            
        if  otvet.isdigit() == True:
            otvet = int(otvet)
            if 0 <= otvet <= 2: break
            else:
                print('\n** Число не попадает в диапазон действий!')
                continue
        else:
            print('\n** Необходимо целое число!')
            continue
    print('\n-----')
    return otvet
    
    
go = True
while go == True: #цикл запросов программы
    print('\n----------')
    print('0-выход')
    print('1-показать шахматную доску')
    print('2-выполнение задания')

    otvet = OTVET()
    
    if otvet == 0: break
    
    if otvet == 1: PRINT_MATRIX(A)
    
    if otvet == 2: ABWGDE()
        
