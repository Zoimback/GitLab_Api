def main(url:str, token:str) -> bool:
    

    from .gestionUsuarios import creacion_usuario
    
    bool_salida= True
    valor = input("¿Que quieres configurar? \n1.Alta Usuario \n2.Asignacion roles  \n")
    if int(valor) == 1: bool_salida = creacion_usuario(url,token, confinguracionParamsUsuario() )
    
    return bool_salida 
    


def confinguracionParamsUsuario()-> dict:
    """Método para personalización del proyecto que se quiere crear.

        Returns:
        dict: Devuelve los parameretros dle usuario.fd
    """
    ditc_usuario={
    "email": "alejandro.rodriguezgonzalez.ext@lineadirecta.es",
    "username": "AUCARG",
    "name": "ALEJANDRO RODRIGUEZ GONZALEZ",
    "skip_confirmation": "true",
    "reset_password":"true"
    }
    return ditc_usuario