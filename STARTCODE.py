import datetime
start_time = datetime.datetime.now()
import  numpy as np
t=int(input())
for A in range(t):
    r, c = map(int, input().strip().split())
    mat1 = []
    Vones = []
    Hones = []
    for i in range(r):
        mat1.append(list(map(int, input().split())))
    mat1 = np.array(mat1, dtype='int8').reshape(r, c)
    mat = np.zeros((r + 2, c + 2))
    mat[1:-1, 1:-1] = mat1
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            # CASE 1  down,right
            if (mat[i, j] == 1) and (mat[i + 1, j] == mat[i, j + 1] == 1):
                x = j
                while (x < c + 1) and (mat[i, x] != 0):
                    x += 1
                Vones.append(x - j)
                y = i
                while (y < r + 1) and (mat[y, j] != 0):
                    y += 1
                Hones.append(y - i)
            # CASE 2  left,back
            if (mat[i, j] == 1) and (mat[i - 1, j] == mat[i, j - 1] == 1):
                x = j
                while (x > 0) and (mat[i, x] != 0):
                    x -= 1
                Vones.append(j - x)
                y = i
                while (y > 0) and (mat[y, j] != 0):
                    y -= 1
                Hones.append(i - y)
            # CASE3   down,left
            if (mat[i, j] == 1) and (mat[i + 1, j] == mat[i, j - 1] == 1):
                x = j
                while (x > 0) and (mat[i, x] != 0):
                    x -= 1
                Vones.append(j - x)
                y = i
                while (y < r + 1) and (mat[y, j] != 0):
                    y += 1
                Hones.append(y - i)
            # CASE4 right,back
            if (mat[i, j] == 1) and (mat[i - 1, j] == mat[i, j + 1] == 1):
                x = j
                while (x < c + 1) and (mat[i, x] != 0):
                    x += 1
                Vones.append(x - j)
                y = i
                while (y > 0) and (mat[y, j] != 0):
                    y -= 1
                Hones.append(i - y)

    max1 = np.max(Vones)
    max2 = np.max(Hones)
    nb_L_chapes = 0
    for k, j in enumerate(Vones):
        i = 2
        l = True
        while (i < max1 + 1) and (l):
            f = 2 * i
            if ((j == f) or (j == f + 1)) and (Hones[k] >= i):
                nb_L_chapes += 1
                l = False
            i += 1
        for s in range(1, Hones[k] - 1):
            if ((Hones[k] - s) * 2 <= j) and ((Hones[k] - s) != (i - 1)):
                nb_L_chapes += 1
    for k, j in enumerate(Hones):
        i = 2
        l = True
        while (i < max2 + 1) and (l):
            f = 2 * i
            if ((j == f) or (j == f + 1)) and (Vones[k] >= i):
                nb_L_chapes += 1
                l = False
            i += 1
        for s in range(1, Vones[k] - 1):
            if ((Vones[k] - s) * 2 <= j) and ((Vones[k] - s) != (i - 1)):
                nb_L_chapes += 1
    print('case #'+str(A+1)+': '+str(nb_L_chapes))
end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
print(time_diff)