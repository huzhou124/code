当前目录：
   server_info.py
       该脚本是用来看服务器的信息的，包括产品型号，cpu详细信息，内核信息，磁盘信息，以及正在使用的网卡信息。


表现如下（这个警告的意思是该磁盘大于4T应该使用GNU管理而不是使用GPT管理）：
WARNING: GPT (GUID Partition Table) detected on '/dev/sdb'! The util fdisk doesn't support GPT. Use GNU Parted.

sh: line 21: lspci: command not found
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
130:Disk /dev/sda: 239.0 GB, 238999830528 bytes
142:Disk /dev/sdb: 16000.0 GB, 15999998885888 bytes
Totalmem            : 263745628 kB
Ethernet info:
Eth  :   eth0

Speed: 1000Mb/s Duplex: Full
*****************************
