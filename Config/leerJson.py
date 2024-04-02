

def read_json() -> dict:
    """
    Lee los valores de configuracion de las conexiones, branches, projects y users

    Args:
        valor (str): Argumento que se le pasa al metodo para ver su configuracion en el .json
        path  (str): Argumento que se le pasa al metodo para identificar el .json del que se 
        quiere extraer la información

    Returns:
        dict: Devuelve una lista con los parametros obtenidos de la búsqueda del .json

    """
    import json
  
    valores=[]
    with open(r"automate_gitlabjenkins\Config\conexion.json", 'r') as archivo:
        configuracion = json.load(archivo)['gitlab']
        valores = [configuracion[i]  for i in configuracion]

    return valores