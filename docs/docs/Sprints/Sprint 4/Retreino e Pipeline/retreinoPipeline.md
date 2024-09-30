---
title: Retreino e Pipeline
sidebar_position: 2
description : Lógica do pipeline de retreino desenvolvido na sprint 4
---

# Introdução

Dentro de toda a concepção existente no sistema deste projeto, uma das etapas mais importantes é a de retreino do modelo. Ela consiste em treinar novamente o modelo após a adição de novos dados, e dessa forma, proporcionar novas estratégias de aprendizado com base nos dados mais recentes e melhorar os resultados do modelo cada vez mais. 

O fluxo de retreino foi pensado levando em consideração duas personas principais do sistema, o operador e o engenheiro de dados. Para ilustrar esse fluxo, foram utilizados diagramas de blocos, que oferecem uma representação visual de um sistema ou processo. Esses diagramas utilizam blocos para simbolizar diferentes componentes ou etapas, conectados por linhas que indicam a relação entre eles, facilitando uma visão clara e organizada da estrutura do sistema. Esta abordagem é amplamente usada em áreas como engenharia, informática e matemática, entre outras, sendo uma ferramenta eficaz para simplificar informações complexas.

<p align="center"><b> Figura 1 - Fluxo de retreino</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/fluxoRetreino.jpg').default} alt="fluxo retreino"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

O fluxo de retreinamento acima descreve se forma objetiva todo o processo, mas vale detalhar cada etapa e determinar a sua importância. O processo se inicia com o usuário na tela de treinar o modelo, em que é disponibilizada uma opção para adicionar um arquivo .csv para treinar o modelo. Após essa adição, os dados novos inseridos pelo novo arquivo serão juntados aos dados antigos, que estavam no datalake. 

Após essa junção, o modelo é retreinado e os resultados são mostrados em seguida. Esses resultados se referem tanto ao novo modelo recém treinado quanto ao modelo antigo antes do novo treinamento. Com ambos sendo exibidos, o usuário deve escolher entre qual dos dois modelos para seguir com a execução do modelo, para assim ser encaminhado para a tela de execução. Finalmente, após escolher um modelo de fato, ele é direicionado para a tela de execução do modelo, e o modelo escolhido é salvo no datalake.

# Pipeline

Uma pipeline no contexto de machine learning refere-se à automação de todo o fluxo de trabalho necessário para treinar e atualizar um modelo preditivo. Isso inclui o retreinamento do modelo, que pode ser realizado utilizando todos os dados disponíveis ou de forma incremental, com a adição de novos dados conforme necessário. O retreinamento incremental é útil para modelos que precisam ser atualizados com frequência, permitindo que novas informações sejam integradas sem a necessidade de reprocessar todo o conjunto de dados. A forma como o processo é implementado depende do projeto e do fluxo definido para o modelo, garantindo que cada etapa seja realizada de maneira eficiente e sem interrupções.

Além do retreinamento, uma parte crucial da pipeline é a gestão dos modelos gerados. Isso envolve a definição de como os modelos devem ser armazenados e de como as versões mais recentes podem substituir o modelo em produção. Um bom gerenciamento de modelos garante que o modelo mais atualizado seja utilizado para fazer previsões, sem comprometer a integridade do sistema, buscando assegurar que os modelos sejam constantemente aprimorados e que novas versões possam ser implementadas de forma transparente e controlada. 

Seguindo estes princípios, a pipeline deste projeto foi desenvolvida para permitir o funcionamento do processo de retreinamento do modelo. Dentre todo este desenvolvimento, cabe destacar algumas etapas:

## Router de retreino

explicação + código

## Controler de lógica para o processamento dos dados

## Junção dos dados

## Retreino cmo novos dados

## Salvamento dos dados e do modelo no datalake

[1] DIAGRAMA DE BLOCOS: CONCEITO E APLICAÇÃO
. Jdevtreinamento. Disponível em: https://www.jdevtreinamento.com.br/diagrama-de-blocos-conceito-e-aplicacao/. Acesso em: 28 set. 2024.
