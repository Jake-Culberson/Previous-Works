


F = [1000000]

fibonacci = 100


i = 0
while (i+1) <= fibonacci:
    
    nextnum = F[0+i]*1.02
    round(nextnum)
    nextnum += 10000
    F.append(nextnum)
    
    print(f"{i}: ${F[i]}")
    i = i+1
    