def make_stats(matches):
    teams = {} # dict of dicts: name -> {GF, GA, GD, PT}
    for name_A, name_B, score_A, score_B in matches:
        if name_A not in teams:
            teams[name_A] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
        if name_B not in teams:
            teams[name_B] = {'GF':0, 'GA':0, 'GD':0, 'PT':0}
        
        if score_A > score_B:
            teams[name_A]['PT'] += 3
        elif score_B > score_A:
            teams[name_B]['PT'] += 3
        else:
            teams[name_A]['PT'] += 1
            teams[name_B]['PT'] += 1

        teams[name_A]['GF'] += score_A
        teams[name_B]['GF'] += score_B
              
        teams[name_A]['GA'] += score_B
        teams[name_B]['GA'] += score_A        
        
        teams[name_A]['GD'] += score_A - score_B
        teams[name_B]['GD'] += score_B - score_A

    return teams




# an example for the "matches" datastructure
FIFA_1998_A = [
    ("Brazil", "Scotland", 2, 1),
    ("Morocco", "Norway", 2, 2),
    ("Scotland", "Norway", 1, 1),
    ("Brazil", "Morocco", 3, 0),
    ("Brazil", "Norway", 1, 2),
    ("Scotland", "Morocco", 0, 3),
]

# make_stats(FIFA_1998_A) takes this ^^^^ 
# and the return value should be 

FIFA_1998_A_data = { 
    'Brazil': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6}, 
    'Scotland': {'GF': 2, 'GA': 6, 'GD': -4, 'PT': 1},
    'Morocco': {'GF': 5, 'GA': 5, 'GD': 0, 'PT': 4},
    'Norway': {'GF': 5, 'GA': 4, 'GD': 1, 'PT': 5}
}


if make_stats(FIFA_1998_A) == FIFA_1998_A_data:
    print("make_stats looks good, you can remove the exit() line now!\n\n\n")
else:
    print("Something is wrong in make_stats")

# If teams were level on points, they were ranked on the following criteria in order:
# 
# Greatest total goal difference in the three group matches
# Greatest number of goals scored in the three group matches
# Most points earned in matches against other teams in the tie
# Greatest goal difference in matches against other teams in the tie
# Greatest number of goals scored in matches against other teams in the tie
# Drawing of lots

def compare(matches, data, a, b):
    for crit in ['PT','GD','GF']:
        if data[a][crit] > data[b][crit]:
            #print(a,b,crit)
            return 1
        elif data[a][crit] < data[b][crit]:
            #print(b,a,crit)
            return -1
    # find match
    for nx, ny, x, y in matches:
        if nx == b and ny == a:
            nx,ny = ny,nx
            x,y = y,x
        if nx == a and ny == b:
            #print(a,b,f'{x}:{y}')
            if x > y:
                return 1
            elif y > x:
                return -1
            print("LOTTERY",a,b)
            return 0
    assert False, "Should never get here"

######################################################
######################################################
######################################################

FIFA_1994_D = [
    ("Argentina", "Greece", 4, 0),
    ("Nigeria", "Bulgaria", 3, 0),
    ("Argentina", "Nigeria", 2, 1),
    ("Bulgaria", "Greece", 4, 0),
    ("Argentina", "Bulgaria", 0, 2),
    ("Greece", "Nigeria", 0, 2),
]

FIFA_1994_D_data = {
    'Argentina': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6}, 
    'Greece': {'GF': 0, 'GA': 10, 'GD': -10, 'PT': 0}, 
    'Nigeria': {'GF': 6, 'GA': 2, 'GD': 4, 'PT': 6}, 
    'Bulgaria': {'GF': 6, 'GA': 3, 'GD': 3, 'PT': 6},
}

FIFA_1994_E = [
    ("Italy", "Ireland", 0, 1),
    ("Norway", "Mexico", 1, 0),
    ("Italy", "Norway", 1, 0),
    ("Mexico", "Ireland", 2, 1),
    ("Italy", "Mexico", 1, 1),
    ("Ireland", "Norway", 0, 0),
]

FIFA_1994_E_data = {
    'Italy': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 4}, 
    'Ireland': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 4}, 
    'Norway': {'GF': 1, 'GA': 1, 'GD': 0, 'PT': 4}, 
    'Mexico': {'GF': 3, 'GA': 3, 'GD': 0, 'PT': 4},
}


FIFA_1990_F = [
    ("England", "Ireland", 1, 1),
    ("Netherlands", "Egypt", 1, 1),
    ("England", "Netherlands", 0, 0),
    ("Ireland", "Egypt", 0, 0),
    ("England", "Egypt", 1, 0),
    ("Ireland", "Netherlands", 1, 1),
]

FIFA_1990_F_data = {
    'England': {'GF': 2, 'GA': 1, 'GD': 1, 'PT': 5}, 
    'Ireland': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 3}, 
    'Netherlands': {'GF': 2, 'GA': 2, 'GD': 0, 'PT': 3}, 
    'Egypt': {'GF': 1, 'GA': 2, 'GD': -1, 'PT': 2},
}

from functools import cmp_to_key, partial

def pretty(order, data):
    print(f"{' ':14} {'GF':>3} {'GA':>3} {'GD':>3}   {'PT':>3}")
    for team in order:
        k = team
        v = data[team]    
        print(f"{k:14} {v['GF']:3d} {v['GA']:3d} {v['GD']:3d}   {v['PT']:3d}")
    print("-"*20)

all_groups = [FIFA_1998_A, FIFA_1994_D, FIFA_1994_E, FIFA_1990_F]
all_data = [FIFA_1998_A_data, FIFA_1994_D_data, FIFA_1994_E_data, FIFA_1990_F_data]

expected = [
    ['Brazil', 'Norway', 'Morocco', 'Scotland'],
    ['Nigeria', 'Bulgaria', 'Argentina', 'Greece'],
    ['Mexico', 'Ireland', 'Italy', 'Norway'],
    ['England', 'Ireland', 'Netherlands', 'Egypt'],
]

for matches,data,ex in zip(all_groups,all_data,expected):
    order = sorted(data, key=cmp_to_key(partial(compare,matches,data)), reverse=True)
    pretty(order, data)
    if order == ex:
        print("This looks good!\n\n\n")
    else:
        print("!!! expected {ex}, but got {order}")
        
    
