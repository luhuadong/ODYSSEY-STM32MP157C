#!/bin/bash

while True:
	gpioset gpiochip0 14=0
	sleep 1
	gpioset gpiochip0 14=1
	sleep 1