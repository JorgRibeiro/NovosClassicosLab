# RESOURCES — Materiais de Estudo

> Prioridade: documentação oficial → papers originais → cursos/livros → tutoriais.

As bibliotecas e modelos mudam. Fixe versões/revisions usadas em cada experimento.
Os itens abaixo são referências de estudo e candidatos para avaliação; não representam
seleções definitivas. Verifique documentação, acesso e compatibilidade ao iniciar cada
experimento. Decisões e resultados pertencem a ADRs e experimentos.

---

# 1. Hugging Face — trilha principal

## Hugging Face Course — ESSENCIAL
Curso oficial, gratuito, com Transformers, Datasets, Tokenizers, Accelerate e Hub.

- Português: https://huggingface.co/docs/course/pt/chapter1/1
- Código/conteúdo: https://github.com/huggingface/course

### Ordem sugerida
**Dias 1–15**
- Cap. 1 — Transformer models
- Cap. 2 — Using Transformers
- Cap. 3 — Fine-tuning
- Cap. 4 — Hub
- Cap. 5 — Datasets

**Dias 45+**
- retomar partes de tokenização, fine-tuning e tarefas avançadas.

## Open Source Models with Hugging Face — DeepLearning.AI
Curso curto útil para aprender a navegar pelo Hub e usar modelos de texto/áudio.

https://www.deeplearning.ai/alpha/short-courses/open-source-models-hugging-face/

## Documentação oficial
- Hub: https://huggingface.co/docs/hub/index
- Transformers: https://huggingface.co/docs/transformers/
- Datasets: https://huggingface.co/docs/datasets/
- PEFT: https://huggingface.co/docs/peft/
- TRL: https://huggingface.co/docs/trl/
- Accelerate: https://huggingface.co/docs/accelerate/
- Evaluate: https://huggingface.co/docs/evaluate/
- Dataset Cards: https://huggingface.co/docs/hub/datasets-cards
- Model Cards: https://huggingface.co/docs/hub/model-cards
- Spaces: https://huggingface.co/docs/hub/spaces-overview
- Collections: https://huggingface.co/docs/hub/collections

---

# 2. Matemática, Deep Learning e Transformers

## Dive into Deep Learning — ESSENCIAL
Livro gratuito e interativo.

- Geral: https://d2l.ai/
- Tradução PT (versão disponível): https://pt.d2l.ai/
- Atenção: https://pt.d2l.ai/chapter_attention-mechanisms/index.html

### Partes relevantes
- linear algebra / probability: revisar conforme necessidade;
- optimization;
- multilayer perceptrons;
- attention mechanisms;
- Transformers;
- NLP applications;
- BERT.

## Paper — Attention Is All You Need
Vaswani et al. (2017)

https://arxiv.org/abs/1706.03762

### Primeira leitura
1. Abstract
2. Figure 1
3. Section 3
4. Conclusion

### Segunda leitura
- positional encoding;
- multi-head attention;
- complexity discussion.

## Stanford CS224N — RECOMENDADO
NLP with Deep Learning.

- Curso: https://web.stanford.edu/class/cs224n/
- Vídeos públicos são indicados pelo próprio site da disciplina.

Estude especialmente:
- word vectors;
- neural networks;
- attention;
- transformers;
- pretraining;
- question answering;
- retrieval quando presente na edição escolhida.

---

# 3. Speech AI

## Whisper

### Model card inicial
`openai/whisper-large-v3-turbo`

https://huggingface.co/openai/whisper-large-v3-turbo

### Paper
**Robust Speech Recognition via Large-Scale Weak Supervision**

https://arxiv.org/abs/2212.04356

### Estudar
- ASR;
- encoder-decoder;
- mel spectrogram;
- timestamps;
- WER;
- multilingual speech.

## pyannote

### Pipeline candidato para baseline
`pyannote/speaker-diarization-community-1`

https://huggingface.co/pyannote/speaker-diarization-community-1

### Tutorial
https://colab.research.google.com/github/pyannote/pyannote-audio/blob/develop/tutorials/intro.ipynb

### Estudar
- VAD;
- segmentation;
- speaker embeddings;
- clustering;
- overlapping speech;
- DER.

## Speaker recognition

Candidato a baseline:
`speechbrain/spkrec-ecapa-voxceleb`

https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb

### Conceitos
- verification;
- identification;
- embedding;
- cosine similarity;
- threshold;
- ROC/EER.

---

# 4. NLP para português

## BERTimbau
`neuralmind/bert-base-portuguese-cased`

https://huggingface.co/neuralmind/bert-base-portuguese-cased

Usar como candidato para:
- classificação;
- stylometry;
- NER experiments;
- speaker-from-text classifier.

## Zero-shot / NLI
Candidato:
`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`

https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli

Estudar:
- entailment;
- contradiction;
- neutral;
- zero-shot classification.

---

# 5. Embeddings e Retrieval

## Sentence-BERT — PAPER FUNDAMENTAL
Reimers & Gurevych (2019)

https://arxiv.org/abs/1908.10084

Estude:
- bi-encoder;
- siamese networks;
- cosine similarity;
- semantic textual similarity.

## Sentence Transformers
https://www.sbert.net/

Estude:
- semantic search;
- training;
- losses;
- hard negatives;
- CrossEncoder.

