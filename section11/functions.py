'''
사용자 정의 함수

print(), input(), len(),...

함수 정의 : Define a function
함수의 호출 : Call a function

매개변수 : 함수의 입력값
반환값 : 함수의 출력값

매개변수 O, 반환값 O
매개변수 x, 반환값 O
매개변수 O, 반환값 x
매개변수 x, 반환값 x
'''



# 함수의 정의
# 매개변수 O, 반환값 x
# consumer function(method)
def greet(message, count):  # 파라미터(parameter), 매개변수, 아규먼트(Argument), 인수, 인자
    for n in range(count):
        print(message)       
        
# 매개변수 x, 반환값 x        
def say_hello():
    print('안녕하세요, 반갑습니다')

# 매개변수 x, 반환값 O
def get_pi():
    return 3.14


# 매개변수 O, 반환값 O
def add(num1:int, num2:int)->int:
    return num1 + num2


# 문자열에서 문자의 갯수를 구하는 함수를 만들기
def upper_case(message:str)->str:
    return message.upper()
    

s = 'abcde'
s.upper()

greet('안녕하세요', 5)
greet('반갑습니다', 3)
greet('잘가세요', 7)

num3 = add(10, 20)
num3 = add(3, 7)
num3 = add(1.1, 3.5)
num3 = add(1.1, 3)
num3 = add('안녕하세요','반갑습니다')

