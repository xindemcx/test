FROM python:3.7.0

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
	gettext \
	mysql-client \
#	libmysqlclient-dev \
	libpq-dev \
	sqlite3 \
    && rm -rf /var/lib/apt/lists/* \

ENV PROJECT_PATH /usr/src/app
ENV PROJECT_LOG_PATH /var/log/project

RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        supervisor \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/log/supervisor \
    && chmod 777 /var/log/supervisor
	
COPY bootstrap.sh /bootstrap.sh
RUN set -x \
    && mkdir -p /bootstrap/init.d \
    && chmod +x /bootstrap.sh \
    && mv /bootstrap.sh /bootstrap/
ENV BOOTSTRAP_PATH /bootstrap

COPY r.txt /tmp/r.txt
RUN set -x \
	&& pip install -r /tmp/r.txt \
	&& rm -rf /tmp/r.txt

WORKDIR $PROJECT_PATH
VOLUME ["$PROJECT_PATH", "$PROJECT_LOG_PATH"]

ENTRYPOINT ["/bootstrap/bootstrap.sh"]
CMD ["/bin/bash"]
