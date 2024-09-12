# Etapa 1: Build da aplicação com Node.js
FROM node:18 AS build

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar package.json e package-lock.json
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar o código restante para o container
COPY . .

# Rodar o build da aplicação
RUN npm run build

# Etapa 2: Usar Nginx para servir os arquivos estáticos
FROM nginx:alpine

# Copiar os arquivos do build gerados na etapa anterior para o diretório de HTML do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expor a porta 88 para servir a aplicação
EXPOSE 88

# Comando para rodar o Nginx
CMD ["nginx", "-g", "daemon off;"]
