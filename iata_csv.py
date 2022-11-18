### Airport map: 25 pt


import csv
import matplotlib.pyplot as plt

large = [] # [(lat, lon, iata_code)]
medium = [] # [(lat, lon)]
with open('airport-codes.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for line in reader:
        type = line[1]
        iata_code = line[9]
        coords = line[11]
        lat, lon = map(float,coords.split(','))
        
        if type == "large_airport":
            large.append((lat, lon, iata_code))
        elif type == "medium_airport":
            medium.append((lat, lon))
            
# print(large[:5], medium[:5])

lats, lons, _ = zip(*large)
plt.plot(lons, lats, 'oy')

lats, lons = zip(*medium)
plt.plot(lons, lats, '.y')

for lat, lon, iata in large:
     plt.annotate(iata, (lon, lat))

plt.title('Airports')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# plt.savefig("airports.png")
plt.show()
