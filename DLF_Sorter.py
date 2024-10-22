import os
import platform
import time
from pathlib import Path

# Download Folder Sorter v1.4.0

class Int:
    # Directorios del sistema
    HOME_DIR = str(Path.home())  # Directorio de inicio del usuario
    DOWNLOADS = os.path.join(HOME_DIR, 'Downloads')  # Carpeta de descargas

    # Extensiones de archivos
    DOC_EXTENSIONS = ['.txt', '.doc', '.docx', '.odt', '.pdf']
    PICTURE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
    VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv']
    MUSIC_EXTENSIONS = ['.mp3', '.wav']
    EXECUTABLE_EXTENSIONS = ['.exe', '.py', '.kt']  # Nuevas extensiones para ejecutables

    # Hora y fecha actuales
    CURRENT_TIME = time.ctime(time.time())


# Función principal
def main():
    # Crear carpeta "Otros" si no existe
    others_folder = os.path.join(Int.DOWNLOADS, 'Otros')
    if not os.path.exists(others_folder):
        os.makedirs(others_folder)

    # Especificar la ruta del log en la carpeta "Otros"
    log_file_path = os.path.join(others_folder, 'Output Log.txt')

    # Documentos
    print('Ordenando archivos de documentos... \n')
    for extension in Int.DOC_EXTENSIONS:
        sort(Int.DOWNLOADS, extension, log_file_path)

    # Imágenes
    print('Ordenando archivos de imágenes... \n')
    for extension in Int.PICTURE_EXTENSIONS:
        sort(Int.DOWNLOADS, extension, log_file_path)

    # Videos
    print('Ordenando archivos de videos... \n')
    for extension in Int.VIDEO_EXTENSIONS:
        sort(Int.DOWNLOADS, extension, log_file_path)

    # Música
    print('Ordenando archivos de música... \n')
    for extension in Int.MUSIC_EXTENSIONS:
        sort(Int.DOWNLOADS, extension, log_file_path)

    # Ejecutables
    print('Ordenando archivos ejecutables... \n')
    for extension in Int.EXECUTABLE_EXTENSIONS:
        sort(Int.DOWNLOADS, extension, log_file_path)

    # Otros
    print('Ordenando archivos no clasificados... \n')
    sort_others(Int.DOWNLOADS, log_file_path)

    print('Ordenación de archivos completada.')


# Escribir en el registro
def log_output(data, log_file_path):
    with open(log_file_path, 'a+') as write:
        write.write(Int.CURRENT_TIME + ' ' + data + '\n' + '\n')


# Mover archivos y manejo de errores
def sort(target, ext, log_file_path):
    # Crear carpetas para cada tipo de archivo
    folder_name = ''
    if ext in Int.DOC_EXTENSIONS:
        folder_name = 'Documentos'
    elif ext in Int.PICTURE_EXTENSIONS:
        folder_name = 'Imágenes'
    elif ext in Int.VIDEO_EXTENSIONS:
        folder_name = 'Videos'
    elif ext in Int.MUSIC_EXTENSIONS:
        folder_name = 'Música'
    elif ext in Int.EXECUTABLE_EXTENSIONS:
        folder_name = 'Ejecutables'

    target_folder = os.path.join(target, folder_name)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    try:
        for files in os.listdir(target):
            if files.endswith(ext) and os.path.isfile(os.path.join(target, files)):  # Verificar que sea un archivo
                # Si el archivo existe en la carpeta de destino, se omite
                if os.path.isfile(os.path.join(target_folder, files)):
                    log_output('Archivo duplicado encontrado y omitido: ' + files, log_file_path)
                else:
                    os.replace(os.path.join(target, files), os.path.join(target_folder, files))
                    log_output('Movido -> ' + files + ' a -> ' + target_folder, log_file_path)

    except IOError as error:
        log_output('Error ocurrido -> ' + str(error), log_file_path)
        print('Error ocurrido, consulta el registro de salida.')


# Mover archivos no clasificados a "Otros"
def sort_others(target, log_file_path):
    others_folder = os.path.join(target, 'Otros')
    
    try:
        for files in os.listdir(target):
            # Verificar si el archivo no encaja en las extensiones conocidas
            if not (files.endswith(tuple(Int.DOC_EXTENSIONS)) or
                    files.endswith(tuple(Int.PICTURE_EXTENSIONS)) or
                    files.endswith(tuple(Int.VIDEO_EXTENSIONS)) or
                    files.endswith(tuple(Int.MUSIC_EXTENSIONS)) or
                    files.endswith(tuple(Int.EXECUTABLE_EXTENSIONS))):
                if os.path.isfile(os.path.join(target, files)):  # Verificar que sea un archivo
                    os.replace(os.path.join(target, files), os.path.join(others_folder, files))
                    log_output('Movido a Otros -> ' + files, log_file_path)

    except IOError as error:
        log_output('Error ocurrido en Otros -> ' + str(error), log_file_path)
        print('Error ocurrido, consulta el registro de salida.')


# Iniciar el script
if __name__ == '__main__':
    main()
