#!/usr/bin/env python3

"""
Script de Migração e Carga de Dados de Teste
Projeto: seuemprego.com
"""

from database import Session, init_db, engine
from models import Vagas, Base
from datetime import datetime, timedelta
import random


def limpar_banco():
    """Remove todas as tabelas existentes"""
    print("Removendo tabelas antigas...")
    Base.metadata.drop_all(engine)
    print("✓ Tabelas removidas")


def criar_banco():
    """Cria todas as tabelas do banco"""
    print("Criando novas tabelas...")
    init_db()
    print("✓ Tabelas criadas")


def gerar_vagas_teste():
    """Gera vagas de teste para popular o banco de dados"""
    
    vagas_teste = [
        {
            'titulo_vaga': 'Desenvolvedor Python Full Stack',
            'cargo': 'Desenvolvedor Full Stack',
            'regime_contratacao': 'CLT',
            'numero_vagas': 2,
            'descricao': '''Buscamos desenvolvedor Python com experiência em Flask/Django para 
atuar no desenvolvimento de aplicações web robustas e escaláveis. 

Responsabilidades:
- Desenvolvimento de APIs RESTful
- Integração com bancos de dados SQL e NoSQL
- Implementação de testes automatizados
- Participação em code reviews
- Trabalho em equipe ágil (Scrum)''',
            'experiencia_desejada': 'Mínimo 3 anos de experiência com Python e frameworks web',
            'forma_trabalho': 'Remoto',
            'local': 'São Paulo - SP (Remoto)',
            'beneficios': '''- Vale-refeição de R$ 30/dia
- Vale-transporte
- Plano de saúde Unimed
- Plano odontológico
- Auxílio home office R$ 200/mês
- Day off no aniversário''',
            'expediente': 'Segunda a Sexta, 9h às 18h (flexível)',
            'salario': 'R$ 8.000,00 - R$ 12.000,00',
            'como_candidatar': 'Envie seu currículo e portfólio para vagas@empresa.com.br com o assunto "Vaga Python Full Stack"'
        },
        {
            'titulo_vaga': 'Designer UX/UI Sênior',
            'cargo': 'Designer UX/UI',
            'regime_contratacao': 'PJ',
            'numero_vagas': 1,
            'descricao': '''Procuramos designer criativo e experiente para criar experiências 
digitais incríveis para nossos produtos.

Atividades:
- Criação de wireframes e protótipos
- Design de interfaces web e mobile
- Pesquisa com usuários
- Testes de usabilidade
- Manutenção de design system''',
            'experiencia_desejada': 'Experiência sólida com Figma, Adobe XD e ferramentas de prototipagem',
            'forma_trabalho': 'Híbrido',
            'local': 'Rio de Janeiro - RJ',
            'beneficios': '''- Horário flexível
- Equipamento fornecido (MacBook Pro)
- Budget para cursos e eventos
- Coworking pago pela empresa''',
            'expediente': 'Flexível, com 2 dias presenciais por semana',
            'salario': 'R$ 10.000,00 - R$ 15.000,00',
            'como_candidatar': 'Preencha o formulário em nosso site: www.empresa.com.br/carreiras'
        },
        {
            'titulo_vaga': 'Analista de Dados Júnior',
            'cargo': 'Analista de Dados',
            'regime_contratacao': 'CLT',
            'numero_vagas': 3,
            'descricao': '''Oportunidade para iniciar carreira em análise de dados em uma 
startup em crescimento.

O que você vai fazer:
- Coleta e análise de dados
- Criação de dashboards no Power BI
- Geração de relatórios gerenciais
- Suporte às áreas de negócio''',
            'experiencia_desejada': 'Excel avançado, SQL básico, conhecimento em Power BI é um diferencial',
            'forma_trabalho': 'Presencial',
            'local': 'Belo Horizonte - MG',
            'beneficios': '''- Vale-refeição
- Vale-transporte
- Convênio com academias
- Plano de saúde após experiência
- Programa de treinamento''',
            'expediente': 'Segunda a Sexta, 8h às 17h',
            'salario': 'R$ 3.500,00 - R$ 5.000,00',
            'como_candidatar': 'Candidate-se através do LinkedIn ou envie currículo para rh@startup.com.br'
        },
        {
            'titulo_vaga': 'Gerente de Projetos de TI',
            'cargo': 'Gerente de Projetos',
            'regime_contratacao': 'CLT',
            'numero_vagas': 1,
            'descricao': '''Buscamos profissional experiente para liderar projetos de tecnologia 
de alta complexidade.

Atribuições:
- Gestão de múltiplos projetos simultâneos
- Coordenação de equipes multidisciplinares
- Relacionamento com stakeholders
- Gestão de orçamento e cronograma
- Mitigação de riscos''',
            'experiencia_desejada': 'Certificação PMP ou equivalente, mínimo 5 anos gerenciando projetos de TI',
            'forma_trabalho': 'Híbrido',
            'local': 'São Paulo - SP',
            'beneficios': '''- Salário compatível com o mercado
- Bônus anual por performance
- Plano de saúde premium
- Previdência privada
- Carro da empresa
- Notebook e celular''',
            'expediente': 'Comercial com flexibilidade',
            'salario': 'R$ 15.000,00 - R$ 20.000,00',
            'como_candidatar': 'Envie seu currículo com carta de apresentação para gerencia@empresa.com.br'
        },
        {
            'titulo_vaga': 'Estágio em Desenvolvimento Web',
            'cargo': 'Estagiário de Desenvolvimento',
            'regime_contratacao': 'Estágio',
            'numero_vagas': 5,
            'descricao': '''Programa de estágio para estudantes de Ciência da Computação, 
Sistemas de Informação ou áreas correlatas.

Você vai aprender:
- HTML, CSS e JavaScript
- Frameworks modernos (React, Vue)
- Git e versionamento de código
- Metodologias ágeis
- Trabalho em equipe''',
            'experiencia_desejada': 'Cursando superior em TI (a partir do 3º semestre), conhecimentos básicos de programação',
            'forma_trabalho': 'Híbrido',
            'local': 'Curitiba - PR',
            'beneficios': '''- Bolsa auxílio compatível
- Vale-transporte
- Vale-refeição
- Seguro de vida
- Possibilidade de efetivação
- Mentoria com desenvolvedores sêniores''',
            'expediente': '6 horas diárias (flexível com horário da faculdade)',
            'salario': 'R$ 1.800,00',
            'como_candidatar': 'Inscreva-se em www.empresa.com.br/programa-estagio até 31/12/2024'
        },
        {
            'titulo_vaga': 'Especialista em Segurança da Informação',
            'cargo': 'Analista de Segurança',
            'regime_contratacao': 'CLT',
            'numero_vagas': 1,
            'descricao': '''Profissional para atuar na proteção de ativos digitais e conformidade 
com padrões de segurança.

Principais atividades:
- Análise de vulnerabilidades
- Implementação de políticas de segurança
- Resposta a incidentes
- Auditorias de segurança
- Treinamento de equipes''',
            'experiencia_desejada': 'Certificações como CEH, CISSP ou Security+, experiência com SIEM e ferramentas de segurança',
            'forma_trabalho': 'Remoto',
            'local': 'Todo o Brasil',
            'beneficios': '''- Home office 100%
- Auxílio internet e energia
- Equipamentos de trabalho
- Plano de saúde nacional
- Budget para certificações
- Participação em eventos internacionais''',
            'expediente': 'Flexível (plantões eventuais)',
            'salario': 'R$ 12.000,00 - R$ 18.000,00',
            'como_candidatar': 'Candidate-se através da plataforma Gupy: empresa.gupy.io'
        },
        {
            'titulo_vaga': 'Desenvolvedor Mobile React Native',
            'cargo': 'Desenvolvedor Mobile',
            'regime_contratacao': 'PJ',
            'numero_vagas': 2,
            'descricao': '''Desenvolvedor mobile para atuar em projetos de aplicativos iOS e Android 
usando React Native.

Stack principal:
- React Native
- TypeScript
- Redux/Context API
- APIs REST
- Firebase''',
            'experiencia_desejada': '2+ anos com React Native, experiência com publicação nas stores',
            'forma_trabalho': 'Remoto',
            'local': 'Remoto - Qualquer lugar do Brasil',
            'beneficios': '''- Contrato PJ com pagamento mensal
- Projetos desafiadores
- Equipe internacional
- Inglês no dia a dia (oportunidade de praticar)''',
            'expediente': 'Flexível',
            'salario': 'R$ 9.000,00 - R$ 13.000,00',
            'como_candidatar': 'Envie seu GitHub e LinkedIn para tech@company.com'
        },
        {
            'titulo_vaga': 'Analista de Suporte Técnico',
            'cargo': 'Analista de Suporte',
            'regime_contratacao': 'CLT',
            'numero_vagas': 4,
            'descricao': '''Atendimento de primeiro e segundo nível para suporte técnico de sistemas 
corporativos.

Responsabilidades:
- Atendimento via telefone, chat e e-mail
- Resolução de problemas técnicos
- Abertura e acompanhamento de chamados
- Documentação de soluções
- Treinamento de usuários''',
            'experiencia_desejada': 'Experiência em suporte técnico, conhecimento de sistemas Windows e Linux',
            'forma_trabalho': 'Presencial',
            'local': 'Porto Alegre - RS',
            'beneficios': '''- Vale-refeição
- Vale-transporte
- Plano de saúde
- Plano odontológico
- Gympass
- PLR''',
            'expediente': 'Escala 6x1, horário comercial',
            'salario': 'R$ 3.000,00 - R$ 4.500,00',
            'como_candidatar': 'Envie currículo para selecao@empresa.com.br com assunto "Suporte Técnico"'
        },
        {
            'titulo_vaga': 'Engenheiro de Machine Learning',
            'cargo': 'Engenheiro de ML',
            'regime_contratacao': 'CLT',
            'numero_vagas': 1,
            'descricao': '''Profissional para desenvolver e implementar modelos de Machine Learning 
em ambiente de produção.

Desafios:
- Desenvolvimento de modelos preditivos
- Deploy de modelos em produção
- Otimização de performance
- MLOps e monitoramento
- Pesquisa aplicada''',
            'experiencia_desejada': 'Mestrado ou experiência equivalente, domínio de Python, TensorFlow/PyTorch, conhecimento em cloud (AWS/GCP)',
            'forma_trabalho': 'Remoto',
            'local': 'Brasil (Remoto)',
            'beneficios': '''- Salário competitivo
- Stock options
- Budget ilimitado para cursos
- Conferências internacionais
- Equipamento top de linha
- Ambiente inovador''',
            'expediente': 'Totalmente flexível',
            'salario': 'R$ 18.000,00 - R$ 25.000,00',
            'como_candidatar': 'Aplique via LinkedIn ou envie CV + papers/projetos para ai@techcompany.com'
        },
        {
            'titulo_vaga': 'Scrum Master',
            'cargo': 'Scrum Master',
            'regime_contratacao': 'CLT',
            'numero_vagas': 2,
            'descricao': '''Facilitador ágil para times de desenvolvimento de produto digital.

Você vai:
- Facilitar cerimônias Scrum
- Remover impedimentos
- Coaching do time
- Promover melhoria contínua
- Trabalhar com múltiplos times''',
            'experiencia_desejada': 'Certificação CSM ou PSM, experiência prévia como Scrum Master',
            'forma_trabalho': 'Híbrido',
            'local': 'Florianópolis - SC',
            'beneficios': '''- Vale-refeição
- Plano de saúde
- Auxílio educação
- Ambiente descontraído
- Frutas e café à vontade
- Happy hour mensal''',
            'expediente': 'Segunda a Sexta, horário flexível',
            'salario': 'R$ 7.000,00 - R$ 10.000,00',
            'como_candidatar': 'Candidate-se em www.empresa.com.br/carreiras/scrum-master'
        }
    ]
    
    return vagas_teste


