# Build Stage
FROM node:20 AS build
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . ./

# Build the project
RUN npm run build --prod

# Production Stage
FROM nginx:alpine

# Copy the build output to nginx's html directory
COPY --from=build /app/dist/devops /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
