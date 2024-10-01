---
title: ETL
sidebar_position: 2
description : Construção do ETL na sprint 4
---

# Introdução

O processo de ETL (Extract, Transform, Load) é uma etapa essencial em qualquer projeto que envolva a manipulação de grandes volumes de dados, especialmente em machine learning. A sigla ETL se refere à extração (Extract) dos dados de diversas fontes, à transformação (Transform) desses dados para garantir sua adequação e à carga (Load) dos dados processados em um ambiente onde possam ser utilizados para análises ou modelos preditivos. Esse fluxo garante que os dados brutos possam ser convertidos em um formato útil e otimizado para as necessidades específicas do projeto.

Na primeira fase, a **extração**, os dados são recuperados de diferentes fontes, como bancos de dados, APIs ou arquivos fornecidos por parceiros. É crucial que esse processo de extração esteja de acordo com o que foi previamente definido no fluxo do modelo, ou seja, de que maneira os dados serão recebidos e com que frequência. Para garantir que o modelo esteja sempre atualizado, o processo de extração deve ser bem planejado e automatizado, permitindo a recuperação eficiente de novos dados para treinamento ou retreinamento do modelo preditivo.

A segunda fase é a **transformação**, onde os dados extraídos passam por uma série de operações para garantir que estejam no formato correto para serem utilizados no modelo. Isso inclui limpeza, formatação, agregação e outras formas de processamento para garantir a integridade dos dados e eliminar inconsistências. Alinhar esse processamento ao fluxo do modelo é fundamental, pois os dados precisam ser preparados de forma que o modelo possa ser treinado com as informações mais relevantes e úteis, maximizando sua eficácia.

Por fim, na etapa de **carga**, os dados transformados são armazenados em um local adequado, como um data warehouse ou banco de dados específico, onde ficarão disponíveis para serem usados no treinamento ou retreinamento do modelo. Esse ambiente de armazenamento precisa ser acessível e otimizado para que o modelo possa consumir os dados de maneira eficiente, permitindo um ciclo contínuo de treinamento e retreinamento, conforme novos dados são extraídos e processados. [1]

O processo de ETL, portanto, é o backbone da preparação de dados, permitindo que informações brutas se tornem a base para decisões inteligentes no modelo preditivo. A partir desses conceitos sobre ETL, todo o banco de dados do projeto foi estruturado e construído. Para ter uma visão da movimentação dos dados como um todo, um diagrama ETL foi desenvolvido:

<p align="center"><b> Figura 1 - Diagrama ETL</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/diagramaETL.png').default} alt="Diagrama ETL"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

A partir da análise desse diagrama, é possível definir como todo os dados estão inseridos em cada uma das três etapas do ETL:

**1. Extração:** A extração de dados no projeto é realizada a partir de arquivos csv, com dados fornecidos pela Volkswagen. Estes arquivos possuem informações sobre a produção dos carros na fábrica, destacando os resultados dessa produção e informando se ocorreu ou não algum erro em cada veículo.

**2. Transformação:** Na etapa de transformação, os dados passam por vários processos de preparação para estarem adequados para serem usados no treinamento do modelo. Alguns desses processos são a padronização dos dados, criação de novas features, remoção de valores nulos e a limpeza dos dados, além da divisão dos dados em conjuntos de treino e teste.

**3. Carga:** Por fim, na última etapa, os dados transformados são armazenados em um data lake, onde ficarão disponíveis para serem usados no retreinamento do modelo.

[1] O que é ETL?. Oracle. Disponível em: https://www.oracle.com/br/integration/what-is-etl/. Acesso em: 28 set. 2024.