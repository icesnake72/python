'''
비시퀀스와 for 반복문
'''

comp = {'현대', '기아', '쌍용', '벤쯔'} # 초기화된 세트
for s in comp:
    print( s )
    
di = {
    'flower':'꽃',
    'car':'자동차',
    'cup':'컵',
    'object':'객체',    
    }
# 딕셔너리를 이용하여 for반복문을 수행하면 key를 반환한다
for s in di:
    print( f'{s} : {di[s]}' )
    di.get(s)    # di[s]