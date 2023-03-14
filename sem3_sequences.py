#%% Les modules

import random
print(random)
dir(random)
help(random)
dir(random)
# *ou bien*
help(random.randint)# calcule un entier ou hasard

random.randint(1, 100)


#%% Set the wd
from os import chdir, getcwd
wd=getcwd()
chdir(wd)

#%% Les fichiers
f = open(r'\spam.txt','w+', encoding= 'utf8') # on crée un fichier
# mettre le r'C: pour que le \t ne soit pas interprété comme une tabulation
# w pour ouvrir en écriture
# r pour ouvrir en lecture

for i in range(100):
    f.write(f"ligne {i+1}\n")

f.close() # ne pas oublier de fermer le fichier
#\n permet qu'il passe à la ligne après avoir écrit chaque itération
# i+1 pcq numérotation commence à 0

%edit \spam.txt

f = open(r'.\spam.txt','r+', encoding= 'utf8')
f2 = open(r'.\spam2.txt','w+', encoding= 'utf8')
for line in f:
    line = line.split()
    line[0] = line[0].upper()
    f2.write(",".join(line) + "\n")
f.close()
f2.close()
%edit \spam.txt
%edit \spam2.txt

with open(r'.\spam.txt', 'r', encoding= 'utf8') as f:
    for line in f:
        print(line)
# with permet d'ouvrir un contexte manager qui permet d'éxécuter un protocole
# pour fermer les fichiers automatiquement au lieu de devoir f.close()
# il a ouvert le fichier, print les lignes et fermé

with open(r'.\spam.bin', 'w+b') as f:
    for i in range(100):
        f.write(b'\x3d')
        
# mode binaire et écriture

#%% Exercices

# avec un `with' on garantit la fermeture du fichier
with open("./foo.txt", "w", encoding='utf-8') as sortie:
    for i in range(2):
        sortie.write(f"{i}\n")
        
# on ouvre le fichier en mode 'a' comme append (= ajouter)
with open("foo.txt", "a", encoding='utf-8') as sortie:
    for i in range(100, 102):
        sortie.write(f"{i}\n")

# maintenant on regarde ce que contient le fichier
# remarquez que sans 'mode', on ouvre en lecture seule
with open("foo.txt", encoding='utf-8') as entree: 
    for line in entree:
        # line contient déjà un retour à la ligne
        print(line, end='')
        
# un fichier est son propre itérateur
        
with open("foo.txt", encoding='utf-8') as entree:
    print(entree.__iter__() is entree)       
        
# Si l'on essaie d'écrire deux boucles imbriquées
# sur le même objet fichier, le résultat est inattendu
with open("foo.txt", encoding='utf-8') as entree:
    for l1 in entree:
        # on enlève les fins de ligne
        l1 = l1.strip()
        for l2 in entree:
            # on enlève les fins de ligne
            l2 = l2.strip()
            print(l1, "x", l2)
            
#%% le module pathlib

from pathlib import Path

nom = 'fichier-temoin'
path = Path(nom)
# le fichier n'existe pas
path.exists()
# si j'écris dedans je le crée
with open(nom, 'w', encoding='utf-8') as output:
    output.write('0123456789\n') # existe et mis dans le working directory
    
#%% Les métadonnées
# cette méthode retourne (en un seul appel système) les métadonnées agrégées
# de path
path.stat()
# la taille du fichier en octets est de 11 
# car il faut compter un caractère "newline" en fin de ligne 
path.stat().st_size
# la date de dernière modification, sous forme d'un nombre
# c'est le nombre de secondes depuis le 1er Janvier 1970
mtime = path.stat().st_mtime
mtime
# que je peux rendre lisible comme ceci
# en anticipant sur le module datetime
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime)
mtime_datetime
# ou encore, si je formatte pour n'obtenir que
# l'heure, la minute, la seconde
f"{mtime_datetime:%H:%M:%S}"      
      
# je peux maintenant détruire le fichier
path.unlink()
# ou encore mieux, si je veux détruire 
# seulement dans le cas où il existe je peux aussi faire
try: 
    path.unlink()
except FileNotFoundError:
    print("no need to remove")

path.exists() # n'existe plus

#%% Recherche de fichiers
# recherche dans un dossier
dirpath = Path('./.ipynb_checkpoints/')
# tous les fichiers *.json dans le répertoire data/
for ipynb in dirpath.glob("*.ipynb"):
    print(ipynb)

