#!/bin/sh
set -e

echo "Pregatesc mediul cron..."

# Salvez variabilele de mediu pentru sarcinile cron.
printenv | grep -v '^_' > /etc/environment || true

# Creez fisierul in care vor fi scrise rezultatele.
touch /var/log/cron.log
chmod 666 /var/log/cron.log

# Instalez configuratia cron.
cp /app/cronjob /etc/cron.d/currency-cron
chmod 0644 /etc/cron.d/currency-cron

# Pornesc cron in fundal.
echo "Pornesc serviciul cron..."
cron

# Pastrez containerul activ si afisez logurile.
echo "Monitorizez /var/log/cron.log..."
exec tail -F /var/log/cron.log
