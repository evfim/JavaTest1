FROM php:8.0-apache

COPY ./ /var/www/html
RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"
RUN sed -i 's/allow_url_include = Off/allow_url_include = On/g' "$PHP_INI_DIR/php.ini"

EXPOSE 8082

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN service apache2 restart
#ENTRYPOINT ["catalina.sh", "run"]
