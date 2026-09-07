# Diário Técnico — Dia 1

## Data / fase / objetivo

2026-09-07 — Sprint 1, Fase 0. Fundação Python, sem código de produto.
EXP-ID: N/A. DoD: ambiente reproduzível, import, teste, lint, formatter e CI configurado.

## Inspeção inicial

- CachyOS Linux rolling, x86_64; Python 3.11.14 via pyenv; Git 2.55.0.
- uv 0.11.7, pip 26.1.2, Ruff global 0.15.11, pytest global 9.1.1.
- venv/ensurepip disponíveis; Poetry/mypy não encontrados no PATH.
- Branch main acompanhando origin/main, árvore limpa, commit 2d12441.
- Nenhuma instalação anterior à conclusão da inspeção.

## Hardware observado

- Intel Core i5-13450HX: 10 núcleos, 16 CPUs lógicas.
- RAM e swap reportadas por free -h: 23 GiB cada.
- nvidia-smi: NVIDIA GeForce RTX 3050 6GB Laptop GPU, 6144 MiB.
- Sem teste de CUDA/PyTorch ou benchmark de hardware.

## O que implementei

Pacote mínimo, pyproject, lockfile, pytest/Ruff no grupo dev, gitignore,
env.example e workflow CPU. Python 3.11.14, uv 0.11.7, pytest 9.1.1 e Ruff 0.15.22
no ambiente local; ferramentas globais preservadas. Runtime sem dependências.

## Validações

- uv sync --locked e uv lock --check: ambiente e lock consistentes.
- uv run --locked pytest: 1 passed.
- uv run --locked ruff check .: All checks passed.
- uv run --locked ruff format --check .: 2 files already formatted.
- Smoke import: novos_classicos_lab.__version__ retorna 0.1.0.
- Ambiente temporário independente recriado do lock: teste, lint e formatter aprovados.
- Gitignore: 17 cenários aprovados; metadados e gold datasets continuam versionáveis.
- CI remoto ainda não executado; eval de ML: N/A.

## Decisão

[ADR-0001](../adr/ADR-0001-python-project-structure.md): uv, Python 3.11, pytest e Ruff.

## Aprendizado pessoal / dúvidas

Não aferidos; preencher pelo usuário. LEARNING_ROADMAP.md preservado.

## Pendências / próxima ação

Revisar e commitar a entrega; observar primeiro CI remoto. Estudos pessoais e conta
Hugging Face Hub pendentes. Dataset dummy e schema ficam para o Dia 2, não iniciado.
