# Build Stage
FROM node:20 AS build
WORKDIR /app

# Copy package.json and package-lock.json
COPY cvRankerFront/package.json cvRankerFront/package-lock.json ./

# Install dependencies
RUN npm install

# Copy all other source files into the container
COPY cvRankerFront/ ./

# Build the project
RUN npm run build --prod

# Production Stage
FROM nginx:alpine

# Copy the built project to NGINX's directory
COPY --from=build /app/dist/devops /usr/share/nginx/html

# Expose port 80 for the application
EXPOSE 80

# Start NGINX in the foreground
CMD ["nginx", "-g", "daemon off;"]
