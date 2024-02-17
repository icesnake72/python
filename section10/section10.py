'''
메소드
어떤 객체가 가지고 있는 함수
'''

# 문자열의 메소드
# print( "10자리 폭 왼쪽 정렬 '{:<10d}'".format(123) )
# print( "10자리 폭 오른쪽 정렬 '{:>10d}'".format(123) )
# print( "10자리 폭 가운데 정렬 '{:^10d}'".format(123) )

val = 123
print(f"10자리 폭 왼쪽 정렬 '{val:<10}'")

val = 42.195
print(f"10자리 폭 왼쪽 정렬 '{val:>10.3f}'")

# count : 문자열안에서 특정 문자(열)의 갯수를 반환한다
s = 'Hello Python'
print(f'문자열 {s}에서 o는 {s.count('o')}개 있습니다.')
s.count('o', 6) # 'o'를 s문자열에서 6번째 인덱스에서부터 찾아서 그 갯수를 반환한다

s = 'Hello Python Python Python Python'



# find : 문자열에서 주어진 문자(열)을 찾아 그 인덱스를 반환한다
# 못찾으면 -1을 반환한다
s = 'Hello Python'
print(f"{s}에서 'o'는 {s.find('o')}번째 인덱스 위치에 있습니다")
print(f"{s}에서 'p'는 {s.find('p')}번째 인덱스 위치에 있습니다")
print(f"{s}에서 'Python'는 {s.find('Python')}번째 인덱스 위치에 있습니다")
print(f"{s}에서 'Python'는 {s.find('PythOn')}번째 인덱스 위치에 있습니다")


# index : 문자열에서 주어진 문자(열)을 찾아 그 인덱스를 반환한다
# 에러(예외상황, Exception)를 발생시킨다
idx = s.index('o')
# idx = s.index('p')


# 대소문자 변환시키기
print(s.upper())    # 대문자로 변환
print(s.lower())    # 소문자로 변환

# join
print('-'.join(['010','1234','5678']))
print('+'.join('python'))

print(''.join(['1','2','3','4','5','6','7','8','9']))

# split
s = "Hello Python"
li = s.split()   # s문자열에서 공백을 기준으로 데이터를 나누어 리스트를 생성한다
print(li)

s = "010-1234-5678"
li = s.split('-')   # s문자열에서 공백을 기준으로 데이터를 나누어 리스트를 생성한다
print(li)

# replace : 
s = "Hello Python"
s.replace('H', 'h')     # 문자열 내의 특정 문자를 주어진 문자로 대치시킨다, H --> h
s.replace('P', 'p')     # P --> p

# lstrip
# rstrip
# strip
s = '      apple'
s.lstrip()  # 왼쪽에 공백들을 전부 지운다
s.strip()   # 양쪽끝 공백들을 전부 지운다

# 리스트 메소드 : 추가, 삽입, 삭제,
li = [10, 20, 30]
li.append(40)   # 리스트에 데이터를 추가
li.append(50)   # 리스트에 데이터를 추가

li.insert(1, 15)    # 두번째 요소에 값 15를 삽입

li.extend([10, 20]) 
print(li)

value = li.pop()    # 인덱스를 지정하면 해당 인덱스의 값을 밖으로 꺼낸다
print(value)

value = li.pop(1)    # 인덱스를 지정하면 해당 인덱스의 값을 밖으로 꺼낸다
print(value)

li.remove(10)   # 리스트 내의 값을 지정하여 삭제한다
li.clear()      # 리스트의 내용을 전부 지운다

# 세트(SET) 메소드
s1 = {10, 20, 30,}
s2 = set(20, 30, 40)

# 교집합 s1 & s2
s3 = s1.intersection(s2)
print(s3)

s3 = s1 & s2
print(s3)

# 합집합 s1 | s2
s3 = s1.union(s2)
s3 = s1 | s2

# 차집합 s1 - s2
s3 = s1.difference(s2)
s3 = s1 - s2
