#%% Introduction

"ceci est un mooc".title()


s="le poulet c'est bon"
s.replace("le poulet","le caca")

"123".isdecimal() # converti en decimal

n="Sonia"
age=30

f"{n} a {age} ans".format()
name="Marion"
print('Hi %s'%name) # %s = substitue avec %variable


"\u03a6" # caractère UTF-8

#%% Les chaines de caractères

s="bacon, egg"
print(s)

len(s) # il y a 10 éléments 0 à 9
s[0] # les séquences commencent à 0
s[9]

"egg" in s # true, on trouve egg dans s
"egg" not in s

s+",and beans" # ajoute , and beans à la séquence de charac

s.index("g") # place de la première occurence  de g (compte commence à 0)
s.count("g") # nbre occurences de g dans s
s*30
s[0:3] #!!! 0 inclu et 3 exclu
s[:3]# même chose
s[3:] #apd de 3 jusqu'à la fin
s[:] # donne toute la chaine mais une copie
s[0:10:2] # tous les éléments par pas de 2
s[::2]# même chose
s[2::3] # éléments de 2 jusqu'à la fin par pas de 3
s[100] # erreur
s[5:100] # fonctionne parce que donne une intersection "bacon"
s[100:200] # donnera un vecteur vide
s[::-1] # retourne la séquence de droite à gauche
s[-10:-7] # donne egg pcq e est 0 et -10 etc
s[2::-1] # va de 2 à 0 par pas de 1 renversé soit "gge"


chaine = "douarnenez"
chaine.index('z') == len(chaine)-1 # true
chaine[-3:] == 'nez' # prend les trois derniers characters
chaine[1:3] + chaine[3:5] + chaine[5:] == chaine[1:] # l'équivalent d'au-dessus

#%% Les listes

a = []
type(a) # vérifie la classe de l'objet
i = 4
a = [i, 'spam', 3.2, True] # liste contient réf vers une var, une chaine de chara,
                            # un float et un booleen
a
a[0]
a[0] = 6
a
a[0] = a[0] + 10
a
a[1:3]
a[1:3] = [1, 2, 3]
# première opération : enlève les élements entre 1 et 3 exclu
# deuxième opération: insère les éléments 1,2,3 à la place de ceux enlevés

a
a[1:3] = [] # efface les éléments entre 1 et 3 exclu
a
del a[1:2] # permet aussi d'effacer des éléments
a
dir(list) # donne les commandes utiles sur les types liste
list.append() # donne des infos sur la fct append
help(list.append)
a
a.append('18')
a
a.extend([1, 2, 3])
a
a = [1, 5, 3, 1, 7, 9, 2]
a.sort()
a
a = a.sort() # trie les éléments en place càd modifie directement a
a
s = 'spam egg beans'
a = s.split() # découpe en utilisant l'espace comme séparateur
                # on peut aussi préciser quel est le séparateur
a
a[0] = a[0].upper() # uppercase l'éléments 0
a
" ".join(a) # recolle les éléments en mettant un espace entre chaque

# on veut trier en sens inverse les éléments dans liste
liste = [1, 0, 3, 2]
liste.sort(reverse=True)
liste.sort(); liste.reverse()

# on veut que suivant soit le permier élément de liste
# et que le premier élément de liste soit deleted
suivant = liste.pop(0)
suivant = liste[0]; del liste[0]

#%% Introduction aux tests if et syntaxe

note = 8
if note > 10:
    print("reçu")
    print("bravo !")
else: 
    print("recalé")



entree = 'spam'

if 'a' in entree:
    if 'b' in entree:
        cas11 = True
        print('a et b')
    else:
        cas12 = True
        print('a mais pas b')
else:
    if 'b' in entree:
        cas21 = True
        print('b mais pas a')
    else:
        cas22 = True
        print('ni a ni b')

condition = False

if condition:
        print("non")
else:
        print("bingo")

condition = False

if condition:
        # print "non" 
        pass # si on ne veut pas qu'il print le "non"
else:
        print("bingo")

#%% Introduction aux boucles for et fonctions

print(1**2)
print(2**2)
print(3**2) # fastidieux

