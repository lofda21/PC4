import requests

def obtener_precio_bitcoin(n):
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        precio_bitcoin = data['bpi']['USD']['rate_float']
        total = n * precio_bitcoin
        print(f"El valor de {n} Bitcoin(s) es: ${total:,.4f} USD")
    except requests.RequestException as e:
        print("Error al realizar la solicitud:", e)
n = float(input("Introduce la cantidad de Bitcoins que posees: "))
obtener_precio_bitcoin(n)