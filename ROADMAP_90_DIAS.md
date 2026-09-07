# ROADMAP DE 90 DIAS — Novos Clássicos Persona Lab

## Estado atual — Dia 1

Fundação Python validada localmente; CI configurado, ainda sem execução remota.
Fase 0 em andamento; estudos não aferidos e Dia 2 não iniciado.
O estado atual fica em [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md); a estrutura preparada
está em [INITIAL_REPO_TREE.md](INITIAL_REPO_TREE.md).
Modelos, bibliotecas e infraestrutura citados são candidatos a experimentação, sem
escolha definitiva até registro de evidência e ADR. As tarefas abaixo são planejamento.

## Como usar este arquivo

Este é o arquivo que deve ficar aberto durante o projeto.

Marcação:
- `[ ]` não iniciado
- `[-]` em andamento
- `[x]` concluído

Prioridades:
- **MVP** — obrigatório;
- **PLUS** — faça se MVP estiver estável;
- **RESEARCH** — experimento científico, nunca bloqueia o produto.

### Rotina diária sugerida

Não precisa seguir horários rígidos. Preserve a sequência:

1. **60–90 min — teoria**
2. **2–4 h — implementação**
3. **45–90 min — experimento/eval**
4. **20–30 min — documentação**
5. **10 min — explicar em voz alta o que aprendeu**

### Regra semanal

A cada 7 dias:
- não adicione feature nova na primeira metade da revisão;
- rode testes;
- atualize métricas;
- escreva retrospectiva;
- corte escopo se necessário;
- crie `docs/checkpoints/week-XX.md` com o [template](docs/checkpoints/TEMPLATE.md);
- atualize PROJECT_CONTEXT.md com o estado atual e o link do último checkpoint.

O primeiro checkpoint será criado ao final do primeiro sprint (revisão do Dia 7).
Checkpoints são históricos imutáveis; não antecipar week-01 no Dia 0.

---

# FASE 0 — Preparação e baseline mental
## Dias 1–3

### Objetivo
Criar o repositório, ambiente, documentação e entender a arquitetura antes de coletar dados.

### Dia 1 — Projeto e ambiente

#### Estudo
- [ ] Ler `README.md`, `ARCHITECTURE.md`, `LEARNING_ROADMAP.md`.
- [ ] Hugging Face Course: introdução + capítulo 1.
- [ ] Entender encoder, decoder e encoder-decoder em nível conceitual.

#### Implementação
- [x] Criar repositório Git.
- [x] Criar ambiente Python.
- [x] Definir gerenciador (`uv`, `poetry` ou pip/venv).
- [x] Adicionar lint/formatter.
- [x] Criar estrutura de pastas.
- [x] Criar `.env.example`.
- [x] Criar `.gitignore`.
- [x] Criar primeiro CI simples.
- [ ] Criar conta/configurar Hugging Face Hub.
- [ ] Nunca commitar tokens.

#### Documentação
- [x] Registrar ADR-0001: stack inicial.
- [x] Criar journal Dia 1.
- [x] Registrar hardware disponível.

#### DoD
- [x] `pytest` roda.
- [x] lint roda.
- [x] import básico do projeto funciona.
- [ ] primeiro commit limpo.

---

### Dia 2 — Hugging Face Hub e Datasets

#### Estudo
- [ ] HF Course: Hub/Datasets introdutório.
- [ ] Ler docs de Dataset Cards.
- [ ] Entender Arrow em nível conceitual.
- [ ] Entender dataset split.

#### Implementação
- [ ] Criar dataset dummy local com 10 segmentos.
- [ ] Converter para `datasets.Dataset`.
- [ ] Definir schema canônico v0.
- [ ] Criar validação Pydantic/dataclass.
- [ ] Testar salvar/carregar dataset.
- [ ] Se apropriado, criar repo HF privado para artefatos experimentais.

#### Mini desafio
- [ ] Criar dataset sem copiar tutorial linha a linha.

#### DoD
- [ ] Dataset dummy validado e versionável.

---

### Dia 3 — Plano de dados e Responsible AI

#### Estudo
- [ ] Data lineage.
- [ ] Copyright/termos das fontes usadas.
- [ ] Model Cards/Dataset Cards.
- [ ] Diferença persona × identidade.

