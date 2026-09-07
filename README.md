# Novos Clássicos Persona Lab

> Programa intensivo de 90 dias para construir uma plataforma de personas fundamentadas em corpus público, usando Speech AI, NLP, Information Retrieval, RAG, PEFT, pós-treinamento, agentes, avaliação e MLOps — com o ecossistema Hugging Face como eixo principal.

## Visão

O objetivo não é simplesmente “treinar duas LLMs”. O projeto deverá produzir:

1. um **corpus estruturado e rastreável** de Antoun e Pessoa;
2. um pipeline de **transcrição, diarização e identificação de speaker**;
3. uma camada de **NLP enrichment**;
4. um mecanismo de **busca semântica/híbrida**;
5. um **RAG com citações e temporalidade**;
6. duas **personas independentes**;
7. experimentos com **PEFT/LoRA, SFT e DPO**;
8. um **modo debate multiagente**;
9. um framework de **avaliação de persona, grounding e leakage**;
10. uma demo pública/privada via **Hugging Face Spaces**;
11. um portfólio de **datasets, models, adapters, evals e relatórios**.

## Regra central

Cada fase deve combinar:

**ESTUDAR → IMPLEMENTAR → MEDIR → DOCUMENTAR → REVISAR**

Nenhuma tecnologia entra no sistema apenas porque “é popular”. Sempre que possível, compare com um baseline mais simples.

## Documentos principais

- [ROADMAP_90_DIAS.md](ROADMAP_90_DIAS.md) — execução diária e semanal.
- [LEARNING_ROADMAP.md](LEARNING_ROADMAP.md) — trilha conceitual.
- [ARCHITECTURE.md](ARCHITECTURE.md) — arquitetura-alvo e princípios.
- [EXPERIMENTS.md](EXPERIMENTS.md) — metodologia de experimentação.
- [RESOURCES.md](RESOURCES.md) — livros, papers, cursos, vídeos e documentação.
- [docs/research/RESEARCH_TRACK.md](docs/research/RESEARCH_TRACK.md) — hipóteses de IC/TCC.
- [docs/journal/TEMPLATE.md](docs/journal/TEMPLATE.md) — diário técnico.
- [docs/adr/TEMPLATE.md](docs/adr/TEMPLATE.md) — Architecture Decision Record.

## Critério de sucesso dos 90 dias

### Obrigatório
- [ ] pipeline reproduzível de ingestão de episódios;
- [ ] ASR com timestamps;
- [ ] diarização;
- [ ] identificação Antoun/Pessoa/outro;
- [ ] corpus v1 versionado;
- [ ] golden set;
- [ ] BM25 baseline;
- [ ] dense retrieval;
- [ ] hybrid retrieval;
- [ ] reranking;
- [ ] RAG com filtros por speaker e fonte;
- [ ] respostas com citações;
- [ ] Antoun e Pessoa isolados;
- [ ] avaliação automática;
- [ ] avaliação humana pequena;
- [ ] demo funcional;
- [ ] relatório final.

### Avançado
- [ ] topic classifier próprio;
- [ ] stance detection;
- [ ] persona LoRA;
- [ ] SFT;
- [ ] DPO;
- [ ] memória temporal;
- [ ] modo debate;
- [ ] knowledge graph inicial.

### Research
- [ ] Persona Fidelity Benchmark;
- [ ] Persona Leakage Score;
- [ ] ablation studies;
- [ ] contamination study;
- [ ] quantization study;
- [ ] paper-style report.

## Filosofia de escopo

Se no dia 90 estiverem excelentes:

**dados + speech + retrieval + RAG + avaliação**

e LoRA/DPO/GraphRAG ficarem incompletos, o projeto ainda será um grande sucesso.

Qualidade e compreensão vencem quantidade de features.
