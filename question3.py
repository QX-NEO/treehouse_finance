def pascal(n):
    a = []
    b = []
    for i in range(n):
        a.append(1)
        b = []
        if len(a) >=3:
            for j in range(i-1):
                b.append(a[j]+ a[j+1])
        if len(b) > 0:
            for k in range(len(b)):
                a[k+1] = b[k]
        for l in a:
            print(l,'',end ="")
        print() 
    
pascal(7)