import jieba

cut = jieba.cut("河北新希望养殖有限公司", cut_all=True)
print("全模式：" + '/'.join(cut))
cut = jieba.cut("河北新希望养殖有限公司", cut_all=False)
print("精准模式：" + '/'.join(cut))
cut = jieba.cut_for_search("河北新希望养殖有限公司")
print("搜索引擎模式：" + '/'.join(cut))
