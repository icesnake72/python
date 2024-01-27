'''
Collection 
list
tuple
set
dictionary
'''
li = []     # 빈 리스트를 생성한다
li = [1,2,3,4,5]
print(li)
li.append(6)
li.append(7)
print(li)
li.remove(1)    # 리스트내에서 1이라는 값 삭제
print(li)

tp = tuple(li)
print(li[0])
print(tp[0])

s = set()   # 인덱싱이 없다
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)

# 인덱싱 기능이 없다
# Key : Value의 쌍(couple)으로 데이터를 관리한다.
di = dict()     # 빈 딕셔너리를 만든다.
di = {
        "tomato":"토마토", 
        "banana":"바나나", 
        "apple":"사과"
    }
print(di)
di['orange'] = '오렌지'     #딕셔너리명[키값] = 밸류
print(di)
di["apple"]  = "애플"
print(di)
print(di['tomato'])

some_fruit = di["banana"]
print(some_fruit)
some_fruit = di["tomato"]
print(some_fruit)
di.setdefault("tomato", "토마토")
di.update(tomato="토마토")

val = di.pop("tomato")
print(val)
print(di)