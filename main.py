import requests

def result_api(url):
    headers = {'Content-type': 'application/json'}
    try:
        res = requests.get(url, headers=headers).json()
    except:
        return 'error'
    return res

result_api("https://api.kauri.finance/api/v1/exchange_rat")