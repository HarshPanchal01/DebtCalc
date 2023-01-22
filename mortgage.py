<<<<<<< HEAD
import requests

api_url = 'https://api.api-ninjas.com/v1/interestrate'
response = requests.get(api_url, headers={'X-Api-Key': 'lzOCBfqKWqzS3OjFEVo38A==VtpOgKNNypCAecv5'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
=======
import requests


def find_canada(countries):
    for country in countries:
        if 'Canada' in country:
            return country

def mortgage(debt):
    api_url = 'https://api.api-ninjas.com/v1/interestrate'
    response = requests.get(api_url, headers={'X-Api-Key': 'lzOCBfqKWqzS3OjFEVo38A==VtpOgKNNypCAecv5'})
    if response.status_code == requests.codes.ok:
        response=response.text.split("{")
        canada=find_canada(response)
        canada=canada.split(",")            ##please find a better way to clean this data
        canada=canada[2]
        canada=canada[-4:]
        canada=float(canada)
        canada=(canada/100)
        
        debt_over_time=debt*(canada+1)

        return debt_over_time


    else:
        print("Error:", response.status_code, response.text)
>>>>>>> 6a54df6d66b8bd8a341d063bed8f88c7402776a8
