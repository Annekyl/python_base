import random as r
class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='■'
        self.stat=False
    def __str__(self):
        return ("mine%d%d"%(self.x,self.y))
   
mines=[[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mines[i][j]= Mine(i,j)
sum=0
while(sum<10):
    a,b=r.randint(0,9),r.randint(0,9)
    if(mines[a][b].stat==False):
        mines[a][b].stat=True
        mines[a][b].txt='❁'
        sum+=1

print("\n\n",end=' ')
for i in range(10):
    print(' '+str(i),end=' ')
print()
for i in range(10):
    print(i,end=' ')
    for j in range(10):
        print(mines[i][j].txt,end=' ')
    print()
#■□
