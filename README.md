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
gh repo create
```