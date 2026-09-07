# LEARNING ROADMAP

## Objetivo

Este documento acompanha **conhecimento adquirido**, não features concluídas.

Use:
- `[ ]` não estudado
- `[-]` estudando
- `[x]` consigo explicar sem consultar material

---

## Bloco A — Fundamentos de ML e representação

- [ ] treino / validação / teste
- [ ] overfitting e generalização
- [ ] loss functions
- [ ] gradient descent / backpropagation
- [ ] classificação e regressão
- [ ] precision / recall / F1
- [ ] embeddings
- [ ] produto escalar
- [ ] norma vetorial
- [ ] cosine similarity
- [ ] PCA
- [ ] clustering
- [ ] TF-IDF
- [ ] logistic regression
- [ ] SVM

### Deve conseguir explicar
- Por que um conjunto de teste não deve orientar o treinamento?
- Por que cosine similarity ignora magnitude?
- O que um embedding tenta preservar?

---

## Bloco B — Transformers

- [ ] tokenização
- [ ] self-attention
- [ ] Q, K, V
- [ ] scaled dot-product attention
- [ ] multi-head attention
- [ ] positional information
- [ ] encoder
- [ ] decoder
- [ ] encoder-decoder
- [ ] masked language modeling
- [ ] causal language modeling
- [ ] sequence-to-sequence

### Matemática mínima

```text
Attention(Q,K,V) = softmax(QKᵀ / √d_k)V
```

### Deve conseguir explicar
- Por que existe `√d_k`?
- Diferença entre BERT, Whisper e uma causal LLM.
- Por que attention permite dependências de longa distância.

---

## Bloco C — Speech AI

- [ ] ASR
- [ ] spectrogram / mel spectrogram
- [ ] WER
- [ ] VAD
- [ ] speaker diarization
- [ ] speaker embeddings
- [ ] speaker verification
- [ ] diarization error rate (DER)
- [ ] overlapping speech
- [ ] clustering em diarização

### Deve conseguir explicar
- ASR responde “o que foi dito”; diarização responde “quem falou quando”.
- Speaker verification ≠ diarization.
- Por que convidados geram contaminação de persona.

---

## Bloco D — NLP

- [ ] BERT-style encoders
- [ ] NER
- [ ] NLI
- [ ] zero-shot classification
- [ ] topic classification
- [ ] stance detection
- [ ] entity linking
- [ ] argument mining
- [ ] stylometry

### Deve conseguir explicar
- Por que NLI pode ser usado como zero-shot classifier.
- Diferença entre entity recognition e entity linking.
- Como avaliar macro-F1.

---

## Bloco E — Information Retrieval

- [ ] inverted index
- [ ] TF-IDF
- [ ] BM25
- [ ] dense retrieval
- [ ] sparse retrieval
- [ ] hybrid retrieval
- [ ] bi-encoder
- [ ] cross-encoder
- [ ] reranking
- [ ] hard negatives
- [ ] MRR
- [ ] Recall@K
- [ ] NDCG
- [ ] RRF

### Deve conseguir explicar
- Por que BM25 ainda é um baseline sério.
- Por que bi-encoder escala melhor que cross-encoder.
- Por que reranking ocorre depois de retrieval.
- O que torna “Pessoa falando do mesmo assunto” um excelente hard negative para Antoun.

---

## Bloco F — RAG

- [ ] chunking
- [ ] conversational chunking
- [ ] metadata filtering
- [ ] retrieval pipeline
- [ ] context construction
- [ ] grounding
- [ ] citation
- [ ] abstention
- [ ] temporal retrieval
- [ ] query expansion

### Deve conseguir explicar
- RAG não ensina estilo.
- Fine-tuning não é substituto de retrieval.
- Por que chunk sem contexto pode inverter o significado de uma fala.

---

## Bloco G — Fine-tuning e PEFT

- [ ] full fine-tuning
- [ ] PEFT
- [ ] LoRA
- [ ] QLoRA
- [ ] rank
- [ ] target modules
- [ ] quantization
- [ ] gradient accumulation
- [ ] mixed precision
- [ ] adapters

### Deve conseguir explicar
- O que LoRA aproxima com matrizes de baixo rank.
- Por que dois adapters podem compartilhar uma base.
- Diferença de LoRA e QLoRA.

---

## Bloco H — Post-training

- [ ] chat templates
- [ ] SFT
- [ ] preference datasets
- [ ] DPO
- [ ] reward model
- [ ] distillation
- [ ] synthetic data risks

### Deve conseguir explicar
- O que SFT aprende.
- O que DPO otimiza conceitualmente.
- Por que preferência “parece mais Antoun” não pode substituir grounding.

---

## Bloco I — Agents

- [ ] agent loop
- [ ] tools
- [ ] state
- [ ] memory
- [ ] orchestration
- [ ] multi-agent
- [ ] moderator
- [ ] debate state
- [ ] agent evaluation

### Deve conseguir explicar
- Quando uma pipeline determinística é melhor que um agente.
- Por que Antoun e Pessoa precisam de retrieval isolado.

---

## Bloco J — Knowledge Graph

- [ ] graph model
- [ ] node / edge
- [ ] entity normalization
- [ ] temporal relation
- [ ] graph query
- [ ] GraphRAG
- [ ] structured + unstructured retrieval

### Deve conseguir explicar
- Quais perguntas graph retrieval resolve melhor que vector search.

---

## Bloco K — Evaluation

- [ ] golden dataset
- [ ] automatic metrics
- [ ] human evaluation
- [ ] blinded comparison
- [ ] ablation study
- [ ] error analysis
- [ ] calibration
- [ ] failure taxonomy
- [ ] adversarial tests

### Métricas próprias do projeto

**Persona Fidelity**
- estilo;
- vocabulário;
- estrutura argumentativa;
- consistência de posição.

**Persona Leakage**
- sinais de Pessoa em respostas de Antoun e vice-versa.

**Grounding**
- proporção de claims sustentadas por fontes.

**Temporal Accuracy**
- posição recuperada respeita data da consulta.

---

## Bloco L — MLOps / ML Systems

- [ ] dataset versioning
- [ ] experiment tracking
- [ ] model cards
- [ ] dataset cards
- [ ] reproducibility
- [ ] seeds
- [ ] CI
- [ ] data tests
- [ ] model smoke tests
- [ ] latency
- [ ] VRAM
- [ ] throughput
- [ ] quantization benchmark
- [ ] deployment

### Deve conseguir explicar
- Como reproduzir um experimento de 60 dias atrás.
- Por que código, dados, modelo e métricas precisam ser versionados juntos.
