
# Boucles while


#%% Quizz

a = 'disparaitre'

while a:
    a = a[:-1]
    print(a)


#%% Règle LEGB

# Ordre de recherche des variables

# Localement
# Englobantes (fonction la plus proche)
# Globalement
# Built-in (module built in)

a, b, c = 1, 1, 1

def g():
     b, c = 2, 4
     b = b + 10
     def h():
         c = 5
         print(a, b, c)
     h()
g()


# g() englobe le h()
# print est une variable built in qui référence la fonction print()

print(a, b, c)
import builtins
dir(builtins)
print(1)
print = 10
print(1)
x = 1
print = builtins.print
print(1)


#%% Exercices: fuite de variable

# une façon très scabreuse de calculer la longueur de l
def length(l):
    for i, x in enumerate(l):
        pass
    return i + 1

length([1, 2, 3]) # fonctionne mais

length([]) # ne fonctionne pas parce que la boucles est vide

# Comment faire:

# on veut chercher le premier de ces nombres qui vérifie une condition
candidates = [3, -15, 1, 8]

# pour fixer les idées disons qu'on cherche un multiple de 5, peu importe
def checks(candidate):
    return candidate % 5 == 0

# plutôt que de faire ceci
for item in candidates:
    if checks(item):
        break
print('trouvé solution', item)

# il vaut mieux faire ceci et définir la variable en dehors de la boucle
solution = None
for item in candidates:
    if checks(item):
        solution = item
        break

print('trouvé solution', solution)

# la fonction length de tout à l'heure
def length1(l):
    for i, x in enumerate(l):
        pass
    return i + 1

length1([])

# une version plus robuste 
def length2(l):
    # on initialise i explicitement
    # pour le cas où l est vide
    i = -1
    for i, x in enumerate(l):
        pass
    # comme cela i est toujours déclarée
    return i + 1

length2([])

#%% Quizz

x = 0

def f():
    print(x)

f()


def f():
    print(x)
    x=3

x = 0 
def f():
    x = 3
    print(x)
    x = 4

var = 'globale'
def f():
    print(var)
    var = 'locale'
    return var


var =10
def f():
    var = 20
    def g():
        return var
    return g()

print(f())


#%% Changer la portée des variables avec global et nonlocal

a = 'a globale'
def f():
    a = 'a dans f'
    print(a)

    Faire: File → save as w4s5.py puis F5

print(a)
f()
print(a)

    Rajouter la ligne (sous def f())

    global a

    Control-s puis F5

print(a)
f()
print(a)

    Reprendre w4s5.py

a = 10

def f():
    global a
    a = a + 10

    Control-s puis F5

print(a)
f()
print(a)

    Reprendre w4s5.py et modifier la fonction

note = 10

def add_10(n):
    return n + 10

    Control-s puis F5

note = add_10(note)
note

    Modifier la fonction

a = 'a globale'

def f():
    a = 'a de f'
    def g():
        a = 'a de g'
        print(a)
    g()
    print(a)

f()
print(a)

    Control-s puis F5

    Rajouter dans g() la ligne:

        nonlocal a



#%% Passage d'arguments et de fonctions


def agenda(nom, prenom, tel):
    return {'nom': nom, 'prenom': prenom,
            'tel': tel}

    Faire: File → save as w4s6.py puis F5

agenda('idle', 'eric', '07070707')
agenda(tel='070707707', nom='idle', prenom='eric')

    Dans la fonction agenda rajouter après le paramètre tel

='?'

    Control-s puis F5

agenda('idle', 'eric')
agenda('idle', 'eric', '07070707')

    Reprendre le programme ou bien prendre un nouveau

def f(*t):
    print(t)

    Faire Control-s puis F5

f()
f(1)
f(1, 2, 3, 4)

def f(**d):
    print(d)

    Faire Control-s puis F5

f()
f(nom='idle', prenom='eric')
print(1)
print(1, 2, 3, 4)

    Reprendre le programme ou bien prendre un nouveau

def f(a, b):
    print(a, b)

    Faire Control-s puis F5

L = [1, 2]
f(L[0], L[1])
f(*L)
d ={'a': 1, 'b': 2}
f(**d)
print(1, 2, sep=';', end='FIN')
pp = {'sep':';', 'end':'FIN'}
print(1, 2, **pp)



#%% Quizz

def f(a, b, var=10):
    print(a, b, var)







