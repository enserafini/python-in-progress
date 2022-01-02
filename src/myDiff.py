def myDivInt(a,b):
    c=int(a/b)
    print(c)
    
def myDivFl(a,b):
    c=a/b
    print(c)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    myDivInt(a,b)
    myDivFl(a,b)