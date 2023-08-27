FROM node:16-alpine AS build
WORKDIR /app
COPY . .
COPY package*.json ./
RUN npm install
RUN npm run build
EXPOSE 80
CMD  npm run dev -- --host