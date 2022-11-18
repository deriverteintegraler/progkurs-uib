import csv
from collections import Counter

def mandatfordeling(datafile, N_seats):
    distrikt = {}
    with open(datafile, newline='', encoding='utf8') as f:
        data = csv.reader(f)
        next(data)
        for name, people, area in data:
            distrikt[name] = float(people) + 1.8 * float(area)

    factors = list(range(1, N_seats, 2))

    ranking = []
    for d_name, count in distrikt.items():
        for f in factors:
            ranking.append((count/f, d_name))
    ranking.sort(reverse=True)

    print(ranking)

    chosen = [name for _,name in ranking[:N_seats]]
    return Counter(chosen)


seats = mandatfordeling("valgdistrikt_2020-01-01.csv", 169)
print("Distrikt      Mandater")
print('=' * 22)
for k,v in seats.items():
    print(f"{k:18} {v:3d}")
