---
layout:     post
title:      "Linux命令-echo"
subtitle:   " \"echo -e -n\" "
date:       2019-01-08 12:23:20
author:     "Kingtous"
header-img: "img/post-bg-unix-linux.jpg"
catalog: true
tags:
- Linux
- Shell
typora-root-url: ../../Kingtous.github.io-master

---

# Linux命令-echo

- -n 

  - 不换号输出(echo 默认为换行输出)

- -e 处理特殊字符

  - \a 发出警告声；

  - \b 删除前一个字符；

    - ```bash
      ➜  ~ echo -e "ae\bbc"
      abc
      ➜  ~ echo -e "a\bbc"
      bc
      ➜  ~ echo -e "a\b"
      a 
      ➜  ~ echo -e "a\bc"
      c
      #只有一个字符的话是不是不会删除？
      ```

  - \c 最后不加上换行符号；

  - \f 换行但光标仍旧停留在原来的位置；

  - \n 换行且光标移至行首；

  - \r 光标移至行首，但不换行；

  - \t 插入tab；

  - \v 与\f相同；

  - \\\\ 插入\字符；