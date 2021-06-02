import random
import math
import numpy as np

def create_cromosome():
    kromosom=[]
    for j in range(10):
        kromosom.append(random.randint(0,9))
    return kromosom

def separate_x(k):
    kromosom_x=[]
    j = len(k)
    for i in range(j//2,j):
        kromosom_x.append(k[i])
    return kromosom_x

def separate_y(k):
    kromosom_y=[]
    j = len(k)
    for i in range(j//2,j):
        kromosom_y.append(k[i])
    return kromosom_y

def sigma():
    nilai=0
    for i in range(5):
        nilai+=(9*10**(-(i+1)))
    return nilai

def gen(kromosom):
    g = 0
    for i in range (0,5):
        g += (kromosom[i]*(10**(-(i+1))))
    return g

def decode_kromosom(b,a,g):
    nilai = b+(((a-b)/sigma())*g)
    return nilai

def decode_indiv(krom):
    x = decode_kromosom(-1,2,gen(separate_x(krom)))
    y = decode_kromosom(-1,1,gen(separate_y(krom)))
    return {'krom':krom,'fitness':fitness(x,y)}

def fungsi(x,y):
    return ((math.cos(x*x)*math.sin(y*y))+(x+y))

def fitness(x,y):
    return fungsi(x,y)

def create_population(n):
    populasi=[]
    for i in range (n):
        krom = create_cromosome()
        x = decode_kromosom(-1,2,gen(separate_x(krom)))
        y = decode_kromosom(-1,1,gen(separate_y(krom)))
        individual = {'krom':krom,'fitness':fitness(x,y)}
        populasi.append(individual)
    #print(populasi)
    return populasi

def tournament_selection(populasi):
    #mengambil parent dari populasi
    size = 8
    pop_tour = sorted(np.random.choice(populasi, size, replace=True),key=lambda x:x['fitness'])
    #print(pop_tour)
    hus = pop_tour[len(pop_tour)-1]
    wif = pop_tour[len(pop_tour)-2]
    #for i in range (len(pop_tour)):
    #    print(pop_tour[i])
    #print("hus", hus,"wif", wif)
    return hus,wif

def separate(k,n):
    up =[]
    down=[]
    for i in range(len(k)):
        if (i<n):
            up.append(k[i])
        else :
            down.append(k[i])
    #print("Up=", up, "down = ", down)
    return {'up':up,'down':down}

def single_crossover(individual_a, individual_b):
    #crossover untuk parent
    n = 2
    a = separate(individual_a,n)['up']
    b = separate(individual_b,n)['up']
    a.extend(separate(individual_b,n)['down'])
    b.extend(separate(individual_a,n)['down'])
    return a,b

def mutasi(kromosom):
    #mutasi untuk parent
    new_kromosom=[]
    new_kromosom.extend(kromosom)
    #print("kr",len(kromosom),"newkr",len(new_kromosom))
    i = random.randint(1,9)
    n = random.randint(0,9)
    while n == kromosom[i]:
      n = random.randint(0,9)
    new_kromosom[i] = n
    return new_kromosom

def steady_state(populasi,generasi_baru):
    #seleksi survivor
    #print("Min Genererasi baru : ", min([individual for individual in generasi_baru], key=lambda x: x['fitness']))
    generasi_baru.remove(min([individual for individual in generasi_baru], key=lambda x: x['fitness']))
    #print("Max Genererasi baru : ", max([individual for individual in generasi_baru], key=lambda x: x['fitness']))
    generasi_baru.append(max([individual for individual in populasi], key=lambda x: x['fitness']))
    return generasi_baru

batascrossover = 0.7
batasmutasi = 0.01
generasi = 60
nilai_populasi = 100
populasi = create_population(nilai_populasi)
"""
parent1, parent2 = tournament_selection(populasi)
print("----------------------------------steady_state----------------------------------")
print("Hasil steady_state = ",steady_state(populasi))
print("----------------------------------POPULASI----------------------------------")
for i in range (len(populasi)):
    print("Kromosom ke - ",i+1," = ",populasi[i])
print("----------------------------------TOURNAMENT----------------------------------")
print("Parent 1 =",parent1)
print("Parent 2 =",parent2)
print("----------------------------------Crossover----------------------------------")
anak1, anak2 = single_crossover(parent1['krom'],parent2['krom'])
print("------------------------ANAK PERTAMA------------------------")
print("Anak pertama hasil crossover = ",anak1)
print("Hasil mutasi anak pertama    = ", mutasi(anak1))
print("------------------------ANAK KEDUA------------------------")
print("Anak kedua hasil crossover = ",anak2)
print("Hasil mutasi anak kedua    = ", mutasi(anak2))
#print(populasi)
"""
#PROSES GA

#generasi_baru = []
best_case=[]
best_case.append(max(populasi, key=lambda x:x['fitness']))
#print(best_case)
for i in range (generasi):  
    #print("---------------------------------Generasi {i}----------------------------------------")
    generasi_baru=[]
    generasi_baru = create_population(nilai_populasi-2)
    probcross = random.random()
    probmutasi = random.random()
    parent1, parent2 = tournament_selection(populasi)
    if (probcross <= batascrossover):
        anak1, anak2 = single_crossover(parent1['krom'],parent2['krom'])
        #print("Anak 1 xover=",anak1)
        if(probmutasi <= batasmutasi):
            anak1 = mutasi(anak1)
            anak2 = mutasi(anak2)
        generasi_baru.append(decode_indiv(anak1))
        generasi_baru.append(decode_indiv(anak2))
    else :
        generasi_baru.append(parent1)
        generasi_baru.append(parent2)
    """
    print("New gen",generasi_baru)
    print("best case: ",best_case[1]['fitness'])
    print(generasi_baru)
    for i in range (len(generasi_baru)):
        print("Kromosom ke - ",i+1," = ",generasi_baru[i])
    print("\n----------------------------------steady_state----------------------------------")
    """
    generasi_baru = steady_state(populasi,generasi_baru)
    populasi = generasi_baru
    best_case.append(max(populasi, key=lambda x:x['fitness']))

best = []
for i in range (len(best_case)):
    best.append(best_case[i]['fitness'])
    #print("best",best_case[i]['fitness'])
print("--------------------------HASIL-------------------------")
print("Kromosom terbaik :",best_case[len(best_case)-1]['krom'])
print("Nilai x terbaik :",decode_kromosom(-1,2,gen(separate_x(best_case[len(best_case)-1]['krom']))))
print("Nilai y terbaik :",decode_kromosom(-1,1,gen(separate_y(best_case[len(best_case)-1]['krom']))))
print("Fitness terbaik :",best_case[len(best_case)-1]['fitness'],"\n")
import matplotlib.pyplot as plt
fig = plt.figure()
fig.suptitle('Grafik Nilai Fitness Terbaik', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_ylabel('Nilai Fitness')
ax.set_xlabel('Generasi')
 
plt.plot(best)
plt.show()

    


"""
populasi =create_population(15)
print(populasi)
print("======================")
print(max(populasi))
tournament_selection(populasi)
hus =tournament_selection(populasi)['hus']
wif = tournament_selection(populasi)['wif']
cx = single_crossover(hus['krom'],wif['krom'])
print("setelah cross over ", cx['anak1'])
print("setelah mutasi ", mutasi(cx['anak1']))


k = create_cromosome()
x = decode_kromosom(-1,2,gen(separate_x(k)))
y = decode_kromosom(-1,1,gen(separate_y(k)))
print("Nilai x=",x,"nilai y=",y)
print("Fitness : ",fitness(x,y))
"""