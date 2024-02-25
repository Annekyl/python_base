def hnt(n, a, b, c): 
    if n >= 1:        
        hnt(n-1, a, c, b)  
     
        print(f"把第%d个盘子从{a}移动到{c}"%n)
    
        hnt(n-1, c, b, a)
g=int(input("输入汉诺塔层数："))
hnt(g,"a","b","c")
