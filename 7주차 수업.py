# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:40:04 2024

@author: skell
"""
"""
country_info = {
    'USA': {
        'capital': 'Washington D.C.',
        'population': 331002651,
        'continent': 'North America',
        'language': 'English'
    },
    'China': {
        'capital': 'Beijing',
        'population': 1439323776,
        'continent': 'Asia',
        'language': 'Mandarin'
    },
    'Brazil': {
        'capital': 'Brasília',
        'population': 212559417,
        'continent': 'South America',
        'language': 'Portuguese'
    },
    'India': {
        'capital': 'New Delhi',
        'population': 1380004385,
        'continent': 'Asia',
        'language': 'Hindi'
    },
    'Russia': {
        'capital': 'Moscow',
        'population': 145934462,
        'continent': 'Europe/Asia',
        'language': 'Russian'
    }
}

a=list(country_info.keys())
b=list(country_info.values())

i=0
while i < len(country_info):
    print(a[i],":", b[i]["capital"])
    i+=1

print()
#기본 구조
print(a[0], ":",country_info["USA"]['capital'])
print(a[1], ":",country_info["China"]['capital'])
print(a[2], ":",country_info["Brazil"]['capital'])
print(a[3], ":",country_info["India"]['capital'])
print(a[4], ":",country_info["Russia"]['capital'])

coun_info = list(country_info.items()) 
# 두 개를 같이 뽑고(딕셔너리는 순서가 없어서 혼합가능) 키와 벨류를 따로 뽑는 것이 안전
print()
q=0
while q < len(coun_info):
    print(coun_info[q][0],":",coun_info[q][1]['capital'])
    q+=1
"""


'''
우유(1L) : ₩2,400
 빵(1개) : ₩3,200
 사과(1kg) : ₩5,000
 닭가슴살(1kg) : ₩9,800
 과일은15% 할인
'''

milk_cost=2400
bread_cost=3200
apple_cost=5000
chicken_cost=9800
a_discount=0.15
m_t=0
b_t=0
c_t=0
a_t=0
sh_list={}
shop=["a","b","c","m"]
while True:
    item = input("원하는 품목 입력, 우유m, 빵b,사과a,닭고기c,주문 완료q: ")
    if item == "q":
        break
    num = input("수량 ")
    if num == "q":
        break
    if num in shop: 
        pass
    else:
        print("error")
    sh_list[item]=int(num)
sh_list = list(sh_list.items())
i=0
while i < len(sh_list):
    if sh_list[i][0] == 'm':
        milk_n=sh_list[i][1]
        m_t=milk_n*milk_cost
    elif sh_list[i][0] == 'b':
        bread_n=sh_list[i][1]
        b_t=bread_n*bread_cost
    elif sh_list[i][0] == 'a':
        apple_n=sh_list[i][1]
        a_t=apple_n*apple_cost*(1-a_discount)
    elif sh_list[i][0] == 'm':
        chicken_n=sh_list[i][1]
        c_t=chicken_n*chicken_cost
    i+=1
total = m_t+b_t+c_t+a_t


if a_t:
    print(f"총 결재금액, {round(total)}원 과일 할인 적용")
else:
    print(f"총 결재금액, {round(total)}원")










"""
fruit=['a','b','c']

for i in range(len(fruit)):
    print(f'{i+1}.{fruit[i]}')
        
t=0
for j in range(1,11):
    t+=j
print(t)


t=0 
for i in range(1, 100, 2):
    t+=i
print(t)
t=0
for i in range(100, 1, -2):
    t+=i
print(t)
"""  
'''
a="We're studying for loop"
w=a.split()
l=1
for i in w:
    print(f"{l},{i}")
    l+=1
    print(f"{i}, {len(i)}")
#for j in w:
    #if 'o' in j:
        #print(j)
'''
#딕셔너리는 키만 나옴 벨류를 보고 싶으면 .values() 사용
