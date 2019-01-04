---
typora-root-url: ../../Kingtous.github.io-master
---

\---

layout:     post

title:      "2019-01-04 OMPi任务分配"

subtitle:   " \"任务分配\""

date:       2019-01-04 11:13:20

author:     "Kingtous"

header-img: "img/RTCO_Omp-DAG.jpg"

catalog: true

tags:

\- OMPi小组会议

\---



## 任务总流程

![img](/img/RTCO/2019-01-04_OMPi_1.png)







## dot图整合

- taskFunc1_recursive
  - 指向入口结点

- 普通函数
  - 我们将函数的图加入task图中

- task结点
  - 不用
- 递归函数
  - 将函数中调用的递归函数改名(加上_recursive)，并指向递归函数开始的部分

效果图：

![img](/img/RTCO/2019-01-04_OMPi_2.jpg)





