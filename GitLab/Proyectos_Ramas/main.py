



def main(url:str, token:str) -> bool:
    
    from .crearProyecto import creacion_proyecto 
    from .crearRamas import creacion_ramas
    
    
    bool_salida= True
    valor = input("¿Que quieres configurar? \n1.Proyecto \n2.Rama \n")
    if int(valor) == 1: bool_salida = creacion_proyecto(url,token, confinguracionParamsProyects() )
    elif int(valor) == 2: bool_salida = creacion_ramas(url,token, confinguracionParamsRama())
    
    
    return bool_salida 
    



def confinguracionParamsProyects()-> dict:
    """Método para personalización del proyecto que se quiere crear.

    Returns:
        dict: Devuelve los parámetros de configuración del proyecto.
    """
    dict_proyectos={
        "name":"",
        "namespace_id":"",
        "default_branch":"default",
        "builds_access_level" :"private",
        "descripcion":"",
        "initialize_with_readme":"true",
        "push_access_level":"0",
        "merge_access_level":"40",
        "remove_source_branch_after_merge": "False"
    }

    for key in dict_proyectos:
        if dict_proyectos[key] == "": dict_proyectos[key] = input(f"Indique el parámetro {key} --> ")
    return dict_proyectos


def confinguracionParamsRama()-> dict:

    ramas={"branch": input("Nombre de la rama"), "ref": input("Referencia de la rama")}
    
    return ramas
