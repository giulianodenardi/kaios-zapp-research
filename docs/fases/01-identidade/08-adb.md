# 8. ADB: Porta de Entrada para o Sistema

## Visão geral

O **Android Debug Bridge (ADB)** é uma das ferramentas mais importantes utilizadas na investigação do Zapp II.

Embora tenha sido desenvolvido para o ecossistema Android, sua presença no ambiente estudado permite estabelecer uma interface de comunicação entre o computador de pesquisa e o dispositivo.

No contexto deste projeto, o ADB é tratado principalmente como uma **ferramenta de investigação, diagnóstico e desenvolvimento**.

## O papel do ADB

O ADB cria uma ponte entre dois ambientes:

```text
┌─────────────────────────┐
│ Computador              │
│                         │
│ ADB Client              │
└────────────┬────────────┘
             │
             │ USB
             │
┌────────────▼────────────┐
│ Zapp II                 │
│                         │
│ ADB Daemon              │
│         ↓               │
│ Sistema operacional     │
└─────────────────────────┘
```

Essa comunicação permite realizar operações que seriam difíceis ou impossíveis apenas pela interface gráfica do aparelho.

## Principais funções utilizadas

Durante a investigação, o ADB pode ser utilizado para:

### Identificação

Obter informações sobre o dispositivo e o sistema.

### Execução

Executar comandos remotamente no ambiente do Zapp II.

### Transferência

Enviar arquivos para o dispositivo e recuperar arquivos dele.

### Diagnóstico

Investigar processos, arquivos, propriedades e comportamento do sistema.

### Desenvolvimento

Testar scripts, programas e ferramentas desenvolvidas externamente.

Essas funções tornam o ADB uma ferramenta central para a metodologia experimental do projeto.

## Comunicação com o dispositivo

A comunicação normalmente começa com a identificação do dispositivo pelo computador.

Um procedimento básico pode ser representado como:

```text
Computador
    ↓
Conexão USB
    ↓
ADB
    ↓
Detecção do dispositivo
    ↓
Sessão de investigação
```

O estabelecimento da comunicação é uma etapa importante porque permite verificar se o ambiente externo consegue reconhecer corretamente o dispositivo.

Problemas nessa etapa também podem fornecer informações relevantes sobre:

- configuração USB;
- drivers;
- modo de conexão;
- permissões;
- estado do dispositivo;
- compatibilidade do ambiente externo.

## ADB Shell

Uma das funções mais importantes para a pesquisa é a possibilidade de acessar um shell remoto.

A partir dele, o investigador pode interagir diretamente com o ambiente de execução do dispositivo.

Isso permite consultar informações, executar comandos e realizar experimentos sem depender da interface gráfica.

O shell é particularmente importante para a investigação de:

- filesystem;
- processos;
- permissões;
- variáveis de ambiente;
- dispositivos;
- memória;
- serviços;
- ferramentas disponíveis.

## Coleta de informações

Uma das primeiras aplicações do ADB durante uma investigação é a coleta sistemática de informações.

Podem ser levantados dados como:

- propriedades do sistema;
- versão do Android;
- versão do KaiOS;
- versão do kernel;
- arquitetura;
- hostname;
- memória;
- armazenamento;
- processos;
- dispositivos;
- variáveis de ambiente.

Essas informações formam uma espécie de **fotografia técnica do sistema** em determinado momento.

## Arquivos e filesystem

O ADB também pode ser utilizado para investigar a estrutura de arquivos do dispositivo.

A análise pode incluir:

- diretórios;
- arquivos executáveis;
- bibliotecas;
- configurações;
- scripts;
- permissões;
- links simbólicos;
- arquivos de sistema;
- dados de aplicações.

Quando permitido pelo nível de acesso disponível, arquivos relevantes podem ser copiados para a estação de investigação para análise posterior.

## Processos

O acesso ao shell permite observar processos em execução.

Essa informação é importante porque permite comparar:

**o que está armazenado no sistema**

com

**o que está efetivamente sendo executado.**

A investigação de processos pode ajudar a identificar:

