a='y'
while(a=='y'):
    chose=int(input('请选择几位水仙花（3-8）'))
    if chose==3:
        for i in range(1,10):
            for u in range(1,10):
                for y in range(10):
                    if i**3+u**3+y**3==i*100+u*10+y:
                        print(i*100+u*10+y)
    if chose==4:
        for q in range(1,10):
            for i in range(1,10):
                for u in range(1,10):
                    for y in range(10):
                        if i**4+u**4+y**4+q**4==q*10**3+i*100+u*10+y:
                            print(q*1000+i*100+u*10+y)
    if chose==5:
        for w in range(1,10):
            for q in range(1,10):
                for i in range(1,10):
                    for u in range(1,10):
                        for y in range(10):
                            if w**5+i**5+u**5+y**5+q**5==w*10**4+q*1000+i*100+u*10+y:
                                print(w*10000+q*1000+i*100+u*10+y)                    
    if chose==6:
        for e in range(1,10):
            for w in range(1,10):
                for q in range(1,10):
                    for i in range(1,10):
                        for u in range(1,10):
                            for y in range(10):
                                if e**6+w**6+i**6+u**6+y**6+q**6==e*10**5+w*10**4+q*1000+i*100+u*10+y:
                                    print(e*10**5+w*10000+q*1000+i*100+u*10+y)                    
    if chose==7:
        for r in range(1,10):
            for e in range(1,10):
                for w in range(1,10):
                    for q in range(1,10):
                        for i in range(1,10):
                            for u in range(1,10):
                                for y in range(10):
                                    if r**7+e**7+w**7+i**7+u**7+y**7+q**7==r*10**6+e*10**5+w*10**4+q*1000+i*100+u*10+y:
                                        print(r*10**6+e*10**5+w*10000+q*1000+i*100+u*10+y)                    
    if chose==8:
        for t in range(1,10):
            for r in range(1,10):
                for e in range(1,10):
                    for w in range(1,10):
                        for q in range(1,10):
                            for i in range(1,10):
                                for u in range(1,10):
                                    for y in range(10):
                                        if t**8+r**8+e**8+w**8+i**8+u**8+y**8+q**8==t*10**7+r*10**6+e*10**5+w*10**4+q*1000+i*100+u*10+y:
                                            print(t*10**7+r*10**6+e*10**5+w*10000+q*1000+i*100+u*10+y)                    
    a=input('是否再玩一次？（y/n）')                        
                        
                        
                    
                
