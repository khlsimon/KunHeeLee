# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:13:20 2024

@author: skell
"""


#지역 변수 한 함수 안에서만 유효한 변수 한 변수 안에서 정의 
#전역 변수 프로그램 내에서 유효한 변수 
#global는 잘 사용하지 않음 
#함수 값을 리턴하고 매개변수를 쓰고 그 매개변수를 집어 넣기. 

a=1#전역변수
def vartest(x): #매개변수 x x를 a로 써도 실행은 됨 헷갈리는 것 주의 
    x=a+1
    print(x)
    
vartest(a) # a=2 1인 a를 함수에 넣어서 나온 결과 
print(a) # a=1 전역변수의 a 출력 
print()
#기본값 매개변수는 정의 함수를 정의할 떄 정해진 값을 넣음, 정해지지 않으면 기본값

def p_s(data, count=3):
    for i in range(count):
        print(data)


p_s("안녕")
#기본값 매개 변수 뒤에 일반 매개변수가 올 수 없음(맨 뒤로 가야함)
#기본값 매개 변수는 생략 가능, 하지만 맨 앞에 쓰면 생략시 순서 오차가 생김.
print()
#키워드 매개변수는 호출 키워드가 있으면 순서가 바뀌어도 됨 
#주요 활용처 매개변수가 매우 많을 때 
#주의 일부는 키워드, 매개변수일 경우 키워드가 뒤로!
p_s(data = "yee",count =4)
print()
#가변 매개 변수(매개 변수에 넣을 수 있는 개수 조절 가능, 몇 개 들어올지가 모른다는 의미)
#가변 매개 변수는 맨 뒤에 와야하며, 하나만 사용 가능!
def plus(*a):
    print(sum(a))# 튜플로 판정! 
plus(1,2,3,4)

print()
def plus_2(*a):
    x=0
    for i in a:
        x+=i
    print(x)
plus_2(1,2,3,4)

def f_reader(file, mode, l):
    if mode == "r":
       f1= open(file, 'r')
       a = f1.read()
       f1.close()
       return a
    if mode == "w":
        r = ", ".join(l)
        f2 = open(file, 'w')
        f2.write(r)
        f2.close()

def f_info(v,*t):
    infos=[]
    data = v.split('\n')
    for tt in t:
        info = []
        for d in data:
            if tt =="이름":
                d_type = "Name"
            elif tt == "나이":
                d_type = "Age"
            elif tt == "학번":
                d_type = "id"
            elif tt == "위치":
                d_type = "Location"
            elif tt == "전화":
                d_type = "Phone"
            if d_type in d:
                d = d.split(": ")
                info.append(d[1])
        infos.append(info)
    return infos
   
 #return이 함수 맨마지막에 와야함 

a= f_reader("Personal_info.txt", "r", "")
b=f_info(a, "이름", "나이", "학번","위치","전화")
def mod_print(b):
    for i in range(len(b[0])):
        r = ""
        for j in range(len(b)):
            r +=b[j][i] + " "
        print(r)
mod_print(b)

# 딕셔너리 가변 매개 변수 ** key = "value" 형식으로 작성 
print()
def print_POS(**words):
    for i in words:
        print(f"{i}:{words[i]}")
print_POS(love="verb", computer="noun")

print()
def mod_print_2 (b):
    info_dic = {}
    for i in range(len(b[0])):
        r=[]
        for j in range(len(b)):
            if j!=0:
                r.append(b[j][i])
            else:
                k = b[j][i]
        info_dic[k] = r
    print(info_dic)
mod_print_2(b)
                






