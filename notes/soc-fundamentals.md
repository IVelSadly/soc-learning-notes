# 🛡️ SOC Fundamentals

Este documento reúne **fundamentos essenciais de um Security Operations Center (SOC)**, escritos com foco em aprendizado prático e compreensão do fluxo defensivo. O objetivo é consolidar conceitos básicos usados diariamente por times de Blue Team.

---

## 🔍 O que é um SOC?

Um **Security Operations Center (SOC)** é a área responsável por **monitorar, detectar, analisar e responder a eventos de segurança** dentro de uma organização.

O SOC atua de forma **contínua**, analisando dados de múltiplas fontes para identificar comportamentos suspeitos antes que causem impacto real.

---

## 🎯 Principais Objetivos de um SOC

* Monitorar eventos de segurança
* Detectar atividades suspeitas ou maliciosas
* Analisar alertas e validar incidentes
* Responder a incidentes de forma controlada
* Reduzir riscos e impactos ao negócio

---

## 👥 Papéis Comuns em um SOC

### 🔹 SOC Analyst (Nível 1)

* Monitoramento de alertas
* Triagem inicial
* Identificação de falsos positivos
* Escalonamento quando necessário

### 🔹 SOC Analyst (Nível 2)

* Análise aprofundada de incidentes
* Correlação de eventos
* Investigação técnica

### 🔹 SOC Analyst (Nível 3)

* Resposta avançada a incidentes
* Threat hunting
* Desenvolvimento de playbooks

---

## ⚙️ Fluxo Básico de Trabalho em SOC

1. **Coleta de eventos** (logs, tráfego, alertas)
2. **Geração de alertas**
3. **Triagem inicial**
4. **Análise**
5. **Classificação** (falso positivo ou incidente)
6. **Resposta ou escalonamento**
7. **Documentação**

---

## 🚨 Evento x Alerta x Incidente

* **Evento:** qualquer atividade registrada (ex: login, conexão, erro)
* **Alerta:** evento que dispara uma regra de segurança
* **Incidente:** evento confirmado como ameaça real

Entender essa diferença é essencial para **evitar respostas desnecessárias**.

---

## 🧠 Falso Positivo

Um **falso positivo** ocorre quando um alerta é gerado, mas não representa uma ameaça real.

Reduzir falsos positivos é importante para:

* Diminuir ruído
* Evitar fadiga do analista
* Melhorar eficiência do SOC

---

## 📋 Importância de Procedimentos (Playbooks)

SOC não funciona com improviso.

**Playbooks** definem:

* Como agir diante de cada tipo de alerta
* Passos claros de análise
* Critérios de escalonamento

Seguir procedimentos garante **consistência, rastreabilidade e segurança**.

---

## 🧪 Ambiente de Estudo

Todo o conteúdo aqui é baseado em:

* Cenários simulados
* Ambientes controlados
* Objetivo educacional

Nenhuma análise envolve sistemas reais sem autorização.

---

## 📌 Conclusão

SOC é uma área que valoriza:

* Atenção
* Método
* Documentação
* Pensamento analítico

Este documento representa a base do meu aprendizado em **segurança defensiva**.
