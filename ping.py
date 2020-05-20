

import platform
import subprocess
import socket as sc

sistemas_operativo = platform.system().lower()
print(sistemas_operativo)

hostName = sc.gethostname()
direccion_IP = sc.gethostbyname(hostName)


def ping(host):
    """
    Realizamos PING a un servidor/host
    :param host: Nombre o Direcion del host
    """
    parametro = '-n' if sistemas_operativo =='windows' else '-c'

    comando = ['ping', parametro, '7', host]

    subprocess.call(comando)

ping(direccion_IP)

