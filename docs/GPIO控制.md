# GPIO 控制



### 使用 Grove 方式控制 GPIO

1、在编译之前，需要下载对应版本的内核头文件。

```shell
sudo apt update
sudo apt install linux-headers-$(uname -r) -y
```

注意：这一步可能需要开启代理才能完成！

2、下载 seeed-linux-dtverlays 仓库，编译并安装 stm32p1 驱动。

```shell
git clone https://github.com/Seeed-Studio/seeed-linux-dtverlays
```

编译、安装

```shell
cd seeed-linux-dtverlays
make all_stm32mp1 CUSTOM_MOD_FILTER_OUT="jtsn-wm8960" && sudo make install_stm32mp1 CUSTOM_MOD_FILTER_OUT="jtsn-wm8960"
```

3、修改 /boot/uEnv.txt 文件，在该文件末尾添加下面几行。

```shell
uboot_overlay_addr1=/lib/firmware/stm32mp1-seeed-spi5-overlay.dtbo
uboot_overlay_addr2=/lib/firmware/stm32mp1-seeed-usart2-overlay.dtbo
uboot_overlay_addr3=/lib/firmware/stm32mp1-seeed-i2c4-overlay.dtbo
```

重启系统

```shell
sudo reboot
```

4、安装 Python3 环境

```shell
sudo apt install python3 python3-pip -y
```

5、安装 Grove.py

```shell
sudo pip3 install Seeed-grove.py
```

下载 grove.py 库源代码

```shell
git clone https://github.com/Seeed-Studio/grove.py
```

运行示例

```shell
cd grove.py/grove
sudo python3 grove_gpio.py 5
```





### 使用 sysfs 方式控制 GPIO

```shell
sudo gpioinfo
```





### 其他方案

- WiringPi
- Libgpiod
- Adafruit-PureIO



### Libgpiod

固件已经安装了 libgpiod 库，所以可以看到系统中有一些 gpio 命令

- gpiodetect
- gpiofind
- gpioget
- gpioinfo
- gpiomon
- gpioset



```shell
# gpioinfo 
gpiochip0 - 16 lines:
        line   0:      unnamed       unused   input  active-high 
        line   1:      unnamed       unused   input  active-high 
        line   2:      unnamed       unused   input  active-high 
        line   3:      unnamed       unused   input  active-high 
        line   4:      unnamed       unused   input  active-high 
        line   5:      unnamed       unused   input  active-high 
        line   6:      unnamed       unused   input  active-high 
        line   7:      unnamed       unused   input  active-high 
        line   8:      unnamed       unused   input  active-high 
        line   9:      unnamed       unused   input  active-high 
        line  10:      unnamed       unused   input  active-high 
        line  11:      unnamed       unused   input  active-high 
        line  12:      unnamed       unused   input  active-high 
        line  13:      unnamed       unused   input  active-high 
        line  14:      unnamed       unused   input  active-high 
        line  15:      unnamed       unused   input  active-high
```

设置 GPIO_A3 管脚电平

```shell
gpioset gpiochip0 3=1
gpioset gpiochip0 3=0
```

