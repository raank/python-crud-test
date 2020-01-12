### Instalando
`git clone https://github.com/raank/python-crud-test.git`
`cd python-crud-test && bash install.sh`

### Usando o CRUD

Commandos:
    `python run.py -m {model} -a {action} id={id|opcional}`

Exemplos:
- Todos os registros: `python run.py -m clients -a index`
- Criando um cliente `python run.py -m clients -a store`
- Visualizando: `python run.py -m clients -a show id=1`
- Atualizando um cliente `python run.py -m clients -a update id=1`
- Removendo: `python run.py -m clients -a delete id=1`
- Exportar: `python run.py -m clients -a export`

Models disponíveis:
- **clients**: Clientes
- **products**: Produtos dos clientes.

Rodando testes: `python tests.py`