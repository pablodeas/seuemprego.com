from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class Vagas(Base):
    __tablename__ = 'vagas'

    id = Column(Integer, primary_key=True)
    
    titulo_vaga = Column(String(200), nullable=False)
    cargo = Column(String(100), nullable=False)
    regime_contratacao = Column(String(50), nullable=True)  # CLT, PJ, Estágio, etc.
    numero_vagas = Column(Integer, default=1)
    descricao = Column(Text, nullable=True)
    experiencia_desejada = Column(String(200), nullable=True)
    forma_trabalho = Column(String(50), nullable=True)  # Presencial, Remoto, Híbrido
    local = Column(String(200), nullable=True)
    beneficios = Column(Text, nullable=True)
    expediente = Column(String(100), nullable=True)  # Ex: Segunda a Sexta, 8h às 18h
    salario = Column(String(100), nullable=True)
    como_candidatar = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)