import requests

def credit(loans):

    api_url = 'https://api.api-ninjas.com/v1/interestrate'
    response = requests.get(api_url, headers={'X-Api-Key': 'lzOCBfqKWqzS3OjFEVo38A==VtpOgKNNypCAecv5','country':'Canada'})
    if response.status_code == requests.codes.ok:
        print(type(response.text))
    else:
        print("Error:", response.status_code, response.text)

credit(5)

