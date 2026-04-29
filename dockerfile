FROM python:3.10

WORKDIR /app

# Copia a pasta core e o arquivo principal
COPY ./core ./core
COPY ./tests ./tests
COPY ./pytest.ini .
COPY ./app.py . 

COPY ./requirements.txt .
# Copia os requisitos se houver (ex: pytest)
RUN pip install -r requirements.txt

RUN pytest tests/

# Comando para rodar a aplicação
CMD [ "python", "./app.py" ]