#### Implementação
- [ ] Criar `docs/data-policy.md`.
- [ ] Definir o que pode ser armazenado localmente.
- [ ] Definir o que pode ser publicado.
- [ ] Criar níveis `DIRECT / INFERRED / UNSUPPORTED`.
- [ ] Criar taxonomy de fontes.

#### DoD
- [ ] Nenhuma coleta massiva começa sem política de dados registrada.

---

# FASE 1 — Ingestão e Corpus bruto
## Dias 4–9

### Meta
Um comando recebe um vídeo autorizado/permitido e gera metadata + áudio + registro rastreável.

### Dia 4 — Ingestion design
- [ ] Estudar APIs/formatos das fontes.
- [ ] Definir `SourceRecord`.
- [ ] Implementar ingestão de metadata de um episódio.
- [ ] Criar hash/content identity.
- [ ] Registrar source URL/ID/date/title/duration.
- [ ] Teste unitário.

### Dia 5 — Áudio
- [ ] Estudar sample rate, mono/stereo, PCM e formatos.
- [ ] Criar pipeline de normalização de áudio.
- [ ] Padronizar 16 kHz quando apropriado.
- [ ] Preservar original ou referência rastreável.
- [ ] Medir tamanho de armazenamento por hora.

### Dia 6 — Corpus inicial
- [ ] Ingerir 3 episódios variados.
- [ ] Incluir pelo menos um episódio com convidado se existir.
- [ ] Criar manifesto.
- [ ] Detectar duplicatas.
- [ ] Definir IDs determinísticos.

### Dia 7 — Revisão Sprint 1
- [ ] Rodar pipeline do zero.
- [ ] Excluir caches e verificar reprodutibilidade.
- [ ] Documentar falhas.
- [ ] Atualizar ADRs.
- [ ] Explicar data lineage sem consultar.

### Dia 8 — Social text design
- [ ] Definir schema para posts/replies/quotes.
- [ ] Preservar parent context em replies.
- [ ] Não coletar massivamente antes de verificar acesso/termos.
- [ ] Criar dataset dummy com conversa encadeada.

### Dia 9 — Corpus v0
- [ ] Unificar `youtube` e `social` sob interfaces comuns.
- [ ] Criar Dataset Card inicial.
- [ ] Gerar `NC-Corpus-v0`.
- [ ] Criar relatório de qualidade inicial.

### DoD Fase 1
- [ ] 3+ episódios ingeridos.
- [ ] lineage funciona.
- [ ] schema validado.
- [ ] duplicação detectável.
- [ ] dataset pode ser recriado.

---

# FASE 2 — Automatic Speech Recognition
## Dias 10–16

### Meta
Transcrever episódios com timestamps e benchmark de qualidade.

### Dia 10 — Fundamentos ASR
- [ ] Estudar mel spectrogram.
- [ ] Ler Whisper paper: abstract, arquitetura, conclusão.
- [ ] Ler model card Whisper no HF.
- [ ] Entender encoder-decoder.
- [ ] Entender WER.

### Dia 11 — Whisper baseline
- [ ] Rodar modelo menor em trechos.
- [ ] Rodar `whisper-large-v3-turbo` se hardware permitir.
- [ ] Guardar timestamps.
- [ ] Registrar velocidade e VRAM.
- [ ] EXP-001.

### Dia 12 — Ground truth ASR
- [ ] Selecionar 15–30 min de áudio.
- [ ] Corrigir manualmente transcript.
- [ ] Criar `gold/asr`.
- [ ] Calcular WER.
- [ ] Separar erros de nomes próprios.

### Dia 13 — ASR benchmark
- [ ] Comparar subtitle original vs Whisper.
- [ ] Comparar 2 configurações/modelos.
- [ ] Medir WER, real-time factor e VRAM.
- [ ] EXP-002.

### Dia 14 — Revisão Sprint 2
- [ ] Explicar Whisper.
- [ ] Explicar WER.
- [ ] Revisar erros.
- [ ] Escolher baseline ASR.
- [ ] ADR: modelo ASR inicial.

