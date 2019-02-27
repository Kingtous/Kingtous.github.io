---
layout: post
title: Android Fragment使用记录
subtitle: 出现的问题/疑问以及解决方法
author: Kingtous
date: 2019-02-27 10:28:18
header-img: img/post-bg-os-metro.jpg
catalog: True
tags:
- Android
---

#### fragment获取systemservice

- getActivity()获取Activity对象后再操作

#### 获取fragment对象

- 可以实例化，(然后通过FrameLayout显示fragment)

#### java.lang.IllegalStateException: Can't change container ID of fragment

- fragment动态加载：

```java
private FragmentTransaction switchFragment(Fragment targetFragment) {
        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        if (!targetFragment.isAdded()) {
         //第一次使用switchFragment()时currentFragment为null，所以要判断一下        
            if (currentFragment != null) {
                transaction.hide(currentFragment);
            }
         transaction.add(R.id.fragmentShow,targetFragment,targetFragment.getClass().getName());
        } else {
            transaction.hide(currentFragment).show(targetFragment);
        }
        currentFragment = targetFragment;
        return transaction;
    }
```

