---
title: Desenvolvimento do Frontend
sidebar_position: 1
description : Frontend desenvolvido na sprint 3
---

# Documentação do Projeto

## Tecnologias Utilizadas

### TypeScript (.tsx)
**TypeScript** é uma linguagem de programação que estende o JavaScript, adicionando tipos estáticos. Ao utilizar `.tsx`, estamos lidando com arquivos que combinam TypeScript e JSX, permitindo a criação de componentes React com a segurança adicional de tipos, o que torna o desenvolvimento mais robusto e fácil de manter. O TypeScript ajuda a detectar erros durante o desenvolvimento, evitando problemas em tempo de execução.

### Vite
**Vite** é uma ferramenta de build que oferece um ambiente de desenvolvimento rápido e otimizado. Diferentemente de ferramentas como Webpack, o Vite carrega os módulos sob demanda, resultando em um tempo de inicialização quase instantâneo, especialmente útil em projetos React. Ele também permite uma integração eficiente com TypeScript e frameworks como Tailwind.

### Tailwind CSS
**Tailwind CSS** é um framework CSS utilitário que permite a criação rápida de interfaces de usuário ao fornecer classes de estilos predefinidas. Ele possibilita a criação de layouts responsivos e bem estilizados sem a necessidade de escrever CSS personalizado, o que acelera o desenvolvimento e garante consistência.

## Estrutura do Código

### 1. **Home.tsx**

O componente `Home` é a página principal da aplicação. Ele utiliza o `useState` para gerenciar o estado de visibilidade do popup e `useNavigate` para controlar a navegação entre as páginas. Dois botões principais permitem ao usuário executar um modelo ou iniciar o processo de treinamento.

#### Partes Importantes:
- **Estado e navegação**: O `useNavigate` permite a navegação programática entre páginas. Por exemplo, o botão "Executar" redireciona para `/exc`, enquanto o botão "Treinar" abre um popup modal.
- **Popup Modal**: O modal é controlado por um estado booleano (`isPopupVisible`). A função `handleConfirm` fecha o modal e redireciona para a página de treinamento.

```typescript
const handleExecuteClick = () => {
    navigate('/exc');  
};

const handleTrainClick = () => {
    setIsPopupVisible(true); 
};
```

### 2. **ExcModelPage.tsx**

Esta página exibe o resultado de um modelo executado, incluindo gráficos e métricas. O uso de estados permite controlar a abertura de popups, e a estrutura de layout com Tailwind facilita a estilização da página.

#### Partes Importantes:
- **Seção de Resultados**: São exibidos o resultado atual e o modelo anterior, com caixas estilizadas utilizando Tailwind.
- **Gráficos Placeholder**: Espaços são reservados para gráficos e métricas, permitindo futura integração com bibliotecas de visualização.

```typescript
<div className="w-full bg-gray-300 h-10 rounded-lg flex justify-center items-center">
  <span className="text-black">XXXXXX</span>
</div>
```

### 3. **ExcPage.tsx**

A página `ExcPage` lida com o upload de arquivos e a inserção de dados necessários para a execução de modelos. Inclui componentes reutilizáveis como `FileUpload` e `KNRInput`.

#### Partes Importantes:
- **Componente de Input**: Um campo de entrada é fornecido para que o usuário insira seu KNR. O botão "Confirmar" navega para a página de progresso da execução do modelo.
- **File Upload**: O componente `FileUpload` facilita o upload de arquivos, como `.csv`, necessários para a análise.

```typescript
<KNRInput />
<ConfirmButton />
```

### 4. **ExcProgressPage.tsx**

Essa página simula o progresso da execução de um modelo, exibindo uma barra de progresso que é atualizada periodicamente usando `useEffect`.

#### Partes Importantes:
- **Simulação de Progresso**: O estado `progress` é atualizado a cada segundo até atingir 100%, simulando a execução de um modelo de machine learning.
- **Barra de Progresso**: Um componente `BarExc` é responsável por renderizar visualmente o progresso.

```typescript
useEffect(() => {
  const interval = setInterval(() => {
    setProgress((prev) => {
      if (prev < 100) {
        return prev + 10;
      } else {
        clearInterval(interval);
        return 100;
      }
    });
  }, 1000);
}, []);
```

### 5. **App.tsx**

O componente `App` é o ponto de entrada da aplicação, responsável por definir as rotas utilizando o `react-router-dom`. Cada rota mapeia um caminho específico para um componente.

#### Partes Importantes:
- **Rotas**: O sistema de rotas é responsável por controlar a navegação entre páginas. Por exemplo, a rota `/exc` leva à página `ExcPage`, enquanto `/excProgress` leva à página de progresso.

```typescript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/exc" element={<ExcPage />} />
  <Route path="/excProgress" element={<ExcProgressPage />} />
</Routes>
```
