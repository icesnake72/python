i = 2
j = 1
while j <= 9:   # 곱수
    i=2
    while i <= 9: # 단수
        print(f'{i} x {j} = {i*j}', end='\t') 
        i+=1
        
    j+=1
    print()