### Dia 15 — Long-form pipeline
- [ ] Processar episódio completo.
- [ ] Retomar jobs interrompidos.
- [ ] Salvar progresso incremental.
- [ ] Logs estruturados.
- [ ] Testar idempotência.

### Dia 16 — ASR v1
- [ ] Processar os 3 episódios.
- [ ] Criar dataset de segmentos ASR.
- [ ] Quality report.
- [ ] Marcar confiança/estado de revisão.

### DoD Fase 2
- [ ] ASR automatizado.
- [ ] timestamps.
- [ ] WER calculado.
- [ ] velocidade conhecida.
- [ ] erros documentados.

---

# FASE 3 — Diarização
## Dias 17–23

### Meta
Responder com qualidade: “quem falou quando?”.

### Dia 17 — Fundamentos
- [ ] Estudar VAD, segmentation, embeddings, clustering.
- [ ] Ler pyannote docs/model card.
- [ ] Entender DER.
- [ ] Entender overlap.

### Dia 18 — pyannote baseline
- [ ] Aceitar requisitos de acesso do modelo quando necessário.
- [ ] Rodar `speaker-diarization-community-1`.
- [ ] Exportar RTTM.
- [ ] Visualizar segmentos.
- [ ] EXP-003.

### Dia 19 — Gold diarization
- [ ] Anotar manualmente trecho pequeno.
- [ ] Incluir troca rápida de speaker.
- [ ] Incluir overlap quando possível.
- [ ] Calcular DER.

### Dia 20 — Speaker count
- [ ] Comparar detecção automática.
- [ ] Comparar limite conhecido em episódios com 2 hosts.
- [ ] Testar episódio com convidado.
- [ ] EXP-004.

### Dia 21 — Revisão Sprint 3
- [ ] Explicar diarization pipeline.
- [ ] Explicar DER.
- [ ] Documentar principais erros.
- [ ] ADR baseline.

### Dia 22 — ASR + diarization alignment
- [ ] Alinhar tokens/segments a speaker turns.
- [ ] Usar exclusive diarization quando fizer sentido.
- [ ] Criar conversation turns.
- [ ] Preservar overlaps como metadata quando possível.

### Dia 23 — Pipeline Speech v1
- [ ] `audio → transcript → speakers`.
- [ ] Gerar JSONL/Dataset.
- [ ] Teste ponta a ponta.
- [ ] Quality report.

### DoD
- [ ] turnos com timestamps;
- [ ] speaker labels;
- [ ] DER conhecido;
- [ ] ASR e diarização reconciliados.

---

# FASE 4 — Identificação Antoun/Pessoa
## Dias 24–30

### Meta
Converter `SPEAKER_00` em `antoun/pessoa/guest/unknown`; baixa confiança resulta em `unknown`.

### Dia 24 — Speaker embeddings
- [ ] Estudar verification vs identification.
- [ ] Estudar cosine similarity.
- [ ] Explorar ECAPA/SpeechBrain.
- [ ] Implementar embeddings de referência.

### Dia 25 — Reference bank
- [ ] Selecionar áudio limpo de Antoun.
- [ ] Selecionar áudio limpo de Pessoa.
- [ ] Criar várias referências, não uma única.
- [ ] Guardar provenance.

### Dia 26 — Classificador por similaridade
- [ ] Segment → embedding.
- [ ] Similaridade com centroids/references.
- [ ] Threshold para unknown.
- [ ] EXP-005.

### Dia 27 — Eval speaker ID
- [ ] Criar gold set.
- [ ] Accuracy/F1.
- [ ] Matriz de confusão.
- [ ] Estudar falso positivo de convidados.
- [ ] EXP-006.

### Dia 28 — Revisão Sprint 4
- [ ] Explicar embeddings de voz.
- [ ] Rever threshold.
- [ ] Criar failure gallery.
- [ ] Decidir baseline.

### Dia 29 — Contamination guard
- [ ] Marcar baixa confiança.
- [ ] Não atribuir speaker em caso duvidoso.
- [ ] Criar validações de corpus.
- [ ] PLUS: texto + voz para anomaly detection.

