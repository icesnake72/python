'''
1 ~ 99사이의 모든 정수들을 대상으로...
369게임을 한 결과를 출력

1   2   짝  4   5   짝  7   8   짝  10
11  12  짝...
21  22 ...                          짝
짝  짝  짝짝 짝 짝  짝짝 짝 짝  짝짝  40   
41
51
짝  짝  짝짝 짝 짝  짝짝 짝 짝  짝짝  70   
71 ..
81 ...
짝  짝  짝짝 짝 짝  짝짝 짝 짝  짝짝
'''

ten = 0
il = 0
for n in range(1, 100):
    out = ''    # 짝 을 출력하기 위한 변수 초기화
    ten = n // 10   # 10의 자리를 판단하기 위한 변수
    il = n % 10     # 1의 자리를 판단하기 위한 변수
    
    # 10의 자리를 3으로 나눈 나머지가 0이면 3, 6, 9중에 하나임
    if ten % 3==0 and ten!=0:   
        out = '짝'  # 짝을 대입
        
    # 1의 자리를 3으로 나눈 나머지가 0이면 3, 6, 9중에 하나임
    if il % 3==0 and il!=0:
        out += '짝'  # 짝을 추가
    
    # 3항 연산자를 이용하여, out변수에 값이 있으면 out을, 아니면 n을 출력
    print( n if len(out)==0 else out, end='\t')
    
    if n % 10 == 0: # 10의자리까지 다 갔으면 
        print()     # 줄바꿈
        
    