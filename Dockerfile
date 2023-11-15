FROM python:3.11-bookworm

# TinyTeX installation
RUN apt update
RUN apt-get install -y wget perl build-essential python3-dev
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh"

# Add TinyTeX binaries to PATH
ENV PATH="/root/.TinyTeX/bin/x86_64-linux/:${PATH}"

# Set environment variables for TinyTeX
ENV TINYTEX_HOME="/root/.TinyTeX"
ENV TEXMF_HOME="/root/texmf"

ENV APP_HOME=/usr/src/createx
ENV DJANGO_ROOT=$APP_HOME/src
ENV STATIC_ROOT=$APP_HOME/static

RUN mkdir -p $DJANGO_ROOT

COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt

COPY src/ $DJANGO_ROOT/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $DJANGO_ROOT

COPY run.sh /usr/local/bin

ARG APP_VERSION="dev"
ENV APP_VERSION=${APP_VERSION}

CMD ["run.sh"]