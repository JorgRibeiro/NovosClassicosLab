# INITIAL_REPO_TREE

Estrutura preparada no **Dia 0**, somente documentação e diretórios reservados.
`.gitkeep` mantém diretórios vazios no Git; não há código de produto.

```text
novos-classicos-persona-lab/
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
├── configs/
│   └── .gitkeep
├── data/
│   └── .gitkeep
├── src/
│   └── .gitkeep
├── tests/
│   └── .gitkeep
├── experiments/
│   └── .gitkeep
└── docs/
    ├── research/
    │   └── RESEARCH_TRACK.md
    ├── journal/
    │   └── TEMPLATE.md
    ├── adr/
    │   └── TEMPLATE.md
    └── checkpoints/
        └── TEMPLATE.md
```

## Expansão prevista

Conforme a implementação começar, a estrutura sugerida em
[ARCHITECTURE.md](ARCHITECTURE.md) poderá ganhar:

- `data/raw/`, `data/interim/`, `data/processed/` e `data/gold/`;
- módulos `src/ingestion/`, `src/speech/`, `src/corpus/`, `src/nlp/`,
  `src/retrieval/`, `src/rag/`, `src/persona/`, `src/agents/` e `src/evals/`;
- configuração de ambiente, ferramentas de qualidade e CI no Dia 1;
- relatórios `experiments/EXP-XXX-nome.md` e ADRs ao executar tarefas pertinentes;
- `docs/checkpoints/week-01.md` somente ao final do primeiro sprint.

Essa expansão é planejada, não implementada nem uma decisão definitiva de stack.
