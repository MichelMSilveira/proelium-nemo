\# Movimento 7 - Expansão da Memória Estruturada da N.E.M.O.



\## Núcleo de Engenharia e Memória Operacional



Documento de planejamento responsável por registrar a evolução da camada de memória da N.E.M.O.



\---



Versão: 0.7.0



Projeto: Proelium Serviços



Responsáveis:



Michel Silveira



Natália Silveira



\---



\# 1. Objetivo



Expandir a capacidade de memória da N.E.M.O. para utilizar toda a estrutura organizada da Base de Conhecimento Proelium.



O objetivo é permitir que a inteligência consulte não apenas arquivos existentes na raiz da pasta de conhecimento, mas também toda a estrutura hierárquica organizada por categorias.



\---



\# 2. Situação Atual



A N.E.M.O. possui:



\- banco vetorial ChromaDB;

\- embeddings utilizando Ollama;

\- modelo `nomic-embed-text`;

\- coleção `proelium`;

\- sistema de recuperação semântica.



A arquitetura atual funciona corretamente.



\---



\# 3. Problema Identificado



Durante a auditoria da implementação foi identificado que o carregador de memória atual utiliza leitura apenas dos arquivos localizados diretamente na pasta:

Conhecimento/



A estrutura atual da base possui categorias organizadas:

Conhecimento/



├── 01\_EMPRESA

├── 02\_PROCESSOS

├── 03\_AUTOMACAO

├── 04\_REDES

├── 05\_SEGURANCA

├── 06\_AUDIO\_VIDEO

├── 07\_EQUIPAMENTOS

├── 08\_PROJETOS

└── 09\_INTEGRACAO\_IA



Porém essas subpastas ainda não participam da memória semântica.



\---



\# 4. Objetivo Técnico da Evolução



Atualizar o mecanismo de carregamento da memória para:



\- percorrer subpastas automaticamente;

\- localizar documentos `.txt`;

\- indexar toda a base de conhecimento;

\- preservar a organização das categorias;

\- melhorar a precisão das consultas.



\---



\# 5. Arquivo Envolvido



Componente principal:

Sistema/memoria.py



Responsável por:



\- criar a coleção ChromaDB;

\- gerar embeddings;

\- carregar documentos;

\- reconstruir a memória semântica.



\---



\# 6. Alteração Planejada



Atualizar o processo de leitura dos documentos.



Modelo atual:

Conhecimento/

arquivo.txt



Novo modelo:

Conhecimento/

categoria/

&#x20;   documento.txt



A leitura deverá ser recursiva.



\---



\# 7. Critérios de Sucesso



A evolução será considerada concluída quando:



\- todos os documentos da base forem carregados;

\- as categorias forem preservadas;

\- a quantidade de documentos indexados aumentar;

\- as respostas da N.E.M.O. utilizarem conhecimento mais completo;

\- os testes de consulta apresentarem melhoria.



\---



\# 8. Riscos e Cuidados



Durante a evolução devem ser preservados:



\- documentos oficiais da Proelium;

\- hierarquia de conhecimento;

\- regras de governança da N.E.M.O.;

\- rastreabilidade das alterações.



Nenhuma alteração deve modificar o conteúdo da base de conhecimento.



\---



\# 9. Próximas Etapas



1\. Atualizar carregador de memória.



2\. Recriar banco vetorial.



3\. Validar quantidade de documentos carregados.



4\. Realizar testes de consulta.



5\. Atualizar documentação arquitetural.



\---



\# 10. Histórico



Movimento 1:

Fundação da N.E.M.O.



Movimento 2:

Construção da Base de Conhecimento.



Movimento 3:

Desenvolvimento da Inteligência e Engenharia.



Movimento 4:

Integração do Assistente Inteligente.



Movimento 5:

Profissionalização Git e GitHub.



Movimento 6:

Consolidação da Arquitetura.



Movimento 7:

Expansão da Memória Estruturada.



\---



Projeto em desenvolvimento contínuo.