### Dia 30 — Corpus Speech v1
- [ ] Reprocessar amostra.
- [ ] `speaker=antoun|pessoa|guest|unknown`.
- [ ] Gerar relatório de proporções.
- [ ] Criar release interna `NC-Speech-v1`.

### Marco 30 dias
Você deve ter:
- ingestão;
- ASR;
- diarização;
- identificação;
- dataset rastreável.

Se isso não estiver sólido, **não avance para fine-tuning**.

---

# FASE 5 — NLP Enrichment e ML clássico
## Dias 31–38

### Dia 31 — Texto e stylometry
- [ ] Estudar TF-IDF.
- [ ] Implementar TF-IDF.
- [ ] Logistic Regression speaker-from-text.
- [ ] EXP-025 (speaker-from-text; distinto de EXP-020, baseline de tópicos).

### Dia 32 — Topics zero-shot
- [ ] Estudar NLI.
- [ ] Definir taxonomia inicial de temas.
- [ ] Testar zero-shot multilíngue.
- [ ] Avaliar manualmente 100 exemplos.
- [ ] EXP-021.

### Dia 33 — BERTimbau
- [ ] Estudar encoder BERT.
- [ ] Fine-tunar classificador pequeno se houver labels.
- [ ] Comparar TF-IDF vs zero-shot vs BERT para tópicos, no mesmo dataset/split.
- [ ] EXP-020 para o baseline TF-IDF de tópicos, separado do speaker-from-text do Dia 31.
- [ ] EXP-022.

### Dia 34 — Entity extraction
- [ ] Estudar NER.
- [ ] Extrair pessoas, livros, lugares, organizações.
- [ ] Criar normalização inicial.
- [ ] EXP-023.

### Dia 35 — Stance
- [ ] Estudar stance detection.
- [ ] Criar annotation guideline.
- [ ] Rotular amostra pequena.
- [ ] Construir baseline.
- [ ] EXP-024.

### Dia 36 — Argument structure
- [ ] Estudar claim/premise/evidence.
- [ ] Anotar manualmente 20–30 conversas.
- [ ] RESEARCH: testar extração assistida por LLM.

### Dia 37 — Quality
- [ ] Verificar propagação de erro ASR → NLP.
- [ ] Comparar transcript corrigido vs bruto.
- [ ] Documentar.

### Dia 38 — Revisão
- [ ] Explicar NLI/NER/stance.
- [ ] Atualizar corpus enrichment.
- [ ] Decidir quais annotations realmente valem manter.

### DoD
- [ ] tópicos básicos;
- [ ] entidades;
- [ ] pelo menos um baseline clássico;
- [ ] métricas, não apenas outputs.

---

# FASE 6 — Information Retrieval
## Dias 39–47

### Meta
Construir benchmark de busca antes de RAG.

### Dia 39 — IR clássico
- [ ] Ler capítulos introdutórios de Information Retrieval.
- [ ] Inverted index.
- [ ] TF-IDF.
- [ ] BM25.
- [ ] Implementar mini BM25 ou estudar implementação.

### Dia 40 — Retrieval eval set
- [ ] Criar 50 queries.
- [ ] Marcar documentos relevantes.
- [ ] Incluir consultas Antoun/Pessoa.
- [ ] Incluir nomes próprios e termos exatos.
- [ ] Incluir consultas semânticas.

### Dia 41 — BM25
- [ ] Implementar baseline.
- [ ] Recall@5/@10.
- [ ] MRR.
- [ ] EXP-040.

### Dia 42 — Embeddings
- [ ] Ler Sentence-BERT.
- [ ] Estudar bi-encoder.
- [ ] Estudar cosine.
- [ ] Testar BGE-M3.
- [ ] EXP-041.

### Dia 43 — E5
- [ ] Testar multilingual E5.
- [ ] Comparar com BGE.
- [ ] Registrar latência e memória.
- [ ] EXP-042.

### Dia 44 — Revisão Sprint
- [ ] Explicar BM25 × dense retrieval.
- [ ] Error analysis.
- [ ] Identificar queries onde cada abordagem vence.

### Dia 45 — Hybrid retrieval
- [ ] Combinar sparse + dense.
- [ ] Estudar RRF.
- [ ] Qdrant.
- [ ] EXP-043.

