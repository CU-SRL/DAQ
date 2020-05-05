#!/bin/bash

# Update system
sudo apt update
sudo apt install software-properties-common

# ---
# Install Python 3
# ---

# Add PPA repository
# sudo add-apt-repository ppa:deadsnakes/ppa

# Install pip
sudo apt install -y python3-pip

# Install Flask
# sudo pip3 install flask

# ---
# Install NodeJS
# ---

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs

# ---
# DHCP Server and Wireless AP
# ---

# Install DNSMasq and HostAPD
sudo apt install -y dnsmasq hostapd

# Enable wifi
sudo ifconfig wlan0 up

# Stop services
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

# Edit netplan config file to set static IP for wifi
netplanConfFile="/etc/netplan/01-netcfg.yaml"
echo "network:
  version: 2
  ethernets:
    wlan0:
      dhcp4: no
      addresses:
        - 192.168.3.1/24
      gateway4: 192.168.3.1" >> $netplanConfFile

# Apply static IP change
sudo netplan apply

# Get rid of the original config file
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig

# Write a new file
echo "interface=wlan0
dhcp-range=192.168.3.2,192.168.3.20,255.255.255.0,24h" >> /etc/dnsmasq.conf

# Restart DHCP server
sudo systemctl start dnsmasq