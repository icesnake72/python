'''
연산자와 우선순위
'''

'''
15 = 5 + ((10 * 4) / 3)



산술연산자 : +, -, *, /, //(정수의 나누기, 몫만 취함), %(정수의 나누기, 나머지만 취함), **
대입연산자 : =, +=, -=, *=, /=, //=, %=, **=
total = 0
total = total + number ==> total += number
total = total + 1 ==> 
total = total + 1
total = total + 1

관계연산자 : >, >=, <, <=, ==, != 
관계연산의 결과는 True 또는 False (논리값)로 정해진다
False = 5 > 10

논리연산자 : and, or, not
논리연산의 결과는 True 또는 False (논리값)로 정해진다
True = True or False

비트연산자 : &, |, ^, ~, <<, >>, >>>

기타연산자 : 삼항연산자(참 if 논리식 else 거짓), in, +, *
'''

print( 5 > 10 )
result = 5 > 10
print( result )
result = 5 <= 10
print( result )
result = 5 == 10
print( result )

# 논리 연산
res1 = 5 == 10  # False
res2 = 5 <= 10  # True
print(res1, res2) # False True

result = res1 and res2 # False and True ===> False
print( result )

result = res1 or res2 # False or True ===> True
print( result )

result = not res2 # not True ===> False
print( result )

# age = int(input('나이를 입력하세요'))
# age 10보다 크고 18보다 작으면 청소년
# (10 < age) and (age < 18)

# 비트의 연산의 결과는 산술연산과 동일하다
'''
1byte ===> 8bit
0 ===> 0000 0000
1 ===> 0000 0001
2 ===> 0000 0010
3 ===> 0000 0011
4 ===> 0000 0100
5 ===> 0000 0101
6 ===> 0000 0110
7 ===> 0000 0111
8 ===> 0000 1000

비트연산자 : &, |, ^, ~, <<, >>, >>>
  0011 
| 0100
=======
  0111

^ : Exclusive OR
  0011 
^ 0110
=======
  0101

~ 0011 ====> 1100

Shift 연산 : 비트를 왼쪽(오른쪽) 방향으로 이동시킨다

result = 3 << 2  ==> 3을 왼쪽으로 2비트 이동시킨다
result = 0011 << 2
result = 1100 

>>, >>>
1001 1000
'''




