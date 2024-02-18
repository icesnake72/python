'''
키(Key)가 과목명, 값(value)이 점수인 marks 딕셔너리
해당 딕셔너리에 저장된 점수들의 평균을 반환하는 get_average() 함수를 구현하세요

반환값 : 평균
함수이름 : get_average()
매개변수 : 딕셔너리 marks

출력형식)
평균은 85.0점 입니다
'''

def get_average(marks:dict) -> float:
    # total = marks['국어'] + marks['영어'] + marks['수학']
    total = 0
    for key in marks:
        total += marks[key]
    
    return total / len(marks)


marks = {'국어':90, '영어':80, '수학':85}

# 호출
avg = get_average(marks)

# 평균은 85.0점 입니다
print(f'평균은 {avg:.1f}점 입니다')
