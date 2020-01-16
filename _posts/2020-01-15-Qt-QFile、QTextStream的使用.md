---
layout: post
title: Qt-QFile、QTextStream的使用
subtitle: Qt C++
author: Kingtous
date: 2020-01-15 20:03:43
header-img: img/post-bg-miui6.jpg
catalog: Qt
tags:
- Qt
- C++
---

> 环境：Qt 5.14.0 + macOS Catalina 10.15.2

#### 读取文件

```c++
QFile* configFile = new QFile();
configFile->setFileName(str+"/.blogPosition.cfg");
// 读取配置
bool openFlag = configFile->open(QIODevice::ReadOnly | QIODevice::Text);
if (!openFlag){
  return;
} else {
  QTextStream textStream(configFile);
  QString leastFolder = textStream.readLine();
  ui->BlogPositionEdit->setText(leastFolder);
}
configFile->close();
```

#### 写入文件

```c++
QString str=QDir::homePath();
QFile* configFile = new QFile();
configFile->setFileName(str+"/.blogPosition.cfg");
// 写入配置
bool openFlag = configFile->open(QIODevice::WriteOnly | QIODevice::Text | QIODevice::Truncate);
if (!openFlag){
  return -1;
} else {
  QTextStream textStream(configFile);
  textStream << pos;
}
configFile->close();
```

其中，`QIODevice::Truncate`为删除原内容写入，改为`QIODevice::append`即为追加写入