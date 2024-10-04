import requests

# api,base ,target
def exchange_rate(api_key , base , target):
    url="https://v6.exchangerate-api.com/v6/"+ api_key+"/latest/"+base
    # response=requests.get(url).json()
    # return response.get("conversion_rates",{}).get(target)

def converter(api_key ,amount , base , target):
    rate=exchange_rate(api_key, base , target )
    print(rate*amount)
# converter("f12cc685671993d72fc9dbcb",100,"usd","inr")
base=input("enter base currency name:")
target=input("enter target currency name:")
amount=float(input("enter amount:"))
converter("f12cc685671993d72fc9dbcb",amount,base,target) 


















# import requests


# url="https://v6.exchangerate-api.com/v6/f12cc685671993d72fc9dbcb/latest/USD"
# response=requests.get(url).json()
# main=response.get("conversion_rates")
# # print(response.get('conversion_rates'))
# for i in main.items():
#     print(i)