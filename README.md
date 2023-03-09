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
| 15 | + |
| 16 | + |
| 17 | + |
| 18 | |
| 19 | + |
| 20 | + |
| 21 | + |
| 22 | |
| 23 | + |
| 24 | + |
| 25 | + |
| 26 | + |
| 27 | |


##Уникальные команды#

print() - выводит на экран какой-то элемент
for i in range() - перебирает элементы в каком-то диапозоне
def() - объявить функцию
sort - сортировать элементы в порядке возрастания
index() - поиск индекса
int() - преобразует число в целое
str()- преобразует элемент в строку
if - оператор если, то else - иначе elif - дгое условие
% - нахождение остатка от деления
replace - заменить один элемент на другой
all - требование, чтобы все условия в последующем if были правда
False - ложь
True - правда
and - и
or - или
= - импликация
pop - удалить элемент
break - прервать выполнения цикла
continue - цикл проходит к следующей итерации
product - формирует все возсожные комбинации по заданным нами условиям
setrecursionlimit - установить лимит на рекурсию
repeat - повторить действие некоторое количество раз
readline - прочитать строку
with open - открыть файл
import - импортировать файл
max - найти максимальное значение
min - найти минимальное значение
return - вернуть результат выполнения функции
def() - объявить функцию
dot() - поставить точку за черепашку
goto()- двигаться за черепашку
up() - идти вверх за черепашку
down() - идти вниз за черепашку
right() - идти вправо за черепашку
not - нет
list.append- добавить элемент в список
input() - ввести с клавиатуры значение
pip install - установка программного пакета
len() - найти количество элементов в объекте
// - деление с остатком


% - нахождение остатка от деления
replace - заменить один элемент на другой
all - требование, чтобы все условия в последующем if были правда
False - ложь
True - правда
and - и
or - или
= - импликация

break - прервать выполнения цикла
continue - цикл проходит к следующей итерации
product - формирует все возсожные комбинации по заданным нами условиям
setrecursionlimit - установить лимит на рекурсию
repeat - повторить действие некоторое количество раз




#5
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
    
#6
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
   
   
   
   


#8

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



#12


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





#14


```python
a='0123456789abcde'
for x in a:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(f//14)
        break
 ```
 
 
 #15
 ```python
 
 for A in range(1,1000):
   if all(((x%2==0)<=(x%3!=0)) or (x+A>=100) for x in range (1,100)):
        print(A)
        break
 ```

#16
 
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

#17

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


#23

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

#24
```python
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

```


#25
```python
for i in range (2023,10**10,2023):
    n=str(i)
    if n[0]=='1' and n[2:6]=='2139' and n[-1]=='4': print(i,i/2023)

```

    
#26
```python
with open('26.txt') as f:
    s=[int(x) for x in f]
    s.pop(0)
    s.sort(reverse=True)
    k,mini=1,s[0]
    for i in range(1, len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k, mini)

```
#25
```python
for i in range (17,10**11,17):
    n=str(i)
    if n[0:5]=='12345' and n[5]=='6' and n[-1]=='8': print(i,i/17)

  
```  