def inserir_vagas(vagas_teste):
    """Insere as vagas de teste no banco de dados"""
    session = Session()
    try:
        print(f"\nInserindo {len(vagas_teste)} vagas de teste...")
        
        for i, vaga_data in enumerate(vagas_teste, 1):
            # Varia a data de criação para simular vagas de períodos diferentes
            dias_atras = random.randint(0, 30)
            data_criacao = datetime.now() - timedelta(days=dias_atras)
            
            vaga = Vagas(
                titulo_vaga=vaga_data['titulo_vaga'],
                cargo=vaga_data['cargo'],
                regime_contratacao=vaga_data['regime_contratacao'],
                numero_vagas=vaga_data['numero_vagas'],
                descricao=vaga_data['descricao'],
                experiencia_desejada=vaga_data['experiencia_desejada'],
                forma_trabalho=vaga_data['forma_trabalho'],
                local=vaga_data['local'],
                beneficios=vaga_data['beneficios'],
                expediente=vaga_data['expediente'],
                salario=vaga_data['salario'],
                como_candidatar=vaga_data['como_candidatar'],
                created_at=data_criacao
            )
            session.add(vaga)
            print(f"  {i}. {vaga_data['titulo_vaga']} - ✓")
        
        session.commit()
        print(f"\n✓ {len(vagas_teste)} vagas inseridas com sucesso!")
        
    except Exception as e:
        session.rollback()
        print(f"\n✗ Erro ao inserir vagas: {e}")
    finally:
        session.close()


