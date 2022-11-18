import csv

### part a) ###

fylker = {}
kommuner = {}

all_kommuner = [] # for part b)

with open('NO_ADM12.csv', newline='', encoding='utf8') as f:
    data = csv.reader(f, delimiter=';')
    for line in data:
        #print(line[5])
        _,name,_,_,_,feature,_,adm1code,_,pop,_ = line
        if feature == 'ADM1':
            fylker[adm1code] = name
        elif feature == 'ADM2':
            kommuner.setdefault(adm1code, [])
            kommuner[adm1code].append((name,pop))
            all_kommuner.append((int(pop),name)) # for part b)

### part b) ###

pop_sorted = sorted(all_kommuner)

print('The 5 smallest kommuner')
for pop, name in pop_sorted[:5]:
    print(f'{name:20}{pop:6d}')

print('The 5 largest kommuner')
for pop, name in pop_sorted[-5:]:
    print(f'{name:20}{pop:6d}')

### part c) ###

def print_fylke(num):
    koms = kommuner[num]
    print('='*26)
    print(num, fylker[num])
    print('='*26)
    for name, pop in sorted(koms):
        pop = int(pop)
        print(f'{name:20}{pop:6d}')


### part d) ###

while True:
    wanted = input("Search word (q to quit)? ")
    if wanted == 'q':
        break

    code = None
    for adm1code, fylke in fylker.items():
        if wanted.lower() in fylke.lower():
            code = adm1code
            break
    
    if code is None:
        print("Not found. Try again")
        # print("Possible options:")
        # for fylke in sorted(fylker.values()):
        #     print(fylke)
        continue

    print_fylke(code)
    
