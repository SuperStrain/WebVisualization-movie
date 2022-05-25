# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

import jieba    #分词
from matplotlib import pyplot as plt    #绘图，数据可视化，生成图片（而echarts用于html）
from wordcloud import WordCloud     #词云
from PIL import Image   #图片处理
import numpy as np      #矩阵运算
import sqlite3          #数据库




#1、准备词云所需的文字（词）
con=sqlite3.connect('movie.db')
cur=con.cursor()
sql='select instroduction from movie250'
data=cur.execute(sql)
text=""
for item in data:
    text=text+item[0]
# print(text)#测试显示结果
cur.close()
con.close()

#2、分词并设置停用词
cut=jieba.cut(text)
string=' '.join(cut)#化作字符串，方便打印
# print(len(string))

#设置停用词
stopwords = set()
content = [line.strip() for line in open('./static/stopWords.txt',encoding='utf-8').readlines()]
stopwords.update(content)


#3、设置词云
img=Image.open(r'.\static\assets\img\tree.jpg')#打开遮罩图片
img_array=np.array(img)     #将图片转换为数组
wc=WordCloud(
    background_color='white',
    mask=img_array, #设置遮罩
    font_path='simhei.ttf',    #设置字体，字体所在位置：C:\Windows\Fonts
    stopwords = stopwords       #设置停用词语
)#设置词云的基本信息
wc.generate_from_text(string)

#4、绘制图片并生成
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标
# plt.show()#测试显示结果
plt.savefig(r'.\static\assets\img\wordcloud.jpg',dpi=500)#生成图片

