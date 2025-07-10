# Define o interpretador Python
PYTHON = python3

start:
	$(PYTHON) index.py

# Comando para rodar testes unitários
test:
	$(PYTHON) -m unittest discover tests


# Construção do Docker e execução do programa no container
docker-start:
	docker build -f ./dockerfiles/dockerfile.python_run -t app_start
	docker run --rm app_start

# Construção do Docker e execução dos testes no container
docker-test:
	docker build -f ./dockerfiles/dockerfile.python_test -t app_tests .
	docker run --rm app_tests
