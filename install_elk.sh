#!/bin/bash

# @author Shadoworker5 Dev
# @email shadoworker5@protonmail.com
# @create date 2023-04-24 21:54:10
# @modify date 2023-06-16 12:28:52

INSTALL_FOLDER="elk_stack_install_folder"
ELASTIC_INSTALL_RESULT="elastic_install_result.log"
KIBANA_INSTALL_RESULT="kibana_install_result.log"
LOGSTASH_INSTALL_RESULT="logstash_install_result.log"

function checkUser() {
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script with root user"
        exit 1
    fi
}

checkUser

mkdir $INSTALL_FOLDER && chmod 777 $INSTALL_FOLDER
cd $INSTALL_FOLDER

echo "start script running by launch apt update first............."
apt update

echo "install default java and jre"
apt install default-jre default-jdk

echo "add ELK stack source in source list"
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

echo "add apt-transport-https"
apt-get install apt-transport-https

echo "add elastic 8.x repository in source list"
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

echo "run update"
apt-get update

echo "run install elastic 8.x"
sudo apt-get install elasticsearch > $ELASTIC_INSTALL_RESULT

echo "install Kibana"
apt-get install kibana > $KIBANA_INSTALL_RESULT

echo "install Logstash"
apt install logstash > $LOGSTASH_INSTALL_RESULT

echo "end script running............."