#需要安装pyecharts

from pyecharts.charts import Bar

dic={'a':69,'b':669,'c':400,'d':255,'e':155,'f':55}
#dic={'a':'899','b':'669','c':'400','d':'55'}   #值为字符串也不影响绘图

#　绘图
list1=list(dic.keys())      #提取字典里的键作X轴
list2=list(dic.values())  #提取字典里的值作Y轴数据
Bar().add_xaxis(list1).add_yaxis("数据统计图",list2).render("统计图.html")

