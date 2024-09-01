---
title: Wireframe
sidebar_position: 1
description : Esboço da Interface
---

### Introdução

Wireframes são essenciais no processo de design e desenvolvimento de qualquer aplicação de software. Eles servem como um esboço que delineia a estrutura, o conteúdo e a funcionalidade da interface antes do início do design ou desenvolvimento real. Wireframes ajudam a visualizar o layout e o fluxo da aplicação, facilitando a compreensão de como o produto final funcionará para desenvolvedores, designers e stakeholders. Ao criar um wireframe, podemos identificar possíveis problemas de usabilidade logo no início, garantindo que o design seja amigável ao usuário e atenda aos requisitos do projeto. Além disso, wireframes fornecem um guia claro para os desenvolvedores seguirem durante a fase de codificação, reduzindo a probabilidade de mal-entendidos e garantindo que o produto final esteja alinhado com o design pretendido.

Neste documento, vamos percorrer o wireframe da interface Käfer, detalhando cada parte da interface conforme apresentado nas imagens fornecidas. Esta documentação é clara e compreensível tanto para leitores técnicos quanto para não técnicos, garantindo que todos os envolvidos no projeto possam acompanhar.

### Visão Geral do Wireframe

O wireframe da aplicação Käfer consiste em várias telas principais, cada uma servindo a uma função específica dentro da aplicação. A aplicação parece se concentrar na análise de dados e no treinamento de modelos, com um fluxo claro guiando o usuário desde a entrada de dados até os resultados do modelo. Abaixo, vamos descrever cada tela em detalhe com base nos wireframes fornecidos.

### 1. Tela Inicial

![Tela Inicial](/img/tela_inicial1.png)

A **Tela Inicial** é o ponto de entrada da aplicação Käfer. Ela apresenta um logotipo proeminente de um besouro (Käfer) no centro da tela, simbolizando o nome da aplicação. Abaixo do logotipo, há dois botões principais: **Executar** e **Treinar**.

- **Executar**: Este botão provavelmente leva o usuário à seção onde ele pode executar ou analisar um conjunto de dados.
- **Treinar**: Este botão provavelmente navega o usuário até a seção de treinamento de modelo, onde ele pode fazer upload de dados e treinar seus modelos.

O design é minimalista, com foco em guiar o usuário para essas duas ações principais.

### 2. Execução e Treino

![Tabela](/img/carregamento.png)

Ao clicar em **Executar** na tela inicial, o usuário é levado à tela de **Upload**.

- Esta tela solicita que o usuário faça o upload de um arquivo CSV para análise.
- O usuário tem a opção de arrastar e soltar o arquivo na área designada ou clicar para fazer o upload.
- Uma barra de progresso na parte inferior indica o status do upload, ajudando o usuário a entender o progresso da entrada de dados.


Se o usuário selecionar **Treinar** na tela inicial, ele é direcionado para a tela de **Treino do Modelo**.

- Semelhante à etapa anterior, esta página solicita que o usuário faça o upload de um arquivo CSV para treinar o modelo.
- Uma barra de progresso indica o status do upload, fornecendo feedback em tempo real para o usuário.

### 3. Modelo Treinado

![Resultados Treino](/img/resultados_treino.png)

Após o processo de treinamento, o usuário é levado à tela de **Modelo Treinado**.

- Esta tela exibe os resultados atuais e anteriores do modelo treinado.
- O usuário pode visualizar **Gráficos e Métricas** relacionados ao desempenho do modelo.
- Esta tela permite que o usuário compare o desempenho do modelo atual com o anterior, auxiliando na avaliação da eficácia do treinamento.

### 4. Modelo Executado

![Resultados Execução](/img/resultados_exc.png)

Após o processo de treinamneto do modelo, o usuário ao clicar no botão **Home** é redirecionado para a **Tela Inicial**, após todo processo de carregamento da **Execução** do Modelo, o usuário é levado pra tela de resultados do **Modelo Executado**.

- Esta tela exibe os resultados atuais e anteriores do modelo treinado.
- O usuário pode visualizar **Gráficos e Métricas** relacionados ao desempenho do modelo.
- Esta tela permite que o usuário compare o desempenho do modelo atual com o anterior, auxiliando na avaliação da eficácia do treinamento.

### 5. POPUP Ver Mais

![Resultados Ver mais](/img/vermais.png)


Clicar em **Ver Mais** na tela de Resultados abre uma janela detalhada de **POPUP**.

- Este popup fornece uma visão mais aprofundada dos resultados atuais, com foco em um gráfico de barras comparando o desempenho real do modelo com os resultados desejados.
- O usuário pode ver tanto o **Resultado Atual** quanto o **Resultado Desejado**, permitindo uma comparação clara e compreensão de como o modelo se saiu em relação às expectativas.

### Fluxo da Aplicação

A imagem abaixo ilustra o fluxo da aplicação Käfer conforme descrito nas seções acima:

![Fluxo da Aplicação Käfer](/img/fluxo.png)

O fluxo da aplicação começa na **Tela Inicial**, onde o usuário escolhe entre **Executar** uma análise de dados ou **Treinar** um modelo. Dependendo da escolha, o usuário será levado para a tela de **Tabela Para Análise** ou **Treino do Modelo**. Após a conclusão das respectivas ações, o usuário pode visualizar os resultados em **Modelo Treinado** ou **Resultados**, com a opção de explorar mais detalhes através do **POPUP Ver Mais**. Este fluxo garante uma navegação intuitiva e eficiente, guiando o usuário por todas as etapas do processo de análise e treinamento de forma clara e direta.
