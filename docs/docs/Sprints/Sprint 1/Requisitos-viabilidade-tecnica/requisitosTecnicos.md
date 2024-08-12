---
title: Requisitos de viabilidade técnica
sidebar_position: 1
description : Levantamento de requisitos técnicos para o projeto
---

# Introdução

&emsp;&emsp;A seção de Requisitos Técnicos é fundamental para o sucesso de qualquer projeto, pois define as especificações necessárias para que o desenvolvimento ocorra de maneira eficiente e alinhada aos objetivos. Portanto, esta documentação tem como propósito detalhar os requisitos técnicos levantados, abordando aspectos cruciais como software, desempenho, e outras necessidades técnicas. Com esses requisitos bem definidos, garantimos que todos os envolvidos no projeto tenham uma compreensão clara das expectativas e das metas a serem alcançadas.

## Proposta Geral do Sistema 

&emsp;&emsp;Durante a apresentação do parceiro, sendo ele a Volkswagen, foi apresentado a necessidade de inspeções mais assertivas antes do processo de rodagem dos veículos na fábrica montadora. Em resposta a essa demanda, foi proposto que os alunos desenvolvessem um projeto de modelo preditivo para classificar os carros com possíveis defeitos nas seguintes categorias: classe 1 e classe 2. O objetivo principal é tornar o processo de inspeção mais eficiente, concentrando-se nos problemas mais prováveis, o que permitirá economizar tempo e reduzir a ocorrência de problemas na fase de testes de rodagem.

&emsp;&emsp;Então, a solução, sendo um modelo preditivo - que, a desejo do parceiro, a acurácia deve ser acima de 95% - e de classificação, tem como objetivo melhorar a eficiência dos testes de rodagem, através da classificação e identificação prévia (durante a montagem) de possíveis defeitos. Além disso, a solução precisa ser projetada visando a escalabilidade do sistema, tendo como proposta calibrar mensalmente com novos dados de produção, visando, cada vez mais, a assertividade no tipo de inspeção que deve ser realizada em determinados veículos na rodagem.

&emsp;&emsp;O sistema será utilizado pelos analistas de sistemas da fábrica para ajustar o processo de inspeção e fornecer uma visualização clara dos resultados do algoritmo. Isso permitirá que o motorista inspetor saiba exatamente o tipo de inspeção necessária para cada veículo, garantindo uma abordagem mais eficaz e direcionada na fase de rodagem.

## Requisitos Funcionais

&emsp;&emsp;Requisitos funcionais são as funcionalidades específicas que o sistema deve proporcionar para executar as operações desejadas.

&emsp;&emsp;Para este projeto, foi elaborado os seguintes requisitos funcionais para atender às necessidades das personas identificadas e entregar o valor estipulado:

&emsp;&emsp;RF1 - Interface Gráfica simples
- A interface gráfica deve apresentar de forma clara e objetiva o resultado da classificação gerada pelo modelo preditivo.
- O usuário final deve ser capaz de identificar, através da interface, qual tipo de inspeção deverá ser realizada.

&emsp;&emsp;RF2 - Funcionalidade que permite importar dados
- Deve suportar a importação de dados a partir de diferentes fontes, como arquivos CSV, bancos de dados SQL, e APIs externas.
- Sendo assim, deve permitir o ajuste e re-treinamento do modelo para melhorar a precisão com base em dados atualizados.

&emsp;&emsp;RF3 - Utilização em Cloud
- A aplicação deve ser migrada para a nuvem, utilizando a infraestrutura da AWS. 
- O sistema deve integrar um dashboard interativo para a visualização dos resultados do modelo e métricas associadas. 
- Deve ser feito o deploy da API do projeto.

&emsp;&emsp;Esses requisitos funcionais cobrem as principais necessidades do projeto e garantem que o modelo preditivo seja eficaz e fácil de usar, atendendo às expectativas da fábrica.

## Requisitos Não Funcionais

&emsp;&emsp;Requisitos não funcionais são as características de qualidade essenciais para o sistema, garantindo que a solução atenda aos critérios de eficiência e eficácia, oferecendo uma base sólida para alcançar os requisitos funcionais com excelência.

&emsp;&emsp;Para este projeto, foi elaborado os seguintes requisitos não funcionais para atender às necessidades das personas identificadas e entregar o valor estipulado:

&emsp;&emsp;RNF1 - Acurácia do Modelo
- Acurácia eficiente em relação às classificações das possíveis manutenções necessárias.
- O modelo deve categorizar os carros corretamente nas duas classes.
- O modelo deve apresentar uma acurácia de 95%.
**Métrica associada** - a seguinte métrica foi definida para que o modelo funcione de forma apropriada:
- A precisão deve ser superior a 95% 

&emsp;&emsp;RNF2 - Usabilidade da Interface Gráfica
- A interface gráfica deve ser projetada para ser fácil de usar e entender, permitindo que os operadores rapidamente compreendam a classe do defeito identificado e o tipo de inspeção que deve ser feita.
**Métrica associada**: A usabilidade da interface será avaliada pelo número de etapas (cliques) necessárias para concluir uma tarefa, limitado a no máximo 3 cliques. Além disso, espera-se que 90% das funcionalidades estejam disponíveis ou indicadas diretamente na tela inicial, facilitando o acesso às ferramentas necessárias.

&emsp;&emsp;Segurança não foi mencionado como um requisito do projeto dado que esse não é o foco do projeto. Apesar disso, é fortemente sugerido que seja desenvolvido um sistema de segurança para esse projeto dado que contém dados confidenciais.

## Diagrama de blocos

&emsp;&emsp;A arquitetura da solução desenvolvida é estruturada em três fases principais: ETL (Extração, Transformação e Carga), Aprendizado de Máquina (Machine Learning) e Dashboard. Todo o sistema é hospedado na nuvem, utilizando os serviços da AWS.

&emsp;&emsp;O processo inicia-se na fase de ETL, onde os dados são cuidadosamente tratados para otimizar o desempenho do modelo preditivo. Durante essa etapa, os dados são também divididos em conjuntos de treino e teste, permitindo a validação eficaz do modelo com base em novos dados inseridos.

&emsp;&emsp;Na fase de aprendizado de máquina, os dados de treino são submetidos ao processo de treinamento do modelo, visando a geração de novos dados que possibilitem prever a ocorrência de falhas.

&emsp;&emsp;Finalmente, na fase do Dashboard, os dados gerados pelo modelo são armazenados em uma nova tabela. Essa tabela alimenta o servidor backend, que, por sua vez, apresenta essas informações em uma interface interativa e intuitiva, facilitando a visualização e interpretação dos resultados.

