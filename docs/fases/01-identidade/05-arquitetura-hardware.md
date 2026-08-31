# 5. Arquitetura de Hardware

## Visão geral

O hardware constitui a camada fundamental do Projeto KaiOS / Zapp II.

Antes de investigar o sistema operacional, os processos ou as aplicações, é necessário compreender a plataforma física sobre a qual esses componentes são executados.

A investigação do hardware busca estabelecer uma relação entre os componentes identificados no dispositivo e os recursos que posteriormente aparecem nas camadas de firmware, kernel e sistema operacional.

O objetivo não é produzir inicialmente um inventário completo de cada componente eletrônico, mas construir progressivamente um **mapa técnico da plataforma**.

## Arquitetura geral

O Zapp II pode ser analisado inicialmente como uma plataforma composta por diferentes grupos funcionais:

```text
┌───────────────────────────────┐
│          Aplicações           │
├───────────────────────────────┤
│            KaiOS              │
├───────────────────────────────┤
│      Sistema / Frameworks     │
├───────────────────────────────┤
│         Linux Kernel          │
├───────────────────────────────┤
│       Firmware / Boot         │
├───────────────────────────────┤
│       SoC / Hardware          │
└───────────────────────────────┘
```

O hardware fornece os recursos necessários para que as camadas superiores possam funcionar.

Entre esses recursos estão processamento, memória, armazenamento, comunicação e interfaces com dispositivos periféricos.

## System-on-Chip

O componente central identificado na plataforma é o **MediaTek MT6572**.

Um SoC, ou *System-on-Chip*, reúne em um único componente diversas funções que, em arquiteturas computacionais tradicionais, poderiam estar distribuídas entre vários circuitos.

Para esta investigação, o SoC é particularmente importante porque estabelece uma ligação entre diferentes áreas:

```text
CPU
│
├── Arquitetura ARM
│
├── Memória
│
├── Periféricos
│
├── Interfaces
│
└── Controladores
       │
       ↓
     Kernel
       │
       ↓
    Sistema
```

A documentação específica de cada componente do MT6572 será desenvolvida posteriormente, conforme forem obtidas evidências suficientes.

## Processador

A CPU representa a unidade responsável pela execução das instruções dos programas.

A identificação da arquitetura do processador possui consequências práticas para todo o projeto.

Ela determina, entre outras coisas:

- formato dos executáveis;
- conjunto de instruções;
- arquitetura dos compiladores;
- compatibilidade de bibliotecas;
- ABI;
- possibilidades de cross-compilation;
- compatibilidade de ferramentas.

Por isso, a arquitetura ARM não será tratada apenas como uma característica do hardware, mas também como um requisito para os experimentos de software realizados posteriormente.

## Memória

A memória é uma das principais limitações a serem consideradas em uma plataforma móvel de baixo custo.

A investigação deverá distinguir diferentes tipos de armazenamento e memória sempre que houver informações suficientes para fazê-lo.

Entre os elementos relevantes estão:

- memória RAM;
- armazenamento permanente;
- partições;
- áreas reservadas ao sistema;
- áreas destinadas aos usuários;
- memória utilizada por firmware.

A quantidade e a organização desses recursos podem afetar diretamente:

- desempenho;
- execução de aplicações;
- disponibilidade de ferramentas;
- compilação local;
- armazenamento de arquivos;
- possibilidade de execução de determinados programas.

## Armazenamento

O armazenamento permanente possui importância especial para a investigação porque pode conter diferentes componentes da plataforma.

Dependendo da estrutura encontrada, poderão existir áreas destinadas a:

- boot;
- sistema;
- recuperação;
- dados;
- configurações;
- aplicativos;
- firmware.

A identificação dessas áreas deverá ser realizada por meio de evidências obtidas no próprio dispositivo sempre que possível.

Não será assumida uma estrutura de partições apenas com base em modelos semelhantes.

## Interfaces e periféricos

Um dispositivo móvel não é composto apenas por CPU, memória e armazenamento.

O SoC e os demais componentes precisam interagir com diversos dispositivos físicos.

Entre as categorias de interesse estão:

- tela;
- touchscreen;
- teclado;
- áudio;
- câmera;
- comunicação USB;
- rede móvel;
- Wi-Fi;
- Bluetooth;
- rádio;
- sensores;
- gerenciamento de energia.

A investigação dessas interfaces poderá ser realizada posteriormente por meio da análise de:

**hardware → driver → kernel → dispositivo → serviço → aplicação.**

Essa cadeia permite relacionar um componente físico ao modo como ele é apresentado ao sistema operacional.

## USB

A interface USB possui importância especial neste projeto por constituir uma das principais formas de comunicação entre o Zapp II e um computador externo.

Por meio dela, foi possível utilizar ferramentas como **ADB** e realizar atividades de investigação e desenvolvimento.

A análise da interface USB poderá incluir:

- modos de conexão;
- identificação do dispositivo;
- ADB;
- MTP;
- armazenamento;
- configuração USB;
- comportamento durante boot;
- comunicação entre dispositivo e computador.

Essa investigação será tratada em maior profundidade na seção dedicada ao ambiente de desenvolvimento.

## Relação entre hardware e sistema

Uma das metas da investigação é evitar estudar o hardware como uma lista isolada de componentes.

Cada componente deverá, sempre que possível, ser relacionado à sua representação nas camadas superiores.

Por exemplo:

```text
Componente físico
       ↓
Controlador
       ↓
Driver
       ↓
Kernel
       ↓
Dispositivo do sistema
       ↓
Serviço
       ↓
Aplicação
```

Essa abordagem permite responder perguntas como:

> Qual componente físico fornece determinado recurso?

> Qual driver controla esse componente?

> Como o kernel o apresenta ao sistema?

> Qual serviço utiliza esse recurso?

> Como uma aplicação acessa essa funcionalidade?

## Nível de confiança

As informações de hardware serão classificadas conforme sua origem.

### Confirmado

Informação sustentada por evidência direta ou por múltiplas fontes confiáveis.

### Identificado

Componente ou característica encontrada durante a investigação, mas que ainda pode exigir confirmação adicional.

### Inferido

Informação deduzida a partir do comportamento do sistema ou de documentação relacionada.

### Desconhecido

Informação para a qual ainda não existem evidências suficientes.

Essa classificação será mantida ao longo do projeto para evitar que especificações presumidas sejam apresentadas como fatos.

## Objetivos desta etapa

A investigação de hardware deverá produzir progressivamente:

- [ ] Mapa geral da plataforma.
- [ ] Identificação dos principais componentes.
- [ ] Documentação do SoC.
- [ ] Identificação da arquitetura da CPU.
- [ ] Levantamento de memória e armazenamento.
- [ ] Mapeamento das principais interfaces.
- [ ] Relação entre hardware e componentes do sistema.
- [ ] Registro das informações ainda desconhecidas.

O objetivo não é desmontar imediatamente o dispositivo ou identificar cada componente eletrônico.

A prioridade é construir uma compreensão funcional da plataforma.

## Próxima etapa

Com a arquitetura de hardware estabelecida como ponto de partida, a investigação pode avançar para uma camada particularmente importante:

**o ambiente de software que transforma o hardware em uma plataforma utilizável.**

A próxima etapa deverá investigar o **sistema operacional, o kernel Linux e a relação entre Android e KaiOS**, estabelecendo a cadeia de software executada pelo dispositivo.

## Princípio da investigação

> **Hardware não é apenas especificação. É o fundamento sobre o qual todo o comportamento observado no sistema se torna possível.**
