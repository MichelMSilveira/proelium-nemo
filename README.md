# N.E.M.O.

## Nucleo de Engenharia e Memoria Operacional

Assistente inteligente local para engenharia, conhecimento técnico, organização de projetos e desenvolvimento assistido por IA.

> Projeto público em evolução. A N.E.M.O. é uma base experimental de memória e método, não um produto acabado nem uma fonte automática de decisões.

## Visão rápida

A N.E.M.O. combina modelo local, recuperação semântica de documentos e regras de contexto para apoiar projetos sem misturar automaticamente o conhecimento de empresas, clientes ou repositórios diferentes.

## Executar localmente

Requisitos atuais:

- Python;
- Ollama em execução local;
- modelo conversacional configurado no `Modelfile`;
- `chromadb`, `requests` e a função de embeddings do Ollama.

O fluxo principal está em `Sistema/`:

1. preparar ou recriar a memória com `Sistema/memoria.py`;
2. iniciar o assistente com `Sistema/nemo.py`;
3. usar `sair` para encerrar a sessão.

O arquivo `Iniciar_NEMO.bat` contém o atalho de inicialização usado no ambiente original. Os caminhos de memória e conhecimento ainda precisam ser configurados para cada máquina.

## Segurança e isolamento

- o modelo e a memória são locais;
- cada projeto deve manter sua própria fonte de verdade;
- regras, identidade, dados e processos não devem ser transferidos entre projetos sem validação;
- senhas, tokens, chaves e bases privadas não devem ser versionados;
- respostas devem diferenciar informação confirmada, inferência, hipótese e sugestão.

## Estado atual

A fundação conceitual, a base de conhecimento Proelium, a memória semântica e o padrão multi-projeto já estão documentados. A interface, a recuperação de conhecimento e as automações ainda estão em evolução.

---

# Visao Geral

A **N.E.M.O. (Nucleo de Engenharia e Memoria Operacional)** e uma plataforma de inteligencia artificial local criada para organizar conhecimento, apoiar decisoes tecnicas, auxiliar desenvolvimento e preservar contexto entre sessoes e projetos.

O projeto nasceu dentro da Proelium Servicos, mas sua arquitetura atual e **multi-projeto**. A N.E.M.O. fornece metodo, memoria e regras de trabalho; cada repositorio fornece seu proprio contexto, conhecimento, processos e regras de negocio.

A N.E.M.O. nunca deve transportar automaticamente regras, identidade, dados ou processos de um projeto para outro.

---

# Principios centrais

- Cada projeto e uma fonte de verdade independente.
- Informacao confirmada, inferencia, hipotese e sugestao sao categorias diferentes.
- Suposicoes nunca devem ser registradas como fatos.
- O contexto deve ser carregado de forma progressiva e apenas quando necessario.
- Decisoes importantes devem ser documentadas com seu motivo.
- Projetos devem possuir um estado curto e atualizado para facilitar retomadas.
- Alteracoes devem ser pequenas, reversiveis, testaveis e documentadas.
- Segredos, senhas, tokens, chaves e dados privados nao devem ser versionados.

---

# Arquitetura conceitual

```text
                    N.E.M.O.
                       |
        +--------------+--------------+
        |              |              |
   Metodo global   Memoria/IA    Padrao de projetos
        |              |              |
        +--------------+--------------+
                       |
          Contexto do projeto ativo
                       |
       +---------------+---------------+
       |               |               |
   Proelium         Jurandi       Outros projetos
   Operacional
```

A camada global define **como trabalhar**. O repositorio ativo define **com o que trabalhar**.

---

# Padrao de projetos assistidos por IA

O diretorio `PadraoProjetos/` contem a estrutura reutilizavel para projetos novos e para normalizar projetos ja existentes.

Estrutura recomendada:

```text
projeto/
|-- AGENTS.md
|-- PROJECT.md
|-- README.md
|-- docs/
|   |-- STATUS.md
|   |-- REQUIREMENTS.md
|   |-- DECISIONS.md
|   |-- KNOWLEDGE.md
|   `-- SESSION.md
|-- .continue/
|   `-- rules/
|       `-- projeto.md
`-- src/ ou estrutura nativa do projeto
```

