def creacion_ramas(url :str, token:str, valores:dict) -> bool:
    """
    Método para la solicitud a la api

    Args:
        url (str): URL de GitLab
        token (str): Token obtenido de GitLab (Personal de cada usuario)
        valores (dict): Diccionario con los parametros de configuración de las ramas

    Returns:
        bool: si se crea correctamente devuelve un True, sino un false. (A futuro
        se creará un log).
    
    """
    
    import requests
    a = input("ID del proyecto \n")
    print(valores)

    response = requests.post(f'{url}/api/v4/projects/{a}/repository/branches', params=valores, headers= token, verify=False)
    
    if response.status_code == 201:
            return "Bien"

    else:
        #print(f"Error al crear el proyecto: {response.text}") 
        #diccionario = json.load(response.json()['message'] )
            
        print( response.text)

    return "response.json()"
    
    