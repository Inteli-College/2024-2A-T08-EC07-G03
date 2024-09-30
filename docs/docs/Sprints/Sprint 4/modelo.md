---
title: Tratamento de dados e Feature Engineering
sidebar_position: 1
description : Tratamento de dados e Feature Engineering desenvolvidos na sprint 3
---

# Introdução

&emsp;&emsp;Durante a sprint 03, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 02. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento. 

<p align="center"><b> Figura 1 - Crisp-DM</b></p>
<div align="center" class="zoom-image">
  <img src={require('./../../../static/img/crispEtapas.png').default} alt="Crisp-DM"/>
  <p><b>Fonte:</b> EBAC Online</p>
</div>

## Metodologia

&emsp;&emsp;Durante a sprint 4, o grupo trabalhou na exploração de novas features para o modelo preditivo com base no protótipo desenvolvido na sprint 3. Assim como nas fases anteriores, a metodologia CRISP-DM foi fundamental para o desenvolvimento.

&emsp;&emsp;Nesta sprint, identificou-se que a planilha "STATUS" fornecida pelo parceiro continha informações relevantes sobre o tempo gasto nas estações, juntamente com as informações de identificação de resultados do sistema em relação aos KNRs, por meio da tabela de resultados na coluna NAME.

&emsp;&emsp;Para melhor aproveitamento dos dados, foi realizado um tratamento em cada uma das tabelas para garantir que não haveria dados nulos, repetidos ou dados de estações pelas quais os KNRs passam depois do teste de rodagem, que não serão utilizados no treinamento do modelo. Isso porque, no momento de uso real desse projeto, esses dados ainda não terão sido obtidos, dado que o objetivo do projeto é desenvolver uma solução que será utilizada antes do processo de rodagem dos carros da VW.

&emsp;&emsp;