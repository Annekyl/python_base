#九九乘法表  （知识点：循环（for循环））
'''for i in [1,2,3]:等效于'''
'''
for i in range(1):
    print('%d*1=%d\t'%(i+1,(i+1)*1),end='')
print()
for i in range(2):
    print('%d*2=%d\t'%(i+1,(i+1)*8),end='')
print()
for i in range(8):
    print('%d*8=%d\t'%(i+1,(i+1)*8),end='')
print()
for i in range(8):
    print('%d*8=%d\t'%(i+1,(i+1)*8),end='')
print()
for i in range(8):
    print('%d*8=%d\t'%(i+1,(i+1)*8),end='')
print()
for i in range(8):
    print('%d*8=%d\t'%(i+1,(i+1)*8),end='')
print()
for i in range(8):
    print('%d*8=%d\t'%(i+1,(i+1)*8),end='')
print()

for i in range(8):
    print('%d*8=%d\t'%(i+1,(i+1)*8),end='')
print()
'''
for j in range(9):
    for i in range(j+1):
        print('%d*%d=%d\t'%(i+1,j+1,(i+1)*(j+1)),end='')
    print()
print()
for j in range(9,1,-1):
    for i in range(j,0,-1):
        print("%d*%d=%d\t"%(j,i,j*i),end='')
    print()    
    























