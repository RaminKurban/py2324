def printall(a=None,b=None,c=None):
    print(a,'первый')
    print(b,'второй')
    print(c,'третий')

if __name__ == '__main__':

    printall('ramin')


    l1 = [1,2,3]
    l2 = [l1,4,5,6]
    print(l2)

    print("________________")
    print(l1)
    print(*l1)
    