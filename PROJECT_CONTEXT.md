# Project Context — Novos Clássicos Persona Lab

Snapshot resumido e mutável. O repositório é a fonte da verdade; conversas são insumos.
Atualizado em: 2026-09-07.

## Current Phase

- Phase: Repository initialization — preparação documental anterior à Fase 0.
- Day: 0.
- Sprint: Not started.
- Status: No product code implemented.

## Current Objective

Estabelecer documentação e memória para os 90 dias de desenvolvimento de duas
personas independentes, Antoun e Pessoa, fundamentadas no corpus público do
Novos Clássicos Show. Ciclo: ESTUDAR → IMPLEMENTAR → MEDIR → DOCUMENTAR → REVISAR.

## Completed

- Documentos de arquitetura, execução, estudos e pesquisa disponíveis.
- Regras para agentes, contribuição e snapshot atual documentados.
- Template de checkpoint e diretórios iniciais preparados.
- Nenhuma fase técnica concluída.

## In Progress

Nenhuma implementação ou experimento em andamento.

## Next

Iniciar o Dia 1 da [Fase 0](ROADMAP_90_DIAS.md): preparar ambiente Python,
definir gerenciador, configurar ferramentas de qualidade e registrar a stack em ADR.
Confirmar hardware disponível. Aprendizagem será avaliada pelo usuário.

## Current Architecture

Somente [arquitetura-alvo](ARCHITECTURE.md); nenhum componente implementado.
Fluxo previsto: ingestão → speech → corpus → NLP → retrieval → RAG → personas → avaliação.
WHAT = corpus + retrieval + evidências; HOW = estilo + persona + adapters.
Antoun e Pessoa permanecem isolados; evidências preservam fonte e timestamp.

## Current Models

- ASR: Not selected.
- Diarization: Not selected.
- Speaker Identification: Not selected.
- Embedding: Not selected.
- Reranker: Not selected.
- LLM: Not selected.
- Adapter strategy: Not selected.
- Vector database: Not selected.

Nomes no roadmap e nos recursos são candidatos, sujeitos a experimento e ADR.

## Current Datasets

Not started. Nenhuma coleta; corpus e gold dataset ainda não existem.
Nomes como `NC-Corpus-v0` e `NC-Gold-v1` são entregáveis planejados.

## Relevant Experiments

Nenhum executado. [EXPERIMENTS.md](EXPERIMENTS.md) contém apenas o registro planejado.

## Current Metrics

N/A — nenhuma medição realizada.

## Known Problems

Ambiente Python, testes, lint, CI e hardware ainda não configurados/documentados.
Não há falhas de produto observadas, pois não há produto implementado.

## Constraints

- Escopo atual: preparação documental; sem coleta, código de ML ou instalação de bibliotecas.
- Planejamento de aproximadamente 90 dias; priorizar dados, speech, retrieval, RAG e avaliação.
- Nunca treinar com gold dataset nem substituir baseline sem evidência.
- Baixa confiança de speaker resulta em `unknown`; não inventar posições.
- Apenas o usuário atualiza o próprio progresso em LEARNING_ROADMAP.md.

## Recent Decisions

Organização documental definida pelo pedido inicial: estado atual aqui, decisões em
ADRs, evidências em experimentos e snapshots históricos em checkpoints.
Nenhum ADR técnico aceito; stack e modelos continuam pendentes.

## Last Checkpoint

N/A. Existe somente o [template](docs/checkpoints/TEMPLATE.md).
Criar `docs/checkpoints/week-01.md` ao final do primeiro sprint.
