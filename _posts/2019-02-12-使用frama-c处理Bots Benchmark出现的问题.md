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





## alignment

修改的地方：

> seq = (char *) realloc(seq, ((*len) + MAXLINE + 2) * sizeof(char));

![image-20190217152150776](/Users/kingtous/Library/Application Support/typora-user-images/image-20190217152150776.png)

> get_seq函数（见 assert语句）

![image-20190217152324567](/Users/kingtous/Library/Application Support/typora-user-images/image-20190217152324567.png)

>





原本取值就应当是无穷的变量：

> names        = (char   **) malloc((nseqs + 1) * sizeof(char *));

nseqs取决于传入文件:

![image-20190217105810071](/Users/kingtous/Library/Application Support/typora-user-images/image-20190217105810071.png)

![image-20190217105859390](/Users/kingtous/Library/Application Support/typora-user-images/image-20190217105859390.png)



>strlcpy函数

s-src也是无法确定的

![image-20190217110112620](/Users/kingtous/Library/Application Support/typora-user-images/image-20190217110112620.png)