## BGE-M3
`BAAI/bge-m3`

https://huggingface.co/BAAI/bge-m3

Importante porque permite experimentar:
- dense;
- sparse;
- multi-vector.

## Multilingual E5
`intfloat/multilingual-e5-large-instruct`

https://huggingface.co/intfloat/multilingual-e5-large-instruct

## Reranker
`BAAI/bge-reranker-v2-m3`

https://huggingface.co/BAAI/bge-reranker-v2-m3

## Dense Passage Retrieval — PAPER
Karpukhin et al.

https://arxiv.org/abs/2004.04906

## Qdrant Hybrid Search
https://qdrant.tech/documentation/tutorials-basics/reranking-hybrid-search/

### Estudar antes
- inverted index;
- TF-IDF;
- BM25;
- cosine similarity;
- Recall@K;
- MRR;
- NDCG;
- RRF.

---

# 6. RAG

## Paper original
**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**

Lewis et al.

https://arxiv.org/abs/2005.11401

### Perguntas ao ler
- Por que separar memória paramétrica e não-paramétrica?
- Qual é o papel do retriever?
- Quais problemas surgem quando retrieval falha?

## Prática
Construir primeiro RAG manualmente:
1. query;
2. retrieve;
3. rerank;
4. format context;
5. generate;
6. cite.

Evitar começar com framework que esconda essas etapas.

---

# 7. PEFT, LoRA e QLoRA

## PEFT docs
https://huggingface.co/docs/peft/

## LoRA — PAPER FUNDAMENTAL
Hu et al.

https://arxiv.org/abs/2106.09685

Estudar:
- low-rank matrices;
- rank;
- frozen weights;
- target modules.

## QLoRA
Dettmers et al.

https://arxiv.org/abs/2305.14314

Estudar:
- 4-bit quantization;
- NF4;
- memory savings;
- paged optimizers.

---

# 8. SFT, DPO e Post-training

## TRL
https://huggingface.co/docs/trl/

A documentação atual inclui trainers para SFT, DPO, GRPO, KTO, reward modeling, distillation e outros.

### Para este projeto
Prioridade:
1. SFT
2. DPO
3. reward modeling — opcional
4. distillation — research
5. GRPO — não obrigatório para o MVP

## DPO — PAPER
Rafailov et al.

https://arxiv.org/abs/2305.18290

Pergunta central:
> Como aprender preferências sem construir explicitamente todo o pipeline de RLHF clássico?

---

# 9. LLM base

Não fixe um vencedor antes do benchmark.

Candidatos devem ser verificados no Hub quando o experimento começar.

Um baseline razoável da família Qwen pode ser usado, escolhendo tamanho compatível com hardware.

Hub:
https://huggingface.co/Qwen

Critérios:
- licença;
- português;
- context window;
- chat template;
- memória;
- quantização;
- PEFT compatibility.

---

# 10. Agents

## Hugging Face Agents Course
https://huggingface.co/agents-course

Unidades úteis:
- agent fundamentals;
- tools/actions;
- frameworks;
- observability/evaluation.

Não use agentes onde uma pipeline determinística resolve melhor.

---

# 11. Knowledge Graph / GraphRAG

## Neo4j GraphRAG
https://neo4j.com/docs/neo4j-graphrag-python/current/

## RAG tutorial
https://neo4j.com/blog/developer/rag-tutorial/

Estudar:
- entity graph;
- relations;
- graph querying;
- vector + graph retrieval;
- temporal edges.

---

# 12. MLOps

## Made With ML — MLOps
https://madewithml.com/courses/mlops/

Tópicos especialmente relevantes:
- data preparation;
- testing;
- experiment tracking;
- reproducibility;
- CI/CD;
- monitoring;
- serving.

---

# 13. Livros complementares

## Dive into Deep Learning
Gratuito e diretamente aplicável.
https://d2l.ai/

## Speech and Language Processing — Jurafsky & Martin
Use a edição disponibilizada oficialmente pelos autores.
https://web.stanford.edu/~jurafsky/slp3/

Partes úteis:
- text classification;
- embeddings;
- transformers;
- information retrieval;
- question answering;
- speech recognition;
- dialogue.

## Introduction to Information Retrieval — Manning, Raghavan, Schütze
Material oficial:
https://nlp.stanford.edu/IR-book/

Partes úteis:
- inverted indexes;
- scoring;
- TF-IDF;
- evaluation;
- probabilistic retrieval.

## Designing Machine Learning Systems — Chip Huyen
Complementar para:
- data;
- training-serving skew;
- monitoring;
- system design.

---

# 14. Modelo de leitura de paper

Para cada paper:

### Passo 1 — 15 min
- título;
- abstract;
- figuras;
- conclusão.

### Passo 2 — 30–60 min
- problema;
- método;
- arquitetura;
- experimento principal.

### Passo 3
Escrever:
- problema;
- contribuição;
- o que vou usar;
- o que não entendi.

### Passo 4 — opcional
Reproduzir uma ideia em escala pequena.

---

# 15. Ordem mínima de papers

1. Attention Is All You Need
2. Whisper
3. Sentence-BERT
4. Dense Passage Retrieval
5. RAG
6. LoRA
7. QLoRA
8. DPO

Não é obrigatório compreender todas as derivações matemáticas na primeira leitura.
