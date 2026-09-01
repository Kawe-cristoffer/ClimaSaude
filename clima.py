import requests


# Coordenadas aproximadas de Curitiba - PR
LATITUDE = -25.4284
LONGITUDE = -49.2733


def obter_clima():
    """Obtém as condições climáticas atuais de Curitiba."""

    url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "wind_speed_10m",
            "weather_code"
        ],
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "America/Sao_Paulo"
    }

    try:
        resposta = requests.get(url, params=parametros, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        clima = dados["current"]

        return {
            "temperatura": clima["temperature_2m"],
            "umidade": clima["relative_humidity_2m"],
            "sensacao": clima["apparent_temperature"],
            "vento": clima["wind_speed_10m"],
            "codigo": clima["weather_code"],
            "horario": clima["time"]
        }

    except requests.RequestException:
        return None

    except (KeyError, TypeError):
        return None