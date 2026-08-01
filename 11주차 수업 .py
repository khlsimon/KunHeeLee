# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:54:26 2024

@author: skell
"""
'''
import calendar
import random
calendar.prmonth(2003,3)
print()

print(calendar.weekday(2024, 5, 15)) #월요일이 0번 
print(random.randint(0, 1)) #정수만 판정함.
print(random.random()) 
'''
#def multiply (a,b): #함수 정의 및 호출 입력과 결과 모두 있음
    #return a*b

def multiply (a,b): #함수 정의 및 호출  입력만 있는 함수
    result = a*b
    print(result)

c=multiply(9, 9) #81 none 
print(multiply(9, 9)) # 81 none
print(c) #none 


def hi():
    a= "Hi"
    return a 

b=hi()
print(b)

def hola():
    a = "Hola"
    print(a)
    
hola()
c= hola()
print(c) #none도 함께 나옴 