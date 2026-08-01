# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:28:45 2024

@author: skell
"""

#파일 쓰기(w)는 문자열만 가능 
#writelines는 문자열 리스트(숫자는 안 됨)가 가능. 단 다 붙여서 씀, 그래서 잘 안 씀 
#join은 문자만 연결 가능 
'''
a=[1,2,3,4,5]

f = open("write1.txt","w")
for i in a:
    r = str(i)
    f.write(r)
    f.write("\n")
new_a=[]
for i in a:
    new_a.append(str(i))
    

f.writelines(new_a)
f.close()
'''
with open("Personal_info.txt", "r") as f4:
    f4_r=f4.read()

    a=f4_r.split("\n")
b=[]
g=[]
k=0
for i in a:
    if k%6==0:
        b.append(a[k])
    k+=1    
c=": ".join(b)
d=c.split(": ")
i=1
while i < len(d):
    g.append(d[i])
    i+=2
with open("name_", "w") as f5:
    for i in g:
        f5.write(i)
        f5.write("\n")
print(f4_r)

'''
fl = open("Personal_info.txt", "r")
data = f1.read()
print(data)

f2 = open("name.txt", "w")
data = data.split()
'''