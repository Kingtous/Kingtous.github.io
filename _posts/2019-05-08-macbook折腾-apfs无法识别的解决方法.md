---
layout: post
title: macbook折腾-apfs无法识别的解决方法
subtitle: apfs type变为FFFF
author: Kingtous
date: 2019-05-08 22:49:19
header-img: img/about-bg-walle.jpg
catalog: True
tags:
- 搞机
---

> 环境：Macbook Air 2017 + macOS 10.14.4 + Ubuntu 18.04 LTS

用Disk Utility磁盘工具缩小apfs分区的时候，居然中途崩了！

重启后发现引导不见了！浑身难受，香菇哦。

冷静下来，缩小分区应该也能够修复吧…经过99八十一难，总结出了过程。



### 尝试fsck_apfs 

```
fsck_apfs /dev/disk0s2
```

失败告终.无法修复，而且无法检测到是APFS文件系统



### 使用diskutil list查看分区列表

```
➜  ~ diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *251.0 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:      FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF         220.7 GB   disk0s2
   3:       Microsoft Basic Data un                      9.9 GB     disk0s7
   4:           Linux Filesystem                         19.9 GB    disk0s4

/dev/disk2 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +220.7 GB   disk2
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            130.5 GB   disk2s1
   2:                APFS Volume Preboot                 45.3 MB    disk2s2
   3:                APFS Volume Recovery                522.7 MB   disk2s3
   4:                APFS Volume VM                      1.1 GB     disk2s4
```

这里面看出disk0s2本应该是APFS，这里变成了

```
  FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF
```

我们想，是不是可以想办法改变这个type呢？



### 使用gpt更新label

- 查看信息

```
➜  # gpt show disk0
  start        size  index  contents
           0           1         PMBR
           1           1         Pri GPT header
           2          32         Pri GPT table
          34           6        
          40      409600      1  GPT part - C12A7328-F81F-11D2-BA4B-00A0C93EC93B
      409640  1691407112      2  GPT part - FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF
  1691816752        1232        
  1691817984    68358144      3  GPT part - 0FC63DAF-8483-4772-8E79-3D69D8477DE4
  1760176128   192764416      4  GPT part - 53746F72-6167-11AA-AA11-00306543ECAC
  1952940544     1269536      5  GPT part - 426F6F74-0000-11AA-AA11-00306543ECAC
  1954210080           7        
  1954210087          32         Sec GPT table
  1954210119           1         Sec GPT header
```

我们得到这几个数：

`start:409640`  `size:1691407112` `index:2`



- 卸载磁盘

```
diskutil umountDisk [force] disk0
```

如果无法卸载，加上force即可

- 删除FFFF标签

```
gpt remove -i 2 disk0
```

2表示的是disk0的第二个磁盘，即disk0s2，我们需要修复的磁盘

- 添加FFFF标签

```
gpt add -i 2 -b 409640 -s 1691407112 -t 7C3457EF-0000-11AA-AA11-00306543ECAC  disk0
```

其中-b为start起点数值，-s为apfs的size，-t为GUID数值，填写为原来的GUID(我这个直接用了网上找的一个),disk0为磁盘号



重启系统，熟悉的引导就回来啦~