#%% Les tuples

# très proche de la liste mais est un objet immuable
t = ()
type(t)
t = (4,) # pour un tuple singleton, pas oublier de mettre la , à la fin
t
t = (True, 3.4, 18)
t
t = True, 3.4, 18 # pas besoin de parenthèses
t
t= 4, # fonctionne aussi 
3.4 in t
t[1]
t[:2]
a = list(t) # tuple converti en liste
a
a[0] = False # on modifie le premier élément
t = tuple(a) # re-modifie en tuple
t
(a, b) = [3, 4] # unpacking -> mtn a référence 3 et b référence 4
a
b
a, b = 3, 4 # on peut aussi alléger l'écriture en enelevant les [] et ()
a
b
a = list(range(10)) # extended tuple unpacking pou isoler des éléments d'une
                        # grande séquence
a
x, *y = a
x # x égal au premier élément de a
y # y référence une liste qui référence le reste de a
*x, y = a
x # x référence de 0 à 8
y # y référence le dernier élément

couple = (100, 'spam')
gauche = couple[0]
droite = couple[1]
print('gauche', gauche, 'droite', droite) # fonctionne mais pas très
                                            # pythonien
(gauche, droite) = couple
# ou alors
gauche, droite = couple
print('gauche', gauche, 'droite', droite)

# Faisable avec d'autres types
# comme ceci
liste = [1, 2, 3]
[gauche, milieu, droit] = liste
print('gauche', gauche, 'milieu', milieu, 'droit', droit)
# membre droit: une liste
liste = [1, 2, 3]
# membre gauche : un tuple
gauche, milieu, droit = liste
print('gauche', gauche, 'milieu', milieu, 'droit', droit)

# Les valeurs à droite sont toutes évaluées en premières donc:
a = 1
b = 2
a, b = b, a
print('a', a, 'b', b) # a, b de droite remplace a de gauche donc = 2, b, 1
# ça va de droite : a à gauche : est égal à b qui est égal à 2
#%%% quizz tuple

triple = (1, 2, 3,)
triple[0]
triple[:]
triple[len(triple)] # fonctionne pas pcq qu'on compte apd 0
triple[0] = 0 # fonctionne pas car tuple est immuable

quadruple = (1, [2, 3], True, [ (4,) ] )
# quelles lignes affectent 4 à four?
( one, (two, three), ignored, ( ( four ) ) ) = quadruple
print(four) # faux, ça print une liste qui contient (4,)
( one, (two, three,), _, ( ( four, ), ) ) = quadruple
print(four)
( one, (two, three), _, [ [ four ] ] ) = quadruple
print(four)
quadruple     

liste=(1,2,3) # liste est un tuple!
liste=[1,2,3,4,5] # liste est une liste
# on veut intervertir les deux derniers éléments
# faux
tmp = liste[-1];liste[-1] = liste [-2] ; liste[-2] = tmp
liste
# faux
#liste.reverse(-2, -1)

liste[-2], liste[-1] = liste[-1], liste[-2]

#%%% Compléments intermédiaires tuples

# Plusieurs manières de créer des tuples à plusieurs éléments
# sans parenthèse ni virgule terminale
couple1 = 1, 2
# avec parenthèses
couple2 = (1, 2)
# avec virgule terminale
couple3 = 1, 2,
# avec parenthèses et virgule
couple4 = (1, 2,)

couple1==couple2==couple3==couple4

# tuples à 1 élément
# ATTENTION : ces deux premières formes ne construisent pas un tuple !
simple1 = 1
simple2 = (1)
# celles-ci par contre construisent bien un tuple
simple3 = 1,
simple4 = (1,)

# En général, il vaut mieux utiliser les parenthèses et la virgule finale
# pcq parfois messages d'erreur quand 1, = x

