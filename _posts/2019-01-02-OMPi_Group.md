---
layout:     post
title:      "2019-01-02 OMPi小组会议"
subtitle:   " \"软件部署\""
date:       2019-01-02 19:07:00
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi小组会议
---

## 软件安装

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
    -  export PATH=/usr/local/ALFbuild:$PATH
    - export PATH=/usr/local/ALFbuild/bin:$PATH
- alf.zip
  - unzip alf.zip -d /usr/local/
  - sudo vim /etc/profile
    - alias ALFpy="python3 /usr/local/alf/main.py "
- Slicing_V1.5.zip
  - unzip Slicing_V1.5.zip -d /usr/local/
  - sudo vim /etc/profile
    - alias CLpy="python3 /usr/local/Slicing_V1.5/main.py "
- SWEET-8013.zip
  - unzip SWEET-8013.zip -d /usr/local/
  - sudo vim /etc/profile
    -  export PATH=/usr/local/SWEET-8013/trunk/build/cmakedir/src:$PATH



完成后 source /etc/profile
