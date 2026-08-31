# 7. Ambiente de Investigação

## Visão geral

A investigação do Zapp II depende de um conjunto de ferramentas capazes de estabelecer comunicação com o dispositivo, observar seu estado interno e executar procedimentos controlados.

Esse ambiente não é apenas uma coleção de programas. Ele constitui a **infraestrutura de pesquisa** utilizada para transformar perguntas sobre o dispositivo em experimentos verificáveis.

A partir dele, torna-se possível:

- acessar informações do sistema;
- executar comandos;
- coletar evidências;
- analisar arquivos;
- observar processos;
- testar hipóteses;
- desenvolver ferramentas;
- registrar resultados.

## Computador de investigação

O computador utilizado como estação de pesquisa funciona como o ambiente externo de desenvolvimento e análise.

Ele é responsável por fornecer recursos que não estão necessariamente disponíveis no próprio dispositivo, como:

- compiladores;
- ferramentas de análise;
- editores;
- armazenamento;
- documentação;
- scripts;
- ferramentas de controle de versão;
- ferramentas auxiliares de IA.

A separação entre **estação de investigação** e **dispositivo investigado** é importante.

O computador externo fornece as ferramentas.

O Zapp II fornece o ambiente que está sendo estudado.

## Comunicação com o dispositivo

A comunicação entre a estação de investigação e o Zapp II é uma das bases do projeto.

Entre as interfaces utilizadas ou investigadas está o **USB**, que permite estabelecer diferentes modos de comunicação.

Um dos mecanismos mais importantes é o:

### ADB

**Android Debug Bridge** é uma ferramenta utilizada para comunicação e gerenciamento de dispositivos compatíveis.

No contexto deste projeto, o ADB permite investigar o sistema de maneira mais profunda do que seria possível utilizando apenas a interface gráfica do aparelho.

## ADB como instrumento de pesquisa

O ADB pode ser utilizado para diferentes finalidades.

### Observação

Coleta de informações sobre:

- sistema;
- propriedades;
- processos;
- arquivos;
- dispositivos;
- conectividade.

### Interação

Execução de comandos no ambiente do dispositivo.

### Transferência

Movimentação de arquivos entre o computador e o dispositivo.

### Diagnóstico

Auxílio na identificação de problemas e comportamentos inesperados.

### Desenvolvimento

Execução e teste de ferramentas ou binários preparados externamente.

Dessa forma, o ADB funciona como uma das principais portas de entrada para a investigação do ambiente interno.

## Shell

Uma vez estabelecida uma sessão com o dispositivo, o shell fornece uma interface textual para interação com o sistema.

O shell permite investigar o ambiente sem depender exclusivamente da interface gráfica do KaiOS.

Entre as operações possíveis estão:

```text
identificar arquivos
      ↓
examinar processos
      ↓
consultar informações do sistema
      ↓
executar ferramentas
      ↓
testar hipóteses
      ↓
registrar resultados
```

A disponibilidade e as limitações dos comandos devem ser verificadas diretamente no dispositivo.

Um comando existente em uma distribuição Linux convencional pode não existir ou possuir comportamento diferente em um ambiente embarcado.

## BusyBox

O **BusyBox** possui papel importante no ambiente investigado.

Ele reúne diversos utilitários Unix em um único executável, sendo amplamente utilizado em sistemas embarcados.

Sua presença permite disponibilizar ferramentas fundamentais mesmo em ambientes com armazenamento e recursos limitados.

Durante a investigação, deverão ser registrados:

- versão do BusyBox;
- comandos disponíveis;
- diferenças em relação às implementações convencionais;
- limitações;
- comportamento observado.

Essa informação é importante para compreender as capacidades reais do shell disponível no dispositivo.

## Ferramentas Linux

Além do BusyBox, o ambiente poderá conter outras ferramentas ou utilitários específicos.

A investigação deverá identificar quais estão disponíveis em vez de assumir que o ambiente possui o conjunto completo de ferramentas de uma distribuição Linux.

Entre as categorias de interesse estão:

- gerenciamento de arquivos;
- processos;
- rede;
- armazenamento;
- diagnóstico;
- compactação;
- manipulação de texto;
- desenvolvimento;
- análise de sistema.

A identificação dessas ferramentas ajudará a determinar o que pode ser investigado diretamente no dispositivo e o que precisa ser analisado externamente.

## Coleta de informações

Uma parte importante do ambiente de investigação consiste em coletar informações de maneira organizada.

Os dados podem incluir:

- propriedades do sistema;
- informações do kernel;
- arquitetura;
- memória;
- armazenamento;
- processos;
- dispositivos;
- interfaces;
- logs;
- arquivos de configuração.

