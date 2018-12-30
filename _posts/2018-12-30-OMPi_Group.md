---
layout:     post
title:      "2018-12-30 OMPi小组会议"
subtitle:   " \"跟进任务\""
date:       2018-11-05 23:59:00
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi小组会议
---

##### Abstract部分

针对 traditional timing analysis isapplied only in the late stages of embedded system software development, when the hardware is available and the code the code is compiled and liked. 

论文关注 preliminary timing estimates

> 原文：preliminary timing estimates are often needed already in early stages of system development, both for hard and soft real-time system.

论文提出的方法主要解决两种情况：the hardware is not yet fully accessible, or the code is not yet ready to compile or link

方法需要的基本条件：given combinations of hardware architecture and compiler

> 硬件体系结构和编译器的结合

简单描述：The models are identified from measure execution times for a set of synthetic "training programs" for the hardware platform in question.

偏差估计：最大20%

> 原文：Our experiments indicate that the models can predict the execution times of final, compiled code with a deviation up to 20%.

##### Introduction部分

一些背景介绍（略）

论文提供了建立时序模型的一种方法

> 原文：present a method to identify a source level timing model for a given combination of hardware configuation and compiler.

这个模型可以用来做静态的source-level的WCET分析

> 原文:The timing model can be used for static source-level WCET analysis as well as estimating performance dynamically with source-level simulators.

##### Related Work部分

###### approach for early stage WCET analysis

TimingExplorer(a version of the static WCET analysis tool aiT)

> 特点：The analysis uses the binary, and can thus only be applied if the code is ready to compile.
>
> The tool relies on hand-crafted hard-ware timing models.

integration of timing analysis and modeling/code generation tools(aiT,SCADE,ASCET)

> 特点：the binary is needed, the models must be in the state that code can be generated from them.

###### Identification of linear timing models

#### Identification of Linear Timing Models


简明要点：

这种处理是初步的时间估计

这种处理针对 the hardware is not yet fully accessible, or the code is not yet ready to compile or link

This paper describes how source-level timing models can be derived automatically for given combinations of hardware architecture and compiler.





compile函数的作用是对指令的模板进行转换。

link的作用是在模型和视图之间建立联系，包括在元素上注册事件监听。

ＬＩＮＫ-->链接器进行链接的时候，首先决定各个目标文件在最终可执行文件里的位置。然后访问所有目标文件的地址重定向表，对其中记录的地址进行重定向（即加上该编译单元实际在可执行文件里的起始地址）。然后遍历所有目标文件的未解决符号表，并且在所有的导出符号表里查找匹配的符号，并在未解决符号表中所记录的位置上填写实际的地址（也要加上拥有该符号定义的编译单元实际在可执行文件里的起始地址）。最后把所有的目标文件的内容写在各自的位置上，再作一些别的工作，一个可执行文件就出炉了。



模拟退火算法(Simulated Annealing，SA)最早的思想是由N. Metropolis [1]  等人于1953年提出。1983 年,S. Kirkpatrick 等成功地将退火思想引入到组合优化领域。它是基于Monte-Carlo迭代求解策略的一种随机寻优算法，其出发点是基于物理中固体物质的退火过程与一般组合优化问题之间的相似性。模拟退火算法从某一较高初温出发，伴随温度参数的不断下降,结合[概率](https://baike.baidu.com/item/%E6%A6%82%E7%8E%87)突跳特性在[解空间](https://baike.baidu.com/item/%E8%A7%A3%E7%A9%BA%E9%97%B4)中随机寻找[目标函数](https://baike.baidu.com/item/%E7%9B%AE%E6%A0%87%E5%87%BD%E6%95%B0)的全局最优解，即在局部最优解能概率性地跳出并最终趋于全局最优。模拟退火算法是一种通用的优化算法，理论上算法具有概率的全局优化性能,目前已在工程中得到了广泛应用，诸如VLSI、生产调度、控制工程、机器学习、神经网络、信号处理等领域。

模拟退火算法是通过赋予搜索过程一种时变且最终趋于零的概率突跳性，从而可有效避免陷入局部极小并最终趋于全局最优的串行结构的优化算法。
