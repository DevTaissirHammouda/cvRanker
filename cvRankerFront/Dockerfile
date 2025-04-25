# Build Stage
FROM node:20 AS build
WORKDIR /app

# Copy package.json and package-lock.json from cvRankerFront
COPY cvRankerFront/package.json cvRankerFront/package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files from cvRankerFront to /app
COPY cvRankerFront/ ./

# Build the project
RUN npm run build --prod

# Production Stage
FROM nginx:alpine

# Copy the build output from the build stage to nginx's html directory
COPY --from=build /app/dist/devops /usr/share/nginx/html

# Expose port 80 for the application
EXPOSE 80

# Start NGINX in the foreground
CMD ["nginx", "-g", "daemon off;"]
