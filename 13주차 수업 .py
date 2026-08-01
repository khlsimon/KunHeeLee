# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:16:36 2024

@author: skell
"""

# 함수를 변수에 담기, 함수 이름을 치환
'''
def plus (a,b):
    return a+b

p = plus
b = p(3,4)
print(p(1,2))
print(b)

def minus (a,b):
    return a-b
m = minus 
l= m(6,5)
print(l)
'''
#함수를 변수에 담기 
'''
def plus (a,b):
    return a+b

def minus (a,b):
    return a-b

cal = [plus, minus]
print(cal[0](1,2),cal[1](1,2))
print(cal[0])
print(cal[1])

for c in cal:
    print(c(3,2))
'''    
#함수 안에 함수 넣기
'''
print()
def hello_k():
    print("안녕하세요")
def hello_e():
    print("Hello")
    
def greeting(a):
    print(a())
    
hello_k()
greeting(hello_e)


def plus (a,b):
    return a+b

def minus (a,b):
    return a-b


def cal(A,a,b):
    print(A(a,b))
    
cal(plus, 1, 2) # -> plus(1,2)
'''
'''
def hello_k():
    print("안녕하세요")
def hello_e():
    print("Hello")
    
def open_kiosk():
    a = input("언어 선택 한국어/English ")
    if a == "한국어":
        hello_k()
    elif  a == "English":
        hello_e()
open_kiosk()

'''
# 함수 중첨 안의 함수는 밖에서 호출 할 수는 없음 
#큰 함수 안의 함수는 큰 함수 안에서 호출해야함 
# 함수에 print() 사용
'''
def open_kiosk():
    def hello_k():
        print("안녕하세요")
    def hello_e():
        print("Hello")
    def lang_sel():    
        a = input("언어 선택 한국어/English\n:")
        if a == "한국어":
            hello_k()
        elif  a == "English":
            hello_e()
    lang_sel() #함수 안에서 함수를 호출해야 함. 
open_kiosk()
'''
'''
# 함수에 return 사용
def open_kiosk(): #함수 안에서 함수를 호출해야 함. 
    def hello_k():
        return "안녕하세요"
    def hello_e():
        return "Hello"
    def lang_sel():    
        a = input("언어 선택 한국어/English\n:")
        if a == "한국어":
            v = hello_k() #print(v)
        elif  a == "English":
           v = hello_e() #print(v)
        return v # print(v)

    n =lang_sel()
    return n #print(n)

m = open_kiosk()
print(m)

'''

'''

def cal(T,a,b): #부모 
    def plus (): #1.바로 전달 되는 것이 아님 3. 2번을 여기서 받음 
        print(a+b) #자식 밖의 매개 변수는 사용 가능 

    def minus (a,b):
        print(a-b)
    def sel(T):
        if T== "plus":
            plus() #2.이쪽으로 먼저 전달 
        elif T == "minus":
            minus(a,b) #비우면 둘 다 비우고, 채우면 둘 다 채워야 함. #헷갈리면 안전하게 다 쓰기 
    sel(T)
cal("plus", 1,2 ) #? plus는 밖의 함수 그래서 호출 불가 
'''
'''
def cal(T,a,b): 
    def plus (a,b):
        c = a+b
        return c

    def minus (a,b):
        c = a-b
        return c
    def sel(T):
        if T== "plus":
            r = plus(a,b) 
        elif T == "minus":
            r = minus(a,b) 
        return r 
    m = sel(T)
    return m

x = cal("minus", 9,2 ) 
print(x)
'''

def personal_info(file, t):
    def f_reader(file):
        f1= open(file, 'r')
        a = f1.read()
        f1.close()
        return a
    f = f_reader(file) #호출 및 변수 할당을 까먹지 말기! 
    data = f.split('\n')
    def f_info(): #고유의 매개 변수를 가질 수 있음 초보는 단계 별로 나누어서 쓰기
        name = []
        age =[]
        stu_id = []
        location = []
        phone = []
        i =0 
        while i < len(data):
            name.append(data[i])
            i+=6
        i = 1 
        while i < len(data):
            age.append(data[i])
            i+=6
        i = 2
        while i < len(data):
            stu_id.append(data[i])
            i+=6        
        i = 3
        while i < len(data):
            location.append(data[i])
            i+=6
        i = 4
        while i < len(data):
            phone.append(data[i])
            i+=6
        info = [name, age, stu_id, location, phone]
        return info
            
    r= f_info()

    def f_select(t):
        if t == '이름':
            for i in r[0]:
                print(i)
        elif t =='나이':
            for i in r[1]:
                print(i)
        elif t =="학번":
            for i in r[2]:
                print(i)
        elif t == "위치":
            for i in r[3]:
                print(i)
        elif t == '번호':
            for i in r[4]:
                print(i)
    f_select(t) #함수 호출 잊지 말기
    print()
a= personal_info("Personal_info.txt", "이름")
b= personal_info("Personal_info.txt", "나이")
c= personal_info("Personal_info.txt", "학번")
d= personal_info("Personal_info.txt", "위치")
e= personal_info("Personal_info.txt", "번호")

    
#매개 변수 최소화 버젼 