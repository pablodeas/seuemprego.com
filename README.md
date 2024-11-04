# seuemprego.com

### Live
A produção do projeto será feito na plataforma [PythonAnywhere](https://pythonanywhere.com/)

Para funcionar, necessário instalar:
- docker >= 27.2
- python3 >= 3.10

Para iniciar o PostgreSQL:
```bash
docker compose build && docker compose up -d
```

Caso esteja recebendo algum erro de permissão ao tentar executar o Docker, acrescente o grupo Docker ao seu usuário:
```bash
# Verificar o usuário atual
echo $USER
# Adiciona o grupo Docker ao seu usuário atual
sudo usermod -aG docker $USER
# Registra a mudança
newgrp docker
# Verificar se funcionou
docker ps -a
```

A utilização do banco de dados está sendo automatizada no arquivo source.py.

O arquivo migrations.sql é o principal para mudanças na produção.

---

Leituras Relevantes:

[psql-basico](https://hasura.io/blog/top-psql-commands-and-flags-you-need-to-know-postgresql)
[psycopg2-docs](https://www.psycopg.org/docs/usage.html#)