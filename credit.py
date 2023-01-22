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
    intrest = [1, 3, 5, 10]
    for i in range(len(intrest)):
        credit = 0
        for j in range(intrest[i]):
            credit = credit + balance
        credit = credit + credit*0.1999
        intrest[i] = credit
    return intrest

print(Credit(20000))
>>>>>>> 176bbb1d6e3432b5e5bb4fb3d0cd9906c23682b2
