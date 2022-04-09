FROM mysql:8.0

COPY database.sql docker-entrypoint-initdb.d/database.sql
# Setup the custom configuration
ADD mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
