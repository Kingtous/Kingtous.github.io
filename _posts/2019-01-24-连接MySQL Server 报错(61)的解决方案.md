---
layout: post
title: 连接MySQL Server 报错(61)的解决方案
subtitle: 服务器配置
author: Kingtous
date: 2019-01-24 10:46:36
header-img: img/post-bg-css.jpg
catalog: true
tags:
- MySQL
---



#连接MySQL Server 报错(61)的解决方案

- MySQL配置

## 排查MySQL IP、端口配置

对象：一般出现在服务器等需要外网访问上。

问题：

- 监听IP只有本地IP

- ```bash
  #通过netstat查看监听情况
  netstat -tlupen | grep [port]
  ```

  - netstat 命令参考

  - ```bash
    usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
           netstat [-vWnNcaeol] [<Socket> ...]
           netstat { [-vWeenNac] -i | [-cnNe] -M | -s [-6tuw] }
    
            -r, --route              display routing table
            -i, --interfaces         display interface table
            -g, --groups             display multicast group memberships
            -s, --statistics         display networking statistics (like SNMP)
            -M, --masquerade         display masqueraded connections
    
            -v, --verbose            be verbose
            -W, --wide               don't truncate IP addresses
            -n, --numeric            don't resolve names
            --numeric-hosts          don't resolve host names
            --numeric-ports          don't resolve port names
            --numeric-users          don't resolve user names
            -N, --symbolic           resolve hardware names
            -e, --extend             display other/more information
            -p, --programs           display PID/Program name for sockets
            -o, --timers             display timers
            -c, --continuous         continuous listing
    
            -l, --listening          display listening server sockets
            -a, --all                display all sockets (default: connected)
            -F, --fib                display Forwarding Information Base (default)
            -C, --cache              display routing cache instead of FIB
            -Z, --context            display SELinux security context for sockets
    
      <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
               {-x|--unix} --ax25 --ipx --netrom
      <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
      List of possible address families (which support routing):
        inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25)
        netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP)
        x25 (CCITT X.25)
    ```

  - 

解决方案：

- 修改MySQL配置文件

  - MySQL 5.7在Ubuntu下的配置文件存放在```/etc/mysql/mysql.conf.d/mysql.conf```中，网上很多教程上写的是```/etc/mysql/my.cnf```.

  - 修改其中的bind-address为0.0.0.0, 即为

## 排查MySQL 用户配置

- 用户未设置外网访问，即host为localhost

  - 解决方案：使用通配符

    - ```bash
      #查询用户的host,以cloud为例
      mysql> select host,user from user;
      +-----------+------------------+
      | host      | user             |
      +-----------+------------------+
      | %         | root             |
      | localhost | cloud            |
      | localhost | debian-sys-maint |
      | localhost | mysql.session    |
      | localhost | mysql.sys        |
      | localhost | phpmyadmin       |
      +-----------+------------------+
      ```

    - 如果user需要通过外网访问，host需为%

    - 更新user配置

      - ```bash
        >> update user set host='%' where user='cloud';
        >> flush privileges #刷新系统权限表
        ##效果
        mysql> update user set host='%' where user='cloud';
        Query OK, 0 rows affected (0.00 sec)
        Rows matched: 1  Changed: 0  Warnings: 0
        ```