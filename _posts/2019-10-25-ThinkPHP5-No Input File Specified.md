---
layout: post
title: ThinkPHP5-No Input File Specified
subtitle: 伪静态
author: Kingtous
date: 2019-10-25 19:43:11
header-img: img/neuq-sky.png
catalog: True
tags:
- PHP
typora-root-url: ../../Kingtous.github.io-master
---

打开网页，发现只有如题几个英文单词。百度的方案，要不是网页服务器不是`nginx`，要不是压根没有用...反正最后通过`composer`解决了，但还是把问题解决过程描述一下.

> 问题环境：
>
> nginx 1.17 + php 7.1 + mysql 5.7 + thinkphp 5.0.24

#### No Input File Specified

产生问题的原因有下列几个

- 网站目录没有读写权限

    - `chmod -R 777 /your/path/to/website `

- 设置好伪静态

    - nginx上的thinkphp伪静态设置

        ```shell
        location / {
        	if (!-e $request_filename){
        		rewrite ^/(.*)$ /index.php?s=$1 last;   break;
        	}
        }
        ```

        代码中 `!-e`表示访问的地址没有写`index.php`，则重定向到`index.php`下，`last`为nginx的重写函数(应该是吧).

    - apache的话是改`.htaccess`，具体没测试过

        **1.**办法1

        ```shell
        #.htaccess文件中的
        #RewriteRule ^(.*)$ index.php/$1 [QSA,PT,L]
        #在默认情况下会导致No input file specified.
        #修改成
        #RewriteRule ^(.*)$ index.php [L,E=PATH_INFO:$1]
        <IfModule mod_rewrite.c>
          Options +FollowSymlinks -Multiviews
          RewriteEngine On
        
          RewriteCond %{REQUEST_FILENAME} !-d
          RewriteCond %{REQUEST_FILENAME} !-f
          #RewriteRule ^(.*)$ index.php/$1 [QSA,PT,L]
          RewriteRule ^(.*)$ index.php [L,E=PATH_INFO:$1]
        </IfModule>
        ```

        **2.**办法2

        ```shell
        RewriteEngine On
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteCond %{REQUEST_FILENAME} !-d
        RewriteCond $1 !^(index\.php|robots\.txt)
        RewriteRule ^(.*)$ index.php?/$1
        
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteRule ^(application|modules|plugins|system|themes) index.php?/$1 [L]
        ```

- 查看`index.php`引用的`start.php`的相对路径是否写对

    - 默认是在`public`里面，应该为

        ```php
        <?php
        // +----------------------------------------------------------------------
        // | ThinkPHP [ WE CAN DO IT JUST THINK ]
        // +----------------------------------------------------------------------
        // | Copyright (c) 2006-2016 http://thinkphp.cn All rights reserved.
        // +----------------------------------------------------------------------
        // | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
        // +----------------------------------------------------------------------
        // | Author: liu21st <liu21st@gmail.com>
        // +----------------------------------------------------------------------
        
        // [ 应用入口文件 ]
        
        // 定义应用目录
        define('APP_PATH', __DIR__ . '/../application/');
        // 加载框架引导文件
        require __DIR__ . '/../thinkphp/start.php';
        ```

- 如果上述都没解决，在根目录执行一次`composer update`,再重试一下。(笔者就是这样解决的)
    - 如果`update`速度太慢，可以更换源：[中国全量镜像](https://pkg.phpcomposer.com)

![image-20191025194538165](/img/unsorted/image-20191025194538165.png)



**最后的结果！：**

![image-20191025200139110](/img/unsorted/image-20191025200139110.png)

证明已经解决！

![CB5779FA59310FD3C0539DB0EA7CEB3D](/img/unsorted/CB5779FA59310FD3C0539DB0EA7CEB3D.jpg)

**心得：出错不要惊慌，大家要多看错误日志！！！错误日志很重要！！！这样才能知道自己具体错哪，不要一报错就百度！浪费时间**