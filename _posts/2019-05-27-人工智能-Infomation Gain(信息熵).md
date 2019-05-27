---
layout: post
title: 人工智能-信息熵、平均分支因子
subtitle: Infomation Gain，Average Branching Factor
author: Kingtous
date: 2019-05-27 08:46:03
header-img: img/about-bg-walle.jpg
catalog: True
tags:
- 人工智能
---

## 信息熵(Infomation Gain)

计算公式：

$$Gain(S,A)=H(S)-\sum_{V∈Values(A)} \frac{S_V}{S}H(S_V)$$

H(S)此数使用交叉熵(Entropy)

$Entropy=-\sum_{i=1}^{K}p_klog_2{p_k}$

>$Gini=1-\sum_{i=1}^{K}{p_k}^2$
>
>$Classification~Error = 1-max_{i}p_k$

### 示例

> Wind(9+,5-)   ->   Weak(6+,2-)

> ​	|

> ​	V

> Strong(3+,3-)

Wind:$$H(S)=-\frac{9}{14}log_2^{\frac{9}{14}}-\frac{5}{14}log_2\frac{5}{14}$$

Weak,Strong同理可得

$$Gain(S,wind)=H(S)-\frac{8}{14}H(S_{weak})-\frac{6}{14}H(S_{weak})=0.049$$

PS:若要作为测试结点，Gain需要最大

## 平均分支因子(Average Branching Factor)

> 平均在每个格子能移动的步数的平均数

以八数码为例：

| 1    | 2    | 3    |
| ---- | ---- | ---- |
| 4    | 5    | 5    |
| 7    | 8    |      |

四角(1,3,7,空格)可向2个方向移动

四角中心(2,4,6,8)的4格可向3个方向移动

中心(5)的一格可向4个方向移动

故可计算：

$$\mbox{平均分支因子}=\frac{4·2+4·3+1·4}{4+4+1}=\frac{15}{9}$$



### 参考

- [Infomation Gain && Gini PPT](https://www3.nd.edu/~rjohns15/cse40647.sp14/www/content/lectures/23%20-%20Decision%20Trees%202.pdf)

- [Youtube: Decision Tree 4:Infomation Gain](https://www.youtube.com/watch?v=nodQ2s0CUbI)

- [algorithm analysis - How to find the Branch factor of 8 Puzzle - Computer Science Stack Exchange](https://cs.stackexchange.com/questions/39534/how-to-find-the-branch-factor-of-8-puzzle)

- [基尼指数](https://www.sohu.com/a/301007021_354986?sec=wd)