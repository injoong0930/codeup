a, b , c = map(int, input().split())         
                                                             
if a > b:
    if a>c:
        if b>c:
            print(c,b,a)   #a>b>c
        else: #c>=b     a>c>b
            print(b,c,a)
    else: #c>=a  c>a>b
        print(b,a,c)
else: #b>=a
    if b>c: 
        if a>c:   #b>a>c
            print(c,a,b)
        else: #c>a   b>c>a
            print(a,c,b)
    else: #c>b  c>b>a
        print(a,b,c)
