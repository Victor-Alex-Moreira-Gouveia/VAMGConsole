#!/bin/bash
sudo docker build -t vamg_console . 
sudo docker run -it --rm vamg_console