### Dia 46 — Reranking
- [ ] Estudar cross-encoder/reranker.
- [ ] Testar BGE reranker.
- [ ] Top-N retrieval → rerank Top-K.
- [ ] NDCG/MRR.
- [ ] EXP-044.

### Dia 47 — Conversational chunking
- [ ] Chunk por turnos, não tamanho fixo apenas.
- [ ] Preservar pergunta/resposta/discordância.
- [ ] Comparar chunking.
- [ ] EXP-045.

### DoD
- [ ] benchmark;
- [ ] BM25;
- [ ] dense;
- [ ] hybrid;
- [ ] reranker;
- [ ] escolha baseada em métricas.

---

# FASE 7 — RAG com evidências
## Dias 48–56

### Dia 48 — RAG paper
- [ ] Ler paper RAG.
- [ ] Desenhar pipeline sem framework.

### Dia 49 — RAG mínimo
- [ ] query;
- [ ] retrieve;
- [ ] context;
- [ ] generate;
- [ ] resposta.
- [ ] Sem persona ainda.
- [ ] EXP-060.

### Dia 50 — Speaker filters
- [ ] `speaker=antoun`.
- [ ] `speaker=pessoa`.
- [ ] Teste automático contra leakage no retrieval.
- [ ] EXP-061.

### Dia 51 — Citation engine
- [ ] Cada chunk retorna source + timestamp.
- [ ] Construir URL/time pointer quando permitido.
- [ ] Associar claims a evidências.
- [ ] EXP-062.

### Dia 52 — Grounding
- [ ] `DIRECT`.
- [ ] `INFERRED`.
- [ ] `UNSUPPORTED`.
- [ ] Criar prompts e regras.
- [ ] Perguntas propositalmente sem evidência.
- [ ] EXP-064.

### Dia 53 — Temporal retrieval
- [ ] `date <= cutoff`.
- [ ] “mais recente”.
- [ ] “como mudou?”.
- [ ] EXP-063.

### Dia 54 — Research mode
- [ ] Resposta neutra.
- [ ] síntese de fontes.
- [ ] timeline.
- [ ] sem interpretar personagem.

### Dia 55 — RAG eval
- [ ] answer relevance;
- [ ] retrieval relevance;
- [ ] citation precision;
- [ ] unsupported behavior;
- [ ] error analysis.

### Dia 56 — Revisão
- [ ] Explicar parametric vs non-parametric memory.
- [ ] RAG v1.
- [ ] ADR retrieval/RAG.

### Marco
Já deve existir um produto útil mesmo sem persona:
**NC Research / NC Search**.

---

# FASE 8 — Persona sem fine-tuning
## Dias 57–63

### Dia 57 — Persona dataset
- [ ] Separar WHAT/HOW.
- [ ] Coletar exemplos de estilo.
- [ ] Criar speaker style notes derivados de dados.

### Dia 58 — Stylometry
- [ ] sentence length;
- [ ] lexical diversity;
- [ ] interjections;
- [ ] analogies;
- [ ] question patterns;
- [ ] disagreement forms.

### Dia 59 — Persona prompt
- [ ] Antoun system/persona prompt.
- [ ] Pessoa system/persona prompt.
- [ ] RAG isolado.
- [ ] EXP-080/081.

### Dia 60 — Persona eval set
- [ ] 30–50 perguntas;
- [ ] respostas/trechos documentados;
- [ ] perguntas desconhecidas;
- [ ] perguntas adversariais.

### Dia 61 — Blind human eval
- [ ] gerar respostas de baseline;
- [ ] randomizar;
- [ ] formulário simples;
- [ ] 3+ avaliadores se possível.

### Dia 62 — Persona Leakage baseline
- [ ] treinar/testar classificador textual;
- [ ] definir leakage metric inicial.
- [ ] comparar persona prompts.

### Dia 63 — Revisão
- [ ] decidir se fine-tuning é necessário;
- [ ] não treinar só porque é possível.

---

# FASE 9 — PEFT, LoRA e SFT
## Dias 64–72

