FROM python:3.10-slim-bookworm

# System packages
RUN apt-get update && apt-get install -y \
    wget gnupg ca-certificates curl unzip \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libxkbcommon0 libgtk-3-0 libgbm1 libasound2 \
    libxcomposite1 libxdamage1 libxrandr2 libxfixes3 \
    libpango-1.0-0 libcairo2 \
    tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd \
    fonts-liberation fonts-dejavu-core \
    ffmpeg \
    build-essential python3-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright + Chromium
RUN pip install playwright
RUN playwright install chromium

# Install uv package manager
RUN pip install uv

WORKDIR /app
COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

# Install Python dependencies (IMPORTANT FIX)
RUN uv pip install --system -r requirements.txt

EXPOSE 7860

CMD ["uv", "run", "main.py"]
