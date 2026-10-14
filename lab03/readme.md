# Laboratorul 03: Automatizarea executării scripturilor cu Cron și Docker

## 1. Descrierea proiectului

Scopul acestui proiect este automatizarea executării scriptului `currency_exchange_rate.py` folosind serviciul cron într-un container Docker.

Sunt configurate două sarcini:
- În fiecare zi, la ora 06:00, se solicită cursul MDL–EUR pentru ziua precedentă.
- În fiecare vineri, la ora 17:00, se solicită cursul MDL–USD pentru vinerea precedentă.

Rezultatele și erorile comenzilor cron sunt redirecționate în `/var/log/cron.log`.

## 2. Structura proiectului

- `currency_exchange_rate.py` — scriptul Python preluat din laboratorul 02, care solicită cursul de schimb.
- `cronjob` — conține expresiile cron și comenzile executate automat.
- `entrypoint.sh` — pregătește fișierul de log, configurează cron și pornește monitorizarea.
- `Dockerfile` — definește imaginea Docker și instalează dependențele necesare.
- `docker-compose.yml` — configurează construirea imaginii și pornirea containerului.
- `readme.md` — conține instrucțiunile de utilizare.
- `data/` — director pentru datele generate de script, dacă acesta îl utilizează.
- `error.log` — fișierul de erori al scriptului, dacă acesta îl utilizează.

## 3. Cerințe preliminare

Înainte de pornire, trebuie să fie instalate și pornite Docker Desktop și Git. Scriptul Python trebuie să fie prezent în directorul proiectului și să poată fi executat independent.

## 4. Construirea și pornirea containerului

Deschid terminalul în directorul `lab03` și execut:

docker compose build
docker compose up -d

Prima comandă construiește imaginea Docker. A doua pornește containerul în fundal.

Verific starea containerului:
docker compose ps

Pentru a afișa mesajele containerului:
docker compose logs

## 5. Verificarea logurilor cron

Pentru a urmări rezultatele în timp real, execut:
docker exec -it lab03-currency-cron tail -f /var/log/cron.log


Pentru a afișa ultimele 50 de linii:
docker exec lab03-currency-cron tail -n 50 /var/log/cron.log

Pentru a verifica dacă fișierul de log există:
docker exec lab03-currency-cron ls -l /var/log/cron.log

## 6. Testarea manuală a scriptului

Pentru a verifica dacă scriptul Python funcționează, îl pot executa manual în container, utilizând o dată acceptată de API:
docker exec lab03-currency-cron python /app/currency_exchange_rate.py MDL EUR 2025-09-15

Data trebuie să fie acceptată de API-ul și de validările scriptului utilizat.

Pentru a verifica o comandă asemănătoare celei programate, pot executa:

docker exec lab03-currency-cron sh -c 'python /app/currency_exchange_rate.py MDL EUR "$(date -d yesterday +%F)" >> /var/log/cron.log 2>&1'


Apoi verific logul:
docker exec lab03-currency-cron tail -n 20 /var/log/cron.log


Executarea manuală verifică scriptul și redirecționarea ieșirii. Ea nu demonstrează singură că programarea cron funcționează; pentru aceasta trebuie să verific și configurația cron sau să aștept următoarea oră programată.

## 7. Oprirea containerului

Pentru oprirea containerului execut:
docker compose down


Pentru reconstruirea imaginii după modificarea fișierelor:
docker compose up -d --build


## 8. Concluzie

Prin realizarea acestui proiect am configurat două sarcini automate cu cron și am integrat serviciul într-un container Docker. Am separat configurarea sarcinilor de scriptul Python și am configurat înregistrarea rezultatelor în fișierul `/var/log/cron.log`. Utilizarea Docker Compose simplifică construirea, pornirea și administrarea containerului.