## Ordem de contexto

1. `AGENTS.md`
2. `PROJECT.md`
3. `docs/STATUS.md`
4. arquivos diretamente relacionados a tarefa
5. `REQUIREMENTS.md`, `DECISIONS.md` e `KNOWLEDGE.md` apenas quando necessarios

Essa ordem evita carregar o repositorio inteiro e reduz perda de contexto em sessoes longas.

---

# Estrutura da N.E.M.O.

```text
NEMO/
|-- Conhecimento/
|-- Documentacao/
|-- Sistema/
|-- PadraoProjetos/
|-- Modelfile
`-- README.md
```

## Conhecimento

Mantem bases tecnicas e empresariais quando forem explicitamente necessarias. Conhecimento de uma empresa ou cliente nao e automaticamente global.

## Sistema

Contem componentes relacionados a memoria, assistente, testes e operacao da N.E.M.O.

## PadraoProjetos

Define as regras e arquivos-modelo para iniciar, documentar, retomar e evoluir projetos assistidos por IA.

---

# Tecnologias

## Inteligencia Artificial

- Ollama
- modelos de linguagem locais
- memoria baseada em arquivos e conhecimento estruturado
- contexto progressivo por projeto

## Desenvolvimento

- Python
- Git
- GitHub
- VS Code / Continue

---

# Fluxo recomendado

## Novo projeto

```text
Criar repositorio
      |
Aplicar PadraoProjetos
      |
Definir PROJECT.md
      |
Executar discovery
      |
Registrar requisitos
      |
Definir arquitetura
      |
Implementar
```

## Retomar projeto

```text
Abrir repositorio
      |
Ler AGENTS.md
      |
Ler PROJECT.md
      |
Ler STATUS.md
      |
Consultar SESSION.md se necessario
      |
Continuar a partir do proximo passo registrado
```

## Encerrar sessao

Atualizar o estado do projeto, registrar decisoes relevantes, registrar pendencias e deixar um proximo passo claro antes de encerrar uma etapa importante.

---

# Historico de evolucao

## Movimento 1 - Fundacao da N.E.M.O.

Criacao da identidade inicial e conceito do assistente.

## Movimento 2 - Base de Conhecimento Proelium

Organizacao inicial do conhecimento tecnico e empresarial.

## Movimento 3 - Inteligencia e Engenharia

Desenvolvimento da logica de memoria e apoio tecnico.

## Movimento 4 - Integracao do Assistente

Integracao inicial entre conhecimento, IA e consultas.

## Movimento 5 - Profissionalizacao GitHub

Implementacao de controle de versao e documentacao profissional.

## Movimento 6 - Arquitetura Multi-Projeto

Separacao entre regras globais da N.E.M.O. e contexto especifico de cada projeto, com padrao reutilizavel para criacao e retomada de projetos.

---

# Roadmap

## Curto prazo

- [ ] consolidar protocolo de discovery
- [ ] criar fluxo padrao iniciar / retomar / encerrar projeto
- [ ] normalizar projetos ativos com o novo padrao
- [ ] melhorar memoria inteligente
- [ ] ampliar testes automatizados

## Medio prazo

- [ ] interface de interacao
- [ ] integracao com voz
- [ ] mecanismos de busca e recuperacao de conhecimento
- [ ] automacoes de manutencao de contexto

## Longo prazo

- [ ] N.E.M.O. como assistente completo de engenharia e desenvolvimento
- [ ] inteligencia operacional integrada
- [ ] suporte a multiplos projetos e empresas com isolamento de contexto

---

# Filosofia

A N.E.M.O. nao e o conhecimento de uma unica empresa.

Ela e a **arquitetura que organiza, protege e utiliza o conhecimento de cada projeto sem misturar suas fontes de verdade**.

Projeto em evolucao continua.
