# INITIAL_REPO_TREE

Estrutura atual no **Dia 1**, com fundação Python e documentação.
`.gitkeep` mantém diretórios vazios no Git; não há código de produto.

```text
novos-classicos-persona-lab/
├── .github/workflows/ci.yml
├── .gitignore
├── .env.example
├── .python-version
├── pyproject.toml
├── uv.lock
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
│   └── novos_classicos_lab/__init__.py
├── tests/
│   └── test_package.py
├── experiments/
│   └── .gitkeep
└── docs/
    ├── research/
    │   └── RESEARCH_TRACK.md
    ├── journal/
    │   ├── day-01.md
    │   └── TEMPLATE.md
    ├── adr/
    │   ├── ADR-0001-python-project-structure.md
    │   └── TEMPLATE.md
    └── checkpoints/
        └── TEMPLATE.md
```

## Expansão prevista

Conforme a implementação começar, a estrutura sugerida em
[ARCHITECTURE.md](ARCHITECTURE.md) poderá ganhar:

- `data/raw/`, `data/interim/`, `data/processed/` e `data/gold/`;
- módulos `src/novos_classicos_lab/ingestion/`, `src/novos_classicos_lab/speech/`, `src/novos_classicos_lab/corpus/`, `src/novos_classicos_lab/nlp/`,
  `src/novos_classicos_lab/retrieval/`, `src/novos_classicos_lab/rag/`, `src/novos_classicos_lab/persona/`, `src/novos_classicos_lab/agents/` e `src/novos_classicos_lab/evals/`;
- novos grupos de dependências quando houver necessidade;
- relatórios `experiments/EXP-XXX-nome.md` e ADRs ao executar tarefas pertinentes;
- `docs/checkpoints/week-01.md` somente ao final do primeiro sprint.

Essa expansão de produto é planejada; a fundação de engenharia está registrada no ADR-0001.
