# CineBox
Site criado para registrar seus filmes assistidos favoritos.

## Instalação

### Windows

- Instalar python (https://www.python.org/)
- Digite `python --version`, para ver se está funcionando. Tem que aparecer `Python 3.6.8` ou versão superior.
- Crie a **venv** com `python -m venv venv`.
- Ative a **venv** com `source venv/Scripts/activate` (Git Bash) ou `.\venv\Scripts\activate` (PowerShell).
- Verificar se a última versão do pip está instalada utilizando `python -m pip install --upgrade pip`.
- Digite `pip --version` para conferir se o pip foi atualizado.
- Agora instale o **django** através do comando `pip install django`.
- Crie o projeto django utilizando `django-admin.exe startproject cinebox .`.
- Crie o arquivo na raiz do projeto com o comando `pip freeze > requirements.txt`.
- Rode o comando `python manage.py migrate` para criar o banco.
- Depois criar o super usuário do banco com o comando `winpty python manage.py createsuperuser`.
- Por último rode o servidor utilizando `python manage.py runserver`.