for i in range(10): # pour i qui sera dans le range 0 à 9
    print(i**2) # print le carré
    
for i in ['a', 3.5, True]:
    print(i) # i représente chaque élément de la liste à la suite
a = [1, 2, 5, 8, 9]

for i in a:
    print(i**2)
b = [3.6, 18, 12, 25]

for i in b:
    print(i**2)
    
def carre(a): # permet de définir une fonction plutôt que rataper
                # la boucle for
    for i in a:
        print(i**2)
        
carre(a)
carre(b)

def carre(a):
    L = [] # on veut retourner une liste donc on crée une liste vide
    for i in a:
        L.append(i**2) # ajoutera les carrés dans la liste
    return L # ne s'exécutera que quand la boucle a terminé
carre(b) # objet liste qui contient tous les carrés de b
b = carre(b)
b

def affiche_carre(n):
    print("le carre de", n, "vaut", n*n)

affiche_carre(12) # pas forcément utile de print une pharse entière

def carre(n):
    return n*n # retourne la valeur qui nous intéresse

if carre(8) <= 100:
    print('petit appartement')

def premier(n):
    """
    Retourne un booléen selon que n est premier ou non
    Retourne None pour les entrées négatives ou nulles
    """
    # retourne None pour les entrées non valides
    if n <= 0:
        return
    # traiter le cas singulier
    # NB: elif est un raccourci pour else if
    # c'est utile pour éviter une indentation excessive
    elif n == 1:
        return False #1 n'est pas un nbre premier
    # chercher un diviseur dans [2..n-1]
    # bien sûr on pourrait s'arrêter à la racine carrée de n
    # mais ce n'est pas notre sujet
    else:
        for i in range(2, n):
            if n % i == 0:
                # pas de reste après quotient
                # on a trouvé un diviseur donc pas nbre premier
                # on peut sortir de la fonction
                return False
    # à ce stade, le nombre est bien premier
    return True


#%% Introduction aux compréhensions de listes

a = [1, 4, 18, 29, 13]
import math
# on veut prendre les logarithmes de la liste a

b = []
for i in a:
    b.append(math.log(i))
b
b = [math.log(i) for i in a] # manière simplifiée de faire des
                            # opérations math sur liste
                            # kinda commme apply() dans r
b
a.append(-1) # dans le cas où il y a un nbre négatif
            # apparemment ça arrive dans des données corrompues
a
b = [math.log(i) for i in a if i > 0] # on ajoute uen condition
b
# on veut uniformiser la liste de prénoms
prenom = ['Alice', 'evE', 'sonia', 'BOB'] 
prenom
prenom = [p.lower() for p in prenom] # on met tout en miniscule
prenom


#%% Exercices niveau facile
    # On vous demande d'écrire une fonction liste_P
    # qui prend en argument une liste de nombres réels
    # x et qui retourne la liste des valeurs  𝑃(𝑥) .

def P(x):
    return 2*x**2-3*x-2

def liste_P(liste_x):
    L=[]
    for x in liste_x:
        L.append(P(x))
    return L
# si on veut la visualiser

# on importe les bibliothèques
import numpy as np
import matplotlib.pyplot as plt
# un échantillon des X entre -10 et 10
X = np.linspace(-10, 10)

# et les Y correspondants
Y = liste_P(X)
# on n'a plus qu'à dessiner
plt.plot(X, Y)
plt.show()


## Exercices niveau intermédiaire
    # On vous demande d'écrire une fonction carré
    # qui prend en argument une liste de nombres réels
    # séparés aléatoirement avec des points virgules
    # et de retourner leur carré séparés par :

a='; -12 ; ; -23; 1 ;;\t'

# =============================================================================
# def isnumber(i):
#     if len(i)<1:
#         return False
#     if i.isnumeric()==True:
#         return True
#     elif i[0]=="-":
#         if i[1:].isnumeric() == True:
#             return True
#         else:
#             return False
#     else:
#         return False
# =============================================================================

def carre(a):
    L=[]
    b=a.split(";")
    print(b)
    for i in b:
        i=i.strip()
        if i!= "":
            L.append(str(int(i)**2))
    s=""
    for item in L:
        s=s+":"+item
    return s[1:]


