# ceci est un commentaire

def factoriel(n):
    """Semaine 1 factoriel function"""
    if n<= 1:
        return 1
    else:
        return n*factoriel(n-1)

print(factoriel(100))
    
    
