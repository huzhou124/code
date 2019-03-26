# 目录结构说明
>当前目录：
   + server_info.py
   + my_scripts.md
## my_scripts.md
      这里面介绍了4个实用型的脚本，可以配合使用。
## server_info.py
       server_info.py 该脚本是用来看服务器的信息的，包括产品型号，cpu详细信息，内核信息，磁盘信息，  
       以及正在使用的网卡信息,当磁盘大于8T，会有如下警告提示:  
```WARNING: GPT (GUID Partition Table) detected on '/dev/sdb'! The util fdisk doesn't support GPT. Use GNU Parted.```
出现的原因是因为大于8T GPT磁盘管理方式就不支持了，应该要使用GUN
```
******* Information *********
Product Name: RH2288 V3
Product Name: BC11HGSB0
40  Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz
Logical CPU Number  : 40
Physical CPU Number : 2
CPU Core Number     : 10
HT Number           : 2
Kernel version:
4.11.6-1.el6.elrepo.x86_64
Disk:

WARNING: GPT (GUID Partition Table) detected on '/dev/sdb'! The util fdisk doesn't support GPT. Use GNU Parted.

130:Disk /dev/sda: 239.0 GB, 238999830528 bytes
142:Disk /dev/sdb: 16000.0 GB, 15999998885888 bytes
Totalmem            : 263745628 kB
Ethernet info:
Eth  :   eth0
Intel Corporation I350 Gigabit Network Connection (rev 01)
Speed: 1000Mb/s Duplex: Full
*****************************
```
