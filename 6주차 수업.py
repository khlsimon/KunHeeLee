# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:06:39 2024

@author: skell
"""
'''
c=int(input("write a number!"))
if c%2==0:
    print("even")
else:
    print("odd")

a=[1,2,3,4,5]
b=a.append(6)
b=sorted(a,reverse=True)
if b: #b가 True 라면 
    print('list b',b)
else: 
    print('list a',a)
'''   
"""
#elif는 앞의 if가 거짓이여야 발동
a="M eat apples and pears"  

if "pears" in a:
    print("M eats pears")
if "apples" in a:
    print("M eats apples")

if "apples" in a:
    print("M eats apples")
elif "pears" in a:
    print('M eats pears')
"""    
#and 모두 맞아야 참
#or 둘 중 하나이면 참 
#가독성으로 () 가능 
"""
fruits=["apple","orange"]
if ("apple" in fruits) and "orange" in fruits:
    print("ok")
if "apple" in fruits or "pear" in fruits:
    print("yee")
"""
#중첩구문
#위의 구문이 맞아야 판단 시작 
'''
a="apples and pears"3
if "apples" in a:
    if "pears" in a:
        print("yee")
else:
    print("ok")
'''
#좁은 범위를 먼저 쓰기 
"""
grade=int(input("학년을 입력:"))
GPA=float(input("GPA 점수 입력"))
score=int(input("학점 입력"))
"""
'''
if (grade==4 and score >=12 and GPA >=4.0) or (grade <=4 and score >=17 and GPA>=4.0):
    print("장학금 대상")
else:
    print('장학금 불합')
'''    
"""
if grade==4:
    if score >=12 and GPA >=4.0:
        print("장학금 합격")
elif grade <=4:
    if score >=17 and GPA >=4.0:
        print("합격")
else:
    print("불합")
"""   
#a=input() c,b
#a_1=a.split(',')
'''
fruits =['apple','banana','orange','strawberry','grape','watermelon','pineapple','mango','peach','kiwi']
a=input("원하는 과일을 쓰시오").lower()
b=input("원하는 다른 과일을 쓰시오.").lower() # .lower() 주의! 
if (a in fruits) and (b in fruits):
    if (a in ["apple","banana","strawberry","orange"]) and (b in ["apple","banana","strawberry","orange"]):
        print("good!")
    elif (a=='watermelon' and b == 'pineapple') or (b=='watermelon' and a == 'pineapple'):
        print("refreshing!")
else:
    print("no fruits")
'''
'''
#pass는 참 거짓과 상관 없이 실행을 시키지 않음 
p=['Alice','White','Rabit']
word='Alice'
if word in p:
    pass
else:
    print(word.lower())

aa = 100
ee = 120
bb = 3.14
cc = 'amy'
dd = "luke"
a= "%d+%d " %(aa,ee)  #d가 정수 변수가 여러개이면 괄호 안에 쓰고 차레대로 쓰기" 
print(a)
b = 'pie is %f' %bb
print(b)
c = "I'm looking for %s and %s" %(cc,dd)
print(c) 

d="My firends are {1} and {0} and {1}".format(cc,dd)
print(d)

name="K"
age=12
print(f"{name} and {age}")
'''
#whlie 은  조건이 참이라면 무조건 반복 실행 (무한 루프 주의)
# while 밑에 break를 써서 중단 가능 
'''
word=["I", "love","very","much","!"]
i=len(word)
while 0 <i<=len(word):
    print(word[i-1])
    i-=1
    if i == 2: #은 들여쓰기 상관 없이 # 다음을 무력화( 범위는 한 줄)
       break
'''
#'''는 들여쓰기를 맞추어서 주석처리를 해야함 
r=1
e=0
while True:
    e+=r
    r+=1
    if r >= 11:
        break
print(e)

t=2
g=0
while True:
    g+=t
    t+=2
    if t >= 12:
        break
print(g)

p=1
o=0
while p <=10:
    if p %2==0:
        o+=p
    p += 1
print(o)
    