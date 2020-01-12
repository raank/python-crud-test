# Python CRUD via Terminal

Python CRUd via terminal para inserir Clientes e seus Produtos.
Foi usado alguns pacotes para o projeto

- **alembic** migrations.
- **SQLAlchemy** manipular banco de dados.
- **click** manipular os comandos de console.
- **pathlib** manipular arquivo de exportação.
- **env_file** arquivo de envs.

### Instalando
`git clone https://github.com/raank/python-crud-test.git`
`cd python-crud-test && bash install.sh`

### Usando o CRUD

Comandos:
    `python run.py -m {model} -a {action} id={id|opcional}`

Exemplos:
- Todos os registros: `python run.py -m clients -a index`
- Criando um cliente `python run.py -m clients -a store`
- Visualizando: `python run.py -m clients -a show id=1`
- Atualizando um cliente `python run.py -m clients -a update id=1`
- Removendo: `python run.py -m clients -a delete id=1`
- Exportar: `python run.py -m clients -a export`

Modelos disponíveis:
- **clients**: Clientes
- **products**: Produtos dos clientes.

Rodando testes: `python tests.py`