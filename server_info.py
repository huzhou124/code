#!/usr/bin/env python
# coding=utf-8
import os
CMD = """
    logicalNumber=$(grep "processor" /proc/cpuinfo|sort -u|wc -l)
    physicalNumber=$(grep "physical id" /proc/cpuinfo|sort -u|wc -l)
    coreNumber=$(grep "cpu cores" /proc/cpuinfo|uniq|awk -F':' '{print $2}'|xargs)
    HTNumber=$((logicalNumber / (physicalNumber * coreNumber)))
    cpu_info=$(cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c)
    eth_n=$(ip a|grep "eth0||em1||eht1||enslo"|head -n 1|awk '{print $7}')
    echo "******* Information *********"
    echo "`dmidecode | grep "Product Name" `"|awk '{printf "%-s\\n",$0}'|cut -c 2-60
    echo "${cpu_info}"|cut -c 6-60
    echo "Logical CPU Number  : ${logicalNumber}"
    echo "Physical CPU Number : ${physicalNumber}"
    echo "CPU Core Number     : ${coreNumber}"
    echo "HT Number           : ${HTNumber}"
    echo "`fdisk -l |grep -sn "Disk /dev/sd"`"
    echo "Totalmem            : `cat /proc/meminfo|grep "MemTotal"|awk -F: '{print \$2}'|awk '{print $1,$2}'`"
    echo "Ethernet info:"
    echo "Eth  :   ${eth_n}"
    (lspci > /dev/null 2>&1)||(yum install -y pciutils-3.1.10-4.el6.x86_64 > /dev/null 2>&1)
    echo `lspci | grep Ethernet|awk -F: '{print $3}'|head -n 1`
    echo `ethtool ${eth_n}|sed -n '/Speed/p;/Dup/p'|awk '{printf "%s\\n%s\\n",$1,$2}'`
    echo "*****************************"
    """
#假如你的硬盘大于4T就会提示使用gun，而不是使用gtp的东西。
#第10行这里是取ip192.168开头的
#注意第22是会去判断是否有lspci这个命令，没有就去下载pciutils-3.1.10-4.el6.x86_64
        #os.system(CMD)
for i in os.popen(CMD).readlines():
    if i.startswith("WA"):
        pass
    else:
        print i.strip()
