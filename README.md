# DeVops
Repositorio del curso

py -m venv venv 
venv/Scripts/actívate
py -m pip install -r requirements.txt
$env:FLASK_APP="./blacklists/src/main.py"
flask run -h 0.0.0.0 -p 3000