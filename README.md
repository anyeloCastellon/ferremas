# FERREMAS APP

Ambiente creado para ser utilizado en Ubuntu Desktop

De acuerdo a lo visto en clases, deben ejecutar un ambiente virtual (virtual env) o ejecutar directamente run-dev-local.sh ya que tiene cargado la activacion del virtual env con nombre ambiente_desarrollo_virtual

Se deja BBDD db.sqlite3 que tiene informacion de productos y categorias disponibles

sudo apt install python3.8-venv
python3 -m venv ambiente_desarrollo_virtual
source ambiente_desarrollo_virtual/bin/activate
sudo apt install -y libpq-dev python3-dev gcc g++
pip install -r requirements.txt 

Actualización del 16-05-2024

Hemos actualizado Django a la versión Django==4.2.13. Por lo tanto, es esencial que tengan los resguardos necesarios para que el proyecto funcione con la versión correspondiente de Python.

Si experimentan problemas con las migraciones, les recomendamos que eliminen el contenido de la carpeta MIGRATIONS de cada aplicación y borren la base de datos. Luego, ejecuten nuevamente el script de bash para aplicar las migraciones y python init.py para poblar la base de datos.