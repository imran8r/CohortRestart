a=input('Put the fucking word')
b=input('Put the fucking word')

if len(a) !=len(b):
    print(False)
else:
    A=a.upper()
    B=b.upper()
    alist=[char for char in A]
    blist=[char for char in B]

    alist.sort()
    blist.sort()

    if alist == blist:
        print(True)
    else :
        print (False)

