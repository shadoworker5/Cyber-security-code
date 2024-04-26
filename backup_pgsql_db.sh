#!/bin/bash


# @author Kassoum TRAORE
# @email shadoworker5.dev@gmail.com
# @create date 2024-04-26 10:09:55
# @modify date 2024-04-26 10:09:55
# 0 8 * * * /etc/init.d/backup_pgsql.sh # everyday at 8h00 AM

NOWADAY=`date +%Y-%m-%d`
TEMP_FOLDER='/tmp/databases'
BACKUP_PATH='/home/databases'

rm -rf $TEMP_FOLDER
mkdir -p $TEMP_FOLDER

PASSWORD="user_password"
export PGPASSWORD="$PASSWORD"

databases="cilss_projet cilss_db"

for database in $databases; do
    sudo -u postgres pg_dump -U user_name -w -d cilss_db > "$TEMP_FOLDER/$database-$NOWADAY.sql"
done

rsync -a $TEMP_FOLDER/$BACKUP_PATH