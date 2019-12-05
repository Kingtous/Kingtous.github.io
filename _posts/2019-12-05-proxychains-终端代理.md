---
layout: post
title: proxychains-终端代理
subtitle: shell
author: Kingtous
date: 2019-12-05 21:01:50
header-img: img/post-bg-miui6.jpg
catalog: True
tags:
- Linux
typora-root-url: ../../Kingtous.github.io-master
---

**Q：**默认终端不走代理的，那碰到不好下载的东西需要命令行（比如app的依赖关系）怎么办？

**A：**使用**proxychains**！

#### 使用方法

`proxychains4+原命令`

- 配置代理

    >  格式：
    >
    > [ProxyList]
    >
    > `代理类型` `IP地址（一般是localhost或127.0.0.1）` `端口`

![image-20191205210409486](/img/unsorted/image-20191205210409486.png)

- 开始使用！效果如下

![image-20191205210323662](/img/unsorted/image-20191205210323662.png)



[参考链接](https://www.cnblogs.com/wAther/p/10472889.html)

