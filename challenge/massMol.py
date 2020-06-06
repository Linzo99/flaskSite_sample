# Linzo99
import re 
with open('source.txt', 'r') as source:
	donnee = source.readlines()

#dictionnaire contenant la masse molaire de chaque atom
masses = {}
list_atom = []
for ele in donnee:
	m, v = ele.split()
	masses[m] = float(v)

entree = input("Entrez la molecule : ")
#on utilise une expression reguliere
atomes = [*re.findall('([A-Z][a-z]?)?([0-9]?)', entree)]
atomes.pop()

nb_atom = {at[0]:int(at[1]) if at[1].isdigit() else 1 for at in atomes}

print(nb_atom)
masse_mol = sum([masses[x]*nb_atom[x] for x in nb_atom.keys()])
print(masse_mol)

