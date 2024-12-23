FROM php:8.4.2-apache

COPY ./ /var/www/html
RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"
RUN sed -i 's/allow_url_include = Off//g' "$PHP_INI_DIR/php.ini"
RUN echo "allow_url_include = On" >> "$PHP_INI_DIR/php.ini"

RUN apt-get update && apt-get install -y \
    libldap2-dev
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/
RUN docker-php-ext-install ldap
RUN echo "extension=php_ldap.so" >> "$PHP_INI_DIR/php.ini"

EXPOSE 8082

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN service apache2 restart
#ENTRYPOINT ["catalina.sh", "run"]
