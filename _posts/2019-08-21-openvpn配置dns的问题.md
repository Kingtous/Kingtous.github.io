---
layout: post
title: openvpn配置dns的问题
subtitle: openvpn
author: Kingtous
date: 2019-08-21 09:36:41
header-img: img/post-bg-miui-ux.jpg
catalog: True
tags:
- Linux
- OpenVPN
---

自从Ubuntu 18.04 后，连接OpenVPN不会自动刷新dns配置了.

`/etc/resolve.conf`不做任何更改，导致无法上网



### Ubuntu解决方法

Ubuntu使用`system-networkd`和`systemd-resolved`进行网络配置。理论上适用于所有使用该方案的Linux发行版.

1. 安装`openvpn-update-systemd-resolved`

2. 在OpenVPN的配置文件(.ovpn)尾部加入

   ```shell
   script-security 2
   setenv PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
   up /etc/openvpn/scripts/update-systemd-resolved
   up-restart
   down /etc/openvpn/scripts/update-systemd-resolved
   down-pre
   ```

3. 重新连接即可



### Manjaro 解决方法

Manjaro使用`Network Manager`进行网络配置

1. AUR安装`openvpn-update-resolve-conf`

   ```shell
   yaourt openvpn-update-resolve-conf
   ```

2. 在OpenVPN的配置文件(.ovpn)尾部加入

```shell
script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf
```

3. 重新连接即可