- serviços;
- aplicações;
- processos do sistema;
- processos iniciados durante o boot;
- consumo de recursos;
- relações entre componentes.

## Propriedades do sistema

As propriedades do sistema constituem uma fonte particularmente útil de informações.

Elas podem revelar características como:

- modelo;
- versão;
- plataforma;
- configuração;
- identificadores;
- propriedades de build;
- parâmetros do sistema.

Essas informações precisam ser interpretadas cuidadosamente.

Uma propriedade pode indicar uma configuração declarada pelo sistema, mas não necessariamente provar como determinado componente funciona internamente.

## Transferência de arquivos

O ADB permite estabelecer um fluxo de trabalho entre a estação de pesquisa e o dispositivo:

```text
             Computador
                 │
        ┌────────┴────────┐
        │                 │
        ↓                 ↓
      push              pull
        │                 │
        ↓                 ↓
     Zapp II          Computador
```

**Push** representa o envio de arquivos para o dispositivo.

**Pull** representa a recuperação de arquivos do dispositivo.

Essa capacidade é importante para:

- testar ferramentas;
- recuperar logs;
- analisar arquivos;
- coletar evidências;
- transferir binários;
- preparar experimentos.

## ADB e desenvolvimento

Quando o dispositivo não possui ferramentas suficientes para desenvolver ou compilar determinado software localmente, o ADB permite utilizar a estação externa como ambiente de desenvolvimento.

Um fluxo típico pode ser:

```text
Código
  ↓
Compilação externa
  ↓
Binário ARM
  ↓
ADB push
  ↓
Zapp II
  ↓
Execução
  ↓
Teste
  ↓
Logs / resultado
  ↓
ADB pull
```

Esse processo conecta diretamente desenvolvimento e investigação.

## Limitações

O ADB não fornece automaticamente acesso irrestrito ao sistema.

As capacidades disponíveis dependem de fatores como:

- configuração do dispositivo;
- permissões;
- usuário do processo ADB;
- filesystem;
- políticas de segurança;
- modo USB;
- firmware;
- componentes presentes.

Portanto:

> **ter ADB não significa necessariamente ter acesso root.**

Essa distinção é fundamental para interpretar corretamente os experimentos.

## ADB como instrumento científico

Dentro da metodologia deste projeto, o ADB pode ser entendido como um instrumento de observação.

Uma pergunta pode ser transformada em procedimento:

```text
Pergunta
   ↓
Comando / experimento
   ↓
Observação
   ↓
Registro
   ↓
Análise
   ↓
Conclusão
```

Isso permite que comandos deixem de ser simplesmente ferramentas utilizadas "por tentativa e erro" e passem a fazer parte de uma metodologia documentada.

## Registro dos experimentos

Sempre que um comando ADB produzir uma descoberta relevante, recomenda-se registrar:

**Objetivo**

Por que o comando foi executado?

**Procedimento**

Como o teste foi realizado?

**Resultado**

O que foi observado?

**Interpretação**

O que esse resultado significa?

**Limitações**

Existe alguma explicação alternativa?

**Próximo passo**

Que nova pergunta surgiu?

Esse formato mantém a investigação rastreável.

## Objetivos desta etapa

- [ ] Documentar o processo de comunicação ADB.
- [ ] Registrar o ambiente utilizado para ADB.
- [ ] Documentar os principais procedimentos empregados.
- [ ] Registrar limitações de acesso.
- [ ] Documentar o uso do shell.
- [ ] Documentar transferência de arquivos.
- [ ] Registrar procedimentos de coleta de informações.
- [ ] Organizar experimentos realizados através do ADB.
- [ ] Relacionar descobertas obtidas pelo ADB às demais camadas do sistema.

## Próxima etapa

O ADB fornece a porta de entrada.

O próximo nível da investigação será o ambiente disponibilizado depois dessa porta:

### Shell e BusyBox

A próxima seção deverá analisar o ambiente Unix disponível no Zapp II, quais ferramentas estão presentes, quais estão ausentes e como essas limitações influenciam a capacidade de investigação e desenvolvimento.

## Princípio da investigação

> **ADB conecta os ambientes. O shell revela o sistema.**