mon_tuple = ([1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
            )
# plus clair à lire
# On peut quand même faire des opérations quand ça crée un nouveau tuple
tuple1 = (1, 2,)
tuple2 = (3, 4,)
print('addition', tuple1 + tuple2)
# ou alors
tuple1 = (1, 2,)
tuple1 += (3, 4,)
print('apres ajout', tuple1)

# ça peut être chiant de créer un tuple
# donc pour faciliter,
# on fabrique une liste pas à pas
liste = list(range(10))
liste[9] = 'Inconnu'
del liste [2:5]
liste

# on convertit le résultat en tuple
mon_tuple = tuple(liste)
mon_tuple

#%%% Complément extended unpacking

reference = [1, 2, 3, 4, 5]
a, *b, c = reference
print(f"a={a} b={b} c={c}")

# *b peut être de longueur quelconque :
reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")

# intéressant si on s'interesse seulement aux premières variables d'une 
# structure
# si on sait que data contient prenom, nom, 
# et un nombre inconnu d'autres informations
data = [ 'Jean', 'Dupont', '061234567', '12', 'rue du four', '57000', 'METZ', ]

# on peut utiliser la variable _
# ce n'est pas une variable spéciale dans le langage,
# mais cela indique au lecteur que l'on ne va pas s'en servir
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")
# Ca ressemble à une attribution de noms de colonnes ou lignes dans R
# sauf que là tu définis que les colonnes/lignes qui t'intéressent

#%%% Ocurrence de la même variable dans le sequenc unpacking

# ceci en toute rigueur est légal
# mais en pratique on évite de le faire
entree = [1, 2, 3]
a, a, a = entree
print(f"a = {a}")
# il fait a = 1; a = 2; a = 3

entree = [1, 2, 3]

_, milieu, _ = entree
print('milieu', milieu)

ignored, ignored, right = entree
print('right', right)

#%%% Unpacking de plus profond dans la fonction

structure = ['abc', [(1, 2), ([3], 4)], 5]
# si on veut extraire l'emplacement de 3
(a, (b, ([trois], c)), d) = structure
print('extrait', trois)
# ou alors (mais déconseillé)
trois = structure[1][1][0][0]
print('trois', trois)
# pour expliquer:
structure[1]
structure[1][1]
structure[1][1][0].type() # [3] est une liste donc
structure[1][1][0][0] # on extrait le premier élement de cette liste qui
                        # n'a qu'un élément

#%%% Plusieurs variables dans une boucle for et .zip files

item = (1, 2)
a, b = item
print(f"a={a} b={b}")

entrees = [(1, 2), (3, 4), (5, 6)]
for a, b in entrees:
    print(f"a={a} b={b}")
# cette boucle fait trois itérations
# la première a=1 et b=2 puis
# a=3 et b=4 puis a=5 et b=6

villes = ["Paris", "Nice", "Lyon"]
populations = [2*10**6, 4*10**5, 10**6]

list(zip(villes, populations))
# donne une liste composée de tuples pour laquelle on peut faire une boucle
# for comme ceci:

for ville, population in zip(villes, populations):
    print(population, "habitants à", ville)

# et dans le cas où il y a plus de deux variables, on généralise :
    
for i, j, k in zip(range(3), range(100, 103), range(200, 203)):
    print(f"i={i} j={j} k={k}")

# Remarque : lorsqu'on passe à zip des listes de tailles différentes, 
# le résultat est tronqué, c'est l'entrée de plus petite taille qui détermine 
# la fin du parcours.

# on n'itère que deux fois
# car le premier argument de zip est de taille 2
for units, tens in zip([1, 2], [10, 20, 30, 40]):
    print(units, tens)

#%%% La fonction enumerate

for i, ville in enumerate(villes):
    print(i, ville)


#%% Tables de hash

%timeit 'x' in range(100)
%timeit 'x' in range(10_000)
%timeit 'x' in range(1_000_000)
# opération de test d'appartenance prends un temps linéaire à la len(seq)
t = [1, 2]
t[0]
t = [18, 35]
t['alice'] = 35 # si je veux remplacer dans la liste un entier par une chaine
                # de charac, ça ne marche pas
t[35] = 'alice' # pas bon non plus
t[1] = 'alice' # je dois connaitre la position

#%% Les dictionnaires

age = {}
type(age)
age = {'ana':35, 'eve':30, 'bob':38}
age['ana']
a = [('ana', 35), ('eve', 30), ('bob', 38)]
age = dict(a)
age['bob']
age['bob'] = 45
age
del age['bob']
age
len(age)
'ana' in age
'bob' in age
age.keys()
age.values()
age.items()
k = age.keys()
k
age['bob'] = 25
k
'ana' in k
'bill' in k
for k, v in age.items():
    print(f"{k} {v}")
for k in age:
    print(k)

#%% Les dictionnaires

age = {} # crée un objet de type dictionnaire
type(age)
age = {'ana':35, 'eve':30, 'bob':38} # 3 clés et 3 valeurs
age=dict(ana=35,eve=30, bob=38)
age['ana']
a = [('ana', 35), ('eve', 30), ('bob', 38)] # une liste qui contient des tuples
age = dict(a) # crée un dict apd des couples clés valeurs de la liste
age['bob']
age['bob'] = 45 # et on peut le muter puisque contient tuples
age
del age['bob']
age
len(age)
'ana' in age
'bob' in age
age.keys() # couple clé-valeur = item
age.values() # pour accéder aux clés, aux valeurs
age.items() # retourne un objet qui est une "vue" mais qui change quand
            # le dictionnaire est mis à jour. Cet objet prend 0 stockage
            # puisqu'il n'est une liste mais une vue sur son objet
k = age.keys() 
k
age['bob'] = 25
k
'ana' in k
'bill' in k
for k, v in age.items(): # retourne une vue sur les items d'age
    print(f"{k} {v}")
for k in age:
    print(k)
# par défaut, il itèrera sur les clés si on précise pas items


annuaire={'Marc':30, 'Ana':35}
annuaire['Marc'] = 50
annuaire.setdefault('Marc', 50)
annuaire['bob']=42 # ajoute une entrée pour bob

print('la valeur pour marc est', annuaire['Marc'])
# si on est pas sûr que marc est dans le dictionnaire, utiliser get
print('valeur pour marc', annuaire.get('marc', 0))
print('valeur pour inconnu', annuaire.get('inconnu', 0))

#pour parcourir tout le dictionnaire
for nom, age in annuaire.items():
    print(f"{nom}, age {age}")

# la méthode d'update
print(f"avant: {list(annuaire.items())}")
annuaire.update({'jean':25, 'eric':70})
list(annuaire.items())

# Imaginons que vous devez gérer un dictionnaire dont les valeurs sont des 
# listes
# et que votre programme ajoute des valeurs au fur et à mesure dans ces listes.
# Avec un dictionnaire de base, cela peut vous amener à écrire un code qui 
# ressemble à ceci :

# imaginons qu'on a lu dans un fichier des couples (x, y)
tuples = [
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 4),]

