FROM python:3.10-slim


# Install dependencies
WORKDIR /aschonn-mlops
COPY setup.py setup.py
COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install --upgrade pip setuptools wheel \
    && python3 -m pip install -e . --no-cache-dir \
    && python3 -m pip install protobuf==3.20.1 --no-cache-dir \
    && apt-get purge -y --auto-remove gcc build-essential


