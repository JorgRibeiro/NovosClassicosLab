# Project Context — Novos Clássicos Persona Lab

Snapshot resumido e mutável. O repositório é a fonte da verdade; conversas são insumos.
Atualizado em: 2026-09-07.

## Current Phase

- Phase: Fase 0 — preparação e baseline mental.
- Day: 1.
- Sprint: 1.
- Status: No product code implemented.

## Current Objective

Preparar a fundação de engenharia Python do Persona Lab. DoD técnico local do Dia 1
validado; CI configurado e ainda não executado remotamente. Dia 2 não iniciado.

## Completed

- Documentos de arquitetura, execução, estudos e pesquisa disponíveis.
- Regras para agentes, contribuição e snapshot atual documentados.
- Template de checkpoint e diretórios iniciais preparados.
- Pacote instalável, teste de import, lint/formatter, lockfile, gitignore e env.example.
- CI mínimo configurado; ADR-0001 e journal do Dia 1 registrados.
- Fase 0 ainda em andamento; estudos pessoais não aferidos.

## In Progress

Entrega de engenharia do Dia 1 pronta para revisão/commit; nenhum experimento em andamento.

## Next

Revisar/commitar a entrega e acompanhar o primeiro CI remoto. Estudos e configuração
do Hub pendentes. Dia 2 reservado a Hub/Datasets, dataset dummy e schema, sem execução agora.

## Current Architecture

[Arquitetura-alvo](ARCHITECTURE.md) ainda sem componentes de produto implementados.
Fundação: pacote src/novos_classicos_lab, versão 0.1.0, sem dependências de runtime.
Ambiente: uv 0.11.7, Python 3.11.14 (faixa >=3.11,<3.12), pytest 9.1.1, Ruff 0.15.22.
Build: Hatchling 1.29.0. Instalação: `uv sync --locked`; versões em uv.lock.
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

CI remoto ainda não executado. Entrega do Dia 1 ainda sem commit.
Hardware registrado no [journal](docs/journal/day-01.md); GPU não validada para ML.
Não há falhas de produto observadas, pois não há produto implementado.

## Constraints

- Escopo atual: fundação de engenharia do Dia 1; sem coleta, modelos ou código de produto.
- Planejamento de aproximadamente 90 dias; priorizar dados, speech, retrieval, RAG e avaliação.
- Nunca treinar com gold dataset nem substituir baseline sem evidência.
- Baixa confiança de speaker resulta em `unknown`; não inventar posições.
- Apenas o usuário atualiza o próprio progresso em LEARNING_ROADMAP.md.

## Recent Decisions

Organização documental definida pelo pedido inicial: estado atual aqui, decisões em
ADRs, evidências em experimentos e snapshots históricos em checkpoints.
[ADR-0001](docs/adr/ADR-0001-python-project-structure.md) aceito: uv, Python 3.11,
pytest e Ruff. Type checker adiado; modelos continuam pendentes.

## Last Checkpoint

N/A. Existe somente o [template](docs/checkpoints/TEMPLATE.md).
Criar `docs/checkpoints/week-01.md` ao final do primeiro sprint.
