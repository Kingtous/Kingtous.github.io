---
layout: post
title: 使用frama-c处理Bots Benchmark出现的问题
subtitle: 挑战杯
author: Kingtous
date: 2019-02-12 11:42:11
header-img: img/post-bg-unix-linux.jpg
catalog: True
tags:
- OMPi小组会议
---

## 问题汇总

- alignment警告报错基本都涉及到对char型字符串操作的语句
- concom警告报错涉及到结构体操作语句
- fft报错c_re，fft.h里的宏定义
  - \#define c_re(c)  ((c).re)
- floorplan 警告报错涉及结构体操作语句
- Health警告报错涉及math类型库函数pow以及结构体操作.
- knapsack警告报错涉及结构体操作语句
- sort警告报错涉及typedef类型重命名操作语句
  - typedef long ELM;
- Sparselu 警告报错涉及float操作语句

