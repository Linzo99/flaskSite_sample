import random
import numpy as np
import matplotlib.pyplot as plt


TAILLE = 15 # Taille de la grille 
P = 800 # Nombre de pas
N_MAX = 20 # Nombre max de jour pour guerir
NB_JOUR = 200 # Nombre de jour pour la sumilation
NB_ML_INIT = 50 # Nombre initial de malade
P_MOVE = 0.9 # la probabilité de se déplacer
P_CONT = 0.06 # la probabilité d'être contaminer

def creation(nb_habit, dim, nb_malad):
	liste = []
	for i in range(nb_habit):
		# on choisit aléatoirement les coordonnées
		x,y = [random.randint(0, dim), random.randint(0, dim)]
		liste.append([x, y, -1])

	# initiation du nombre de malade
	for i in range(nb_malad):
		liste[i][-1] = 0

	return liste

def deplacement(liste, p_move):
	for habit in liste:
		#pour chaque habitant on choisit de deplacer ou non selon la probabilité
		move = np.random.choice([0, 1], p=[1-p_move, p_move])
		if move and (-1 < habit[0] < TAILLE) and (-1 < habit[1] < TAILLE) :
			x_pos = list(np.add(habit[0], [-1, 0, +1]))
			y_pos = list(np.add(habit[1], [-1, 0, +1]))
			# les different mouvement possibles
			available = [[x, y] for x in x_pos for y in y_pos]
			available.remove([habit[0], habit[1]])
			#on choisit aléatoirement un mouvement
			movement = random.choice(available) 
			habit[0], habit[1] = movement	

	return liste

def evolution(liste, n_max):
	for habit in liste:
		if 0 <= habit[-1] < n_max:
			habit[-1] += 1

	return liste

def contagion(liste, dim, p_cont, n_max):
	# on recupere les malades et leur position
	malade = list(filter(lambda x : 0 <= x[-1] < n_max , liste))
	malade_pos = [hab[:-1] for hab in malade]
	for ind in liste:
		# On vérifie si la personne est malade ou est guéris
		if ind not in malade and ind[-1] != n_max:
			if ind[:-1] in malade_pos:
				cont = np.random.choice([0, 1], p=[1-p_cont, p_cont])
				if cont:
					ind[-1] = 0

	return liste


def statistiques(liste, n_max):
	j_malade = len(list(filter(lambda x : x[-1] == -1, liste)))
	malades = len(list(filter(lambda x : -1 < x[-1] < n_max, liste)))
	gueris = len(list(filter(lambda x : x[-1] == n_max, liste)))

	return j_malade, malades, gueris


population = creation(P, TAILLE, NB_ML_INIT)
cas = {'j_malade' : [], 'malades': [], 'gueris': []}

for _ in range(NB_JOUR):
	update = deplacement(population, P_MOVE)
	evolu = evolution(update, N_MAX)
	conta = contagion(evolu, TAILLE, P_CONT, N_MAX)
	j_m, m, g = statistiques(conta, N_MAX)
	cas['j_malade'].append((j_m*100)/P)
	cas['malades'].append((m*100)/P)
	cas['gueris'].append((g*100)/P)


fig, ax = plt.subplots()
ax.plot(cas['j_malade'], label='jamais malade')
ax.plot(cas['malades'], label='malades')
ax.plot(cas['gueris'], label='gueris')
plt.ylabel('Population %')
plt.xlabel('Temps(nombre de pas)')
ax.legend()

plt.show()
