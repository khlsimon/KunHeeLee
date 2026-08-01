# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:23:05 2024

@author: skell
"""
#9주차 수업 
fruit = ["blueberry", "banana", "strawberry", "cranberry", "tomato", 
"mango"]
"""
for i in range(5): 
    print(i)
    continue #아랫부분을 안 처리 하면서 루프를 지속 
    print(fruit[i])
"""
'''
for i in range(10):
    if i%2==0:
        continue
        #pass 
    print(i)
    
print()
for i in range(10):
    if i%2==0:
        pass 
    else:
        print(i)
'''
    
# pass와 continue의 차이 contiune는 아예 실행을 안 함 
#pass는 자기 부분만 넘어감 밑의 코드는 실행 가능 

"""
jumin_list = ['950101-1234567', '891230-2345678', '010101-3456789', '800101-4567890', '721010-5678901', '660101-6789012', 
'030202-7890123', '480101-8901234', '051231-9012345', '980101-0123456']

for i in range(len(jumin_list)):
    if jumin_list[i][7] == '1' or jumin_list[i][7] == '2':
        print(jumin_list[i])
        continue

print()
for j in jumin_list:
    jl = j.split("-") 
    if jl[1][0] in "3456789":
        continue
    print(j)

print()

for j in jumin_list:
    jl = j.split("-") 
    if jl[1][0] != "1" and jl[1][0] != "2":
        continue
    print(j)
print()
for i in range(len(jumin_list)):
    if jumin_list[i][0] == '0':
        if jumin_list[i][7] == '3' or jumin_list[i][7] == '4':
            print(jumin_list[i])
    elif jumin_list[i][7] == '1' or jumin_list[i][7] == '2':
        print(jumin_list[i])
print()
k=jumin_list[:]
for i in range(len(jumin_list)):
    if jumin_list[i][0] == '0':
        if jumin_list[i][7] != '3' and jumin_list[i][7] != '4':
            k.remove(jumin_list[i])
        else:
            pass
    else:
        if jumin_list[i][7] != '1' and jumin_list[i][7] != '2':
            k.remove(jumin_list[i])
        else:
            pass
print(k)
print()
p=jumin_list[:]
for j in jumin_list:
    jl = j.split("-") 
    if jl[1][0] in "567890" or (jl[1][0] in "34" and int(jl[0][:2]) > 24):
        continue
    print(j)

for j in jumin_list:
    jl = j.split("-") 
    if (jl[1][0] in "12") or (jl[1][0] in "34" and int(jl[0][:2]) < 24): 
        pass
    else:
        p.remove(j)
print(p)
"""
# and or 활용이 취약한 듯 연습 필요 
# 파일 열고 쓰고/읽고 닫기! 기본 값은 읽기 
# w는 덮어쓰기 함 
# t는 텍스트 모드 t만 쓰는 것음 없음 
#파일(임시 이름임)= open()  파일.read() 또는 .write() *파일.close()* 전체 코트의 마지막에 쓰기
#처음에 열고와 마지막에 닫기를 같이 쓰기 습관!!! 닫지 않으면 컴퓨터가 힘들어짐
#절대 경로 주소를 무조건 다 적어서 찾게 함 
#상대 경로 이름과 주소의 일부만 씀 파이썬 파일과 같은 폴더에 텍스트 파일이 있어야함 
#.py와 텍스트 파일을 같은 폴더에 넣고 다른 사람과 공유 가능 !시험 문제 제출 방식!  
#파일 옮기기 주의(드레그X, 복붙 X)
#변수 = 파일변수.read()   변수의 담는 습관!
#f=open("file.txt","r") 전부 스트링으로 판정함 

f=open("Personal_info.txt","r")
f_r=f.read()
#print(f_r)
print("이름 라인 출력")
f_r_l=f_r.split("\n")
a=[]
i=0
while i <len(f_r_l):
    print(f_r_l[i])
    a.append(f_r_l[i])
    i+=6
print()


print()
print("이름만 출력")
b=": ".join(a)
c=b.split(": ")
i=1
while i < len(c):
    print(c[i])
    i+=2
print()
for i in f_r_l:
    if "Name" in i :
        result = i.split(": ")   
        print(result[1])
print()
for i in f_r_l:
    if "Name" in i :
        result = i.split(" ")   
        print(result[1], result[2])




f.close()



