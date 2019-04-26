---
layout: post
title: Linux下SQL Server导入mdf,ldf文件
subtitle: SQL Server
author: Kingtous
date: 2019-04-26 14:31:53
header-img: img/about-bg.jpg
catalog: True
tags:
- SQL Server
- Linux
---



## SQL Server导入数据库文件命令

### step.1 将文件传入服务器

- 通过ftp
- 等等

### step.2 执行命令

```sql
EXEC sp_attach_db @dbname= 'northwnd',
         @filename1 = '/home/ftp/northwnd.mdf',
         @filename2 = '/home/ftp/northwnd.ldf'
```





