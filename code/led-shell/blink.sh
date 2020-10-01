#!/bin/bash

while :
do
    gpioset gpiochip0 3=0
    sleep 1
    gpioset gpiochip0 3=1
    sleep 1
done