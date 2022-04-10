FROM mariadb:latest

COPY database.sql docker-entrypoint-initdb.d/
# Setup the custom configuration
ADD mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf

#ENTRYPOINT service mysql restart && /bin/bash
