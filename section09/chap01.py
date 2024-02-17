'''
내장 함수 : 파이썬 기본 패키지에 이미 포함되어서 제공되는 유틸리티(유용한?) 함수들

a = charg(12,3,4,5,6,)  # 튜플

print('ㄹㄹㄹㄹㅇㅇㅇ') 
val = input('프롬프트')
int('100')
float()
len(list)

메소드(Method) : 어떤 객체가 제공하는 기능
함수(Function) : 파이썬이 기본적으로 제공하는 기능

객체들
list, tuple, set, dict, ''
'''






print(chr(97))      # 해당 unicode의 문자를 반환한다
print(ord('한'))    # 문자를 unicode의 값으로 반환한다

val = eval('3*4')   # 문자열로 수식을 입력하면 계산해서 그 값을 반환한다
print(val)
val = eval('val + 8')
print(val)


# print(format(10000, ','))
# 1_000_000_000

str(10) # 주어진 값을 문자열로 반환한다


# 수학 내장 함수들
# abs(), pow(), round(), sum()
abs(-10)
round(10.5)


# 시퀀스에 관련된 내장 함수들
# range()

li = [10, 20, 30, 40, 50]
for tp in enumerate(li):
    print(tp)
    

li = [5,3,4,2,8,1,9]
li2 = sorted(li)    # 오름차순 정렬
print( li2 )
li = sorted(li, reverse=True)  # 내림차순 정렬
print( li )




li = ['현대', '기아', '쌍용']
li2 = [1,2,3]

for comp in zip(li, li2):
    print(comp)