# et on veut construire un dictionnaire
# x -> [liste de tous les y connectés à x]
resultat = {}

for x, y in tuples:
    if x not in resultat:
        resultat[x] = []
    resultat[x].append(y)

for key, value in resultat.items():
    print(key, value)


# Cela fonctionne, mais n'est pas très élégant. Pour simplifier ce type de 
# traitement, vous pouvez utiliser defaultdict, une sous-classe de dict dans le 
# module collections :

 from collections import defaultdict

# on indique que les valeurs doivent être créées à la volée
# en utilisant la fonction list
resultat = defaultdict(list)

# du coup plus besoin de vérifier la présence de la clé
for x, y in tuples:
    resultat[x].append(y)

for key, value in resultat.items():
    print(key, value)

# ça marche aussi avec des int

compteurs = defaultdict(int)

phrase = "une phrase dans laquelle on veut compter les caractères"

for c in phrase:
    compteurs[c] += 1

sorted(compteurs.items())

# Gérer des enregistrements

personnes = [
    {'nom': 'Pierre',  'age': 25, 'email': 'pierre@example.com'},
    {'nom': 'Paul',    'age': 18, 'email': 'paul@example.com'},
    {'nom': 'Jacques', 'age': 52, 'email': 'jacques@example.com'},
]

personnes[0]['age'] += 1 # changer l'age de pierre

for personne in personnes:
    print(10*"=")
    for info, valeur in personne.items():
        print(f"{info} -> {valeur}")

# Un dictionnaire pour inderxer les enregistrements
# on crée un index permettant de retrouver rapidement
# une personne dans la liste
index_par_nom = {personne['nom']: personne for personne in personnes}
index_par_nom

# du coup pour accéder à l'enregistrement pour Pierre
index_par_nom['Pierre']

for nom, record in index_par_nom.items():
    print(f"Nom : {nom} -> enregistrement : {record}")

# Ou alors (même idée mais avec une classe Personne)

