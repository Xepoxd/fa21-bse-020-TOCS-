FROM node:14

# Set working directory
WORKDIR /app

# Copy static files
COPY . .

# Install HTTP server to serve static files
RUN npm install -g serve

# Expose port 3000
EXPOSE 3000

# Serve the static content
CMD ["serve", "-s", ".", "-l", "3000"]
