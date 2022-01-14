# Django project

    1. Clona el proyecto
    2. Crea un ambiente para el proyectp en el directorio donde se clonó el repositorio(recomiendo usar pyenv)

        cd path/to/fullstack-interview-test
        python -m venv flat_app
        source flat_app/bin/
        pip install -r requirements.txt

    3. Inicia el servidor de desarrollo

        python ./backend/manage.py migrate
        python ./backend/manage.py runserver

# Front end project

    1. Cambia tu ubicación a la   cd path/to/fullstack-interview-test/flat-frontend
    2. Corre npm install
    3. Corre npm run dev
