---
layout: post
title: Android-Fragment切换
subtitle: replace，hide，show等对生命周期的影响
author: Kingtous
date: 2019-03-08 13:03:08
header-img: img/post-bg-android.jpg
catalog: True
tags:
- Android
---

## Fragment切换

- replace，加回退栈，Fragment不销毁，但是切换回销毁视图和重新创建视图。

- replace,不加回退栈，Fragment销毁掉。

- hide、show,Fragment不销毁，也不销毁视图。隐藏和显示不走生命周期。



### replace

```java
private FragmentTransaction switchFragment(Fragment targetFragment) {
        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        if (!targetFragment.isAdded()) {
            transaction.add(R.id.fragmentShow,targetFragment,targetFragment.getClass().getName());
        }
        transaction.replace(R.id.fragmentShow,targetFragment);
        currentFragment = targetFragment;
        return transaction;
    }
```



### hide,show

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
```



