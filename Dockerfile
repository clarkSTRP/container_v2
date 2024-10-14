FROM php:apache

RUN apt-get update && apt-get install -y \
    python3 \
    python3-requests \
    mariadb-client \
    && docker-php-ext-install pdo pdo_mysql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /var/www/html

COPY ./index.php /var/www/html

RUN mkdir -p /var/www/html/tests
COPY ./tests/test.py /var/www/html/tests


# Copy the security headers configuration file to activate some header for testing
COPY ./security.conf /etc/apache2/conf-available/security.conf


RUN a2enmod headers \
    && a2enconf security \
    && service apache2 restart

# Use production php.ini
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"


RUN chown -R www-data:www-data /var/www/html


WORKDIR /var/www/html/tests


EXPOSE 80

