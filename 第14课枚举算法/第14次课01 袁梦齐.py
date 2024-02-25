while(1):
 a=int(input("请输入你想求的水仙花数的位数,如果你想退出，请输入'退出'\n"))

 if (a=='退出'):
     break

 a=int(a)

 
 if (a==3):
     for i in range(10):
         for j in range(10):
             for m in range(10):
                 num=i*100+j*10+m
                 if i**3+j**3+m**3==num and (i!=0):
                    print(f"三位数的水仙花数为{num}")

 elif (a==4):
       for i in range(10):
           for j in range(10):
               for m in range(10):
                   for n in range(10):
                       num=i*1000+j*100+m*10+n
                       if i**4+j**4+m**4+n**4==num and (i!=0):
                          print(f"四位数的水仙花数为{num}")


 elif (a==5):
       for i in range(10):
           for j in range(10):
               for m in range(10):
                   for n in range(10):
                       for h in range(10):
                           num=i*10000+j*1000+m*100+n*10+h
                           if i**5+j**5+m**5+n**5+h**5==num and (i!=0):
                              print(f"五位数的水仙花数为{num}")
 elif (a==6):
       for i in range(10):
          for j in range(10):
              for m in range(10):
                  for n in range(10):
                      for h in range(10):
                          for z in range(10):
                              num=i*100000+j*10000+m*1000+n*100+h*10+z
                              if i**6+j**6+m**6+n**6+h**6+z**6==num and (i!=0):
                                 print(f"六位数的水仙花数为{num}")
 elif (a==7):
       for i in range(10):
           for j in range(10):
               for m in range(10):
                   for n in range(10):
                      for h in range(10):
                          for z in range(10):
                              for y in range(10):
                                  num=i*1000000+j*100000+m*10000+n*1000+h*100+z*10+y
                                  if i**7+j**7+m**7+n**7+h**7+z**7+y**7==num and (i!=0):
                                     print(f"七位数的水仙花数为{num}")

 elif (a==8):
       for i in range(10):
           for j in range(10):
               for m in range(10):
                   for n in range(10):
                       for h in range(10):
                           for z in range(10):
                               for y in range(10):
                                   for x in range(10):
                                       num=i*10000000+j*1000000+m*100000+n*10000+h*1000+z*100+y*10+x
                                       if i**8+j**8+m**8+n**8+h**8+z**8+y**8+x**8==num and (i!=0):
                                          print(f"八位数的水仙花数为{num}")                





























                       
