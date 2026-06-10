# Hub de Mapeamento e Diagnóstico

Sistema web desenvolvido para digitalizar processos de atendimento, levantamento de necessidades e geração de relatórios de diagnóstico.

A aplicação foi projetada para substituir fluxos baseados em anotações manuais, permitindo registrar clientes, documentar atendimentos, organizar informações estratégicas e gerar relatórios de forma estruturada.

## Principais Funcionalidades

* Cadastro de clientes
* Registro de atendimentos
* Histórico de atendimentos por cliente
* Classificação automática de diagnósticos
* Dashboard com indicadores gerais
* Relatórios dinâmicos
* Exportação de relatórios em PDF

## Arquitetura

O projeto foi desenvolvido seguindo uma arquitetura modular baseada em separação de responsabilidades:

```text
models/
routes/
services/
templates/
static/
```

Essa estrutura facilita a manutenção, evolução e escalabilidade da aplicação.

## Tecnologias Utilizadas

### Backend

* Python
* Flask
* SQLAlchemy
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Relatórios

* ReportLab

## Objetivo

Centralizar informações de atendimento em um único ambiente digital, permitindo registrar demandas, organizar diagnósticos e gerar documentação de apoio para processos de análise e tomada de decisão.

## Evoluções Futuras

* Trilhas de diagnóstico e recomendação
* Melhorias de experiência do usuário (UX/UI)
* Responsividade para dispositivos móveis
* Integração com PostgreSQL
* Containerização com Docker
* Novos relatórios e indicadores
