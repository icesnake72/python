
# 점수들을 받아서 총점을 구하는 함수
def get_total(*score:int) -> int:
    total = 0
    for jumsu in score:
        total += jumsu
        
    return total


def get_average(total:int, count:int) -> float:
    return total / count


def __get_memory():
    ...
    
    
