# dio-twitter-py

Projeto criado durante o living code [Consumindo a API do Twitter com Python](https://docs.google.com/presentation/d/11DkkyQUIloVQLm8i6hN6w3xyUaP4WSRE/edit?usp=sharing&ouid=102662434190974209165&rtpof=true&sd=true).

## Tecnologias

- Python 3.8.x
- FastAPI
- MongoDB

## Requisitos

- Docker
- Docker compose

## Instalação

Instale o [Docker](https://www.docker.com) e [Docker compose](https://docs.docker.com/compose/) no seu computador.

## Rodando a aplicação

```sh
poetry shell
python main.py
```

Acesso o [Swagger UI](http://localhost:8000/docs) para listar todos os endpoints.

Use `Ctrl+C` para finalizar o processo servidor.

## Rodando os testes

```sh
poetry shell
pytest
```

## Desafio proposto

- Containerizar a aplicação com Docker e modularizar a aplicação.
- Criar relatórios/dashboards para exibir de forma mais amigável os dados coletados via Twitter API.
