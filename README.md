# 🔄 Script de Migração e Carga de Dados

## 📖 Sobre

O arquivo `migrate_and_seed.py` é um script utilitário para reinicializar o banco de dados e popular com dados de teste. É especialmente útil durante o desenvolvimento para ter um ambiente consistente de testes.

## ⚙️ Como Usar

### Execução Básica

```bash
python migrate_and_seed.py
```

### O que o script faz?

1. **Solicita confirmação** - Avisa que todos os dados serão apagados
2. **Remove tabelas antigas** - Limpa o banco de dados completamente
3. **Cria novas tabelas** - Recria a estrutura conforme models.py
4. **Insere vagas de teste** - Adiciona 10 vagas variadas
5. **Exibe estatísticas** - Mostra resumo dos dados inseridos

## 📊 Exemplo de Saída

```
============================================================
SCRIPT DE MIGRAÇÃO E CARGA DE DADOS
SeuEmprego.com
============================================================

Este script irá APAGAR todos os dados existentes. Continuar? (s/n): s

Iniciando migração...

Removendo tabelas antigas...
✓ Tabelas removidas
Criando novas tabelas...
✓ Tabelas criadas

Inserindo 10 vagas de teste...
  1. Desenvolvedor Python Full Stack - ✓
  2. Designer UX/UI Sênior - ✓
  3. Analista de Dados Júnior - ✓
  4. Gerente de Projetos de TI - ✓
  5. Estágio em Desenvolvimento Web - ✓
  6. Especialista em Segurança da Informação - ✓
  7. Desenvolvedor Mobile React Native - ✓
  8. Analista de Suporte Técnico - ✓
  9. Engenheiro de Machine Learning - ✓
  10. Scrum Master - ✓

✓ 10 vagas inseridas com sucesso!

============================================================
ESTATÍSTICAS DO BANCO DE DADOS
============================================================
Total de vagas: 10
  - Remotas: 4
  - Híbridas: 4
  - Presenciais: 2
============================================================

✓ Migração concluída com sucesso!

Você pode agora executar o servidor Flask com: python main.py
```

## 🎯 Casos de Uso

### 1. Desenvolvimento Inicial
Quando você está começando o projeto e quer ter dados para visualizar:
```bash
python migrate_and_seed.py
python main.py
```

### 2. Reset do Ambiente
Quando o banco está com dados inconsistentes ou você quer recomeçar:
```bash
python migrate_and_seed.py
```

### 3. Testes de Interface
Para testar como a interface se comporta com vários tipos de vagas:
- Vagas remotas, híbridas e presenciais
- Diferentes regimes de contratação (CLT, PJ, Estágio)
- Variação de salários e benefícios
- Datas de publicação distribuídas nos últimos 30 dias

## 📝 Vagas Incluídas no Script

O script insere 10 vagas de teste cobrindo diversos cenários:

| # | Vaga | Regime | Modalidade | Localização |
|---|------|--------|------------|-------------|
| 1 | Desenvolvedor Python Full Stack | CLT | Remoto | São Paulo - SP |
| 2 | Designer UX/UI Sênior | PJ | Híbrido | Rio de Janeiro - RJ |
| 3 | Analista de Dados Júnior | CLT | Presencial | Belo Horizonte - MG |
| 4 | Gerente de Projetos de TI | CLT | Híbrido | São Paulo - SP |
| 5 | Estágio em Desenvolvimento Web | Estágio | Híbrido | Curitiba - PR |
| 6 | Especialista em Segurança | CLT | Remoto | Todo o Brasil |
| 7 | Desenvolvedor Mobile React Native | PJ | Remoto | Remoto |
| 8 | Analista de Suporte Técnico | CLT | Presencial | Porto Alegre - RS |
| 9 | Engenheiro de Machine Learning | CLT | Remoto | Brasil |
| 10 | Scrum Master | CLT | Híbrido | Florianópolis - SC |

## ⚠️ Avisos Importantes

### 🔴 ATENÇÃO - Perda de Dados
- Este script **APAGA TODOS OS DADOS** do banco
- Use apenas em **ambiente de desenvolvimento**
- **NUNCA** execute em produção
- Sempre faça backup antes se tiver dados importantes

### ✅ Boas Práticas
- Execute após mudanças no `models.py` para atualizar o schema
- Use para demonstrações e testes
- Mantenha o script atualizado conforme o modelo evolui

## 🔧 Personalização

### Adicionar Mais Vagas

Edite a função `gerar_vagas_teste()` em `migrate_and_seed.py`:

```python
def gerar_vagas_teste():
    vagas_teste = [
        {
            'titulo_vaga': 'Sua Nova Vaga',
            'cargo': 'Cargo Desejado',
            # ... outros campos
        },
        # Adicione mais vagas aqui
    ]
    return vagas_teste
```

### Modificar Datas

Por padrão, as vagas são criadas com datas aleatórias nos últimos 30 dias. Para mudar:

```python
# Em inserir_vagas()
dias_atras = random.randint(0, 30)  # Modifique o range aqui
```

## 🐛 Troubleshooting

**Erro: "No module named 'database'"**
- Certifique-se de estar no diretório correto do projeto
- Verifique se `database.py` e `models.py` existem

**Erro: "Permission denied" no SQLite**
- Feche o servidor Flask (`python main.py`) antes de executar a migração
- Certifique-se de ter permissões de escrita na pasta `data/`

**Script não encontra o banco**
- O script cria automaticamente a pasta `data/` e o arquivo do banco
- Não precisa criar nada manualmente

## 💡 Dica

Para um reset rápido durante desenvolvimento, crie um alias no terminal:

**Linux/Mac:**
```bash
echo "alias reset-db='python migrate_and_seed.py'" >> ~/.bashrc
source ~/.bashrc
```

**Windows (PowerShell):**
```powershell
Set-Alias reset-db "python migrate_and_seed.py"
```

Depois, basta executar:
```bash
reset-db
```