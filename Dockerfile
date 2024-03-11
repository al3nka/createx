FROM python:3.11-bookworm

ENV APP_HOME=/usr/src/createx
ENV DJANGO_ROOT=$APP_HOME/src
ENV STATIC_ROOT=$DJANGO_ROOT/static

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