import os 

with open(r'HW_6\user_input.txt','w+',encoding='utf-8') as f :
    a=input()
    while a!='' :
        f.write(f"{a}\n")
        a=input()