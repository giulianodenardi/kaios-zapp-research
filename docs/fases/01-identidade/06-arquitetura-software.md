# 6. Arquitetura de Software

## Visão geral

A arquitetura de software é a camada que transforma os recursos físicos do Zapp II em um ambiente computacional funcional.

A investigação parte da identificação de uma combinação de tecnologias de diferentes níveis e gerações:

**Linux → Android → KaiOS**

Essas tecnologias não devem ser tratadas como sistemas independentes. O objetivo desta etapa é compreender como elas se relacionam dentro da plataforma e quais componentes efetivamente estão presentes no dispositivo.

## Modelo inicial

A arquitetura pode ser representada inicialmente da seguinte maneira:

```text
┌───────────────────────────────┐
│          Aplicações           │
├───────────────────────────────┤
│            KaiOS              │
├───────────────────────────────┤
│     Frameworks / Serviços     │
├───────────────────────────────┤
│         Linux Kernel          │
├───────────────────────────────┤
│      Firmware / Boot          │
├───────────────────────────────┤
│       MediaTek MT6572         │
└───────────────────────────────┘
```

Esse modelo é uma representação de trabalho.

Ele deverá ser refinado à medida que a investigação produzir evidências sobre a arquitetura real da plataforma.

## Linux

O Linux constitui uma das camadas fundamentais do sistema.

O kernel atua como intermediário entre o hardware e os componentes de software que precisam utilizar seus recursos.

Entre suas responsabilidades estão:

- gerenciamento de processos;
- gerenciamento de memória;
- comunicação com dispositivos;
- gerenciamento de arquivos;
- controle de recursos;
- interfaces do sistema;
- suporte aos componentes de hardware.

A identificação da versão específica do kernel é importante porque diferentes versões apresentam diferenças significativas em APIs, ferramentas, drivers e comportamentos.

## Android

A investigação identificou uma base relacionada ao **Android 4.4.2** no ambiente do dispositivo.

Esse elemento é relevante porque o Android possui uma arquitetura própria construída sobre o kernel Linux, incluindo bibliotecas, serviços e componentes de sistema.

Entretanto, a simples presença de componentes Android não permite concluir automaticamente qual é sua função dentro do ambiente KaiOS.

O projeto deverá investigar individualmente:

- quais componentes permanecem presentes;
- quais são utilizados;
- quais foram modificados;
- quais permanecem apenas como parte da base do sistema;
- quais relações existem entre esses componentes e o KaiOS.

## KaiOS

O KaiOS representa a camada de software mais diretamente relacionada à experiência do usuário.

Sua arquitetura introduz um modelo diferente daquele encontrado em sistemas Android tradicionais, utilizando tecnologias web para aplicações e interfaces.

Para esta investigação, o interesse não está apenas na utilização do sistema, mas na compreensão de como ele se integra às camadas inferiores.

Entre os elementos que poderão ser investigados estão:

- aplicações;
- WebApps;
- APIs;
- serviços;
- armazenamento;
- permissões;
- comunicação com componentes do sistema;
- mecanismos de inicialização;
- relação com o ambiente Linux.

## A relação entre as camadas

Uma das perguntas centrais do projeto é:

> **Como uma aplicação KaiOS consegue utilizar recursos fornecidos pelo hardware?**

A resposta exige atravessar várias camadas.

Um modelo simplificado seria:

```text
Aplicação
    ↓
API / Serviço
    ↓
Componente de sistema
    ↓
Kernel
    ↓
Driver
    ↓
Hardware
```

Essa cadeia será utilizada como modelo de investigação.

Sempre que uma funcionalidade for analisada, o projeto tentará determinar em qual camada ela é implementada e como se comunica com as demais.

## Boot

O processo de inicialização representa a transição entre o estado inicial do hardware e o sistema operacional funcional.

A investigação do boot poderá envolver:

```text
Hardware
   ↓
Boot ROM
   ↓
Bootloader
   ↓
Kernel
   ↓
Inicialização do sistema
   ↓
Serviços
   ↓
KaiOS
```

A sequência exata deverá ser determinada por evidências.

Não serão assumidos componentes ou etapas que não tenham sido identificados.

## Filesystem

O filesystem representa uma das principais fontes de informações sobre a arquitetura de software.

Sua análise pode revelar:

- executáveis;
- bibliotecas;
- configurações;
- scripts;
- serviços;
- dispositivos;
- logs;
- informações do sistema;
- componentes do KaiOS;
- componentes herdados da base Android.

Diretórios como `/system`, `/data`, `/proc`, `/sys` e `/dev`, quando presentes e acessíveis, poderão ser analisados individualmente.

## Processos e serviços

Os processos em execução fornecem uma visão dinâmica da arquitetura.

Enquanto o filesystem mostra aquilo que está armazenado no dispositivo, os processos mostram parte daquilo que está efetivamente sendo executado.

A investigação poderá registrar:

- nome dos processos;
- usuário responsável;
- PID;
- consumo de recursos;
- processos iniciados durante o boot;
- relação entre processos;
- serviços associados.

Essas informações poderão posteriormente ser relacionadas aos arquivos e componentes responsáveis por sua execução.

## Interfaces do kernel

O Linux disponibiliza diversas interfaces que permitem observar o estado do sistema.

Entre as mais importantes para esta pesquisa estão:

### `/proc`

Informações sobre processos e estado do kernel.

### `/sys`

Representação de dispositivos, drivers e subsistemas do kernel.

### `/dev`

Interface através da qual dispositivos são apresentados ao espaço de usuário.

Essas três estruturas serão importantes para conectar:

**hardware → kernel → espaço de usuário.**

## Ambiente de execução

A investigação também deverá determinar quais ferramentas e recursos estão disponíveis no ambiente.

Entre os elementos relevantes estão:

- shell;
- BusyBox;
- utilitários Unix;
- bibliotecas;
- compiladores;
- interpretadores;
- ferramentas de diagnóstico;
- comandos disponíveis;
- variáveis de ambiente;
- permissões.

O ambiente encontrado no dispositivo não deve ser presumido como equivalente a uma distribuição Linux convencional.

Sistemas embarcados frequentemente possuem ambientes reduzidos e personalizados.

## Limitações

A arquitetura de software poderá apresentar componentes proprietários ou pouco documentados.

Algumas relações entre componentes poderão permanecer desconhecidas.

Além disso, diferentes versões de firmware podem apresentar diferenças.

Por esse motivo, a documentação deverá distinguir:

**arquitetura conhecida**

de

**arquitetura inferida**

e

**arquitetura ainda desconhecida**.

## Objetivos desta etapa

- [ ] Identificar a versão do kernel Linux.
- [ ] Mapear os principais componentes de software.
- [ ] Identificar componentes relacionados ao Android.
- [ ] Identificar componentes específicos do KaiOS.
- [ ] Mapear a estrutura básica do filesystem.
- [ ] Identificar processos e serviços relevantes.
- [ ] Investigar a sequência de inicialização.
- [ ] Relacionar software e hardware.
- [ ] Registrar lacunas de conhecimento.

## Próxima etapa

Com o modelo geral da arquitetura estabelecido, a investigação poderá passar para uma das ferramentas fundamentais utilizadas para acessar o sistema:

### ADB

O **Android Debug Bridge** será investigado não apenas como uma ferramenta de desenvolvimento, mas como uma das principais interfaces utilizadas para observar, diagnosticar e interagir com a plataforma.

A partir dele será possível aprofundar a investigação do ambiente real de execução.

## Princípio da investigação

> **Não basta saber qual sistema está instalado. É preciso compreender o que realmente está executando.**
