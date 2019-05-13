---
layout: post
title: SQL Server 2017导入northwnd数据库的问题
subtitle: 版本太老
author: Kingtous
date: 2019-05-13 21:44:43
header-img: img/home-bg-geek.jpg
catalog: True
tags:
- SQL Server
typora-root-url: ../../Kingtous.github.io-master
---

## SQL Server 导入northwnd数据库的问题

新版本的SQL Server已经无法通过mdf,ldf导入旧版本的northwnd数据库了，但是我们可以寻找其他的办法进行数据库的导入，例如通用的sql文件.



- 下载适配的sql文件

  [下载地址](http://www.downza.cn/soft/191939.html)



- 删去两行内容

  我们下载的文件有很多，但是需要的文件只有其中一个名为"instnwnd.sql"的sql文件，但是其并不能直接用，我们需要删除如下第24行和第25行的exec语句(用\-\-进行注释，如下)

```sql
/*
** Copyright Microsoft, Inc. 1994 - 2000
** All Rights Reserved.
*/

SET NOCOUNT ON
GO

USE master
GO
if exists (select * from sysdatabases where name='Northwind')
		drop database Northwind
go

DECLARE @device_directory NVARCHAR(520)
SELECT @device_directory = SUBSTRING(filename, 1, CHARINDEX(N'master.mdf', LOWER(filename)) - 1)
FROM master.dbo.sysaltfiles WHERE dbid = 1 AND fileid = 1

EXECUTE (N'CREATE DATABASE Northwind
  ON PRIMARY (NAME = N''Northwind'', FILENAME = N''' + @device_directory + N'northwnd.mdf'')
  LOG ON (NAME = N''Northwind_log'',  FILENAME = N''' + @device_directory + N'northwnd.ldf'')')
go

-- exec sp_dboption 'Northwind','trunc. log on chkpt.','true'
-- exec sp_dboption 'Northwind','select into/bulkcopy','true'
GO

set quoted_identifier on
GO

```



- 运行sql文件即可

  以navicat为例，右键点击服务器，选择“运行sql文件”，选择改好的instnwnd.sql文件，等待就好啦~

![](/img/unsorted/2019-05-13-sqlserver2.png)



- 效果图

  ![](/img/unsorted/2019-05-13-sqlserver.png)

