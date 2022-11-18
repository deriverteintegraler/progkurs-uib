# Oppgave 13: Bedre filnavn på datafiler (YYYY-MM-DD_PLACENAME.txt) 
# (25 poeng) 

old_names = ["qwghlm.txt", "qwerty.txt"] 

def write_new_file(data, filename): 
    with open(filename, "w") as f: 
        f.writelines(data) 

for old_file in old_names:          # Henter innholdet i filen, stedsnavn og dato. 
    with open(old_file, "r") as f: 
        data = f.readlines()        # Innholdet i filen 

    placename = data[0].strip() # Stedsnavn 
    date = data[1].strip()      # Dato
    new_name = date + "_" + placename + ".txt"

    write_new_file(data, new_name) 
