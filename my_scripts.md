# 实用脚本
## 1.工具脚本打包
```
#!/usr/bin/env bash
Time=`date +"%Y-%m-%d"`
sed -i "/^update:/c update:${Time}" pta_tool/py_lib/tool_config.py
zip -r pta_tool.zip pta_tool
md5sum pta_tool/py_lib/pta_tool.py > Version.log
```

## 2.安装脚本
**可以作为参考，升级和安装工具脚本**
```
#！/usr/bin/env bash
alias cp='cp -i'
echo "解压pta_tool.zip"
wget http://192.168.18.177/tool/pta_tool.zip
unzip pta_tool.zip
if [ "$?" != "0" ];then
    echo "不存在unzip，yum install -y unzip"
    yum install -y unzip
    unzip pta_tool.zip
fi
cd pta_tool/
chmod 755 pta_tool.py
if [ -e /usr/bin/py_lib ];then
    mode="Update"
    echo "We will update"
    rm -rf /usr/bin/py_lib/*
    cp py_lib/* /usr/bin/py_lib/
else
    mode='Install'
    echo "We will install"
    cp pta_tool.py /usr/bin/
    mkdir /usr/bin/py_lib
    cp py_lib/* /usr/bin/py_lib/
fi
if [ "$?" == "0" ];then
    echo -e "\033[32m ${mode} success !!!\033[0m"
else
    echo -e "\033[31m ${mode} failing !!!\033[0m"
fi
cd ..
rm -rf pta_tool
rm -rf pta_tool.zip
rm -rf $0
```

## 3.工具脚本中相应的升级模块
```
def tool_update(self):
    CMD = "wget http://192.168.18.177/tool/pta_tool_install.sh;bash pta_tool_install.sh"
    os.system(CMD)
```

