# RESEARCH TRACK — Caminhos para IC/TCC

## Objetivo

Transformar o produto em uma plataforma que permita responder perguntas científicas sobre **persona modeling**, **retrieval**, **fine-tuning** e **contaminação**.

## Perguntas candidatas

### RQ1 — RAG × Fine-tuning
> Fine-tuning melhora persona fidelity quando um sistema já possui RAG de alta qualidade?

Comparar:
- prompt;
- prompt + RAG;
- prompt + RAG + LoRA;
- prompt + RAG + SFT;
- prompt + RAG + DPO.

### RQ2 — Persona contamination
> Quanto de dados atribuídos ao speaker errado é necessário para degradar uma persona?

Níveis:
- 0%;
- 1%;
- 2%;
- 5%;
- 10%;
- 20%.

Medir:
- persona fidelity;
- leakage;
- factual consistency.

### RQ3 — Style versus topic
> É possível identificar Antoun/Pessoa apenas pelo estilo, controlando o assunto?

Comparar:
- TF-IDF + logistic regression;
- stylometric features;
- BERTimbau;
- sentence embeddings;
- LLM judge.

### RQ4 — Synthetic augmentation
> Dados sintéticos aumentam ou degradam fidelidade de persona?

### RQ5 — Quantization
> INT8/INT4 alteram significativamente estilo e grounding?

### RQ6 — Temporal persona
> Um RAG temporal reduz atribuição de posições antigas como atuais?

### RQ7 — Hard negatives
> Treinar embeddings com “mesmo tópico + speaker errado” melhora speaker-aware retrieval?

## Métricas candidatas

### Persona Fidelity
Separar:
- lexical style;
- syntactic style;
- argumentative structure;
- known-position consistency.

### Persona Leakage
Classificador speaker-from-answer ou preferência humana.

### Grounding
- claim support rate;
- citation precision;
- citation recall.

### Temporal
- correct time-window retrieval;
- stale-position error rate.

## Entregáveis acadêmicos

- literature review;
- dataset methodology;
- benchmark;
- ablation studies;
- error analysis;
- reproducibility appendix;
- ethics/limitations;
- paper-style report.

## Estrutura possível de artigo

1. Abstract
2. Introduction
3. Related Work
4. Dataset
5. System
6. Persona Fidelity Benchmark
7. Experiments
8. Results
9. Error Analysis
10. Limitations & Ethics
11. Conclusion