class Personne:

    # le constructeur - vous ignorez le paramètre self,
    # on pourra construire une personne à partir de
    # 3 paramètres
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    # je définis cette méthode pour avoir
    # quelque chose de lisible quand je print()
    def __repr__(self):
        return f"{self.nom} ({self.age} ans) sur {self.email}"


personnes2 = [
    Personne('Pierre',  25, 'pierre@example.com'),
    Personne('Paul',    18, 'paul@example.com'),
    Personne('Jacques', 52, 'jacques@example.com'),
]

# je dois utiliser cette fois personne.nom et non plus personne['nom']
index2 = {personne.nom : personne for personne in personnes2}

print(index2['Pierre'])

#%% Les sets

s = set() # souvent utilisé pour obtenir tous les éléments uniques
type(s)
s = {1, 2, 3, 'a', True} # ne peut contenir que des objets immuables
a = [1, 2, 4, 1, 18, 30, 4, 1]
set(a) #transforme a en set
len(s)
1 in s # test d'appartenance
'b' in s
s.add('alice')
s
s.update([1, 2, 3, 4, 5, 6, 7]) # fct pour ajouter plusieurs éléments
s # NB ça ne rajoute que ceux qui ne sont pas encore présents dans le set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 - s2
s1 | s2 # union des ensembles
s1 & s2 # intersection des ensembles

a = [0]
s = set(a)

%timeit -n 50 0 in a # on dit qu'on veut que 50 boucles
%timeit -n 50 0 in s

s.add(set(a)) # set n'est pas immuable
s.add(frozenset('0')) 
s
s.add([frozenset('A'),frozenset('B')]) # liste n'est pas immuable
s.add((frozenset('A'),frozenset('B')))
s
s.add((set(a),set(y))) # liste de set n'est pas immuable


# Un frozenset est un ensemble qu'on ne peut pas modifier, et qui donc peut 
# servir de clé dans un dictionnaire, ou être inclus dans un autre ensemble 
# (mutable ou pas).

ensemble = {1, 2, 1}
ensemble
# pour nettoyer
ensemble.clear()
ensemble
# ajouter un element
ensemble.add(1)
ensemble
# ajouter tous les elements d'un autre *ensemble*
ensemble.update({2, (1, 2, 3), (1, 3, 5)})
ensemble
# enlever un element avec discard
ensemble.discard((1, 3, 5))
ensemble
# discard fonctionne même si l'élément n'est pas présent
ensemble.discard('foo')
ensemble
# enlever un élément avec remove
ensemble.remove((1, 2, 3))
ensemble


# pop() ressemble à la méthode éponyme sur les listes
# sauf qu'il n'y a pas d'ordre dans un ensemble
while ensemble:
    element = ensemble.pop()
    print("element", element)
print("et bien sûr maintenant l'ensemble est vide", ensemble)


heteroclite = {'marc', 12, 'pierre', (1, 2, 3), 'pierre'}
print(heteroclite)
heteroclite2 = set(['marc', 12, 'pierre', (1, 2, 3), 'pierre'])
print(heteroclite2)
A2 = set([0, 2, 4, 6])
print('A2', A2)
A3 = set([0, 6, 3])
print('A3', A3)
superset = {0, 1, 2, 3}
print('superset', superset)
subset =  {1, 3}
print('subset', subset)

heteroclite == heteroclite2
subset <= superset #subset inclu dans superset
subset < superset
heteroclite < heteroclite2
heteroclite.isdisjoint(A3)

#%% Exercice niveau basique

# =============================================================================
# On se propose d'écrire une fonction read_set qui construit un ensemble à 
# partir du contenu d'un fichier. Voici par exemple un fichier d'entrée :
# 
# read_set va prendre en argument un nom de fichier (vous pouvez supposer 
# qu'il existe), enlever les espaces éventuelles au début et à la fin de 
# chaque ligne, et construire un ensemble de toutes les lignes ; par exemple :
# 
# =============================================================================
from os import chdir, getcwd
getcwd()
chdir('C:\\Users\\mario\\Documents\\SBIMQ22-23\\Mooc\\python 3\\Script')
    
def read_set(filename):
    with open(filename, encoding='utf-8') as file: 
        s=set()
        for i in file:
            i=i.strip()
            s.add(i)         
        return(s)

read_set(r'.\spam2.txt')

