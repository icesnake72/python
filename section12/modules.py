'''
모듈 : 파이썬 파일
'''
import myutil as mu

# myutil모듈로부터 get_total함수만 가져온다
from myutil import get_total as gt, get_average as ga

total = gt(90, 100, 100)
avg = ga(total, 3)

total = mu.get_total(80, 90, 100)
avg = mu.get_average(total, 3)