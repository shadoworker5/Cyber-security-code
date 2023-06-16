#!/bin/bash

# @author Shadoworker5 Dev
# @email shadoworker5@protonmail.com
# @create date 2023-06-16 12:25:04
# @modify date 2023-06-16 12:25:04

# Block Ping Sweep Scan
sudo iptables -I INPUT -p ICMP -j DROP
sudo iptables -I INPUT -p tcp --tcp-flags ALL ACK --dport 80 -j DROP
sudo iptables -I INPUT -p tcp --tcp-flags ALL SYN --dport 443 -j DROP

# Block TCP SYN Ping Scan
sudo iptables -I INPUT -p tcp --tcp-flags ALL SYN -j DROP

# Bloc TCP ACK Ping Scan
sudo iptables -I INPUT -p tcp --tcp-flags ALL ACK -j DROP

# Block ICMP Echo Ping Scan
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

# Bloc ICMP Ping Scan
# sudo iptables -I INPUT -p ICMP -j DROP

sudo iptables -I INPUT -p UDP -j DROP

# Block IP Ping Scan
sudo iptables -I INPUT -p IP -j DROP