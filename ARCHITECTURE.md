# ARCHITECTURE — Novos Clássicos Persona Lab

> Estado no Dia 0: somente planejamento, sem componentes implementados. Whisper,
> pyannote, ECAPA e demais tecnologias citadas são candidatos a avaliar, não escolhas
> definitivas. Seleções devem ser sustentadas por experimentos e ADRs; o estado real
> fica em [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md).

## 1. Arquitetura-alvo

```text
                         FONTES
                           │
            ┌──────────────┼───────────────┐
            │              │               │
         YouTube            X         outras fontes
       vídeo/áudio       posts/replies      públicas
            │              │               │
            └──────────────┼───────────────┘
                           ▼
                  INGESTION / LINEAGE
                           │
                           ▼
                     AUDIO PIPELINE
              ┌────────────┼─────────────┐
              ▼            ▼             ▼
             ASR       DIARIZATION   SPEAKER ID
          Whisper        pyannote      ECAPA
              └────────────┼─────────────┘
                           ▼
                     CANONICAL CORPUS
                           │
          ┌────────────────┼──────────────────┐
          ▼                ▼                  ▼
       Antoun            Pessoa             outros
          │                │
          └────────────────┼──────────────────┘
                           ▼
                    NLP ENRICHMENT
     topic / entity / stance / argument / temporal metadata
                           │
                           ▼
                    KNOWLEDGE LAYER
        ┌──────────────────┼───────────────────┐
        ▼                  ▼                   ▼
     Vector DB         Temporal Index      Knowledge Graph
        │                  │                   │
        └──────────────────┼───────────────────┘
                           ▼
                    RETRIEVAL ENGINE
        BM25 + dense + sparse + metadata + reranking
                           │
                           ▼
                      RAG / EVIDENCE
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
        Antoun Persona              Pessoa Persona
       prompt / adapter             prompt / adapter
             │                           │
             └─────────────┬─────────────┘
                           ▼
                       DEBATE ENGINE
                           │
                           ▼
                    APPLICATION LAYER
       Character | Research | Search | Debate | Timeline
                           │
                           ▼
                         EVALS
```

## 2. Princípios

### 2.1 Rastreabilidade
Toda unidade deve ser rastreável:

`answer → evidence → chunk → segment → timestamp → source`

### 2.2 Separação WHAT × HOW

**WHAT** = conhecimento factual/documentado:
- corpus;
- retrieval;
- graph;
- temporal memory.

**HOW** = estilo:
- prompt de persona;
- style profile;
- LoRA/SFT/DPO.

Nunca usar fine-tuning como banco de fatos.

### 2.3 Speaker isolation
Nenhum componente de retrieval do agente Antoun deve recuperar Pessoa sem intenção explícita,
e vice-versa. Mesmo em comparações, preservar a atribuição da evidência.
Speakers válidos: `antoun`, `pessoa`, `guest`, `unknown`.
Baixa confiança deve virar `unknown`, nunca palpite.

### 2.4 Temporalidade
Toda evidência carrega data. “Atual” e “histórico” são consultas diferentes.

### 2.5 Grounding states
Toda resposta importante deve poder ser classificada como:
- `DIRECT`: posição explícita documentada;
- `INFERRED`: inferência sustentada por evidências relacionadas;
- `UNSUPPORTED`: corpus insuficiente.

### 2.6 Modelos substituíveis
ASR, embedding, reranker, LLM e classificadores devem ficar atrás de interfaces simples.

## 3. Schema canônico mínimo

Proposta a validar na Fase 0. O exemplo abaixo é ilustrativo, não um registro coletado.

```json
{
  "segment_id": "nc_0382_002533_antoun",
  "speaker": "antoun",
  "source": {
    "platform": "youtube",
    "source_id": "VIDEO_ID",
    "title": "NC Show #382",
    "date": "2026-05-17"
  },
  "time": {
    "start": 2533.43,
    "end": 2571.81
  },
  "text": {
    "raw": "...",
    "normalized": "..."
  },
  "context": {
    "previous_segment_id": "...",
    "next_segment_id": "..."
  },
  "annotations": {
    "topics": [],
    "entities": [],
    "stances": [],
    "speech_act": null
  },
  "quality": {
    "asr_confidence": null,
    "speaker_confidence": null,
    "reviewed": false
  }
}
```

## 4. Estrutura sugerida do repositório

Expansão futura, conforme as fases. A estrutura efetivamente preparada no Dia 0 está
em [INITIAL_REPO_TREE.md](INITIAL_REPO_TREE.md); Makefile, pyproject.toml e módulos
abaixo ainda não existem.

```text
.
├── README.md
├── ROADMAP_90_DIAS.md
├── LEARNING_ROADMAP.md
├── ARCHITECTURE.md
├── EXPERIMENTS.md
├── RESOURCES.md
├── INITIAL_REPO_TREE.md
├── PROJECT_CONTEXT.md
├── AGENTS.md
├── CONTRIBUTING.md
├── Makefile
├── pyproject.toml
├── configs/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── gold/
├── src/
│   ├── ingestion/
│   ├── speech/
│   ├── corpus/
│   ├── nlp/
│   ├── retrieval/
│   ├── rag/
│   ├── persona/
│   ├── agents/
│   └── evals/
├── experiments/
├── tests/
└── docs/
    ├── research/
    ├── journal/
    ├── adr/
    └── checkpoints/
```

## 5. Hugging Face como backbone

### Hub
Guardar/publicar, conforme direitos e licenças permitirem:
- datasets;
- models;
- adapters;
- Spaces;
- eval artifacts;
- papers/model cards/dataset cards.

### Datasets
Corpus tipado e versionado.

### Transformers
ASR, encoders, classificadores e LLMs.

### Sentence Transformers
Dense retrieval, contrastive training e cross-encoder/reranking.

### PEFT
LoRA/adapters.

### TRL
SFT e preference optimization.

### Accelerate
Treino/inferência em configurações diferentes.

### Evaluate
Métricas e suites.

### Spaces
Demo.

## 6. Responsible AI

A interface deve declarar que é uma **simulação baseada em corpus público**, não a pessoa real.

Nunca apresentar como fala real:
- conteúdo inventado;
- acusação;
- admissão;
- nova posição política;
- fato pessoal não documentado.

Para `INFERRED`, sinalizar inferência.

Para `UNSUPPORTED`, abster-se de atribuir posição.

Antes de redistribuir corpus integral, verificar termos das plataformas, copyright e permissões. Quando necessário, publicar apenas IDs, timestamps, annotations, hashes e scripts de reconstrução.
