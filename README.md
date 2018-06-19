---
title: 根据IP返回所在地理位置
tags: 
 - 17monipdb.dat
categories: python
---
> 代码见 https://github.com/igreedy/ip_finder
### 17monipdb介绍
>17monipdb是一款全球ipv4地址归属地数据库。专注于与地理位置定位相关的数据的整理与发行，致力于将地理位置数据变得更准确、更精确，该 IP 库主要基于 BGP/ASN 数据以及遍布全球的网络监测点进行城市级地域数据标注，准确度远高于国内国外同类产品
### 代码使用
>ip_test.py就是用了17monipdb.dat，来做到离线不联网，可以查询多个ip的所在地理位置。下面展示的是它的main函数，测试了三个ip地址。
```python
if __name__ == '__main__':
    ipfinder = IPIP()
    ip_lists = ['125.224.237.90', '202.106.58.118', '219.137.150.255']
    for ip in ip_lists:
        name = ipfinder.find(ip)
        print ip, name
```

>执行代码 python ip_test.py，结果如下：
```
125.224.237.90 中国	台湾	台中市 
202.106.58.118 中国	北京	北京 
219.137.150.255 中国	广东	广州 
```
