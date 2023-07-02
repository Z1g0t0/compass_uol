
for i in range(2, 101):
    pry = True

    for j in range(2, i):
        if i%j == 0:
            pry = False
            continue
    if pry:
        print(i)