# 📋 Estrutura do Projeto SeuEmprego.com

## 📁 Estrutura de Diretórios

```
seuemprego/
│
├── main.py                 # Arquivo principal do Flask
├── database.py             # Configuração do banco de dados
├── models.py               # Modelos SQLAlchemy
├── migrate_and_seed.py     # Script de migração e carga de dados
│
├── templates/              # Templates HTML
│   ├── index.html         # Página principal
│   ├── nova_vaga.html     # Formulário de nova vaga
│   └── detalhes_vaga.html # Detalhes da vaga
│
└── data/                   # Pasta para o banco de dados
    └── seuemprego.db      # Banco SQLite (criado automaticamente)
```

## 🚀 Como Executar o Projeto

### 1. Instalar Dependências

```bash
pip install flask sqlalchemy
```

### 2. Criar a Estrutura de Pastas

Certifique-se de criar a pasta `templates`:

```bash
mkdir templates
```

A pasta `data/` será criada automaticamente ao executar o projeto.

### 3. Executar o Servidor

```bash
python main.py
```

O servidor estará disponível em: **http://localhost:5000**

### 4. (Opcional) Popular o Banco com Dados de Teste

Para facilitar o desenvolvimento e testes, execute o script de migração:

```bash
python migrate_and_seed.py
```

Este script irá:
- Limpar o banco de dados existente
- Recriar todas as tabelas
- Inserir 10 vagas de teste variadas
- Exibir estatísticas dos dados inseridos

**⚠️ ATENÇÃO**: Este script apaga todos os dados existentes! Use apenas em ambiente de desenvolvimento.

## ✨ Funcionalidades Implementadas

### Página Principal (index.html)
- ✅ Título do site "SeuEmprego.com"
- ✅ Botão para adicionar nova vaga
- ✅ Lista de vagas disponíveis
- ✅ Cards com informações resumidas de cada vaga
- ✅ Badges coloridos para tipo de trabalho (Remoto/Híbrido/Presencial)
- ✅ Link para ver detalhes de cada vaga
- ✅ Botão flutuante para voltar ao topo (aparece ao rolar a página)

### Formulário de Nova Vaga (nova_vaga.html)
- ✅ Todos os campos do modelo de dados
- ✅ Campos obrigatórios marcados
- ✅ Seleção dropdown para regime e forma de trabalho
- ✅ Validação HTML5
- ✅ Design responsivo

### Detalhes da Vaga (detalhes_vaga.html)
- ✅ Visualização completa de todas as informações
- ✅ Design organizado com seções
- ✅ Cards de informação destacados
- ✅ Botão para voltar à página principal
- ✅ Botão flutuante para voltar ao topo
- ✅ Data de publicação

## 🎨 Design

O projeto usa:
- **Cores principais**: Preto (#1a1a1a) e Laranja Escuro (#ff6b35)
- **Gradiente escuro** no cabeçalho com borda laranja
- **Cards brancos** com sombras suaves
- **Badges coloridos** para categorização
- **Design responsivo** para mobile
- **Transições suaves** em hover
- **Ícones emoji** para melhor UX
- **Botão flutuante** para voltar ao topo nas páginas

## 🔧 Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página principal com lista de vagas |
| `/nova-vaga` | GET | Formulário para adicionar vaga |
| `/adicionar-vaga` | POST | Processa e salva nova vaga |
| `/vaga/<id>` | GET | Detalhes de uma vaga específica |

## 🗄️ Script de Migração e Dados de Teste

O arquivo `migrate_and_seed.py` contém:

### Funcionalidades
- **limpar_banco()**: Remove todas as tabelas existentes
- **criar_banco()**: Cria todas as tabelas do modelo
- **gerar_vagas_teste()**: Define 10 vagas variadas para teste
- **inserir_vagas()**: Insere as vagas no banco com datas variadas
- **verificar_dados()**: Exibe estatísticas dos dados inseridos

### Vagas de Teste Incluídas
1. Desenvolvedor Python Full Stack (Remoto)
2. Designer UX/UI Sênior (Híbrido)
3. Analista de Dados Júnior (Presencial)
4. Gerente de Projetos de TI (Híbrido)
5. Estágio em Desenvolvimento Web (Híbrido)
6. Especialista em Segurança da Informação (Remoto)
7. Desenvolvedor Mobile React Native (Remoto)
8. Analista de Suporte Técnico (Presencial)
9. Engenheiro de Machine Learning (Remoto)
10. Scrum Master (Híbrido)

Cada vaga contém informações completas e realistas para facilitar testes da interface.

## 📝 Próximos Passos (Sugestões)

- [ ] Sistema de busca/filtro de vagas
- [ ] Edição de vagas
- [ ] Paginação para muitas vagas
- [ ] Upload de logo da empresa
- [ ] Sistema de candidaturas
- [ ] Painel administrativo
- [ ] API REST
- [ ] Autenticação de usuários

## 🐛 Troubleshooting

**Erro: "No module named 'flask'"**
```bash
pip install flask sqlalchemy
```

**Erro: "templates/index.html not found"**
- Certifique-se de criar a pasta `templates/`
- Verifique se os arquivos HTML estão dentro dela

**Erro de banco de dados**
- Delete a pasta `data/` e execute novamente
- O banco será recriado automaticamente