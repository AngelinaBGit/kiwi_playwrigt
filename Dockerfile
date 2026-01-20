FROM python:3.12-slim

# Install system dependencies required by Playwright
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libxkbcommon0 \
    libgtk-3-0 \
    libgbm1 \
    libasound2 \
    libxshmfence1 \
    libdrm2 \
    libxcomposite1 \
    libxrandr2 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxi6 \
    libxtst6 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libcups2 \
    libatk1.0-0 \
    libatspi2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps

# Default command to run tests
CMD ["pytest"]
