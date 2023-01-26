<<<<<<< HEAD
import requests

def credit(loans):

    api_url = 'https://api.api-ninjas.com/v1/interestrate'
    response = requests.get(api_url, headers={'X-Api-Key': 'lzOCBfqKWqzS3OjFEVo38A==VtpOgKNNypCAecv5','country':'Canada'})
    if response.status_code == requests.codes.ok:
        print(type(response.text))
    else:
        print("Error:", response.status_code, response.text)

credit(5)

=======
def Credit(balance):
    balance = balance + balance*0.1999
    return balance

print(Credit(20000))
>>>>>>> 176bbb1d6e3432b5e5bb4fb3d0cd9906c23682b2
