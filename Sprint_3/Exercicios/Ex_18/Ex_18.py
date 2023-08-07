speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

l = []

for value in speed.values():
    l.append(value)
    
print(list(set(l)))
    