### Dia 64 — LoRA theory
- [ ] Ler LoRA paper.
- [ ] Estudar PEFT docs.
- [ ] Entender rank e target modules.
- [ ] Fazer mini LoRA em modelo pequeno.

### Dia 65 — QLoRA
- [ ] Ler QLoRA.
- [ ] quantization basics;
- [ ] 4-bit;
- [ ] memory benchmark.

### Dia 66 — SFT dataset design
- [ ] NÃO converter transcript cru diretamente.
- [ ] construir instruction/response pairs;
- [ ] manter provenance;
- [ ] separar train/val/test temporalmente.

### Dia 67 — Antoun adapter
- [ ] modelo compatível com hardware;
- [ ] PEFT;
- [ ] SFT com TRL;
- [ ] EXP-082/084.

### Dia 68 — Pessoa adapter
- [ ] mesma metodologia;
- [ ] EXP-083.

### Dia 69 — Evaluation
- [ ] prompt-only vs LoRA;
- [ ] RAG+prompt vs RAG+LoRA;
- [ ] persona;
- [ ] grounding;
- [ ] leakage.

### Dia 70 — Revisão Sprint
- [ ] analisar se LoRA realmente ajudou;
- [ ] registrar custo;
- [ ] salvar adapters e cards.

### Dia 71 — Hard cases
- [ ] discordância;
- [ ] humor;
- [ ] perguntas inéditas;
- [ ] cross-persona tests.

### Dia 72 — Model cards
- [ ] intended use;
- [ ] limitations;
- [ ] training data description;
- [ ] eval results;
- [ ] ethics.

### DoD
- [ ] adapters reproduzíveis;
- [ ] ganho medido ou rejeição documentada.

---

# FASE 10 — DPO / Preferences
## Dias 73–78

### Dia 73 — DPO theory
- [ ] Ler paper DPO.
- [ ] Estudar TRL DPOTrainer.
- [ ] Entender chosen/rejected.

### Dia 74 — Preference dataset
- [ ] criar pares de respostas;
- [ ] regras claras de preferência;
- [ ] grounding nunca perde para estilo.

### Dia 75 — Pilot DPO
- [ ] modelo pequeno/adapter;
- [ ] treino curto;
- [ ] EXP-085.

### Dia 76 — Eval
- [ ] blind persona eval;
- [ ] leakage;
- [ ] grounding;
- [ ] verbosity/style artifacts.

### Dia 77 — Ablation
- [ ] RAG;
- [ ] RAG+LoRA;
- [ ] RAG+LoRA+DPO.

### Dia 78 — Revisão
- [ ] decidir manter/rejeitar DPO.
- [ ] documentar.

---

# FASE 11 — Temporal Memory, Graph e Agents
## Dias 79–85

### Dia 79 — Semantic/episodic memory
- [ ] separar memória episódica e sínteses;
- [ ] não sobrescrever evidência histórica.

### Dia 80 — Opinion timeline
- [ ] tema → stance → data → evidence.
- [ ] consulta “como mudou?”.
- [ ] Temporal Accuracy eval.

### Dia 81 — Knowledge Graph
- [ ] nós: person/topic/entity/book/source.
- [ ] arestas: MENTIONS/SUPPORTS/OPPOSES/RECOMMENDS.
- [ ] construir grafo pequeno.

### Dia 82 — Graph queries
- [ ] autores citados por ambos;
- [ ] temas de divergência;
- [ ] livros por tópico.
- [ ] PLUS: GraphRAG.

### Dia 83 — Agents fundamentals
- [ ] HF Agents Course Unit 1.
- [ ] construir AntounAgent/PessoaAgent como wrappers.
- [ ] retrieval isolado.

### Dia 84 — Debate Engine
- [ ] moderator;
- [ ] turn state;
- [ ] claim/counterclaim;
- [ ] citations por turno.

### Dia 85 — Agent eval
- [ ] loops;
- [ ] topic drift;
- [ ] evidence preservation;
- [ ] leakage;
- [ ] failure gallery.

---

# FASE 12 — MLOps, produto e publicação
## Dias 86–90

