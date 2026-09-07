# EXPERIMENTS

## Regra

Cada experimento deve responder **uma pergunta concreta**.

Não registrar “testei modelo X”. Registrar:

> O modelo X melhora a métrica Y comparado ao baseline Z no dataset V?

## Template

```markdown
# EXP-XXX — Nome

## Pergunta
...

## Hipótese
...

## Baseline
...

## Dataset
- versão:
- split:
- tamanho:

## Modelo
- repo/revision:
- tokenizer:
- adapter:

## Ambiente
- commit:
- Python:
- PyTorch:
- GPU:
- VRAM:
- seed:

## Configuração
...

## Métricas
...

## Resultados
| Métrica | Baseline | Experimento |
|---|---:|---:|

## Error analysis
...

## Conclusão
...

## Decisão
...

## Próximo experimento
...
```

## Registro sugerido

### Speech
- EXP-001 subtitles-vs-whisper
- EXP-002 whisper-model-size
- EXP-003 pyannote-baseline
- EXP-004 diarization-speaker-count
- EXP-005 ecapa-speaker-id
- EXP-006 speaker-threshold
- EXP-007 contamination-detection

### NLP
- EXP-020 tfidf-topic-baseline
- EXP-021 zero-shot-topic
- EXP-022 bertimbau-topic
- EXP-023 entity-extraction
- EXP-024 stance-baseline

### Retrieval
- EXP-040 bm25
- EXP-041 bge-m3
- EXP-042 multilingual-e5
- EXP-043 hybrid
- EXP-044 reranker
- EXP-045 conversational-chunking
- EXP-046 hard-negatives

### RAG
- EXP-060 rag-basic
- EXP-061 metadata-filter
- EXP-062 citations
- EXP-063 temporal-retrieval
- EXP-064 direct-inferred-unsupported

### Persona
- EXP-080 prompt-only
- EXP-081 rag-persona-prompt
- EXP-082 antoun-lora
- EXP-083 pessoa-lora
- EXP-084 sft
- EXP-085 dpo
- EXP-086 persona-leakage
- EXP-087 persona-ablation

### Systems
- EXP-100 int8-int4
- EXP-101 latency
- EXP-102 batching
- EXP-103 local-vs-cloud

## Golden Dataset

Criar `NC-Gold-v1` antes de treinos grandes.

Mínimo recomendado:
- 300–500 segmentos revisados manualmente;
- 50–100 perguntas;
- tópicos variados;
- episódios diferentes;
- exemplos de Antoun;
- exemplos de Pessoa;
- convidados;
- discordâncias;
- posições alteradas ao longo do tempo;
- perguntas sem resposta no corpus.

Nunca usar o gold set para treinar.

## Ablation matrix

Comparar:

| Sistema | BM25 | Dense | Reranker | RAG | LoRA | Temporal |
|---|---|---|---|---|---|---|
| A | ✓ | | | | | |
| B | | ✓ | | | | |
| C | ✓ | ✓ | | | | |
| D | ✓ | ✓ | ✓ | ✓ | | |
| E | ✓ | ✓ | ✓ | ✓ | ✓ | |
| F | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Failure taxonomy

Manter categorias:
- ASR error
- diarization error
- speaker attribution error
- context loss
- retrieval miss
- wrong-speaker retrieval
- stale/temporal error
- hallucinated claim
- citation mismatch
- persona style failure
- persona leakage
- unsupported inference
- prompt injection/adversarial failure