# =============================================================================
# 
# Ceci étant acquis, on veut écrire une deuxième fonction search_in_set qui 
# prend en argument deux fichiers :
# 
# filename_reference est le nom d'un fichier contenant des mots de référence ;
# filename est le nom d'un fichier contenant des mots, dont on veut savoir s'ils 
# sont ou non dans les références.
# Pour cela search_in_set doit retourner une liste contenant, pour chaque ligne 
# du fichier filename, et dans cet ordre, un tuple avec :
# 
# la ligne (sans les espaces de début et de fin, ni la fin de ligne) ;
# un booléen qui indique si ce mot est présent dans les références ou pas.
# 
# =============================================================================

def search_in_set(filename,filename_reference):
    file=read_set(filename)
    reffile=read_set(filename_reference)
    L=[]
    for i in reffile:
        if i in file:
            y=True
        else:
            y=False
        a=(i,y)
        L.append(a)
    return(L)

search_in_set(r'.\file.txt', r'.\ref_file.txt')

# donne les bons résultats mais pas dans le même ordre
# c'est à cause du fait qu'on utilise des set() dans la fct read_set

def read_prout(filename):
    with open(filename, encoding='utf-8') as file: 
        s=[]
        for i in file:
            i=i.strip()
            s.append(i)         
        return(s)
def search_in_set(filename,filename_reference):
    file=read_prout(filename)
    reffile=read_prout(filename_reference)
    L=[]
    for i in reffile:
        if i in file:
            y=True
        else:
            y=False
        a=(i,y)
        L.append(a)
    return(L)

search_in_set(r'.\ref_file.txt', r'.\file.txt')



# =============================================================================
# Le but de l'exercice est précisément d'étudier la différence, et pour cela 
# on vous demande d'écrire une fonction
# 
# diff(extended, abbreviated)
#
# qui retourne un tuple à trois éléments :
# 
# l'ensemble (set) des noms des bateaux présents dans extended mais pas dans 
# abbreviated ;
# l'ensemble des noms des bateaux présents dans extended et dans abbreviated ;
# l'ensemble des id des bateaux présents dans abbreviated mais pas dans 
# extended (par construction, les données ne nous permettent pas d'obtenir les 
#noms de ces bateaux).
# 
# =============================================================================

import json

with open(r'.\data\marine_ext.json', encoding="utf-8") as feed:
    extended_full = json.load(feed)

with open(r'.\data\marine_abb.json', encoding="utf-8") as feed:
    abbreviated_full = json.load(feed)
    

def diff(extended, abbreviated):
    extended=extended_full
    abbreviated=abbreviated_full
    """Calcule comme demandé dans l'exercice, et sous formes d'ensembles
    (*) les noms des bateaux seulement dans extended
    (*) les noms des bateaux présents dans les deux listes
    (*) les ids des bateaux seulement dans abbreviated
    """
    both_names = \
        set([ship[4] for ship in extended if ship[0] in both_ids])
    extended_only_names = \
        set([ship[4] for ship in extended if ship[0] in extended_only_ids])
    names_ext=set(ship[0] for ship in extended)
    return(L)

diff(extended, abbreviated)      
    
    
    

# combien de bateaux sont concernés
def show_result(extended, abbreviated, result):
    """
    Affiche divers décomptes sur les arguments
    en entrée et en sortie de diff
    """
    print(10*'-', "Les entrées")
    print(f"Dans extended: {len(extended)} entrées")
    print(f"Dans abbreviated: {len(abbreviated)} entrées")
    print(10*'-', "Le résultat du diff")
    extended_only, both, abbreviated_only = result
    print(f"Dans extended mais pas dans abbreviated {len(extended_only)}")
    print(f"Dans les deux {len(both)}")
    print(f"Dans abbreviated mais pas dans extended {len(abbreviated_only)}")

show_result(extended, abbreviated, result)

#%% Les exceptions

def div(a, b) :
    print(a/b)

div(1,2)
div(1,0)

def div(a, b) :
    try:
        print(a/b)
    except ZeroDivisionError:
        print("attention, division par 0")
    print("Continuons")
Faire Ctl-s puis F5

div(1, 2)
div(1, 0)
div(1, '0')


def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("attention, division par 0")
    print("Continuons")
    except TypeError:
        print("il faut des int")def div(a, b) :

div(1, 2)
div(1, 0)
div(1, '0')

