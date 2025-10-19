numbers= [str(_) for _ in range(1,int(input())+1)]
slovar = {}
for n in numbers:
    slovar[sum(map(int,list(n)))] = slovar.get(sum(map(int,list(n))),0)+1

print(max(slovar.values()))
