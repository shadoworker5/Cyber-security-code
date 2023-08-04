#!/bin/bash

# @author Kassoum Traore
# @email shadoworker5.dev@gmail.com
# @create date 2023-08-04 22:11:59
# @modify date 2023-08-04 22:11:59
# crontab 30 2 * * * /etc/init.d/backup_mysql.sh

NOWADAY=`date +%Y-%m-%d`
TEMP_FOLDER='/tmp/databases'
BACKUP_PATH='/home/databases'

rm -rf $TEMP_FOLDER
mkdir -p $TEMP_FOLDER

LIST_DATABASES=$( echo 'show databases' | mysql -uroot )

for db in $LIST_DATABASES
do
mysqldump -uroot $db > $TEMP_FOLDER/$db'_'$NOWADAY.sql
done

rsync -a $TEMP_FOLDER/ $BACKUP_PATH