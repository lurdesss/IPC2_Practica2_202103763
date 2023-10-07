from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Usa la variable PORT del archivo .env o el valor predeterminado 5000 si no está definida
port = int(os.getenv("PORT", 5000))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=port)
