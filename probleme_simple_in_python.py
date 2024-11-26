"""
Student MUNTEANU GEORGE CIPRIAN
IFR anul 2
Grupa 2
"""



# Problema 1
def suma_nr_1_100():
    x = 0
    for i in range(1,101):
        print(i,"  ",x)
        x=x+i
suma_nr_1_100()

# Problema 2
def afisare_nr_impare():
    x = 1
    y = 1
    while x <= 20:
        if y%2 != 0:
            print("Numar impar ", x, " este: ",y)
            y+=1
            x+=1
        else:
            y+=1           
afisare_nr_impare()

# Problema 3
def cel_mai_mare_divizor():
    n1 = int(input("Introdu primul numar:   "))
    n2 = int(input("Introdu al doile numar:   "))
    x = n1
    y = n2
    while x > 0 and y > 0:
        if n1%x != 0:
            x-=1 
        elif x == y == 1:
            print("Nu exista divizor comun")
            break  
        else:  
            if n2%y == 0 and y == x:
                print("Divizorul comun este:  ",y)
                break
            elif y > 1:
                y-=1
            elif y == 1 and x > 1:
                x-=1
                y=n2
cel_mai_mare_divizor()

# Problema 4
def numar_prim():
    p = int(input("Introdu un nr. pt a verifica daca este prim:  "))
    a = p-1
    b = []
    if p == 0:
        print("Numarul ales ", p, " nu este prim.")
    elif p == 1:
        print("Numarul ales ", p, " este prim.") 
    else:
        while a > 1:
            if p%(a) != 0 and a > 1:
                a-=1
            else:
                b.append(a)
                a-=1
        if len(b) > 0:
            print("Numarul ",p," nu este prim.")
        else:
            print("Numarul ",p," este prim.")
numar_prim()

# Problema 5
def suma_si_medie_list_nr():
    l = []
    suma = 0
    media = 1
    if len(l) == 0:
        elemente = int(input("Introdu numarul de elemente dorite:  "))
        while len(l) < elemente and elemente > 0:
            l.append(int(input("Introdu numerele pentru a fi calculate suma si media:  ")))
        for i in l:
            suma = suma + i
            media = (media * i)/(len(l))
        print("Suma este: ", suma)
        print("Media este: ",media)
suma_si_medie_list_nr()

# Program 6
def triunghi():
    unghi1 = int(input("Adauga unghiul 1      "))
    unghi2 = int(input("Adauga unghiul 2      "))
    unghi3 = int(input("Adauga unghiul 3      "))
    if unghi1 > 0 and unghi2 > 0 and unghi3 > 0:
        # Verificăm dacă suma unghiurilor este 180
        if unghi1 + unghi2 + unghi3 == 180:
            print( "Unghiurile pot forma un triunghi.")
        else:
            print ("Unghiurile nu pot forma un triunghi (suma diferită de 180).")
    else:
        print ("Unghiurile nu pot forma un triunghi (un unghi este mai mic sau egal cu 0).")
triunghi()

#program 8
def ziua_saptamanii():
    a = int(input("Alege ziua saptamanii de la 1 la 7:     "))
    lista =["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
    print("Ziua aleasa este:  ",lista[a-1])
ziua_saptamanii()

#program 9
def max_vector():
    valori = input("Introduceti elementele vectorului, separate prin spatii: ")
    vector = [int(u) for u in valori.split()]
    maxim = vector[0]
    for nums in vector:
        if nums > maxim:
            maxim = nums
    print("Maximul este:   ", maxim)
max_vector()