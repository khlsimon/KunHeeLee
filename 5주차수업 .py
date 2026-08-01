# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:40:55 2024

@author: skell
"""

#5주차


#튜플() 리스트와 유사하나, 처음 저장된 요소의 값을 바꿀 수가 없음. 
#tuple() : 튜플로 바꿔주는 함수 
#추가, 변경, 삭제, sort()는 안 됨 
#만약 수정하고 싶다면 리스트와 필요.
'''
a=(1,2,3,4)
b=list(a)
b.remove(1)
print(b)
'''
#set{} 인덱스가 없다. set() set로 만들어주는 함수
#중복되는 요소를 포함할 수 없음, 순서가 없음,
#이를 이용해서 중복을 삭제할 수 있음 단 순서를 못 지킴
'''
f1={"apple","banana","apple"}
f2={"banana",'mango'}
print("f1",f1)
print("f2",f2)
f3=f1-f2
print("f3",f3)
f4=f1|f2
print("f4",f4)
f5=f1 or f2
print("f5",f5)
f6=f1&f2
print("f6",f6)
f7=f1 and f2
print("f7",f7)
'''
#차집합 -,  합집합 | or(X), 교집합 & and(x)
#순서를 만들면서 중복을 없애고 싶으면
"""
D=[1,1,1,2,3,6,5,8,9]
E=list(set(D))
print(E)
"""
#문자열을 세트하면 알파벳 단위로 쪼개짐 대소문자는 구분
'''
alice = """'Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her 
elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows 
it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of 
all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an 
attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which 
cause her to shrink too small to reach the key which she has left on the table. She eats a cake with 
"EAT ME" written on it in currants as the chapter closes.’"""
A_L=A=alice.lower()
A_L_N=A_L.replace("\n","").replace(",","").replace('.','').replace("'","").replace('"','')

A_L_S=A_L_N.split()
C=list(set(A_L_S))
C.sort()
print(C)
print(len(A_L_S))
print(len(C))
'''
#딕셔너리 순서가 없음 {Key:Value}

#딕셔너리는 딕셔너리[key]=value로 바로 요소를 넣거나 변경할 수 있음
#key는 인덱스와 비슷 중복되는 것 없음, value는 중복가능 
#key는 주로 문자열, value에는 문자, 숫자, 리스트, 딕셔너리 사용 가능
"""
dic={}
dic["ant"]="개미"
dic["bee"]="벌"
print("변경 전",dic)
dic["ant"]="hormiga"
print("변경 후",dic)
"""
'''
a={}
a[1]=1 
a[2]="two"
a[3]=["three","삼"]
a[4]={"four":"사"}
print(a)
'''
'''
#update() dic1.update(dic2) 원본인 dic1을 바꿈 딕셔너리간 연결 
A={"A":1}
b={"B":2}
A.update(b)
print(A)
print(A["B"])
# del dic["key"] key를 없앰 원본을 바꿈 
del A["A"]
print(A)
#dic.keys() 모든 key들을 출력 dict_keys 라는 자료형으로 나옴 
#튜플과 같이 그 자체로는 수정이 어려움 sorted는 됨
#dic.values() 모든 values를 출력 dic.keys() 와 같음
#dic.items(), 키와 밸류를 튜플로 묶어준다. 
#수정을 하려면 list()로 씌우기
print(A.keys())
print(A.values())
print(A.items())
c=list(A.keys())
d=list(A.values())
e=list(A.items())
print(c)
print(d)
print(e)
'''
#딕셔너리를 쌍으로 정리, 키를 기준 sorted(dic.items())
#value를 기준으로 정릴 패키치가 필요
#operator 또는 lambda 필요 
'''
import operator 
a={"a":12,"b":13,"c":1}
print(sorted(a.items(),key=operator.itemgetter(1),reverse=True))
b=sorted(a.items(), key = lambda z:z[1])
print(b)
'''
# in은 그 안에 있는 지 판정, key를 기준으로 
#리스트는 판정 단어가 다 맞아야 True 판정 
#문자열은 판정 단어가 일부만 있어도 True 판정
"""
s=["apple"]
x="apple"
print("app" in s)
print("app" in x)
"""
#제어 구문 if,while, for 
# if (조건) 들여쓰기 중요 
# == 같은지 비교하는 연산자 
# != 안 같은지 비교하는 연산자 
#money ="have" True 글자가 있는 문자열
#money ="" False 글자가 없는 문자열
#money = 0 False 숫자 0
#money = 100 True 숫자 0을 제외한 숫자 음수도 True 판정 
#money = True True
#money = False False
'''
if money:
    print("buy")
else:
    print("not buy")
'''

lux=int(input("write lux "))
if lux < 50:
    print("ON")
elif lux >= 200:
    print("OFF")
else:
    print("Keep")
    
    
#input("적절한 설명 ") 값을 문자열로 입력 받음,
# 변수 이름을 써주기, int(input()) 같이 
num1=input("숫자를 입력하세요:\nex: 10 ")




