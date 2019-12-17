---
layout: post
title: Vivado&Verilog的基本知识、要点知识
subtitle: 硬件描述语言(HDL)
author: Kingtous
date: 2019-12-17 18:07:54
header-img: img/post-bg-halting.jpg
catalog: True
tags:
- Verilog
- Vivado
typora-root-url: ../../Kingtous.github.io-master
---

### Verilog基础语法部分

#### 模块(module)定义

```verilog
module fenpin(input clk_in,output clk_out);
	reg c_out=0;
  assign clk_out = c_out;
  always @ (posedge clk_in)
  	begin
      c_out = ~c_out;
    end
endmodule
```

#### 单元说明

- 时序逻辑部分在`always`块的内部，在`always`块中只能对寄存器变量赋值
- 对端口或其他wire型变量的赋值，必须在`always`块的外部使用`assign`语句

- 寄存器必须在时钟驱动下（有效边沿）才能改变其内容，编程决定

- `parameter`可以定义宏，可以在不同的module中调用
    - 用`#(xxx,xxx)`可以对宏重新定义

- 存储器是一个寄存器数组
    - `reg [2,0] memory1[3,0]`表示3位位宽（不注明就只为1位），有4个存储单元
    - `memory1[0:3]=0`，速度非常快的大量赋值

#### 运算

- 整数除法，结果略去小数部分，结果的符号位采用模运算符中第一个操作符的符号
    - `-10%3=-1`、`11%-3=2`

- 逻辑运算只区分真假，`4'h01`和`4'ha1`都表示真
    - 注意：`<=`在形如`b<=i_a;`中，表示的是`非阻塞`的赋值

![截屏2019-12-17下午4.13.35](/img/unsorted/截屏2019-12-17下午4.13.35.png)

- 算数运算符同`c++`
- 等式运算符
    - `===`全等
    - `!==`不全等
- 缩减运算符
    - `c=%b`即为`c=((b[0]&b[1])&b[2])&b[3]`

![截屏2019-12-17下午4.17.31](/img/unsorted/截屏2019-12-17下午4.17.31.png)

- 移位同数电

- 条件运算符(同`c++`)
    - `cond?true_cond:false_cond`

#### 结构说明语句

- `always`
    - 有点像GUI中的事件监听
        - `always @ (clk)`，只要`clk`发生变化就触发
        - `always @ (posedge clk)`，`clk`上升就触发
        - `always @ (negedge clk)`，`clk`下降就触发
        - `always @ (negedge clk1 or posedge clk2)`，`clk`上升或下降就触发
        - `always @ (*)`只要模块的任何输入信号变化了都触发
- `initial`
    - 有点像构造函数

#### 条件语句

- `if`

    - 同`C++`用法，但`Verilog`没有花括号括起多条语句而是用`begin`和`end`间隔开

- `case`(每一位都确定)、`casez`（忽略高阻态）、`casex`（忽略高阻态和不定态）

    - 有点像`switch`，但是在每一个`case`尾部不需要加`break`
    - `case`尾部加上`endcase`
    - `case`所有表达式的位宽必须相等

    ![image-20191217181603397](/img/unsorted/image-20191217181603397.png)

#### 循环语句

- `forever`，始终执行
- `repeat (num)`，执行`num`次的循环
- `while`，直到某条件不满足，以`end`结尾

**注意：循环次数必须是能够确定的，代码才有效，下面是一个反例**

![image-20191217182437001](/img/unsorted/image-20191217182437001.png)

- `for(ex1,ex2,ex3)`，与`c++`中的`for`类似

### Vivado初步部分

> 后续更新
>
> 2019.12.17