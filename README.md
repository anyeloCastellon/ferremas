# FERREMAS APP

Ambiente creado para ser utilizado en Ubuntu Desktop

De acuerdo a lo visto en clases, deben ejecutar un ambiente virtual (virtual env) o ejecutar directamente run-dev-local.sh ya que tiene cargado la activacion del virtual env con nombre ambiente_desarrollo_virtual

Se deja BBDD db.sqlite3 que tiene informacion de productos y categorias disponibles


sudo apt install python3.8-venv
python3 -m venv ambiente_desarrollo_virtual
source ambiente_desarrollo_virtual/bin/activate
sudo apt install -y libpq-dev python3-dev gcc g++
pip install -r requirements.txt 