import json
from pathlib import Path

class Item:
    def __init__(self, titulo, valor, data_ocorrido, data_registro, descricao):
        self.titulo = titulo
        self.valor = int(valor)
        self.data_ocorrido = data_ocorrido
        self.data_registro = data_registro
        self.descricao = descricao

class GestorArquivos:
    ARQUIVO = 'GestorFinanceiro.json'

    @classmethod
    def _get_estrutura_vazia(cls):
        """Retorna o esqueleto do seu JSON caso o arquivo não exista."""
        return {
            "Titulo": [],
            "Valor": [],
            "Data-Ocorrido": [],
            "Data-Registro": [],
            "Descrição": []
        }

    @classmethod
    def salvar_item(cls, item: Item):
        # 1. Carrega os dados atuais ou cria a estrutura vazia
        dados = cls.carregar_todos()
        
        # 2. Adiciona os novos valores em suas respectivas listas
        dados["Titulo"].append(item.titulo)
        dados["Valor"].append(item.valor)
        dados["Data-Ocorrido"].append(item.data_ocorrido)
        dados["Data-Registro"].append(item.data_registro)
        dados["Descrição"].append(item.descricao)
        
        # 3. Salva de volta no arquivo
        try:
            with open(cls.ARQUIVO, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Erro: Sem permissão para gravar o arquivo.")

    @classmethod
    def carregar_todos(cls):
        if not Path(cls.ARQUIVO).exists():
            return cls._get_estrutura_vazia()
        
        try:
            with open(cls.ARQUIVO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return cls._get_estrutura_vazia()

# --- Exemplo de Uso ---
# Criando um novo item
item = Item("Salario", 1000, "05-02-2026", "05-02-2026", "Dia do pagamento mensal")
novo_gasto = Item("Medicamentos", -85, "12-02-2026", "12-02-2026", "Medicamento sanguineo")

# Salvando no arquivo com a nova estrutura
GestorArquivos.salvar_item(novo_gasto)
GestorArquivos.salvar_item(item)