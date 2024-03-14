#crear entorno virtual y instalar dependencias en un sistema basado en Windows

import subprocess
import sys
import os

def create_virtual_environment():
    # Comprobamos si el directorio 'venv' ya existe
    if not os.path.exists('venv'):
        print("Creando entorno virtual...")
        # Creamos el entorno virtual usando subprocess
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
        print("Entorno virtual creado exitosamente.")
    else:
        print("El entorno virtual ya existe.")

def install_dependencies():
    print("Instalando dependencias...")
    # Instalamos las dependencias utilizando pip
    subprocess.check_call([os.path.join('venv', 'Scripts', 'pip.exe'), 'install', '-r', 'requirements.txt'])
    print("Dependencias instaladas exitosamente.")

def main():
    create_virtual_environment()
    # Activamos el entorno virtual antes de instalar las dependencias
    activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
    subprocess.call(activate_script, shell=True)
    install_dependencies()

if __name__ == "__main__":
    main()
