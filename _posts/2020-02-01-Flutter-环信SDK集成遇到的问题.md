---
layout: post
title: Flutter-环信SDK集成遇到的问题
subtitle: Flutter坑
author: Kingtous
date: 2020-02-01 20:42:47
header-img: img/post-bg-css.jpg
catalog: True
tags:
- Flutter
---

> 官方Flutter版SDK下载：[Github地址](https://github.com/easemob/im_flutter_sdk)
>
> 以下适用于dev分支commit号：[84a6498](https://github.com/easemob/im_flutter_sdk/commit/84a6498fde36cfccaf80440d3ca8cbbdc81092a6)

不得不说，环信SDK的Flutter版太寒酸了...没有开发文档和集成方法（截止到这篇Post上传）

以下是遇到的坑：

#### 迁移至AndroidX

都0202年了，官方使用的还是android.support库...

解决方法：clone下SDK，用`Android Studio`的`Migrate to AndroidX`功能

#### proguard混淆问题

官方竟然没有打入混淆...（无语）

那么我们自己打入吧 

参考官方安卓SDK集成方法页面最后：[安卓SDK集成方法](http://docs-im.easemob.com/im/android/sdk/import)

- 在项目`android/app/`目录下新建`proguard-rules.pro`，内容如下

```properties
-keep class com.hyphenate.** {*;}
-dontwarn  com.hyphenate.**
-keep class internal.org.apache.http.entity.** {*;}
-keep class com.superrtc.** {*;}
-dontwarn  com.superrtc.**
```

- 在`build.gradle`中引用

```groovy
buildTypes {
        release {
            signingConfig signingConfigs.release
            proguardFiles 'proguard-rules.pro'
        }
        debug {
            signingConfig signingConfigs.debug
        }
    }
```

