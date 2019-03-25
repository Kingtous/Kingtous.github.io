---
layout:     post
title:      "ompTG生成PCFG使用方法"
subtitle:   "生成PCFG"
date:       2019-03-25 17:23:20
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi知识
typora-root-url: ../../Kingtous.github.io-master
---

## ompTG生成PCFG使用方法

> Python执行文件存放于"./ompTG/src/Preprocessing"
>
> > 生成方法：执行 python3 graph.py 即可

**原理&处理流程**

*使用python的networkx以及Graphviz绘图库进行开发*

1、处理bb的函数调用relation表

2、提取出subgraph数据，并声明为全局值

3、开始处理dot图

- 计算特征

  - 点、边、wait结点数量、WCET平均值、方差、分支数...

- 处理task关系

  - taskwait(需要针对单个benchmark手动加在graph.py的NodeWait函数中，需要添加的语句在PCFG文件夹中(nodewait.py))

![](/img/RTCO/pcfg.png)

- taskdepend(还没做，benchmark没有depend，故先暂时不考虑)

4、将图加框(Cluster定义)

5、输出最终的dot文件以及图(pdf)



**PS：针对每一个Benchmark，执行前需要针对不同的路径、不同的文件更改参数**

```python
#设置工作目录，设置为Benchmark中的PCFG目录(目录后的"/"不可省略)
root='/Users/kingtous/github/Bots_OpenMP_Tasks/floorplan/PCFG/'
#=======DOT存放位置===============
dotPath=root+'floorplan_sweet.dot'
#=======relation.txt存放位置======
relationPath=root+'relation.txt'
#=======WCET目录====================
wctPath=root+'floorplan.wct'
```





## 续

生成EFG只需要在上面的代码基础上加功能，具体如图

![](/img/RTCO/addCondition.png)

