---
layout:     post
title:      "2018-12-30 OMPi小组会议"
subtitle:   " \"跟进任务\""
date:       2018-12-30 18:10:00
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi小组会议
---
会议要点：讨论分析benchmark哪些目前可以分析，哪些目前不可以分析

目的：找出之后讨论一下可行的解决方案

会议记录：

张利威学长：

fprintf

align_init：初始化指针数组

align_seq_init

Pair align_seq

def_aa_xref: 功能未明确

diff函数谁调用谁，parallel函数调用diff 由于diff函数本身递归 所以parallel函数不可分析



三大问题不可分析 ： 递归，动态内存分配，lib库函数



老师指出需要跟进的：

> 1. 找出benchmark 调用 之前的操作（比如变量的初始化，**全域的设置（@我的表达不准确 ）**、函数之间谁调用谁等等）—张利威、王佐学长
> 2. 碰到动态内存分配等不能分析的，应该在benchmark里做一下标注，方便后续需要时一层层查找
> 3. 问题1没解决之前，目前得到的结论都有猜的成分，后续要核实

老师提问：

1.对于没有task的函数，能分析吗？需不需要变量的值？

> 会上未解决，老师指的的函数里面有lib函数，lib函数目前不能分析

2.alf文件生成工具能处理递归吗？

> 未解决，我不太清楚

老师总结

三大问题不可分析 ： 递归，动态内存分配，lib库函数

parallel for 问题 目前也没法分析

> 目前可以先注释掉

对于lib和动态内存分配

> alf阶段注释掉这部分

递归问题

> 去掉递归的语义，只留下原始的一层
>
> 重写diff

拓扑步骤：

1. implicit task region 搞清楚
2. explicit task region 
3. 两个都转成alf
4. 查tab得到wcet
5. alf转入sweet得到cfg
6. 步骤4、5结合得到带有wcet的cfg

----

王成部分：

论文Automatic Generation of Timing Models for Timing Analysis of High-Level Code的问题：

![image-20181230104351385](/Users/cpyh/Library/Application Support/typora-user-images/image-20181230104351385.png)

确认一下SimpleScalar这些配置，然后确认sweet对wcet的分析是安全的
