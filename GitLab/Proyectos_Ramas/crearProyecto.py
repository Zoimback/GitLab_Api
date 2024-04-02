def creacion_proyecto(url :str, token:str, valores:dict) -> bool:
    """
    Método para la solicitud a la api

    Args:
        url (str): URL de GitLab
        token (str): Token obtenido de GitLab (Personal de cada usuario)
        valores (dict): Diccionario con los parametros de configuración del proyecto

    Returns:
        bool: si se crea correctamente devuelve un True, sino un false. (A futuro
        se creará un log).
    
    """
    
    import requests

    response = requests.post(f'{url}/api/v4/projects', params=valores, headers= token, verify=False)
    
    if response.status_code == 201:
        return "Bien"

    else:
        #print(f"Error al crear el proyecto: {response.text}") 
        #diccionario = json.load(response.json()['message'] )
        for i in response.json()['message']:
            print( response.json()['message'][i])

        return response.json()
    
def aux_obtenerPid(url:str, token:str, valores:dict) -> int:
    import requests

    response = requests.post(f'{url}/api/v4/projects', params=valores, headers= token, verify=False)
    
    if response.status_code == 201:
        return response.json()

    else:
        print(f"Error al crear el proyecto: {response.text}")   
        return response.json()
    

