# Gest-o-de-Consumo-de-Internet


Sistema de simulação e análise de consumo de dados em Python que gera clientes aleatórios, registra consumo diário em JSON e CSV e produz relatórios automáticos. Identifica usuários com consumo acima de 5GB, calcula consumo mínimo, médio e máximo e gera logs de execução, simulando monitoramento básico de telecomunicações.

---

# 📘 README – Sistema de Monitoramento de Consumo de Dados

## 📖 Sobre o Projeto

Este projeto simula um sistema de monitoramento de consumo de dados móveis. Ele gera clientes automaticamente, atribui consumos diários aleatórios e armazena as informações em ficheiros JSON e CSV.

O sistema também identifica usuários com consumo superior a **5GB (5120MB)** e gera relatórios estatísticos.

> OBS: Caso fosse utilizada uma base de dados (ex: SQLite ou MySQL), não seria necessário manter dados diretamente no código.

---

## ⚙️ Funcionalidades

* ✅ Geração automática de clientes
* ✅ Consumo diário aleatório (MB)
* ✅ Armazenamento em JSON e CSV
* ✅ Cálculo de consumo mínimo, médio e máximo
* ✅ Registro de usuários com consumo acima de 5GB
* ✅ Geração de logs de execução

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* CSV
* datetime
* random

---

## 📂 Estrutura de Ficheiros

```
dados/
   ├── dados.json
   └── dados.csv

logs/
   ├── consumo.txt
   ├── consumo_acima_5GB.txt
   └── logs.txt
```

---

## 📊 Relatórios Gerados

### consumo.txt

* Consumo mínimo diário
* Consumo médio diário
* Consumo máximo diário

### consumo_acima_5GB.txt

* Lista de usuários com consumo superior a 5GB

---

## 🚀 Como Executar

```bash
python nome_do_arquivo.py
```

O sistema irá gerar automaticamente os dados e relatórios.

---


