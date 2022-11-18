# Oppgave 15: Ballens fluktparabel uten luftmotstand 
# (25 poeng) 

import math # cosinus, sinus, og PI 
import matplotlib.pyplot as plt # plot 

# Gravitasjonsakselerasjonskonstanten og v0 
g = 9.81 
startfart = 20     

# Instruks 1 
min_tidssekvens = [tall / 100 for tall in range(0, 505, 5)] 

''' # Alternativt: 
min_tidssekvens = [] 

for i in range(0, 505, 5): 
    min_tidssekvens.append(i / 100)
'''

# Instruks 2 
def calc_x(tidssekvens, vinkel): 
    pos_x = [] # sekvens av x-posisjoner 
    for t in tidssekvens: 
        pos_x.append(startfart * t * math.cos(vinkel)) 
    return pos_x 

def calc_y(tidssekvens, vinkel): 
    pos_y = [] # sekvens av y-posisjoner 
    for t in tidssekvens: 
        pos_y.append(startfart * t * math.sin(vinkel) - (1/2 * g * t**2)) 
    return pos_y

# Instruks 3 
vinkelverdier = [30, 45, 60] 
for vinkel in vinkelverdier:        # Løkke over 30, 45 og 60 grader 
    rad = vinkel * math.pi/180      # Konvertere vinkelen til radianer 
    
    x = calc_x(min_tidssekvens, rad) # Alle verdier for x 
    y = calc_y(min_tidssekvens, rad) # Alle verdier for y

                # X OG Y, over bakken. 
    bane_x = [] # Lagrer x, når y > 0
    bane_y = [] # Lagrer y, når y > 0

    for i in range(len(y)): 
        if y[i] > 0: 
            bane_x.append(x[i]) 
            bane_y.append(y[i])       
        
    plt.plot(bane_x, bane_y, ".")

# Instruks 4 
plt.legend(['30°', '45°', '60°'])       # Fargeforklaring (legend) 
plt.title('Trajectories. v0 = 20 m/s')  # Tittel 
plt.xlabel('distance / m')              # x-aksetittel
plt.ylabel('height / m')                # y-aksetittel
plt.show()                            

''' # Bonus, listekomprehensjon 
plt.legend([str(theta) + '°' for theta in vinkelverdier]) 
'''

# Instruks 5 
plt.savefig('trajectory.png')           