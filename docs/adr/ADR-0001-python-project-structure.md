# ADR-0001 — Fundação Python com uv, pytest e Ruff

- Status: accepted
- Data: 2026-09-07
- Fase: 0, Dia 1

## Contexto

O projeto terá scripts, testes, grupos de dependências, CI e experimentos com ML.
A inspeção encontrou Python 3.11.14 via pyenv, uv 0.11.7 e Git 2.55.0 disponíveis.
Não há código de produto nem requisitos reais de modelos definidos.

## Decisão

Usar uv 0.11.7, `.venv`, `pyproject.toml` e `uv.lock`. Fixar Python 3.11.14 em
`.python-version` e suportar inicialmente a linha 3.11 (`>=3.11,<3.12`), já disponível
e validada. Revisar a faixa quando existirem requisitos reais de ML; esta decisão
não presume compatibilidade de modelos ou CUDA.

Layout `src/novos_classicos_lab/`, metadata mínimo e Hatchling 1.29.0 como backend
explícito de build para instalação do pacote. Nenhuma dependência de runtime.
Grupo `dev` com pytest e Ruff; ferramentas e dependências transitivas fixadas pelo lock.
Ruff atende lint e formatter. Type checker adiado até existir lógica que o justifique;
manter type hints. Sem Makefile, Docker ou pre-commit neste momento.

CI GitHub Actions em CPU, com uv na mesma versão local, Python fixado,
`uv sync --locked`, pytest, lint e verificação de formatação.

## Alternativas consideradas

| Opção | Adequação ao projeto |
|---|---|
| uv | Já disponível; integra ambiente, lock, grupos e execução. Documentação para integração futura com PyTorch. Escolhido. |
| Poetry | Alternativa válida com lock e grupos; exigiria instalar outro gerenciador sem necessidade concreta hoje. |
| venv + pip | Isolamento simples, mas exigiria convenções adicionais para lock, grupos e sincronização equivalentes. |

## Consequências

### Positivas

- Mesmo lock no desenvolvimento e CI; `--locked` detecta divergências de configuração.
- Teste importa o pacote instalado sem injetar src em PYTHONPATH.
- Python existente reutilizado; ambiente global preservado.
- Grupos de ML e índices CPU/CUDA serão definidos quando necessários.

### Negativas

- Fluxo principal depende de uv; manter sua versão alinhada ao CI.
- Outra linha Python exige validação e revisão da faixa suportada.
- Lock não torna SO, hardware ou futuros resultados de ML idênticos.

## Evidências / experimentos relacionados

EXP-ID: N/A — fundação de engenharia, sem experimento de ML.
Teste, import, lint, formatter e recriação do ambiente aprovados localmente.
Detalhes no [journal do Dia 1](../journal/day-01.md). CI remoto ainda não executado.

Referências oficiais consultadas:

- [uv: lock e sincronização](https://docs.astral.sh/uv/concepts/projects/sync/).
- [uv: PyTorch](https://docs.astral.sh/uv/guides/integration/pytorch/).
- [Poetry: dependências](https://python-poetry.org/docs/managing-dependencies/).
- [Python: venv](https://docs.python.org/3.11/library/venv.html).
- [uv: GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/).

## Revisitar quando

Dependências reais exigirem outro Python, grupos para speech/treino/avaliação ou
índices específicos de wheels CPU/CUDA. Modelos continuam sem escolha definitiva.
