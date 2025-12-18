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
