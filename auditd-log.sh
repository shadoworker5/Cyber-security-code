sudo apt-get update
sudo apt-get install auditd


sudo nano /etc/audit/auditd.conf

# Active la journalisation de toutes les commandes tapées par les utilisateurs
-a exit,always -F arch=b64 -S execve

# Active la journalisation de toutes les commandes tapées par le compte utilisateur `ubuntu`
-a exit,always -F arch=b64 -S execve -F euid=ubuntu

sudo service auditd restart
