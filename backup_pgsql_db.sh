#!/bin/bash


# @author Kassoum TRAORE
# @email shadoworker5.dev@gmail.com
# @create date 2024-04-26 10:09:55
# @modify date 2024-04-26 10:09:55
# 0 8 * * * /etc/init.d/backup_pgsql.sh # everyday at 8h00 AM

NOWADAY=`date +%Y-%m-%d`
TEMP_FOLDER='/tmp/databases'
BACKUP_PATH='/home/databases'
FILE_DAYS_OLD=7

USER_NAME=postgres
PASSWORD="user_password"
export PGPASSWORD="$PASSWORD"

cleanUp() {
    if [ -d "$BACKUP_PATH" ]; then
        echo "Suppression des fichiers de plus de $FILE_DAYS_OLD jours dans $BACKUP_PATH"
        
        find "$BACKUP_PATH" -type f -mtime +$FILE_DAYS_OLD -exec rm -f {} \;
    fi
}

rm -rf $TEMP_FOLDER
mkdir -p $TEMP_FOLDER

databases="cilss_projet cilss_db"

for database in $databases; do
    sudo -u postgres pg_dump -U $USER_NAME -w -d cilss_db > "$TEMP_FOLDER/$database-$NOWADAY.sql"
done

cleanUp
rsync -a $TEMP_FOLDER/$BACKUP_PATH