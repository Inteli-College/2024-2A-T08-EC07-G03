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

A router de retreino é uma rota criada dentro da aplicação FastAPI, responsável por realizar o retreinamento de um modelo preditivo a partir de novos dados que são fornecidos pelo usuário. Esta rota também oferece uma opção para salvar o novo modelo ou restaurar o modelo anterior, permitindo uma escolha flexível do usuário após o retreinamento.

Para mostrar o funcionamento do router de treino presente na solução, segue este trecho do código:

```python
@router.post("/retrain")
async def retrain(
    resultados: List[UploadFile] = File(...),
    falhas: List[UploadFile] = File(...),
    status: List[UploadFile] = File(...),
    save_new_model: bool = True
):
    try:
        # Listas para guardar os nomes dos arquivos de cada tipo
        resultado_names = []
        falhas_names = []
        status_names = []

        # Renomear e processar os arquivos de resultado
        for resultado in resultados:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_resultado_{resultado.filename}'
            await upload_file(resultado, name_file)  # Subir arquivo no Data Lake (simulação)
            resultado_names.append(name_file)

        # Renomear e processar os arquivos de falhas
        for falha in falhas:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_falhas_{falha.filename}'
            await upload_file(falha, name_file)  # Subir arquivo no Data Lake (simulação)
            falhas_names.append(name_file)

        # Renomear e processar os arquivos de status
        for stat in status:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_status_{stat.filename}'
            await upload_file(stat, name_file)  # Subir arquivo no Data Lake (simulação)
            status_names.append(name_file)
            
        # Excluir arquivos originais
        for file in resultado_names + falhas_names + status_names:
            if os.path.exists(file):
                os.remove(file)
                
        print(f"Arquivos processados: {resultado_names}, {falhas_names}, {status_names}")

        # Chama a função de processamento dos dados
        final_file_name = await process_data_datawarehouse(resultado_names, falhas_names, status_names)

        # Chama a função de retreinamento do modelo com os dados fornecidos
        retrainModel(final_file_name)

        if save_new_model:
            return {"detail": "Modelo retreinado e salvo com sucesso."}
        else:
            return {"detail": "Novo modelo descartado. Modelo antigo restaurado com sucesso."}

    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Um dos arquivos CSV está vazio ou inválido.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao retreinar o modelo: {str(e)}")
```

## Controler de lógica para o processamento dos dados

O processamento dos dados é responsável por controlar a lógica de decisão sobre o que fazer com o novo modelo treinado. Dependendo da escolha do usuário, ele salva o novo modelo no lugar do antigo ou descarta o novo e restaura o modelo anterior. Dessa forma, ele gerencia tanto o processamento dos dados quanto a atualização do modelo preditivo de forma flexível e controlada.

## Junção dos dados

O controller da junção dos dados é responsável por gerenciar o processo de combinar os novos dados do arquivo CSV com o data lake existente. Sua principal função é garantir que os dados fornecidos pelo usuário, através de um arquivo CSV, sejam integrados de forma correta e eficiente aos dados antigos, permitindo o retreinamento do modelo com um conjunto de dados atualizado.

Essa junção ocorre ao ler o arquivo CSV e transformar os dados, verificando se eles estão no formato correto. Depois, o controller adiciona esses novos dados ao data lake, formando um único conjunto de dados que será usado no retreinamento. Assim, ele assegura que o modelo seja sempre atualizado com informações relevantes. Segue um trecho do código da junção apenas dos dataframes de resultados, para exemplificar o processo:

```python
    # Merge dos dataframes de resultados
    
    df_resultado = pd.concat(df_resultados, ignore_index=True)
        
    df_status_list = []
    
    
    for file in status_names:
        try:
            file_content = await download_file(file)
            
            file_content = file_content['content']
            
            print(f'{file_content}')

            if file.endswith('.xlsx'):
                df = pd.read_excel(file_content)
            elif file.endswith('.csv'):
                df = pd.read_csv(file_content.decode('utf-8'))
            else:
                raise ValueError(f"Formato de arquivo não suportado: {file}")
            
            # Processamento do DataFrame
            df = await status_processing(df)
            df_status_list.append(df)


        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {str(e)}")
            continue
```

## Retreino com novos dados

O retreino do modelo com os novos dados é a etapa onde o modelo preditivo é atualizado para aprender com as novas informações adicionadas. Após a junção dos novos dados ao data lake, o conjunto completo de dados é utilizado para ajustar novamente os parâmetros do modelo, melhorando sua capacidade de fazer previsões com base nas novas tendências ou padrões encontrados.

Durante o retreino, o modelo usa o mesmo algoritmo e processo de aprendizado que foi utilizado inicialmente, mas com um volume de dados maior. Esse processo é importante para manter a precisão do modelo ao longo do tempo, garantindo que ele continue relevante e eficaz ao lidar com mudanças no comportamento dos dados ou no ambiente em que está sendo aplicado.

Segue o código de retreino do modelo com novos dados, até a parte da separação dos dados de treino e teste:

```python
async def retrainModel(name_file: str):
    try:
        
        file_content = await download_file(name_file)
            
        # Tranformar em um dataframe
        
        df = pd.read_csv(file_content['content'])
        
        # Selecionar apenas as colunas numéricas para normalização
        colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

        # Instanciar o MinMaxScaler
        scaler = MinMaxScaler()

        # Aplicar o scaler para as colunas numéricas
        df[colunas_numericas] = scaler.fit_transform(df_final[colunas_numericas])
    
        # Converter as colunas SomaTempo1, SomaTempo2 e SomaTempo718 para o tipo time delta
        df['SomaTempo1'] = pd.to_timedelta(df['SomaTempo1'])
        df['SomaTempo2'] = pd.to_timedelta(df['SomaTempo2'])
        df['SomaTempo718'] = pd.to_timedelta(df['SomaTempo718'])
        
        df['SomaTempo1'] = df['SomaTempo1'].dt.total_seconds()
        df['SomaTempo2'] = df['SomaTempo2'].dt.total_seconds()
        df['SomaTempo718'] = df['SomaTempo718'].dt.total_seconds()
        
        X = dataset[['Nvezes1', 'Nvezes2', 'Nvezes718', 'SomaTempo1', 'SomaTempo2', 'SomaTempo718', 'TemFalhaRod']].values

        Y = dataset['TemFalhaRod'].values
        
        X = np.expand_dims(X, axis=1)
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
```

## Salvamento dos dados e do modelo no datalake

Por fim, o salvamento dos dados e do modelo no data lake é uma etapa importante para garantir que tanto os dados novos quanto o modelo atualizado sejam armazenados de forma adequada. Após o retreinamento, os novos dados provenientes do arquivo CSV são combinados com o data lake existente, garantindo que todos os dados históricos e recém-adicionados fiquem centralizados para futuros treinamentos e consultas.

Além disso, o salvamento do modelo treinado no data lake permite que a versão atualizada do modelo fique disponível para ser utilizada nas previsões futuras. Se o usuário optar por salvar o novo modelo, ele substitui o modelo antigo no armazenamento. Caso contrário, o modelo anterior é restaurado, mantendo a flexibilidade de usar a versão mais confiável. Isso ajuda a manter um histórico atualizado e centralizado de dados e modelos, essencial para garantir a continuidade e melhoria do sistema de predições.

[1] DIAGRAMA DE BLOCOS: CONCEITO E APLICAÇÃO
. Jdevtreinamento. Disponível em: https://www.jdevtreinamento.com.br/diagrama-de-blocos-conceito-e-aplicacao/. Acesso em: 28 set. 2024.
