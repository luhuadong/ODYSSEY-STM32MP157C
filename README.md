# ODYSSEY-STM32MP157C



## 烧录 SD 卡

Etcher 是一个快速将镜像文件刻录到 USB 设备或 SD 卡中的工具，操作简单，整个操作只需要点三下鼠标。



## 登录系统

npi 提供了两个登录用户：

| 序号 | 用户名 | 密码    | 备注                   |
| ---- | ------ | ------- | ---------------------- |
| 1    | debian | temppwd | 支持调试串口、ssh 登录 |
| 2    | root   | root    | 支持调试串口登录       |



## WiFi 设置

使用 `connmanctl` 网络管理工具完成 WiFi 配置，执行如下命令进入交互命令行，输入 quit 退出交互模式。

```shell
debian@npi:~$ sudo connmanctl
connmanctl> 
```

开启 WiFi 功能

```shell
connmanctl> enable wifi
```

扫描 WiFi 服务

```shell
connmanctl> scan wifi
```

列出可用的服务（附近的 WiFi 网络）

```shell
connmanctl> services
```

开启无线网络代理

```shell
connmanctl> agent on
```

连接指定 WiFi 网络，并输入密码

```shell
connmanctl> connect wifi_e8de27077de3_41483034303434393134_managed_psk
Agent RequestInput wifi_e8de27077de3_41483034303434393134_managed_psk
  Passphrase = [ Type=psk, Requirement=mandatory ]
Passphrase? *************
Connected wifi_e8de27077de3_41483034303434393134_managed_psk
```



## 系统更新

### 替换软件源

软件源列表记录在 /etc/apt/sources.list，保险起见，我们先备份一下。

```shell
cd /etc/apt
cp sources.list sources.list.backup
```

然后将 sources.list 修改为：

```shell
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free

deb [arch=armhf] https://seeed-studio.github.io/seeed-linux-deb/ buster main
#deb-src [arch=armhf] https://seeed-studio.github.io/seeed-linux-deb/ buster main

#Kernel source (repos.rcn-ee.com) : https://github.com/RobertCNelson/linux-stable-rcn-ee
#
#git clone https://github.com/RobertCNelson/linux-stable-rcn-ee
#cd ./linux-stable-rcn-ee
#git checkout `uname -r` -b tmp
#
deb [arch=armhf] http://repos.rcn-ee.com/debian/ buster main
#deb-src [arch=armhf] http://repos.rcn-ee.com/debian/ buster main
```

### 更新系统

```shell
sudo apt update
```



## 软件安装

### 安装 ssh

```shell
sudo apt install ssh -y
```



### 安装 python3

```shell
sudo apt install python3 python3-pip -y
```

安装 paho-mqtt

```shell
pip3 install paho-mqtt
```



### 常用软件

为方便后续调试，下载 git、wget、curl 等工具。

```shell
apt install git wget -y
```



## Cortex-M4 核

### 更新固件

```shell
chmod +777 /sys/class/remoteproc/remoteproc0/firmware
echo demo1_CM4.elf > /sys/class/remoteproc/remoteproc0/firmware
echo start > /sys/class/remoteproc/remoteproc0/state
```





## 参考资料

- [STM32MP1 Developer Package](https://wiki.st.com/stm32mpu/wiki/STM32MP1_Developer_Package)

