# Backend do Sistema de Gerenciamento de Processos de Esterilização

## Descrição

Este projeto é o backend de um sistema de gerenciamento de processos de esterilização, desenvolvido para facilitar o controle das etapas de esterilização de materiais em um hospital.

## Funcionalidades

- **Cadastro de Materiais**:
  - Nome do material
  - Tipo do material (cirúrgico, descartável etc.)
  - Data de validade
- **Cadastro de Usuários**:
  - Usuário Técnico: Responsável por realizar as etapas do processo.
  - Usuário Enfermagem: Responsável por verificar a rastreabilidade do processo, consultar as falhas e relatórios.
- **Gerenciamento de Etapas**:
  - Recebimento
  - Lavagem
  - Esterilização
  - Distribuição
- **Relatórios**:
  - Geração de relatório em PDF de materiais que concluíram o processo.
  - Geração de relatório de falhas em XLSX.

## Estrutura de Pastas

backend/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── auth.py
│ ├── reports.py
├── migrations/
├── config.py
├── run.py
├── venv/
├── requirements.txt




