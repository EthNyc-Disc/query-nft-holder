import requests

API_KEY = '' # Enter API KEY
base_url = 'https://api.covalenthq.com/v1'
blockchain_chain_id = '1'
address = '0x12d905447ed4C4a8be3eCA2830A89561207e2e01' # contract address of the NFT

def get_data(chain_id, address):
    endpoint = f'/{chain_id}/tokens/{address}/token_holders/?key={API_KEY}'
    url = base_url + endpoint
    result = requests.get(url).json()
    data = result["data"]
    return [i['address'] for i in data['items']]

res = get_data(blockchain_chain_id, address)
print(res)