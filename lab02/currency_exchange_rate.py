import sys
import json
import logging
from pathlib import Path

import requests


API_URL = "http://localhost:8080/"


logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_exchange_rate(from_currency, to_currency, date):
    try:
        response = requests.post(
            API_URL,
            params={
                "from": from_currency,
                "to": to_currency,
                "date": date
            },
            data={
                "key": "EXAMPLE_API_KEY"
            },
            timeout=10
        )

        response.raise_for_status()
        result = response.json()

        if result.get("error"):
            raise ValueError(result["error"])

        return result["data"]

    except requests.RequestException as error:
        logging.error("API request error: %s", error)
        print(f"Eroare la conectarea la API: {error}")
        return None

    except (ValueError, json.JSONDecodeError) as error:
        logging.error("API response error: %s", error)
        print(f"Eroare în răspunsul API: {error}")
        return None


def save_data(data, from_currency, to_currency, date):
    data_directory = Path(__file__).resolve().parent.parent / "data"
    data_directory.mkdir(exist_ok=True)

    filename = f"{from_currency}_{to_currency}_{date}.json"
    file_path = data_directory / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Datele au fost salvate în: {file_path}")


def main():
    if len(sys.argv) != 4:
        print(
            "Utilizare: python currency_exchange_rate.py "
            "<from_currency> <to_currency> <date>"
        )
        logging.error("Număr invalid de parametri.")
        return

    from_currency = sys.argv[1].upper()
    to_currency = sys.argv[2].upper()
    date = sys.argv[3]

    data = get_exchange_rate(from_currency, to_currency, date)

    if data is not None:
        save_data(data, from_currency, to_currency, date)
        print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()