#!/bin/bash

softpwm() {

    count=1000
    period=$1
    pulse=$2

    while [ $count -gt 0 ]
    do
        let "count--"
    done
}

softpwm2() {

    hightime= $2
    lowtime=`expr $1 - $2`

    gpioset gpiochip0 14=0
    usleep $lowtime

    gpioset gpiochip0 14=1
    usleep $hightime
}

while :
do
    count=0

    while [ $count -lt 1000 ]
    do
        softpwm2 1000 $count
        let ++count
    done
done