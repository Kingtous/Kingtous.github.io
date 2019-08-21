---
layout: post
title: Macbook Air 2017 折腾manjaro记录
subtitle: Manjaro Linux
author: Kingtous
date: 2019-08-18 22:00:15
header-img: img/post-bg-unix-linux.jpg
catalog: True
tags:
- Linux
---

manjaro太香了，可能考虑弃用一段时间的Deepin.

坑：截止到2019.8.19，搜狗输入法仍然用的是qt4组件，而Manjaro 18.0.4中，fcitx无qt4版本，故改用谷歌拼音。

### 修改为国内镜像源

```shell
sudo pacman-mirrors -c China
```

### 添加archlinuxcn与kali软件源

在`/etc/pacman.conf`尾部加入

```shell
[archlinuxcn]
SigLevel = Optional TrustedOnly
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

[blackarch]
SigLevel = Optional TrustAll
Server = https://mirrors.tuna.tsinghua.edu.cn/blackarch/$repo/os/$arch

```

### 必备软件

- yay
- yaourt (访问AUR源)

### 省电

- TLP
- thermald
- macfanctld (通过AUR源安装)
- 在`/etc/default/grub`中加入`acpi_osi=!Darwin`屏蔽雷电接口（Linux兼容TP差）

- 关闭GPE4E中断

  通过加入服务的形式关闭。在`/etc/systemd/system`下创建一个`disable_gpe4e.service`，内容如下.

```shell
[Unit]
Description=Disable GPE4E interrupts

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo "disable" > /sys/firmware/acpi/interrupts/gpe4E'

[Install]
WantedBy=multi-user.target
```

- chromium浏览器使用vaapi硬件加速

  由于Linux下的浏览器默认未开启硬件加速，软解导致CPU占用高，安装`chromium-vaapi`即可

### 更换键盘设置

1. 通过aur安装 hid_apple

2. 关闭iso键盘配置(否则～键会变成书名号和大于小于号)

   ```shell
   sudo vim /etc/modprobe.d/hid_apple_pclayout.conf
   options hid_apple fnmode=2
   options hid_apple swap_fn_leftctrl=1
   options hid_apple swap_opt_cmd=1
   options hid_apple rightalt_as_rightctrl=1
   options hid_apple ejectcd_as_delete=1
   options hid_apple iso_layout=0 ##这行默认配置没有
   ```

3. 将配置conf加入内核

   ```shell
   sudo modprobe hid_apple
   sudo mkinitcpio -p linux(根据当前系统提供的内容改，可以按TAB键补全)
   ```

4. 重启即可

### chromium设置代理

通过shell进行设置(以socks5为例，开放端口1080)

```shell
chromium --proxy-server="socks5://127.0.0.1:1080"
```

### 自定义桌面图标模板

放置在 `/usr/share/applications/`下

```shell
[Desktop Entry]
Categories=Utility;
Comment=Create FrontMatter For Jekyll
Exec=/opt/NoteEasy/bin/NoteEasy
Icon=/opt/NoteEasy/bin/favicon.ico
Name=NoteEasy
StartupNotify=false
Type=Application
Version=1.0
```