\# Dependências Técnicas N.E.M.O.



\## Núcleo de Engenharia e Memória Operacional



Documento responsável por registrar os requisitos técnicos necessários para funcionamento, manutenção e evolução da N.E.M.O.



\---



Versão: 0.6.0



Projeto: Proelium Serviços



Responsáveis:



Michel Silveira



Natália Silveira



\---



\# 1. Objetivo



Este documento apresenta as dependências técnicas da N.E.M.O., permitindo:



\- reconstrução do ambiente;

\- manutenção do sistema;

\- padronização do desenvolvimento;

\- controle da arquitetura;

\- evolução futura da plataforma.



\---



\# 2. Ambiente Atual



A N.E.M.O. opera atualmente em ambiente local, utilizando processamento de inteligência artificial e armazenamento de conhecimento.



Características:



\- execução local;

\- modelo de inteligência artificial privado;

\- memória semântica própria;

\- base de conhecimento empresarial;

\- controle de versão através do Git.



\---



\# 3. Sistema Operacional



Ambiente atual:



Windows



Responsável por hospedar:



\- código da N.E.M.O.;

\- banco de memória;

\- modelos de inteligência artificial;

\- documentação;

\- base de conhecimento.



\---



\# 4. Linguagem de Programação



\## Python



Responsável pela execução dos componentes principais da N.E.M.O.



Utilizado em:



\- núcleo do assistente;

\- gerenciamento de memória;

\- integração com inteligência artificial;

\- ferramentas auxiliares.



Arquivos principais:

Sistema/



├── nemo.py



├── memoria.py



├── teste\_memoria.py



└── ver\_memoria.py



\---



\# 5. Inteligência Artificial



\## Ollama



Responsável pelo gerenciamento dos modelos locais de inteligência artificial.



Funções:



\- execução do modelo de linguagem;

\- processamento das solicitações;

\- geração de respostas.



\---



\## Modelo de Linguagem



Modelo utilizado:

Ollama



Configuração:

Modelfile



Responsável por definir características do comportamento da inteligência.



\---



\# 6. Modelo de Embeddings



A N.E.M.O. utiliza embeddings para transformar documentos em representações semânticas.



Modelo atual:

nomic-embed-text



Responsabilidade:



\- criação de vetores;

\- comparação semântica;

\- recuperação de informações relevantes.



\---



\# 7. Banco de Memória



\## ChromaDB



Responsável pelo armazenamento da memória semântica.



Local atual:

Sistema/conhecimento.db



Funções:



\- armazenar embeddings;

\- organizar coleções;

\- realizar buscas semânticas.



Coleção atual:

proelium



\---



\# 8. Base de Conhecimento



Local:

Conhecimento/



Responsável por armazenar:



\- informações da Proelium;

\- processos;

\- automação;

\- redes;

\- segurança;

\- equipamentos;

\- projetos;

\- regras da N.E.M.O.



\---



\# 9. Controle de Versão



\## Git



Responsável pelo histórico de desenvolvimento.



Utilizado para:



\- versionamento do código;

\- controle documental;

\- rastreabilidade das alterações.



\---



\## GitHub



Repositório remoto:

NEMO-Assistente-Inteligente



Responsável por:



\- backup;

\- colaboração;

\- histórico do projeto.



\---



\# 10. Fluxo das Dependências

Usuário



↓



N.E.M.O.



↓



Python



↓



nemo.py



↓



memoria.py



↓



ChromaDB



↓



Conhecimento Proelium



↓



Embeddings



↓



Ollama



↓



Resposta Inteligente



\---



\# 11. Dependências Futuras



Possíveis evoluções:



\- interface de voz;

\- APIs externas;

\- integração Home Assistant;

\- integração automação residencial;

\- memória operacional avançada;

\- arquitetura RAG completa;

\- servidores locais dedicados.



\---



\# 12. Princípios Técnicos



A evolução da N.E.M.O. seguirá:



\- documentação antes da implementação;

\- preservação do histórico;

\- segurança das informações;

\- arquitetura modular;

\- melhoria contínua.



\---



\# Responsáveis pelo Projeto



Michel Silveira



Natália Silveira



Proelium Serviços





Projeto em desenvolvimento contínuo.

