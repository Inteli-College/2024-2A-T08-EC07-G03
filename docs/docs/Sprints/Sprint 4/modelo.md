---
title: Tratamento de dados e Feature Engineering
sidebar_position: 1
description: Tratamento de dados e Feature Engineering desenvolvidos na sprint 3
---

# Introdução

&emsp;&emsp;Durante a sprint 04, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 03. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento.

<p align="center"><b> Figura 1 - Crisp-DM</b></p>
<div align="center" class="zoom-image">
  <img src={require('./../../../static/img/crispEtapas.png').default} alt="Crisp-DM"/>
  <p><b>Fonte:</b> EBAC Online</p>
</div>

## Metodologia

&emsp;&emsp;Durante a sprint 4, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 3. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento.

&emsp;&emsp;Nesta sprint, identificou-se que a planilha "STATUS" fornecida pelo parceiro continha informações relevantes sobre o tempo gasto nas estações, juntamente com as informações de identificação de resultados do sistema em relação aos KNRs, por meio da tabela de resultados na coluna NAME.

&emsp;&emsp;Para melhor aproveitamento dos dados, foi realizado um tratamento em cada uma das tabelas para garantir que não haveria dados nulos, repetidos ou dados de estações pelas quais os KNRs passam depois do teste de rodagem, que não serão utilizados no treinamento do modelo. Isso porque, no momento de uso real desse projeto, esses dados ainda não terão sido obtidos, dado que o objetivo do projeto é desenvolver uma solução que será utilizada antes do processo de rodagem dos carros da VW.

&emsp;&emsp;Além disso, os dados da coluna NAME da tabela RESULTS foram utilizados, já que essa coluna fornece informações sobre os resultados do sistema após as fases de parafusamento, pintura e outras fases que envolvem muitos detalhes. Para isso, cada NAME único foi transformado em uma coluna com o nome respectivo. Caso o KNR tenha recebido a característica do NAME, ele recebeu o número 1, indicando que teve aquele resultado; caso contrário, recebeu o valor 0, indicando que não teve aquele resultado.

&emsp;&emsp;Ao final do tratamento dos dados, as novas features de STATUS e RESULTS foram agrupadas em um único dataset. Esse novo dataset foi salvo como `results_merged.csv` e utilizado para o treinamento do modelo LSTM. Um ponto importante a se considerar é que, após todo o tratamento dos dados, a base de dados ficou com cerca de 300 linhas, o que é uma quantidade muito pequena para o treinamento do modelo. Por isso, é importante que na próxima sprint seja feita uma análise no último tratamento dos dados para garantir que nenhum dado foi perdido nesse processo.

&emsp;&emsp;Como mencionado anteriormente, o algoritmo escolhido para realizar o treinamento do modelo foi o LSTM. O modelo foi treinado com 100 épocas e chegou aos seguintes resultados:
- Acurácia de teste: 98%
- Precisão: 77%
- Recall: 100%
- F1-Score: 87%

&emsp;&emsp;O próximo passo é testar a performance do modelo com os novos dados fornecidos pela VW, para analisar com mais dados o que deve ser melhorado no modelo.
