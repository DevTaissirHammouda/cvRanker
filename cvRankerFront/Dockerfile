# Build Stage
FROM node:20 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code
COPY . ./

# Build the Angular app for production
RUN npm run build -- --configuration=production --project=cvRankerFront

# Production Stage
FROM nginx:alpine

# Remove the default Nginx site configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the Angular build output from the build stage to the Nginx HTML directory
COPY --from=build /app/dist/cv-ranker-front/browser /usr/share/nginx/html

# Expose port 80 for the web server
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
