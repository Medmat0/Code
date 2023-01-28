from collections import Counter
from matplotlib import pyplot as plt

import random

def generate_random_graph(n, p):
  # Initialisation de la liste d'adjacence
  adj = [[] for _ in range(n)]
  # Génération des arêtes du graphe de manière aléatoire
  for i in range(n):
    for j in range(i+1, n):
      if random.random() < p:
        adj[i].append(j)
        adj[j].append(i)
  return adj

# Nombre de sommets du graphe
n = int(input("number"))


# Probabilité p
p = 0.5

# Initialisation de la liste d'adjacences
adjacency_list = generate_random_graph(n, p)

# Affichage de la liste d'adjacences
print(adjacency_list)

def max_degree(adjacency_list):
  # Initialisation du degré maximum à 0
  max_degree = 0

  # Parcours de tous les sommets du graphe
  for i in range(len(adjacency_list)):
    # Calcul du degré du sommet i
    degree = len(adjacency_list[i])
    # Mise à jour du degré maximum si nécessaire
    max_degree = max(max_degree, degree)

  return max_degree

max_deg = max_degree(adjacency_list)
print(max_deg)

# Question 2 PARTIE1

# Initialisation de l'objet Counter
degrees = Counter()

# Parcours de tous les sommets du graphe
for i in range(len(adjacency_list)):
  # Ajout du degré du sommet i dans l'objet Counter
  degrees[len(adjacency_list[i])] += 1


# Récupération des degrés et des occurences
x, y = zip(*degrees.items())

# Création du graphique
plt.bar(x, y)

# Ajout des étiquettes aux abscisses
plt.xticks(x)

# Ajout de l'étiquette à l'axe des ordonnées
plt.ylabel('Number of vertices')

# Affichage du graphique
plt.show()


# Question 3 PARTIE1

def count_induced_paths_of_length_2(adjacency_list):
  # Initialisation du compteur de chemins de longueur 2 à 0
  count = 0

  # Parcours de tous les sommets du graphe
  for u in range(len(adjacency_list)):
    # Parcours de tous les voisins du sommet u
    for v in adjacency_list[u]:
      # Si le sommet v n'est pas un voisin du sommet u, cela signifie qu'il n'y a pas d'arête entre u et v
      # et donc que le chemin u -> v forme un chemin induit de longueur 2
      if u not in adjacency_list[v]:
        count += 1

  return count

  

# Algorithme de Bron-Kerbosch avec pivot pour énumérer les cliques maximales
def bron_kerbosch_with_pivot(adj, r, p, x):
  # Si le sous-graphe p est vide, on ajoute la clique r à la liste des cliques maximales
  if not p and not x:
    cliques.append(r)
  # Sinon, on parcourt chaque sommet du sous-graphe p
  else:
    # Sélection du pivot
    pivot = p.union(x).pop()
    # Parcours des sommets du sous-graphe p sans le pivot
    for v in p - {pivot}:
      # Ajout du sommet v à la clique r et appel récursif de l'algorithme
      bron_kerbosch_with_pivot(adj, r.union({v}), p.intersection(adj[v]), x.intersection(adj[v]))
      # Suppression du sommet v du sous-graphe p
      p = p - {v}
      # Ajout du sommet v au sous-graphe x
      x = x.union({v})

# Génération d'un graphe aléatoire avec 10 sommets et une probabilité de 0.5 pour chaque arête
adj = adjacency_list

# Initialisation de la liste des cliques maximales
cliques = []

# Appel de l'algorithme de Bron-Kerbosch avec pivot sur le graphe
bron_kerbosch_with_pivot(adj, set(), set(range(10)), set())

# Affichage de la liste des cliques maximales
print("les cliques :",cliques)
 
def compute_induced_bicliques(adjacency_list):
  # Initialisation de la liste des bicliques maximales induites
  induced_bicliques = []

  # Construction de la liste des sommets du graphe
  vertices = set(range(len(adjacency_list)))

  # Initialisation de la liste des cliques maximales
  cliques = []

  # Appel de l'algorithme de Bron-Kerbosch avec pivot pour énumérer les cliques maximales
  bron_kerbosch_with_pivot(adjacency_list, set(), vertices, set())

  # Parcours de toutes les cliques maximales
  for clique in cliques:
    # Construction du sous-graphe induit par la clique
    induced_subgraph = [set(adjacency_list[v]) & clique for v in clique]

    # Appel de l'algorithme de Bron-Kerbosch avec pivot pour énumérer les cliques maximales du sous-graphe induit
    bron_kerbosch_with_pivot(induced_subgraph, set(), clique, set())

    # Ajout des bicliques maximales induites à la liste
    induced_bicliques += [c for c in cliques if len(c) == 2]

  return induced_bicliques

# Appel de la fonction pour trouver les bicliques maximales induites
induced_bicliques = compute_induced_bicliques(adjacency_list)

# Affichage des bicliques maximales induites

print("les bicliques sont :",induced_bicliques)




