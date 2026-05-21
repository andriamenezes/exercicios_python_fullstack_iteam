# Exercício 29 – Parser de JSON de API Meteorológica

import json

resposta_api = """
{
    "cidade": "Manaus",
    "pais": "BR",
    "temperatura": {
        "atual": 32.4,
        "minima": 26.1,
        "maxima": 35.8,
        "sensacao": 38.2
    },
    "umidade": 87,
    "condicao": "Parcialmente nublado",
    "vento": { "velocidade_kmh": 12, "direcao": "NE" },
    "atualizado_em": "2025-01-15T14:30:00"
}
"""

dados = json.loads(resposta_api)

# Extrai os sub-dicionários
temp  = dados["temperatura"]
vento = dados["vento"]

# Formata a data  "2025-01-15T14:30:00" → "15/01/2025 às 14:30"
data_raw        = dados["atualizado_em"]
data, hora      = data_raw.split("T")
ano, mes, dia   = data.split("-")
hora_fmt        = hora[:5]
data_fmt        = f"{dia}/{mes}/{ano} às {hora_fmt}"

print("=" * 38)
print("  BOLETIM METEOROLOGICO")
print("=" * 38)
print(f"  {dados['cidade']} — {dados['pais']}")
print(f"  {dados['condicao']}")
print("-" * 38)
print(f"  Temperatura atual : {temp['atual']}°C")
print(f"  Sensacao termica  : {temp['sensacao']}°C")
print(f"  Minima            : {temp['minima']}°C")
print(f"  Maxima            : {temp['maxima']}°C")
print(f"  Umidade           : {dados['umidade']}%")
print(f"  Vento             : {vento['velocidade_kmh']} km/h — {vento['direcao']}")
print("-" * 38)
print(f"  Atualizado em: {data_fmt}")
print("=" * 38)