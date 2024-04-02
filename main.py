try:
    import logging
    from datetime import datetime 
except Exception as e:
    print(str(e))


def main():
    from GitLab.main import main as menu
    from Config.leerJson import read_json

    valores_json = read_json()
    url = valores_json[0]
    token = valores_json[1]

    valor = input("Indique por número si va a realizar una accion en \nGitLab -> 1  \nJenkins -> 2. \nPara salir del programa pulse cualquier otro carácter.\n")

    if int(valor) == 1: logs('GitLab'),logger.info("SE VA A INICIAR UN PROCESO EN GITLAB"),menu(url, token)
    elif int(valor) == 2:logs('Jenkins'),logger.info("SE VA A INICIAR UN PROCESO EN JENKINS")
    else: exit()



def logs(logtype:str):


    date = datetime.now().strftime("%H_%M_%S")
    global logger
    logger = logging.getLogger(logtype)
    logging.basicConfig(filename=r'automate_gitlabjenkins\\Logs\\{0}.log'.format(str(date)), encoding='utf-8', level=logging.DEBUG)


if __name__ == "__main__":
    main()

    