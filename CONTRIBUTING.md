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
Não há comandos de setup/teste de produto disponíveis no Dia 0; defini-los no Dia 1.

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
