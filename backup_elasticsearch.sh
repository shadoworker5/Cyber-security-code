#!/bin/bash
# @author Kassoum Traore
# @email shadoworker5.dev@gmail.com
# @create date 2023-08-04 23:10:46
# @modify date 2023-08-04 23:10:46

# Install the elasticdump
# npm install elasticdump --location=global
# crontab 30 2 * * * /etc/init.d/backup_elasticsearch.sh

NOWADAY=`date +%Y-%m-%d`
TEMP_FOLDER='/tmp/databases'
BACKUP_PATH='/home/databases'
URL_ELASTIC="http://x.x.x.x:xxxxx"
LISTE_INDEX="index1 index2"

rm -rf $TEMP_FOLDER
mkdir -p $TEMP_FOLDER

for INDEX in $LISTE_INDEX
do
elasticdump --input=$URL_ELASTIC/$INDEX --output=$TEMP_FOLDER/$INDEX"_backup_mapping_"$NOWDATE.json --type=mapping
elasticdump --input=$URL_ELASTIC/$INDEX --output=$TEMP_FOLDER/$INDEX"_backup_data_"$NOWDATE.json --type=data
done

cd $TEMP_FOLDER
tar -cvf $NOWDATE.tar.gz *

rsync -a $TEMP_FOLDER/ $BACKUP_PATH