Sempre que possível, informações relevantes deverão ser preservadas junto ao contexto em que foram obtidas.

Isso permite comparar resultados obtidos em momentos diferentes.

## Logs e diagnóstico

Logs constituem uma fonte importante de evidências.

Eles podem revelar informações sobre:

- inicialização;
- serviços;
- drivers;
- erros;
- dispositivos;
- falhas;
- comportamento inesperado.

Durante um experimento, um log pode transformar uma hipótese em uma observação verificável.

Por isso, a coleta de logs deverá fazer parte dos procedimentos de troubleshooting sempre que estiver disponível e for tecnicamente apropriada.

## Desenvolvimento externo

Nem todo código precisa ou deve ser compilado diretamente no Zapp II.

As limitações de recursos do dispositivo tornam o computador externo especialmente importante.

Um fluxo possível é:

```text
Código-fonte
     ↓
Computador de desenvolvimento
     ↓
Cross-compilation
     ↓
Binário compatível
     ↓
Transferência para o Zapp II
     ↓
Execução
     ↓
Teste
     ↓
Resultado
```

Esse modelo será aprofundado na seção dedicada a desenvolvimento e cross-compilation.

## Scripts de investigação

Scripts podem automatizar tarefas repetitivas.

Exemplos de aplicações:

- coleta de informações;
- organização de arquivos;
- execução de conjuntos de comandos;
- comparação de resultados;
- preparação de experimentos;
- geração de relatórios;
- análise de dados.

A automação é especialmente importante porque permite reduzir erros humanos e tornar procedimentos repetíveis.

## IA como ferramenta auxiliar

Ferramentas de Inteligência Artificial podem participar do ambiente de investigação como instrumentos auxiliares.

Possíveis usos incluem:

- pesquisa exploratória;
- explicação de conceitos;
- análise preliminar de código;
- geração de scripts;
- revisão de documentação;
- organização de informações;
- identificação de possíveis caminhos de investigação.

Entretanto, a IA não constitui uma fonte de verdade por si mesma.

Uma resposta gerada por IA deverá ser tratada como **hipótese ou auxílio de investigação** até que seja validada por evidências apropriadas.

## Controle das experiências

A investigação deverá priorizar experimentos controlados.

Antes de uma alteração potencialmente destrutiva, sempre que possível deverão ser considerados:

1. estado atual do dispositivo;
2. objetivo do experimento;
3. risco envolvido;
4. possibilidade de recuperação;
5. método de registro;
6. resultado esperado.

Quando possível, alterações deverão ser precedidas por coleta de informações e acompanhadas de documentação.

## Estrutura do ambiente

O ambiente de investigação pode ser representado como:

```text
                ┌───────────────┐
                │   Pesquisador │
                └───────┬───────┘
                        │
                        ↓
                ┌───────────────┐
                │      IA       │
                │   auxiliar    │
                └───────┬───────┘
                        │
                        ↓
┌────────────────────────────────────────┐
│       Estação de investigação          │
│                                        │
│  Linux · Git · Compiladores · Scripts  │
│  Ferramentas de análise · Documentação │
└───────────────────┬────────────────────┘
                    │
                   USB
                    │
                    ↓
┌────────────────────────────────────────┐
│             Zapp II                    │
│                                        │
│  ADB · Shell · BusyBox · Linux         │
│  Android · KaiOS · Hardware            │
└────────────────────────────────────────┘
```

Essa estrutura representa o fluxo geral de investigação, não uma descrição completa da arquitetura interna do dispositivo.

## Objetivos desta etapa

- [ ] Documentar o ambiente de desenvolvimento utilizado.
- [ ] Identificar os métodos de comunicação disponíveis.
- [ ] Documentar o uso do ADB.
- [ ] Identificar as ferramentas disponíveis no dispositivo.
- [ ] Documentar o ambiente BusyBox e shell.
- [ ] Estruturar procedimentos de coleta de informações.
- [ ] Registrar ferramentas utilizadas externamente.
- [ ] Documentar o uso de scripts e automação.
- [ ] Registrar o papel da IA na investigação.
- [ ] Estabelecer procedimentos básicos de segurança para experimentos.

## Próxima etapa

Com o ambiente de investigação estabelecido, podemos começar a documentar a primeira ferramenta de acesso profundo ao sistema:

### ADB

A próxima seção será dedicada exclusivamente ao **Android Debug Bridge**, sua função, configuração, comandos utilizados durante a pesquisa e limitações encontradas no Zapp II.

## Princípio da investigação

> **Uma ferramenta só é realmente útil quando permite transformar uma pergunta em uma observação verificável.**
