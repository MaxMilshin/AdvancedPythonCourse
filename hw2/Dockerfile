FROM python:3.8

RUN apt-get update && apt-get install -y \
    texlive \
    texlive-latex-extra \
    texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -i https://test.pypi.org/simple/ latexgen==0.0.3

COPY ./src/main.py /app/src/main.py
COPY ./test_samples /app/test_samples
COPY ./output /app/output

WORKDIR /app