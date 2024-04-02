


def main(url:str,token:str)->bool:
    """_summary_

    Args:
        url (str): _description_
        token (str): _description_

    Returns:
        bool: _description_
    """
    from .Proyectos_Ramas.main import main as menu_ramas
    from .Usuarios.main import main  as menu_usuario

    valor = input("Indique por número si va a realizar una accion en \n Reposiotrio GIT -> 1  \n Usuarios -> 2. \n")

    if int(valor) == 1: menu_ramas(url, token)
    elif int(valor) == 2:menu_usuario(url, token)
    else: exit()


    return "true"