FROM python:3.11-bookworm

RUN apt-get update && \
    apt-get upgrade -y && \
RUN apt-get install -y texlive-base texlive-lang-cyrillic
RUN apt-get clean


WORKDIR /usr/src/tex-engine

COPY requirements.txt /usr/src/tex-engine/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . /usr/src/tex-engine/

CMD ["python3", "-m" , "flask", "--app", "main", "run", "--host=0.0.0.0"]