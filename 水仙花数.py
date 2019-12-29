


for i in range(100,1000):
    l = list(map(int,str(i)))
    if sum(x**3 for x in l) == i:
        print(i)




for i in range(100,1000):
    if sum(x**3 for x in list(map(int,str(i)))) == i:
        print(i)

print(int('1235'))