# Contribuindo com o Persona Lab

Comece pela ordem de leitura em [AGENTS.md](AGENTS.md) e pelo snapshot em
[PROJECT_CONTEXT.md](PROJECT_CONTEXT.md). O ciclo é
**ESTUDAR → IMPLEMENTAR → MEDIR → DOCUMENTAR → REVISAR**.

## Retomada e encerramento de uma sessão

1. Localize a fase, objetivo, Definition of Done, EXP-ID e ADR pertinentes.
2. Execute o escopo da tarefa; compare mudanças de desempenho com baseline.
3. Valide conforme AGENTS.md e registre comandos, resultados e limitações.
4. Registre decisões em ADRs e evidências em experiments/, com índice em EXPERIMENTS.md.
5. Atualize documentos afetados e o snapshot atual; marque apenas tarefas concluídas.
6. Use o journal para trajetória, dúvidas e aprendizados relatados pelo usuário.

Somente o usuário decide quando marcar um conceito em LEARNING_ROADMAP.md.
Materiais de estudo ficam em RESOURCES.md; questões científicas, em docs/research/.
## Ambiente e comandos

Pré-requisito: uv 0.11.7 (versão também fixada no CI). Python 3.11.14 está fixado em
.python-version; `uv python install` pode instalá-lo se não estiver disponível.

```bash
uv python install
uv sync --locked
uv run --locked pytest
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked ruff format .
uv run --locked python -c 'import novos_classicos_lab; print(novos_classicos_lab.__version__)'
```

Para executar `pytest` diretamente: `source .venv/bin/activate`, depois `pytest`.
Use o interpretador `.venv/bin/python` no editor.

Versionar pyproject.toml, .python-version e uv.lock juntos. Após uma mudança intencional
nas dependências, executar `uv lock`, revisar o diff e validar novamente. Não usar
pip global para instalar dependências deste projeto. O grupo dev é incluído por padrão;
runtime permanece sem dependências. Type checker adiado conforme ADR-0001.

Dados locais não versionáveis devem ficar em `data/local/`; pesos em `models/` e
saídas temporárias em `outputs/` ou `artifacts/`. Manifests e metadados ficam fora
dessas áreas, por exemplo `data/manifests/` e `experiments/`. `data/gold/` não está
ignorado: revisar conteúdo e permissão antes de versionar. Checkpoints documentais
em docs/checkpoints/ continuam versionáveis. `.env.example` não contém credenciais e
não precisa ser copiado no Dia 1. O pacote não carrega `.env` automaticamente.

CI: [.github/workflows/ci.yml](.github/workflows/ci.yml), em push/pull request,
sem modelos ou GPU. Sua execução remota depende do envio ao GitHub.

## Ponte entre ChatGPT, Codex e trabalho manual

O usuário pode levar PROJECT_CONTEXT.md e os ADRs/experimentos relevantes ao mentor.
Ao retornar ao repositório, registrar propostas como propostas e decisões aceitas como
decisões, preservando suas evidências. Nenhuma conversa substitui o estado registrado.
O README orienta a navegação; o journal não substitui o snapshot atual.

Ao final do sprint semanal, criar um checkpoint usando
[docs/checkpoints/TEMPLATE.md](docs/checkpoints/TEMPLATE.md) e atualizar o link
Last Checkpoint em PROJECT_CONTEXT.md. Checkpoints preservam o estado daquele momento;
correções posteriores ficam em novo registro referenciando o original.

## Git como memória

Prefira commits semânticos no formato `tipo(escopo): resultado concreto`.
Cada commit deve reunir mudanças relacionadas, com diff revisado e sem secrets.
Não inclua corpus, pesos ou resultados volumosos sem estratégia de versionamento definida.

Exemplos para futuras entregas:

```text
feat(speech): add whisper transcription pipeline
feat(diarization): integrate pyannote pipeline
exp(retrieval): benchmark bge-m3 against bm25
fix(corpus): prevent guest segments entering persona dataset
docs(adr): record vector store decision
```

Evite mensagens isoladas como `update`, `fix`, `stuff`, `working` e `changes`.
No corpo, quando útil, inclua EXP-ID, ADR, motivação e validação para permitir reconstruir
o contexto a partir do histórico Git.
