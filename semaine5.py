
# Itérations, itérables etc

#%% Itérations

s = {1, 2, 3, 'a'} 
for i in s: 
    print(i) 
[x for x in s if type(x) is int] 
s 
it = iter(s) 
it 
next(it) 
next(it) 
next(it) 
next(it) 
next(it) 
 
a = [1, 2] 
b = [3, 4] 
iter(a) 
z = zip(a, b) 
z 
z is iter(z) 
[i for i in z] 
[i for i in z] 
next(z) 
z = zip(a, b) 
[i for i in z] 


















