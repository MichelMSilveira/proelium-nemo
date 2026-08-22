# DISCOVERY

## Objetivo

Transformar informacoes iniciais do usuario ou cliente em entendimento verificavel antes de definir arquitetura ou implementar funcionalidades relevantes.

## Regras

1. Nao escolher stack por habito antes de entender o problema.
2. Nao importar processos de outro projeto.
3. Registrar a origem das informacoes relevantes.
4. Separar confirmado, hipotese, inferencia e sugestao.
5. Perguntas sem resposta viram pendencias; nunca fatos presumidos.

## Blocos de descoberta

### 1. Identidade
- Quem e o usuario/cliente?
- Qual problema o projeto resolve?
- Quem usara o sistema?
- Qual resultado define sucesso?

### 2. Operacao atual
- Como o trabalho e feito hoje?
- Quais etapas existem?
- Quem participa?
- Que ferramentas, documentos e sistemas ja sao usados?
- Onde ocorrem erros, atrasos ou retrabalho?

### 3. Dados
- Quais dados entram?
- De onde vem?
- Quem pode visualizar ou alterar?
- Quais dados sao sensiveis?
- O que precisa ser preservado historicamente?

### 4. Regras de negocio
- Quais regras sao obrigatorias?
- Quais excecoes existem?
- Quem decide quando houver conflito?
- Quais regras ainda precisam ser confirmadas?

### 5. Entregaveis
- O que precisa existir na primeira versao?
- O que pode ficar para depois?
- O que explicitamente nao faz parte do escopo?

### 6. Restricoes
- Plataforma e ambiente.
- Orcamento, prazo e equipe quando aplicavel.
- Integracoes obrigatorias.
- Requisitos legais, seguranca, backup e disponibilidade.

## Saida obrigatoria do discovery

Ao concluir esta etapa, atualizar:

- `PROJECT.md` com identidade, objetivo e limites;
- `docs/REQUIREMENTS.md` com requisitos classificados;
- `docs/KNOWLEDGE.md` com fontes relevantes;
- `docs/STATUS.md` com estado atual e proximo passo;
- `docs/DECISIONS.md` somente para decisoes efetivamente tomadas.

A implementacao pode comecar quando houver entendimento suficiente do primeiro incremento, sem exigir que todo o projeto esteja definido antecipadamente.
