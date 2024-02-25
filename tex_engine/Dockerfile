FROM python:3.11-bookworm

RUN apt update
RUN apt-get install -y wget perl build-essential python3-dev
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh"| sh
RUN apt-get clean


# Add TinyTeX binaries to PATH
ENV PATH="/root/.TinyTeX/bin/x86_64-linux/:${PATH}"

# Set environment variables for TinyTeX
ENV TINYTEX_HOME="/root/.TinyTeX"
ENV TEXMF_HOME="/root/texmf"

WORKDIR /usr/src/tex-engine

COPY requirements.txt /usr/src/tex-engine/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . /usr/src/tex-engine/

CMD ["python3", "-m" , "flask", "--app", "main", "run", "--host=0.0.0.0"]