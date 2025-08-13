FROM python:3.10-slim
WORKDIR /streamlit

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/korceo/aaplticker.git .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK --interval=10s --timeout=5s --retries=6 --start-period=15s \
  CMD bash -lc 'curl -fsS http://localhost:8501/_stcore/health >/dev/null || exit 1'

ENTRYPOINT ["streamlit", "run", "ticker.py", "--server.port=8501", "--server.address=0.0.0.0"]