---
layout: post
title: 人工智能-Backtracking和DFS和相容性(node,arc,path)
subtitle: 复习记录
author: Kingtous
date: 2019-05-25 15:08:15
header-img: img/about-bg-walle.jpg
catalog: True
tags:
- 人工智能
---

## Backtracking和DFS的区别

Wikipedia对DFS的解释：

> One starts at the root (selecting some node as the root in the graph case) and explores as far as possible along each branch **before backtracking.**

即：

- Backtracking是一种更普遍的目的算法
- DFS使用了Backtracking方法去操作一棵树，换种说法来说，DFS是一种运用Backtracking方法的算法，其限制了只能在树状结构中使用



此外还有BFS的解释：

> "an algorithm that choose a starting node, checks all nodes **backtracks**, chooses the shortest path, chose neighbour nodes **backtracks**, chose the shortest path, finally finds the optimal path because of traversing each path due to continuous backtracking.





## AC-3算法(弧相容，3阶)

在解决CSP问题时，AC-3被用于预处理。

伪代码：

```matlab
function solveCSP(csp)
    ac3(csp)
    return backtracking(csp)
```

AC-3用于检测冲突，然后删除有冲突的值(有点像剪枝)，加快backtracking的速度。

### 边的概念

当A与B含有约束条件时，我们认为A与B中有一条边。在边中，我们认为：

- A->B是consistent的
  - 对于每一个A的取值，B都有一个取值与A对应

- B->A是consistent的
  - 对于每一个B的取值，A都有一个取值与B对应



### Example

- 变量：A,B,C
- 约束：A>B,B>C
- 值域：A,B,C均为\[0,9\]

在AC3算法中，我们得到边有

`$\{A\rightarrow B,B \rightarrow A,B \rightarrow C, C \rightarrow B\}$`

步骤如下：

- 1.选取一个约束(例如`$\{A\rightarrow B\}$`)
- 2.查看A取值域中的任意值，B是否有对应的值
- 3.是则值域不变,回到第1步，否则执行第四步
- 4.删除A中有冲突的值，再检查A的相邻结点是否与A满足弧约束，此处即$\{B\rightarrow A\}$
- 5.一直循环，直到约束被选取完

算法伪代码：

```matlab
function AC3(csp) returns csp possibly with the domains reduced
    queue, a queue with all the arcs of the CSP
    while queue not empty
         (X,Y) <- getFirst(queue)
         if RemoveConsistentValues(X,Y, csp) then
              foreach Z in neighbor(X) - {Y}
                   add to queue (Z,X)
    return csp

function RemoveConsistentValues(X, Y, csp) returns true if a value was removed
    valueRemoved <- false
    foreach x in domain(X, csp)
        if there's no value of domain(Y, csp) that satisfies the restriction between X and Y then
            remove x from domain(X, csp)
            valueRemoved <- true
    return valueRemoved
```





## 相容大家庭

- 结点相容

>如果单个变量（对应CSP网络中的结点）值域中的所有取值满足它的一元约束，就称此变量是**结点相容**。 
>例如，地图着色问题中南澳人不喜欢绿色，原先SA变量的值域为{red, green, blue}，删除green此结点即为**结点相容**。

- 弧相容

> 如果CSP中某变量值域中的所有取值满足该变量的所有**二元约束**，就称此变量是**弧相容**

最流行的弧相容算法就是上述的AC-3

- 路径相容

> 两个变量的集合`$\{X_i,X_j\}$`对于第三个变量`$X_m$`是相容的，也就是说，对`$\{X_i,X_j\}$`的每一个相容赋值，`$X_m$`都有合适的取值同时使得`$\{X_i,X_m\}$`和`$\{X_m,X_j\}$`是相容的。

- K相容

> 对于任何k-1个变量赋值，k个变量总有赋予一个和前k-1个变量相容的值，那么这个CSP是相容的