# AGENTS — Regras de trabalho no repositório

## Leitura inicial obrigatória

Leia nesta ordem, antes de trabalhar:

1. [AGENTS.md](AGENTS.md).
2. [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md).
3. [ROADMAP_90_DIAS.md](ROADMAP_90_DIAS.md).
4. [ARCHITECTURE.md](ARCHITECTURE.md).
5. [EXPERIMENTS.md](EXPERIMENTS.md).
6. ADRs relevantes em [docs/adr/](docs/adr/), quando existirem.

Não é necessário ler RESOURCES.md inteiro a cada tarefa; consulte materiais pertinentes.
O repositório é a fonte da verdade. Não deduza implementação, domínio conceitual ou
escolha definitiva de modelo a partir de um plano ou de uma conversa antiga.

## Mapa de memória

- README: visão geral e navegação; não é diário.
- PROJECT_CONTEXT: estado atual resumido; atualizar, sem acumular histórico.
- ROADMAP_90_DIAS: execução, próximas tarefas e Definition of Done.
- LEARNING_ROADMAP: aprendizado pessoal; somente o usuário altera seu progresso.
- ARCHITECTURE: componentes, contratos, fluxos e princípios; distinguir alvo de implementação.
- EXPERIMENTS e experiments/: metodologia, registro e evidências.
- docs/adr/: decisões, alternativas, consequências e evidências.
- docs/journal/: trajetória técnica e dúvidas; não é fonte do estado atual.
- docs/research/: perguntas de pesquisa; RESOURCES: biblioteca de estudos.
- docs/checkpoints/: snapshots históricos imutáveis; Git preserva a evolução.

ChatGPT atua como mentor; Codex atua sobre o repositório; o usuário conduz o projeto.
Conclusões relevantes de sessões devem ser registradas no documento apropriado,
com evidência quando aplicável, para permitir retomada sem o histórico de conversas.

## Antes de implementar

Identifique e registre na descrição da tarefa ou artefato pertinente:

- Roadmap phase e dia.
- Current objective e escopo autorizado.
- Relevant EXP-ID; se não for experimento, registrar N/A e motivo.
- Relevant ADR; registrar ausência ou proposta pendente, sem inventar decisões.
- Definition of Done e validações aplicáveis.

Se for claramente um experimento sem EXP-ID, registre um ID único em EXPERIMENTS.md
antes de executar e crie seu relatório em experiments/. Nomes no plano são candidatos,
não decisões aceitas. Decisões arquiteturais importantes exigem ADR com contexto,
decisão, alternativas, consequências e links para experimentos/evidências existentes.

## Regras de engenharia

- Python é a linguagem principal; usar type hints e pytest para testes.
- Manter código modular, funções pequenas quando possível e interfaces simples.
- Modelos devem ser substituíveis, com configuração externa de modelo e revision.
- Nunca hardcodar tokens nem commitar secrets; usar variáveis de ambiente e exemplos sem credenciais.
- Usar logging estruturado, sem expor credenciais.
- Preservar data lineage: fonte, timestamps, IDs, versões e transformações.
- Evitar dependências desnecessárias e código placeholder sem utilidade.
- Não instalar bibliotecas de ML nem coletar dados para tarefas apenas documentais.

## Regras de ML

- Nunca usar gold dataset para treinamento; preservar a separação de treino, validação e teste.
- Nunca substituir baseline sem experimento comparável e evidência registrada.
- Toda comparação importante deve possuir EXP-ID, hipótese e baseline explícitos.
- Registrar modelo Hugging Face e versão/revision, dataset version, splits e configuração.
- Registrar seed, commit, ambiente e hardware quando relevante.
- Registrar métricas, custos quando pertinentes e resultados reproduzíveis.
- Preservar resultados negativos; fazer error analysis e documentar conclusão/decisão.
- Um experimento planejado não é um experimento executado; não inventar resultados.

## Regras de persona

- Antoun e Pessoa devem permanecer isolados em dados de persona, retrieval e adapters.
- Retrieval de Antoun não pode misturar Pessoa silenciosamente, nem o inverso.
  Comparações explícitas devem preservar a atribuição de cada evidência.
- Speakers válidos: `antoun`, `pessoa`, `guest`, `unknown`.
- Baixa confiança deve resultar em `unknown`, nunca palpite ou atribuição automática a `guest`.
- Evidências possuem timestamp e fonte; preservar também data para consultas temporais.
- WHAT = corpus + retrieval + evidências. HOW = estilo + persona + adapters.
- Fine-tuning não é banco de fatos. Não inventar posições nem apresentar simulação como fala real.
- `DIRECT`: posição explícita documentada.
- `INFERRED`: inferência sustentada por evidências, sinalizada como inferência.
- `UNSUPPORTED`: evidência insuficiente; abster-se de atribuir posição.

## Depois de implementar

1. Rodar testes relevantes.
2. Rodar lint quando configurado.
3. Executar smoke test do fluxo afetado.
4. Executar eval relevante quando existir.
5. Atualizar o experimento aplicável, incluindo resultados negativos e error analysis.
6. Atualizar documentação afetada e ADR quando necessário.
7. Atualizar PROJECT_CONTEXT.md se o estado do projeto mudou.
8. Atualizar checkboxes de ROADMAP_90_DIAS.md apenas para itens realmente concluídos.

Registrar comandos, resultados e limitações. Para alterações exclusivamente documentais,
verificar links locais, coerência da estrutura e diff; testes de produto, smoke test e eval
são N/A enquanto não houver código. Não criar uma stack apenas para validar documentação.
Não atualizar LEARNING_ROADMAP.md automaticamente nem presumir aprendizado do usuário.

## Checkpoints e Git

Ao final de cada sprint semanal, usar [o template](docs/checkpoints/TEMPLATE.md) para
criar `docs/checkpoints/week-XX.md`, com estado observado e referências a ADRs/EXP-IDs.
Não criar week-01 antes de terminar o primeiro sprint. Não reescrever checkpoints
para refletir decisões futuras; registrar correções em novo documento que referencie o original.

Preferir commits semânticos, com escopo e resultado concreto; exemplos e fluxo em
[CONTRIBUTING.md](CONTRIBUTING.md). Evitar mensagens como `update`, `fix`, `stuff`,
`working` ou `changes` sem contexto.
