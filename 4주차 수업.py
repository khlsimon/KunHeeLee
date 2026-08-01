 # -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:26:38 2024

@author: skell
"""

name=["박민아","최현우","송성근","박상현",
           "김민철","이아름","데이비드"] #엔터 가능 
#print(name[0][0]) # name[몇 번의][몇번 째 ]

#마지막 인덱스 len()-1 
#리스트 안에 글자, 숫자, 리스트 중첩 가능
'''
EX
a=[1,[1,2],[1,[2,3]]]
a[2]
Out[13]: [1, [2, 3]]

a[2][1]
Out[14]: [2, 3]

a[2][1][1]
Out[15]: 3
'''
"""
#name[0] = "장지원" # list 는 중간에 바꿀 수 가 있음 문자열은 안 됨 
print(name)
print("\n")
# name[0][1]="박" 박지원 안 됨 

i=name.index("이아름")
print(i) # 왼쪽부터 처음에 만나는 인덱스 출력함 

new_name = [name[0],name[1],name[2],name[3],name[4],name[5]]
new_name_2 =name[:i+1]
new_name_3 =name[i+1:]
print(new_name)
print(new_name_2)
print(new_name_3)
"""
'''
#oh 이런 방법이 
# list 에서 len 함수 
a = [0,1,2,3,4,5,6,7,8]
print(len(a))
b= ["apple","banana","kiwi","melon"]
print(len(b[1]))

#리스트에서 sum 함수 만약 리스트의 요소가 전부 숫자이면 합한다. 
#전부 숫자가 아닐 경우 오류가 발생한다. 

print(sum(a))
'''
#리스트 홪장 
# =============================================================================
# append() 요소 1개를 마지막 위치에 추가하기 list.append(추가할 요소)

# =============================================================================
'''
b=[1,2,3,4]
#v=b.append("mango") 원본이 바뀜 
print(b.append("mango")) # 안 돼요, none 출력 
print("b",b) 
# split, replace 와 달리 원본 데이터를 바꾸는 함수 (변수 담기X, 프린트X)

# b=a 하나의 변수에 이름만 두 개 
#변수 할당하는 법 
c=b[:] # 두개의 변수 
print("c",c)
a = [1, 2, 3, 4, 5, "mango"]
b = a
c = a[:]
b.append(6)
c.append(7)
a.append(8)
print("a" ,a)
print("b" ,b)
print("c" ,c)
a [1, 2, 3, 4, 5, 'mango', 6, 8]
b [1, 2, 3, 4, 5, 'mango', 6, 8]
c [1, 2, 3, 4, 5, 'mango', 7]

'''
# extend 도 원본이 바뀐다. 리스트를  연결해주는 함수, 문자는 쪼개짐, 숫자는 안 됨

'''
a.extend(b)
print(a)
[1, 2, 3, 4, 5, 7, 8, 9]

a.append(b)
print(a)
[1, 2, 3, 4, 5, [7, 8, 9]]

a.extend("mango")
print(a)
[1, 2, 3, 4, 5, 'm', 'a', 'n', 'g', 'o']

a.extend(123)
error 
'''

# insert 는 중간에 요소를 넣을 수 있음. 원본을 바꿈 
#원리: 뒤에 공간을 만들고 넣고 싶은 자리 많큼 그 빈송간을 옮김
'''
a=[1,2,3]
a.insert(1,9)
print(a)
[1, 9, 2, 3]
'''
"""
a = [1,2,3,4,5] # +는 원본을 유지한 extend
b=[7,8,9]
c=a+b
print(a,b,c)
[1, 2, 3, 4, 5] [7, 8, 9] [1, 2, 3, 4, 5, 7, 8, 9]

a += b # extend와 같음 a=a+b, 
#숫자는 += -=, *= /= %=가능 나누기는 결과가 실수로 나옴
#하지만, 글자 및 리스트는 +=만 가능 
print(a)
"""
'''
d="Yee"
e="EEE"
d+=e
print(d)
YeeEEE
'''
'''
b=[1,2,3,4]
v=b.append("mango") #원본이 바뀜 
print(b.append("mango")) #  none 출력 원본이 바뀐다는 신호
print(v) #none 출력 
print("b",b) 
'''
"""
b='Yee'
c="ee"
b-=c
print(b)
TypeError: unsupported operand type(s) for -=: 'str' and 'str'
"""

# del 에약어  del listname[index_number] 원본의 지정한 일부를 삭제 
#del은 그 자체로 출력이 불가능 
"""
a= [1,2,3,4,5,5,6]

print("before del", a)
del a[0]
print("after del" ,a)
before del [1, 2, 3, 4, 5, 5, 6]
after del [2, 3, 4, 5, 5, 6]
"""
'''
print(del a[0])
SyntaxError: invalid syntax
'''
#remove() 지정한 값 중 같은 값을 삭제, 처음에 발견한 값만  원본에서 삭제 
# pop() 마지막 값을 출력하고 삭제 변수.pop() 원본이 변경됨 
#근데 출력 할 경우 그 지워진 마지막 부분이 나옴 
# pop(index_number)
'''
a.remove(5)
print(a)
[1, 2, 3, 4, 5, 6]
'''
#a.pop(3)
#print(a)
#[1, 2, 3, 5, 5, 6]

#a.clear() #원본을 삭제 
#print(a) -> []

#리스트도 문자열 처럼 슬라이싱을 할 수 있다. 슬라이스 재활용
#slice(a,b,c) [a:b:c] slice() 는 c만 생략 가능 
'''
b=[9,8,7,6,5,4,3,2,1]
a=[0,1,2,3,4,5,6,7,8,9]
a1 = slice(1,3)
print(a[a1]) 
print(b[a1])
print(a1) 
a2 = slice(0, len(a),2)
'''


#join 분열된 것을 결합 "연결문자".join
'''
m = "mango"
list_m=list(m)
m_n="".join(list_m)
print("list_m", list_m)
print('"".join',m_n)
'''
'''
f="mango"
list_f=list(f)
list_f.pop(0)
list_f.insert(0,'M')
f_n="".join(list_f)
print(f_n)
'''
"""
f="mango"
F=list(f)
F[0] = F[0].upper()
new_f = "".join(F)
print(new_f)
"""
'''
b=["hello", 'hello',"hello"] #리스트
a = "Hello, Hell, Hello" #문자열 
num2 = a. count("Hello")
num3 = a. count("Hell") #일부만 있어도 있다고 판정
print(num2)
print(num3)
num = b.count("hello") # 딱 그것만 있어야 있다고 판정 
num4 = b.count("h")
print(num)
print(num4)
'''
"""
a=[1,2,46,8,8,5,7,3]

b=sorted(a)
c=sorted(a, reverse = True)
print("a",a)
print("b",b)
print("c",c)

a.sort()
print("a.sort", a)

m = "mango"
list_m=list(m)
m_n="".join(list_m)
print("list_m", list_m)
print('"".join',m_n)

"""
text2 = "Hello, everyone!"
a=text2.replace("H"," ")
print(a)