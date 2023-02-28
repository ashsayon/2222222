## Задачи ЕГЭ
| задание из ЕГЭ |выполнено |
| ------ | ------ |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | + | 
| 6 | + |
| 7 | |
| 8 | + |
| 9 | |
| 10 | |
| 11 | |
| 12 | + |
| 13 | |
| 14 | + |
| 15 | |
| 16 | + |
| 17 | + |
| 18 | |
| 19 | |
| 20 | |
| 21 | |
| 22 | |
| 23 | + |
| 24 | + |
| 25 | + |
| 26 | + |
| 27 | |


## Идеи решения задач:

**Пояснения к 5 задаче:**
  
  1. Организовать цикл перебора чисел
  
  2. Перевод числа в 2-ю СС (bin , f'{n:b}')
  
  3. Выполнение условий задачи с дописью и заменой
  
  4. Перевод в int и проверка на условие
  
  5. После вывода минимального, прерывание break
  
  Пример кода: 
  ```python
  for N in range (516):
    b = f'{N:b}'
    if N % 2 == 0:
        b += '10'
    else:
        b = '1'+ b + '01'
    if int(b,2)>516:
         print(N)
         break
   ```
    

**Пояснения к 6 задаче:**
 
  1. Вспомнить команды черепашки
  
  2. Воспроизвести алгоритм задачи
 
  3. Расставить сами точки внутри контура
  
  4. Вручную посчитать точки
  (жирность точек не влияет на подсчет)
  
 ***Команды для черепашки:***
   1. forward()-движение вперед, в скобках количество пикселей);
   2. left\right()-поворот налево\направо, в скобках градус поворота;
   3. pu()- поднять перо;
   4. goto()- идти на позицю (x,y);
   5. dot()- поставить точку, в скобках толщшина точки;
   6. done()- закончить рисование.

  Пример кода:
  ```python
  from turtle import *
  left(90)
  for i in range (7):
    forward(300)
    right(120)
  pu()
  for x in range (1,9):
    for y in range (1,10):
      goto(x*30, y*30)
      dot(5)
   done()
   ```
   
   ```python
   from turtle import *
left(90)
for i in range (1):
  forward(150)
  right(90)
  forward(150)
  goto(0, 0)
pu()
for x in range (0,15):
  for y in range (0,15):
    goto(x*10, y*10)
    dot(2)
done()
```
   
   
   
   
   ***Поснения к 8 задаче:***
   
  
1. Сгенирировать все возможные варианты чисел;

2. Рассматриваем каждое число (строку) на удовлетворение условиям задачи (count(), index());

3. Выводим счетчик правильных занчений, если число удовлетворяет всем проверкам, пишем количество таких чисел;


Пример кода:

```python 
from itertools import product
nums=product('01234567',repeat=6)
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
for n in nums:
    numb=''.join(n)
    sp=[]
    if numb.count('6')==1 and numb[0]!='0':
        for x in nn:
            if x in numb:
                sp.append(x)
        if not sp: 
            k+=1
print(k)

```



***Пояснения к 12 задаче:***

Пример кода:

```python
spisok=[]
for num in range(2,1000):
    if all(num%delit!=0 for delit in range (2, num-1)):
        spisok.append(num)
flag=False
for i in spisok:
    for y in range (100):
        if y*4+117==i and flag==False:
            print(y, i)
            flag=True
```





***Пояснения к 14 задаче:***

Пример кода:

```python
a='0123456789abcde'
for x in a:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(f//14)
        break
 ```
 
 
 
 ***Пояснения к 15 задаче:***
 
 
 Пример кода:
 
 ```python
 
 for A in range(1,1000):
   if all(((x%2==0)<=(x%3!=0)) or (x+A>=100) for x in range (1,100)):
        print(A)
        break
 ```

***Пояснкния к 16 задаче:***
 Пример кода: 
 
 ```python 
 import sys
sys.setrecursionlimit(3050)
def f(n):
    if n==1: return 1
    elif n>1: return n*f(n-1)
print(f(2023)/f(2020))
```

```python
it1=1
it2=1
for i in range (1, 2024):
    it1=it1*i
for i in range (1, 2021):
    it2=it2*i
print(it1/it2)
```


***Пояснения к 17 задаче:***

 ```python
 with open('17.txt') as f:
    nums=[int(x)for x in f]
    c=list(map(abs,nums))
    count=0
    sp=[]
    for i in range(len(nums)-1):
        if abs(nums[i])%10==3:
            sp.append(nums[i])
    maxi=max(sp)**2
    sqrt=[]
    for i in range(len(c)-1):
        if ((c[i]%10==3 and c[i+1]%10!=3 ) or (c[i]%10!=3 and c[i+1]%10==3)) and (c[i]**2+c[i+1]**2)>=maxi:
            count+=1
            sqrt.append(c[i]**2+c[i+1]**2)
    print(count)
    print(max(sqrt))
 ```




***Пояснения к 21 задаче:***
1. Если в голове не соображжается, составляем таблицу.





***Пояснения к 23 задаче:***

1. 


Пример кода:
```python
from itertools import product
def f (x, y, z):
    count=0
    for i in range(2,z):
        print(i)
        b=product('12',repeat=i) 
        for n in b: 
            a=x
            if x==10 and n.count('2')>1:continue 
            for l in n: 
                if l=='1': a+=1 
                else: a*=2
                if a==17:break
            if a==y: count+=1
    return count
g=f(10, 35, 24)
r=f(1,10, 10)
print(g*r)
```



Альтернативное решение:

```python 

def f(x,y):
    if x>y or x==17:
        return 0
    elif x==y: return 1
    return f(x+1,y) + f(x*2, y)
print(f(1,10)*f(10,35))
```

-24-
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*':
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)

#25
for i in range (2023,10**10,2023):
    n=str(i)
    if n[0]=='1' and n[2:6]=='2139' and n[-1]=='4': print(i,i/2023)


    
