
import sys
sys.setrecursionlimit(3050)
def f(n):
    if n<3:
        return 2
    elif n>2 and n%2==0:
        return (f(n-1)+f(n-2)-n)
    elif n>2 and n%2==1:
        return (f(n-2)-f(n-1)+2*n)
print (f(30))

  *16.1*
import sys
sys.setrecursionlimit(3050)
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print (f(2023)/f(2020))
