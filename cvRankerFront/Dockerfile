# Build Stage
FROM node:20 AS build
WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the app and build
COPY . ./
RUN npm run build --prod

# Production Stage
FROM nginx:alpine

# Copy the correct build output
COPY --from=build /app/dist/cv-ranker-front /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
