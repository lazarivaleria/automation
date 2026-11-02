# Laboratorul 4 – Configurarea Jenkins pentru automatizarea sarcinilor DevOps

## 1. Scopul lucrării

Scopul laboratorului este instalarea și configurarea Jenkins pentru automatizarea procesului de testare a unui proiect PHP, folosind un agent SSH separat și un pipeline.

## 2. Instrumente utilizate

- Docker și Docker Compose
- Jenkins Controller
- Jenkins SSH Agent
- PHP 8.4.27
- Composer 2.8.8
- PHPUnit 11.5.57
- Git și GitHub

## 3. Configurarea mediului

Jenkins Controller a fost pornit într-un container Docker și este accesibil la adresa `http://localhost:8081`.

A fost creat un agent SSH separat, numit `ssh-agent`, conectat la Jenkins cu ajutorul unei chei SSH. Agentul folosește eticheta `php-agent` și are instalate PHP și Composer.

Pentru a evita conflictul cu un alt serviciu care folosește portul 8080, Jenkins a fost expus pe portul 8081 al calculatorului.

## 4. Proiectul PHP

Pentru verificarea funcționării pipeline-ului a fost creat un proiect PHP simplu, care conține o clasă `Calculator`.

Clasa implementează două operații:
- Adunarea a două numere.
- Scăderea a două numere.

Testele automate sunt scrise folosind PHPUnit și verifică rezultatele celor două operații.

Structura proiectului:

```text
lab04/
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── .gitignore
└── php-project/
    ├── composer.json
    ├── src/
    │   └── Calculator.php
    └── tests/
        └── CalculatorTest.php
```

## 5. Configurarea pipeline-ului

A fost creat jobul Jenkins `PHP-Calculator-Pipeline`, configurat să preia codul din repository-ul GitHub `https://github.com/lazarivaleria/automation.git`, de pe branch-ul `lab04`.

Fișierul `Jenkinsfile` definește următoarele etape:

1. **Install Dependencies** – instalează dependențele proiectului folosind Composer.
2. **Run Tests** – execută testele automate cu PHPUnit.
3. **Post Actions** – afișează un mesaj privind rezultatul pipeline-ului.

Pipeline-ul rulează pe agentul identificat prin eticheta `php-agent`.

## 6. Rezultatele testării

A fost executat jobul `PHP-Calculator-Pipeline` în Jenkins.

Primul build a eșuat deoarece comanda PHPUnit nu indica explicit directorul cu teste. Problema a fost rezolvată prin modificarea comenzii în:

```bash
vendor/bin/phpunit --testdox tests
```

La al doilea build, dependențele au fost instalate corect, iar testele au fost executate cu succes.

Rezultatele obținute:

| Test | Rezultat |
|---|---|
| Addition | Reușit |
| Subtraction | Reușit |
| Total teste | 2 |
| Total verificări (assertions) | 2 |
| Rezultatul pipeline-ului | SUCCESS |

Mesajul final din Jenkins a fost `Finished: SUCCESS`.

## 7. Probleme întâlnite și soluții

- **Conflict de port:** portul 8080 era deja utilizat, de aceea Jenkins a fost configurat pe portul 8081 al calculatorului.
- **Configurarea agentului SSH:** a fost generată o pereche de chei SSH și a fost adăugată cheia privată în Jenkins Credentials.
- **Lipsa opțiunii Pipeline:** a fost instalat pluginul necesar.
- **Lipsa opțiunii Git:** a fost instalat pluginul Git.
- **Eroare la executarea testelor:** a fost specificat directorul `tests` în comanda PHPUnit.

## 8. Concluzie

În cadrul laboratorului am configurat Jenkins folosind Docker, am conectat un agent SSH și am creat un pipeline pentru automatizarea testării unui proiect PHP. Am învățat cum Jenkins preia codul din GitHub, instalează dependențele și execută testele automate. După corectarea comenzii PHPUnit, ambele teste au trecut, iar pipeline-ul s-a încheiat cu succes (`SUCCESS`).