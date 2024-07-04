for i in range(poop_size):
    if vivos[i] == false:
        p1 = rand.randint(0,pop_size-1)
        while(vivos[p1] == False):
            p1 = rand.randint(0,pop_size-1)
        p2 = rand.randint(0,pop_size-1)
        while(vivos[p2] == False or p2 == p1):
            p2 = rand.randint(0,pop_size-1)
        j1 = rand.randint(0,n)
        j2 = rand.randint(0,n)
        if j2 < j1:
            temp = j2
            j2 = j1
            j1 = temp
            seleccionados = [0 for i in range(n)]
            for j in range(n):
                p[i][j] = -1
            for j in range(j1,j2):
                p[i][j] = p[p1][j]
                seleccionados[p[p1][j]] = 1
            j2 = 0
            for j1 in range(n):
                while j2 < n and p[i][j2] != -1:
                    j2 += 1
                if seleccionados[p[p2][j1]] == 0:
                    p[i][j2] = p[p2][j1]
                    j2 += 1
    for i in range(pop_size):
        vivos[i] = True