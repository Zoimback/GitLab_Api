def creacion_usuario (url :str, token:str, valores:dict) -> bool:
       
    import requests

    response = requests.post(f'{url}/api/v4/users', params=valores, headers= token, verify=False)
    
    if response.status_code == 201:
        return "Bien"

    else:
        
       # for i in response.json()['message']:b2f
           # print( response.json()['message'][i])

        return print(response.text)