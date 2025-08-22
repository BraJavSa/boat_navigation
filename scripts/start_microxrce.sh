#!/bin/bash
# Lanzador de Micro XRCE-DDS Agent desde boat_navigation

# Si necesitás entorno ROS, descomenta la siguiente línea:
# source /opt/ros/humble/setup.bash

# Ejecutar el agente en el puerto serie
MicroXRCEAgent serial --dev /dev/ttyUSB0 -b 921600
