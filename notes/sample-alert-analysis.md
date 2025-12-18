# 📄 sample-alert-analysis.md

## 🚨 Sample Alert Analysis

Este documento simula a **análise básica de um alerta em um SOC**, com foco em raciocínio, validação e documentação. O objetivo é demonstrar **processo**, não ferramentas avançadas.

---

### 🧩 Cenário do Alerta (Simulado)

* Tipo: Múltiplas tentativas de login falhas
* Origem: Endereço IP externo
* Destino: Servidor interno de autenticação
* Horário: Fora do horário comercial

---

### 🔍 Etapa 1 – Entendimento do Alerta

Perguntas iniciais:

* Esse comportamento é esperado?
* O IP já foi visto antes?
* O usuário existe?

O alerta indica um **comportamento anômalo**, mas ainda não confirma um incidente.

---

### 🧠 Etapa 2 – Análise Inicial

* Verificar quantidade de tentativas
* Avaliar intervalo de tempo entre tentativas
* Conferir se houve login bem-sucedido

Nenhum acesso válido foi identificado.

---

### ⚠️ Classificação

* Status: **Falso positivo com potencial risco**
* Justificativa: Tentativas falhas sem sucesso, sem impacto confirmado

---

### 📋 Ação Tomada

* Registrar ocorrência
* Monitorar IP por reincidência
* Encerrar alerta

---

### 📝 Conclusão

Mesmo sem impacto imediato, o alerta foi tratado com atenção para **evitar escalonamento futuro**.

---

# 📄 network-analysis-intro.md

## 🌐 Network Analysis – Introdução

Este documento apresenta uma **abordagem inicial de análise de tráfego de rede**, focada em compreensão básica e identificação de comportamentos anormais.

---

### 🎯 Objetivo

* Entender o que está acontecendo no tráfego
* Identificar padrões normais
* Reconhecer possíveis anomalias

---

### 🧠 Conceitos Importantes

* IP de origem e destino
* Portas e protocolos
* Frequência de conexões
* Volume de tráfego

---

### 🔍 Exemplo de Análise Simples

* Muitas conexões repetidas em curto período
* Comunicação em porta incomum
* Tráfego constante fora do horário padrão

Esses sinais **não confirmam ataque**, mas justificam investigação.

---

### 🛠️ Ferramentas (Nível Introdutório)

* Wireshark
* Comandos básicos de rede em Linux

Ferramentas são suporte. O principal é **entendimento do contexto**.

---

### 📌 Conclusão

Análise de rede em SOC começa simples: observar, comparar e questionar.

---

# 📄 threat-detection-basics.md

## 🧠 Threat Detection Basics

Este documento resume **conceitos iniciais de detecção de ameaças** em um contexto de segurança defensiva.

---

### 🎯 O que é Detecção de Ameaças?

É o processo de **identificar atividades suspeitas** que podem representar risco à segurança.

---

### 🚨 Fontes Comuns de Detecção

* Logs de autenticação
* Tráfego de rede
* Alertas automatizados
* Comportamento anômalo de usuários

---

### ⚖️ Detecção ≠ Incidente

* Detecção indica possibilidade
* Incidente exige confirmação

Essa distinção evita respostas excessivas.

---

### 🧩 Exemplos de Indicadores

* Login fora do padrão
* Execução de processos incomuns
* Conexões repetidas para IPs externos

---

### 📋 Importância da Correlação

Um evento isolado raramente confirma ameaça.

A correlação de múltiplos sinais aumenta a confiança da detecção.

---

### 📌 Conclusão

Detecção de ameaças exige **atenção, contexto e cautela**. O objetivo é reduzir risco, não gerar ruído.