### Dia 86 — Reproducibility
- [ ] fixar versions;
- [ ] seeds;
- [ ] model revisions;
- [ ] dataset versions;
- [ ] Makefile/task runner:
  - `make ingest`
  - `make transcribe`
  - `make diarize`
  - `make enrich`
  - `make index`
  - `make eval`
  - `make train`
  - `make serve`

### Dia 87 — Tests + CI
- [ ] unit;
- [ ] integration;
- [ ] data tests;
- [ ] model smoke tests;
- [ ] small eval suite no CI.

### Dia 88 — Hugging Face
- [ ] Dataset Card;
- [ ] Model Cards;
- [ ] adapters;
- [ ] Space;
- [ ] Collection agrupando artefatos.
- [ ] Publicar somente o que direitos/licenças permitem.

### Dia 89 — Final benchmark
- [ ] rodar Golden Dataset;
- [ ] tabela final;
- [ ] ablations;
- [ ] latency/VRAM;
- [ ] human eval final;
- [ ] failure analysis.

### Dia 90 — Relatório e retrospectiva
- [ ] escrever paper-style final report;
- [ ] atualizar README;
- [ ] arquitetura final;
- [ ] demo;
- [ ] gravação curta;
- [ ] listar limitações;
- [ ] listar próximos 90 dias;
- [ ] selecionar pergunta de IC/TCC.

---

# CHECKPOINTS

Os marcos abaixo são expectativas de progresso, complementares aos snapshots semanais
em docs/checkpoints/. Não comprovam conclusão.

## Dia 14
Esperado:
- ambiente;
- ingestion;
- ASR começando;
- documentação viva.

## Dia 30
Esperado:
- Speech pipeline completo;
- speaker identity;
- corpus v1.

## Dia 45
Esperado:
- NLP;
- retrieval benchmark em andamento.

## Dia 60
Esperado:
- RAG robusto;
- citation;
- temporal baseline;
- persona prompt.

## Dia 75
Esperado:
- LoRA/SFT;
- talvez DPO;
- avaliação de persona.

## Dia 90
Esperado:
- sistema demonstrável;
- métricas;
- HF artifacts;
- relatório;
- research agenda.

---

# RETROSPECTIVA SEMANAL

Use estas perguntas no journal e na seção de aprendizado do checkpoint semanal.
O snapshot completo deve seguir [docs/checkpoints/TEMPLATE.md](docs/checkpoints/TEMPLATE.md):

```markdown
## Semana X

### Construí
...

### Aprendi
...

### Consigo explicar sem consultar
...

### Ainda não entendo
...

### Experimentos
...

### Principais erros
...

### Métricas
...

### Escopo a cortar
...

### Próxima semana
...
```

---

# DEFINITION OF DONE GLOBAL

Uma fase só está concluída quando:

- [ ] feature roda ponta a ponta;
- [ ] teste existe;
- [ ] métrica existe quando aplicável;
- [ ] baseline foi comparado;
- [ ] erro foi analisado;
- [ ] decisão foi documentada;
- [ ] você consegue explicar o conceito;
- [ ] journal está atualizado.

---

# REGRAS DE APRENDIZADO

## 1. Não copie primeiro
Para conceitos centrais:

`teoria → implementação mínima → biblioteca`

Exemplos:
- cosine similarity manual → NumPy/PyTorch → Sentence Transformers;
- TF-IDF conceitual → sklearn;
- retrieval manual → Qdrant.

## 2. Explique
Ao terminar cada módulo, explique por 5 minutos sem notas.

## 3. Use baseline
Modelo sofisticado sempre compete com algo simples.

## 4. Meça
“Parece melhor” não é resultado.

## 5. Preserve failures
Erros úteis entram na failure gallery.

## 6. Não treine fatos
Fatos documentados pertencem ao corpus/retrieval.

## 7. Não force persona
Se corpus não sustenta uma posição, responda `UNSUPPORTED`.

---

# O QUE NÃO BLOQUEIA O MVP

Estes itens podem ficar para depois do dia 90:
- GraphRAG completo;
- reward model próprio;
- GRPO;
- distillation;
- embedding fine-tuning próprio;
- multimodal video understanding;
- TTS/voice cloning;
- treinamento de LLM do zero;
- grande frontend customizado.

O produto central deve funcionar antes deles.
