#!/bin/bash

# @author Kassoum Traore
# @email shadoworker5.dev@gmail.com
# @create date 2023-08-04 22:11:59
# @modify date 2023-08-04 22:11:59
# crontab 30 2 * * * /etc/init.d/backup_mysql.sh

NOWADAY=`date +%Y-%m-%d`
TEMP_FOLDER='/tmp/databases'
BACKUP_PATH='/home/databases'
FILE_DAYS_OLD=7
MYSQL_USER=root
MYSQL_PASSWORD=root

cleanUp() {
    if [ -d "$BACKUP_PATH" ]; then
        echo "Suppression des fichiers de plus de $FILE_DAYS_OLD jours dans $BACKUP_PATH"
        
        find "$BACKUP_PATH" -type f -mtime +$FILE_DAYS_OLD -exec rm -f {} \;
    fi
}

rm -rf $TEMP_FOLDER
mkdir -p $TEMP_FOLDER

LIST_DATABASES=$( echo 'show databases' | mysql -u$MYSQL_USER -p$MYSQL_PASSWORD )

for db in $LIST_DATABASES
do
    mysqldump -u$MYSQL_USER -p$MYSQL_PASSWORD $db > $TEMP_FOLDER/$db'_'$NOWADAY.sql
done

cleanUp
rsync -a $TEMP_FOLDER/ $BACKUP_PATH