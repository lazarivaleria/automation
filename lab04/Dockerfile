FROM jenkins/ssh-agent

# Install PHP, required extensions and Composer
RUN apt-get update && apt-get install -y \
    php-cli \
    php-xml \
    php-mbstring \
    composer \
    && rm -rf /var/lib/apt/lists/*