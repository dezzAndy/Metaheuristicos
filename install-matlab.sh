#!/bin/bash
# Script para instalar MATLAB mediante Distrobox
# Dependencias: Distrobox, Podman o Docker, unzip

ZIP_FILE="matlab_R2026a_Linux.zip" # Asegúrate de que el nombre coincida

# Verificación del archivo
if [ ! -f "$ZIP_FILE" ]; then
    echo "Error: Descarga '$ZIP_FILE' desde https://mathworks.com/downloads/ y colócalo en esta misma carpeta."
    exit 1
fi

# Creación del contenedor
echo "Creando contenedor Debian..."
distrobox create -i debian:stable -n matlab-env -Y

# Instalación de dependencias dentro del contenedor
echo "Instalando dependencias..."
distrobox enter -n matlab-env -- sudo apt update
distrobox enter -n matlab-env -- sudo apt install -y unzip libnss3 libasound2 libatk1.0-0 libc6 libcairo2 libcap2 libdbus-1-3 libfontconfig1 libfreetype6 libgcc-s1 libgdk-pixbuf-2.0-0 libgl1 libglx-mesa0 libglib2.0-0 libglu1-mesa libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxtst6 zlib1g chromium

# Preparación de directorios
echo "Preparando directorios..."
mkdir -p ~/matlab_folder
distrobox enter -n matlab-env -- mkdir -p ~/.local/share/MATLAB/R2026a/

# Extracción e instalación
echo "Extrayendo el instalador (esto puede tardar)..."
unzip -q "$ZIP_FILE" -d ~/matlab_folder

echo "Lanzando instalador..."
# Ejecutamos el instalador dentro del contenedor
distrobox enter -n matlab-env -- ~/matlab_folder/install

# Limpieza
echo "Limpiando archivos temporales..."
rm -rf ~/matlab_folder
echo "Instalación finalizada :D!"