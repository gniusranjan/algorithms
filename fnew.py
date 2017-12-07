ques=[ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]


def doku(A):
    for i in range(9):
        x = A[i]
        A[i] = list(x)
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    track = []
    for i in range(9):
        for j in range(9):
            if A[i][j] == '.':
                track.append([i, j])
                A[i][j] = l

    for i in track:
            m = i[0]
            n = i[1]
            for j in range(9):
                if A[m][j] in A[m][n]:
                    A[m][n].remove(A[m][j])
            for j in range(9):
                if A[j][n] in A[m][n]:
                    A[m][n].remove(A[j][n])
    min=5
    for i in track:
            m = i[0]
            n = i[1]
            if len(A[m][n]) == 1:
                A[m][n] = A[m][n][0]
                track.remove(i)
                print('done')
            else:
                if len(A[m][n])<min:
                    min=len(A[m][n])
                    pm,pn=m,n
    print(A[pm][pn])
    for p in A[pm][pn]:
        A[track[pm],track[pn]]=[p]
        while len(track)>0:
            for i in track:
                m = i[0]
                n = i[1]
                for j in range(9):
                    if A[m][j] in A[m][n]:
                        A[m][n].remove(A[m][j])
                for j in range(9):
                    if A[j][n] in A[m][n]:
                        A[m][n].remove(A[j][n])
            for i in track:
                m = i[0]
                n = i[1]
                if len(A[m][n]) == 1:
                    A[m][n] = A[m][n][0]
                    track.remove(i)
                    print('done')
            else:
                break

    for i in range(9):
        t = ''
        for j in A[i]:
            t = t + str(j)
        A[i] = [int(t)]
    print(A)
doku(ques)