def verificar_dados():
    """Verifica e exibe estatísticas dos dados inseridos"""
    session = Session()
    try:
        total_vagas = session.query(Vagas).count()
        vagas_remotas = session.query(Vagas).filter(Vagas.forma_trabalho == 'Remoto').count()
        vagas_hibridas = session.query(Vagas).filter(Vagas.forma_trabalho == 'Híbrido').count()
        vagas_presenciais = session.query(Vagas).filter(Vagas.forma_trabalho == 'Presencial').count()
        
        print("\n" + "="*60)
        print("ESTATÍSTICAS DO BANCO DE DADOS")
        print("="*60)
        print(f"Total de vagas: {total_vagas}")
        print(f"  - Remotas: {vagas_remotas}")
        print(f"  - Híbridas: {vagas_hibridas}")
        print(f"  - Presenciais: {vagas_presenciais}")
        print("="*60)
        
    finally:
        session.close()


def main():
    """Função principal do script de migração"""
    print("\n" + "="*60)
    print("SCRIPT DE MIGRAÇÃO E CARGA DE DADOS")
    print("SeuEmprego.com")
    print("="*60 + "\n")
    
    print("Escolha a opção:")
    print("1. Apagar todos os dados")
    print("2. Migração completa (apaga e recria com dados de teste)")
    print("0. Cancelar")
    
    opt = input("\n-> ")
    
    if opt == "1":
        resposta = input("\n⚠️  Tem certeza que deseja APAGAR todos os dados? (s/n): ")
        if resposta.lower() == 's':
            print("\nApagando todos os dados...")
            try:
                limpar_banco()
                criar_banco()
                print("\n✓ Banco de dados limpo com sucesso!")
                print("O banco foi recriado vazio, sem nenhuma vaga.\n")
            except Exception as e:
                print(f"\n✗ Erro ao deletar os dados: {e}")
        else:
            print("\nOperação cancelada.")
    
    elif opt == "2":
        resposta = input("\n⚠️  Este script irá APAGAR todos os dados existentes. Continuar? (s/n): ")
        if resposta.lower() == 's':
            print("\nIniciando migração...\n")
            try:
                # Executa as etapas da migração
                limpar_banco()
                criar_banco()
                
                vagas_teste = gerar_vagas_teste()
                inserir_vagas(vagas_teste)
                
                verificar_dados()
                
                print("\n✓ Migração concluída com sucesso!")
                print("\nVocê pode agora executar o servidor Flask com: python main.py\n")
            except Exception as e:
                print(f"\n✗ Erro na migração: {e}")
        else:
            print("\nOperação cancelada.")
    
    elif opt == "0":
        print("\nOperação cancelada pelo usuário.\n")
    
    else:
        print("\n✗ Opção inválida! Execute o script novamente.\n")


if __name__ == "__main__":
    main()