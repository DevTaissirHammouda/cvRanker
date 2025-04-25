# Build Stage
FROM node:20 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build --prod

# Production Stage
FROM nginx:alpine
COPY --from=build /app/dist/devops /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