# =============================================================================
# L'instruction try est généralement assortie d'une une ou plusieurs clauses except, comme on l'a vu dans la vidéo.
# 
# Sachez que l'on peut aussi utiliser - après toutes les clauses except :
# 
# une clause else, qui va être exécutée si aucune exception n'est attrapée ;
# et/ou une clause finally qui sera alors exécutée quoi qu'il arrive.
# 
# =============================================================================

# une fonction qui fait des choses après un return
def return_with_finally(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return("zero-divide")
    finally:
        print("on passe ici même si on a vu un return")

# sans exception
return_with_finally(1)

# avec exception
return_with_finally(0)

# =============================================================================
# En première approximation, on pourrait penser que c'est équivalent de mettre 
# du code dans la clause else ou à la fin de la clause try. En fait il y a une 
# différence subtile :
# 
# The use of the else clause is better than adding additional code to the try 
# clause because it avoids accidentally catching an exception that wasn’t 
# raised by the code being protected by the try … except statement.
# 
# Dit autrement, si le code dans la clause else lève une exception, celle-ci 
# ne sera pas attrapée par le try courant, et sera donc propagée.
# 
# =============================================================================

# pour montrer la clause else dans un usage banal
def function_with_else(number):
    try:
        x = 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
    else:
        print("on passe ici seulement avec un nombre non nul")
    return 'something else'

# sans exception
function_with_else(1)

# avec exception
function_with_else(0)


# la clause else ne traverse pas les return
def return_with_else(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return("zero-divide")
    else:
        print("on ne passe jamais ici à cause des return")

# sans exception
return_with_else(1)

# avec exception
return_with_else(0)

#%% Références partagées

# Quand on a un objet mutable qui est référencé par deux variables, si on mute 
# l'objet par une variable, il sera modifié pour l'autre

a=[1,2]
b=a
a[0]="spam"
a
b
 
# pour éviter ça, on peut faire une shallow copie

b=a[:]
a[0]=1
a
b

# mais ne fonctionne pas pour un objet mutable qui référence aussi des mutables

a=[1,[2]]
b=a[:]
a[1][0]="spam"
a
b

# pour palier à ça, faire une deep copy

import copy

b=copy.deepcopy(a)

#%%% Exercices

entier = 0
liste = [entier, entier, entier]
liste[0] = 1
print(liste)

cellule = [0]
liste = [cellule, cellule, cellule]
# puis
liste[0][0] = 1
print(liste)

cellule = [0]
liste = [cellule, cellule, cellule]
# puis
cellule[0] = 1
print(liste)

cellule = [0]
liste = [cellule, cellule, cellule]
# puis
cellule = [1]
print(liste)

#%%% Compléments

a=[1,2]
b=[1,2]
a==b
a is b

a=[1,2]
b=a
a == b
a is b

a = b = 3
a is b
a += 1

# ceci n'a pas modifié b
# c'est normal, l'entier n'est pas mutable

print(a)
print(b)
print(a is b)

# Deuxième exemple, cette fois avec une liste

# la même référence partagée
a = b = []
a is b

# pareil, on fait += sur une des variables
a += [1]

# cette fois on a modifié a et b
# car += a pu modifier la liste en place
print(a)
print(b)
print(a is b)

a = []
print("avant", id(a))s
a = a + [1]
print("après", id(a))

#%% Introduction aux classes

# permettent de définir des objets et qu'ils se comportent comme des
# objets built-in
# les fonctions définies dans les classes s'appellent des méthodes 
# (ici __init__)

class Phrase:
    def __init__(self, phrase):
        self.mots=phrase.split()

p= Phrase("je fais un mooc sur python")
p
p.mots

class Phrase:
    def __init__(self, phrase):
        self.mots=phrase.split()
        
    def upper(self):
        self.mots=[m.upper()for m in self.mots]
    
    def __str__(self):
        return "\n".join(self.mots)

p.upper()
p.mots

print(p)

class Parser:
    def __init__(self, sep):
        self.sep = sep
        self.parsed_line = []

    def parse(self, line):
        self.parsed_line = [i.strip() for i in line.split(self.sep)
                            if i.strip().isdigit()]

    def __str__(self):
        return ' '.join(self.parsed_line)

test = '123  : fj356:34:fjjd:    707'

p = Parser(':')
p.parse(test)
print(p)

