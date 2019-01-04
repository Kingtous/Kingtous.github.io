---
layout:     post
title:      "2019-01-02 OMPi小组会议"
subtitle:   " \"软件部署 & 汇总遇到的问题\""
date:       2019-01-02 19:07:00
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi小组会议
typora-root-url: ../../Kingtous.github.io-master
---

## 软件安装

> >

- python3
  - sudo apt install python3
- ompi-2.0.0_edited.zip
  - 解压
  - ./configure
  - make
  - sudo make install
- ALFbackend安装
  - tar -zxvf ALFbuil.tar.gz 
  - sudo vim /etc/profile
    - export PATH=/usr/local/ALFbuild:$PATH
    - export PATH=/usr/local/ALFbuild/bin:$PATH
- alf.zip
  - unzip alf.zip -d /usr/local/alf/
  - sudo vim /etc/profile
    - alias ALFpy="python3 /usr/local/alf/main.py "
- Slicing_V1.5.zip
  - unzip Slicing_V1.5.zip -d /usr/local/CleanPy
  - sudo vim /etc/profile
    - alias CLpy="python3 /usr/local/CleanPy/main.py "
- SWEET-8013.zip

  - sudo apt install doxygen build-essential cmake
  - unzip SWEET-8013.zip -d /usr/local/sweet
  - cd /usr/local/sweet/trunk/build/cmakedir
  - rm -rf *
  - cmake ../.. -G "Unix Makefiles"
  - make
  - sudo vim /etc/profile
    -  export PATH=/usr/local/sweet/trunk/build/cmakedir/src:$PATH

> >

完成后 source /etc/profile



##待解决的问题 

- 动态内存分配 dyn_alloc 
- 转alf没问题，但是sweet分析报错，错误是括号匹配
- 递归
- 调用递归函数转为调用一个不执行任何语句的函数
