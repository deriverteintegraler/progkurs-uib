### Airport map: 25 pt
#

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    'airport-codes.csv',
    usecols = ['type', 'iata_code', 'coordinates'],
)
data['type'] = data['type'].astype("category")

#print(data.columns)

data['lat'] = data.coordinates.apply(lambda x: float(x.split(',')[0]))
data['lon'] = data.coordinates.apply(lambda x: float(x.split(',')[1]))

sizemap = {
    'large_airport' : 30,
    'medium_airport' : 5,
}
data['size'] = data.type.map(sizemap)
data.plot.scatter(x='lon', y='lat', s='size', c='orange')

# or
# large = data[data.type == 'large_airport']
# medium = data[data.type == 'medium_airport']
# ... usual plt.plot(large['lon'], large['lat'], 'oy')

for _,row in data[data.type == 'large_airport'].iterrows():
    plt.annotate(row['iata_code'],(row['lon'],row['lat']))

plt.title('Airports')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# plt.savefig("airports.png")
plt.show()
