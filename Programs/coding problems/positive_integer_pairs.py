

for P in range(100):

    for X in range(100):

        for i in range(P//2+1):
            j = P - i
            if i ^ j == X:
                print(f'{P=}{X=}{i=}{j=}')
                break
