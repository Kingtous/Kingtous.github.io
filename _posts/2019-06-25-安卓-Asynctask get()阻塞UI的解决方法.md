---
layout: post
title: 安卓-Asynctask get()阻塞UI的解决方法
subtitle: asynctask.get()
author: Kingtous
date: 2019-06-25 23:45:46
header-img: img/post-bg-android.jpg
catalog: True
tags:
- 安卓
---

## 安卓-Asynctask get()阻塞UI的解决方法

在项目中使用了Asynctask，发现该出来的动画效果没有出来。

后来在Google上一查，发现**Asynctask虽然是异步封装类，用其get()方法获取返回值却是个阻塞UI的操作**。

> 知道问题了，该怎么解决呢？



### 参考RecyclerView的点击事件的回调方法！通过接口回调返回值！

- 定义接口

  在自定义的Asynctask类中定义接口与设置监听的方法，如下我定义了一个点击事件

```java
public interface OnItemClickListener {
        void OnClick(View view, int Position);
    }
    public interface OnItemLongClickListener {
        void OnLongClick(View view, int Position);
    }

    private FileTransferFolderAdapter.OnItemClickListener mOnItemClickListener;
    private FileTransferFolderAdapter.OnItemLongClickListener mOnItemLongClickListener;

    public void setOnItemClickListener(FileTransferFolderAdapter.OnItemClickListener mOnItemClickListener) {
        this.mOnItemClickListener = mOnItemClickListener;
    }
    public void setOnItemLongClickListener(FileTransferFolderAdapter.OnItemLongClickListener mOnItemLongClickListener){
            this.mOnItemLongClickListener=mOnItemLongClickListener;
        }
```

- 更改UI线程的调用方法

  以本人的RemoteFingerUnlock为例，在Activity或fragment中implements此回调接口

```java
@Override
    public void OnClick(View view, int Position) {
        Log.d("点击","短");
        // 在此处放应该执行的操作
    }
```

- 改完后运行，惊喜的发现动画出来啦~