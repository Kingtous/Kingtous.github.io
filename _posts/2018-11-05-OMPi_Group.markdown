---
layout:     post
title:      "2018-11-05 OMPi小组会议"
subtitle:   " \"Hello World, Hello Blog\""
date:       2018-11-05 23:59:00
author:     "Kingtous"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
- OMPi小组会议
---

- 挑战杯立项

  - 课题名字

  - 背景
    - 明天和王成、张肸讨论
  - 内容
    - 明天和王成、张肸讨论
  - 研究思路和方法，特色/创新之处
    - 转成（照片）
  - 预期实验成果
    - 生成带有WCET, Flow Infomation的，具有并行语义的CFG
  - 实施计划与时间进度
    - 计划：
      - 
    - 进度：

- 操作流程
  - 将OpenMP C文件用OMPi处理成可用gcc等编译工具编译的C文件
  - 将经过OMPi处理过后的C文件通过ALFbackend工具转成alf文件
  - 从alf文件中获取BB
  - 将待测的BB放入新的alf中，并提交至sweet获得每个BB的时间
  - 将时间放置于dot图中







Example：以complex.alf为例

SWEET生成WCET命令（根据insertsort.clt）

> sweet -i=complex.alf,std_hll.alf -ae aac=insertsort.clt tc=st,op merge=all

SWEET生成dot命令：

> sweet -i=complex.alf --dot-print file=complex g=cfg

dot 转 pdf 命令

> sudo dot -Tpdf complex.dot -o complex.pdf





> > alf中发现的问题

- Return 含有多个basic block

> > SWEET发现的问题

- CFG图中无小节点。

> > dot图拼接注意事项

- 有传参的情况会多出一个节点，return节点也需要删除
  - 把Struct 中的内容提取出来，删除前面的赋值语句
- return 是不是openmp中的结点？也就是说，新建一个new task，在openmp中是不是相当于新建了一个函数，在运行完return一个值。
- 直接将entry和exit分别加入到父图中和连接至下一个节点
- return可能含有多个跳转
