# FastAPI
- Atualiza o Swagger e Redoc automaticamente.

# Ruff
Ferramenta em python com duas funções principais:
1. Linter: Analisar o código de forma estática
2. Formatter: Formatar o código

```
poetry add --group dev ruff
``` 

Acrescentar no `pyproject.toml`:

```
[tool.ruff]
line-length = 79
extend-exclude = ['migrations']
```

- Comandos:
    - `ruff check .`
    - `ruff format .`

## Linter do ruff
- `I` Isort: ordenação de imports em ordem alfabética
- `F` Pyflakes: procura por alguns erros em relação a boas práticas de código
- `E` pycodestyle: erros de estilo de código
- `W` pycodestyle: avisos sobre estilo de código
- `PL`Pylint: "erros" em relação a boas práticas de código
- `PT`flake8-pytest: boas práticas do Pytest

```
[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']
```

## Formatter do ruff
```
[tool.ruff.format]
preview = true
quote-style = 'single
```

# Pytest
- Poetry:

```
poetry add --group dev pytest pytest-cov

[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'
```

- Stmts = statements = linhas com código
- Todo arquivo de teste deve começar com "test_" para o pytest reconhecer
- Teste é composto de 3 (ou 4) etapas importantes - triple A:
    - Organizar (Arrange)
    - Agir (Act)
    - Afirmat (Assert)
    - teardown - desorganizar para executar próximo teste

# Taskipy
```
poetry add --group dev taskipy
```

# ignr
```
ignr -p python > .gitignore
```

# gh
```
git init .

git add .

git commit -m "1st commit"

gh repo create

git remote add origin https://github.com/laranapoli/fast_zero.git
```

# DESENVOLVIMENTO WEB

## Cliente-Servidor
- Formato mais importante é cliente-servidor.
    - Relação entre 3 componentes: Cliente <-> Servidor <-> Aplicação Python

## Uvicorn
- Servidor de aplicação (trabalha em uma camada diferente da do servidor web)
- Padrão python: ASGI - Asynchronous Server Gateway Interface
    - WSGI: Web server gateway interface (padrão antigo)
- Em produção seria usado um servidor web na frente do uvicorn (apache ou nginx...)
- É possível usar outro além do uvicorn (de acordo com necessidades do projeto)
- FastApi NÃO sabe nada sobre HTTP

## A rede local
- Loopback: Nosso computador é o cliente e o servidor ao mesmo tempo.
- `127.0.0.1` = endereço especial da nossa porta de loopback (quando falamos com nosso próprio PC)
- O comando abaizo abre o servidor do `uvicorn` para a rede local (basta saber o endereço da sua máquina)
```
fastapi dev fast_zero/app.py --host 0.0.0.0
```

> Para acessar, basta chamar http://seu_ip:8000

## O modelo padrão da web

- Web => URL | HTTP | HTML
- URL: Localizador uniforme de recursos = Endereço de rede pelo qual podemos nos comunicar com um computador na rede.
- HTTP: Protocolo que especifica como deve ocorrer a comunicação
    - Baseia-se no envio e recebimento de mensagens
- HTML: Linguagem usada para criar e estruturar páginas na web

### HTTP - Cabeçalho
Contém metadados sobre a requisição ou resposta:
- Content-Type: O tipo de mídia no corpo da mensagem
- Authorization: Para autenticação com tokens ou credenciais
- Accept: Tipo de mídia que o cliente aceita
- Server: Informações sobre o software do servidor

### HTTP - Verbos
Quando um cliente faz uma requisição HTTP, ele indica sua intenção ao servidor com verbos:
- GET: Recuperação de recursos - Quando queremos solicitar um dado já existente no servidor.
- POST: Criar novo recurso. Ex.: Enviar dados para registrar novo usuário.
- PUT: Atualiza recurso já existente. Ex.: Atualizar cadastro.
- DELETE: Exclui um recurso.

> Obs.: verbos fazem parte do cabeçalho

### HTTP - Códigos de resposta
- 1xx: informativo - para enviar infos ao cliente de que a requisição foi recebida e está sendo processada.
- 2xx sucesso - requisição bem sucedida (200 = ok, 201 = created)
- 3xx redirecionamento - informa que mais ações são necessárias para completar a requisição (ex.: 301 = moved permanently | 302 = found)
- 4xx erro no cliente - erro na requisição feita pelo cliente (ex.: 400 = bad request | 404 = not found)
- 5xx erro no servidor - erro ao processar requisição válida (ex.:  = internal server error, 503 = service unavailable)

#### Código importantes para o curso
- 200 OK: Solicitação bem-sucedida.
- 201 Created: solicitação bem-sucedida e novo recurso criado como resultado.
- 404 Not found: recurso solicitado não pôde sr encontrado.
- 422 Unprocessable entity: usado quando a requisição está bem formada, mas não pode ser seguida devido a erros semânticos (comum em APIs ao validar dados de entrada)
- 500 Internal server error: quando existe um erro na nossa aplicação!

> Obs.: Por padrão, o FastAPI sempre retorna 200. Do post é 201.

## HTML - Hypertext Markup Language
Linguagem de marcação padrão usada para criar e estruturar páginas na internet.

## API - Application Programming Interface
- APIs modernas usam JSON para comunicação
- JSON é um formato leve de troca de dados
- Fácil de ler e escrever para humanos e simples de interpretar e gerar para máquinas.
- APIs REST retornam HTML. API que retorna JSON é uma API "moderna".

## Contratos
Como o JSON oferece esse formato estruturados, podemos definir um contrato (schema).

## Pydantic
- Como o uvicorn, já vem embutido no fastapi.
- Ideia: Criar camada de documentação (via OpenAPI) e fazer validação dos modelos de entrada e saída da API.

# Aula 03 - CRUD

- CRUD: Create, read, update, delete
- Manipular recursos
- CRATE: POST - Status CREATED
- O passando como response_model uma classe criada com BaseModel do pydantic, FILTRAMOS o que é retornado, mesmo quando retornamos mais campos. Há uma validação!
- Quando nós passamos chaves na url, vira uma variável!
- De dentro do fastapi é que extraímos HTTPException (tratamento de erros)
- Assistir:
    - https://www.youtube.com/watch?v=t4C1c62Z4Ag
    - https://www.youtube.com/watch?v=yQtqkq9UkDA