'''
파이썬의 특별한 함수 스타일
'''

# 코드의 생략
def pass_func():
    ...

# 가변 매개 변수
def show(*vals:int, horiz:int=1):
    print(vals)
    for n in vals:
        if horiz==1:
            print(n, end='\t')
        else:
            print(n)
            
    print()
    
  
def greet(message:str, temp:int=2, count:int=3 ):
    for n in range(count):
        if count==2:
            return
        
        print(message)
        
#
def my_divmod(num1:int, num2:int):
    mok = num1 // num2
    nam = num1 % num2
    return mok, nam


mok, nam = my_divmod(10, 3)
print(mok, nam)

values = my_divmod(10, 3)
print(values[0], values[1])


# 다중 반환 함수
# mok, nam = divmod(10, 3)
# print(mok, nam)

# values = divmod(10, 3)  # 튜플로 반환한다
# print(values)



# greet('안녕하세요', count=5)
# greet('반갑습니다')

# show(1,2,3,4,5, horiz=1)
# show(1,2,3)



