---
title: Requisitos de Visualização
sidebar_position: 1
description: Levantamento de requisitos de visualização para o projeto
---

# Introdução

Este documento detalha o levantamento de requisitos de visualização para o projeto de modelo preditivo da Volkswagen, focado na identificação de possíveis defeitos em carros T-Cross na linha de produção, determinando se é necessário ou não passar pelos testes físicos. A proposta é criar um dashboard que permita a visualização clara, interativa e segura dos dados relacionados ao ciclo de produção, com foco na detecção preventiva de possíveis defeitos.

## Necessidades do Projeto

- **Clareza e Intuitividade na Apresentação dos Dados e Resultados:** A visualização deve ser clara e intuitiva, permitindo que os analistas de sistemas e outros stakeholders identifiquem rapidamente os pontos críticos na linha de produção. O sistema de visualização precisa facilitar a compreensão das informações, destacando áreas de risco e fragilidade.

- **Interatividade:** A visualização deve ser interativa, permitindo que os usuários explorem diferentes cenários e dados, como o impacto de variações nas matérias-primas ou nas práticas de logística. A interação pode incluir zoom, filtragem de dados e a seleção de diferentes camadas de informação para uma análise mais detalhada.

- **Integração de Dados Dinâmicos:** O sistema deve integrar dados em tempo real ou dados que possam ser atualizados periodicamente para refletir os novos dados gerados. Isso inclui a capacidade de visualizar dados de novos lotes de produção, impactos atualizados e o desempenho do modelo preditivo ao longo do tempo.

- **Segurança de Dados:** É crucial garantir que o sistema de visualização tenha medidas de segurança robustas, como autenticação de usuários e criptografia de dados, para proteger informações sensíveis.

- **Escalabilidade:** A solução deve ser escalável para acomodar um aumento no volume de dados ou novos requisitos de visualização no futuro.

## Possibilidades de Acesso e Visualização

### Tipos de Usuários e Permissões de Acesso

- **Gerentes de Produção:** Acesso a uma visão geral do ciclo produtivo com dashboards que apresentam KPIs, áreas de risco, e o desempenho geral do processo produtivo. Eles terão permissão para visualizar dados históricos e realizar comparações de desempenho entre diferentes períodos.

- **Analistas de Sistemas:** Acesso a dados detalhados, incluindo a visualização de métricas de desempenho do modelo preditivo, taxas de defeitos por classe, e a análise de tendências. Eles terão a capacidade de exportar dados e realizar análises mais profundas.

- **Equipe de ESG (Environmental, Social, and Governance):** Acesso a dashboards que destacam os impactos ambientais e sociais ao longo do ciclo produtivo, incluindo métricas de sustentabilidade e comparações com benchmarks da indústria.

### Frontend do Dashboard

#### Gráficos e Dados

1. **Visão Geral do Ciclo Produtivo:**
   - **Gráfico de Fluxo de Processo (Process Flow Diagram):** Exibe todas as etapas do ciclo produtivo, desde a entrada das matérias-primas até a saída do produto final. Cada etapa pode ser clicada para mostrar dados detalhados, como tempo de ciclo, uso de recursos e principais KPIs.
   - **Gráfico de Barras Empilhadas:** Mostra a distribuição dos defeitos identificados por classe (Classe 1 e Classe 2) ao longo do tempo. Permite que os usuários vejam a evolução das taxas de defeitos e identifiquem possíveis padrões.

2. **Análise de Risco e Fragilidade:**
   - **Heatmap:** Destaca as áreas do processo produtivo com maior incidência de problemas e riscos, com cores indicando a gravidade. Esse gráfico ajuda a visualizar rapidamente os pontos de atenção na linha de produção.
   - **Gráfico de Pareto:** Utilizado para identificar os principais fatores que contribuem para defeitos no processo produtivo, mostrando quais etapas ou componentes têm o maior impacto.

3. **Impactos Ambientais e Sociais:**
   - **Gráfico de Radar:** Comparação das métricas de sustentabilidade (uso de energia, emissão de CO2, consumo de água, etc.) em diferentes partes do ciclo produtivo. Permite visualizar o desempenho em relação a objetivos de ESG.
   - **Gráfico de Linha:** Exibe a evolução das iniciativas de economia circular ao longo do tempo, como a quantidade de materiais reciclados versus descartados, mostrando o impacto das políticas de sustentabilidade da empresa.

4. **Desempenho do Modelo Preditivo:**
   - **Gráfico de Confusão (Confusion Matrix):** Mostra a precisão do modelo preditivo, exibindo a distribuição de previsões corretas e incorretas para as classes 1 e 2.
   - **Gráfico de Evolução da Acurácia:** Linha do tempo mostrando como a acurácia do modelo tem melhorado ao longo do tempo com a introdução de novos dados e ajustes de parâmetros.

### Critérios de Visualização

- **Relevância:** Somente os dados mais relevantes e acionáveis devem ser destacados. Os gráficos devem facilitar a tomada de decisão, evitando sobrecarga de informações.
  
- **Consistência Visual:** Utilizar uma paleta de cores consistente e um layout uniforme em todo o dashboard para facilitar a navegação e interpretação dos dados.

- **Acessibilidade:** Garantir que o dashboard seja acessível para todos os usuários, incluindo aqueles com deficiências visuais, através de contrastes adequados e suporte para leitores de tela.

- **Atualização Dinâmica:** Os dados devem ser atualizados automaticamente e em tempo real, garantindo que as informações apresentadas estejam sempre atuais.

- **Feedback ao Usuário:** Fornecer feedback visual, como animações sutis, para indicar quando novos dados são carregados ou quando uma interação (como a aplicação de um filtro) foi bem-sucedida.

Este conjunto de requisitos e especificações fornecerá uma base sólida para o desenvolvimento do dashboard, garantindo que ele atenda às necessidades dos usuários e auxilie na melhoria contínua do processo produtivo na Volkswagen.
