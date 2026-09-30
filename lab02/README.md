# IW02 – Currency Exchange Rate API

## Descriere

În cadrul acestei lucrări de laborator am creat un script Python care interacționează cu un serviciu API pentru obținerea cursurilor valutare.

Scriptul primește din linia de comandă moneda inițială, moneda finală și data pentru care este solicitat cursul valutar. Datele primite de la API sunt salvate în format JSON.

## Dependențe

Pentru realizarea lucrării am folosit:

* Python 3
* biblioteca `requests`
* serviciul Currency Exchange Rate din proiectul suport `lab02prep`
* Docker și Docker Compose pentru pornirea serviciului API

Biblioteca Python poate fi instalată cu:

```bash
python -m pip install requests
```

## Pornirea serviciului API

Serviciul API este pornit din proiectul suport folosind:

```bash
docker-compose up --build
```

Serviciul este disponibil la:

```text
http://localhost:8080
```

## Rularea scriptului

Scriptul se execută din rădăcina proiectului folosind următoarea sintaxă:

```bash
python lab02/currency_exchange_rate.py <from_currency> <to_currency> <date>
```

Exemplu:

```bash
python lab02/currency_exchange_rate.py USD EUR 2025-01-01
```

Unde:

* `USD` reprezintă moneda din care se face conversia;
* `EUR` reprezintă moneda în care se face conversia;
* `2025-01-01` reprezintă data pentru care este solicitat cursul.

## Salvarea datelor

Rezultatul primit de la API este salvat automat în directorul `data`, aflat în rădăcina proiectului.

Numele fișierului este construit folosind cele două valute și data solicitării.

Exemplu:

```text
data/USD_EUR_2025-01-01.json
```

Directorul `data` este creat automat de script dacă acesta nu există.

## Gestionarea erorilor

Scriptul verifică numărul parametrilor introduși și gestionează erorile apărute la comunicarea cu API-ul sau la prelucrarea răspunsului.

Mesajele de eroare sunt afișate în terminal și sunt înregistrate în fișierul:

```text
error.log
```

Acest fișier este creat în rădăcina proiectului.

## Structura proiectului

```text
automation/
├── lab01/
├── lab02/
│   ├── currency_exchange_rate.py
│   └── README.md
├── data/
└── error.log
```

## Testare

Pentru verificarea funcționării scriptului am folosit mai multe date din perioada indicată în cerință:

```text
2025-01-01
2025-03-01
2025-05-01
2025-07-01
2025-09-01
```

Pentru fiecare dată am solicitat cursul dintre USD și EUR și am verificat salvarea răspunsului în format JSON.
