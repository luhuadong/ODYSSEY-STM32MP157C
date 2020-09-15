# ODYSSEY-STM32MP157C



## 烧录 SD 卡

Etcher 是一个快速将镜像文件刻录到 USB 设备或 SD 卡中的工具，操作简单，整个操作只需要点三下鼠标



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





## 软件安装

### 安装 ssh

```shell
sudo apt update
sudo apt install ssh -y
```



### 安装 python3

```shell
sudo apt install python3 python3-pip -y
```



```shell
pip3 install paho-mqtt
```



## Cortex-M4 核

更新固件

```shell
chmod +777 /sys/class/remoteproc/remoteproc0/firmware
echo demo1_CM4.elf > /sys/class/remoteproc/remoteproc0/firmware
echo start > /sys/class/remoteproc/remoteproc0/state
```





## 参考资料

- [STM32MP1 Developer Package](https://wiki.st.com/stm32mpu/wiki/STM32MP1_Developer_Package)

