FROM svr.base:v1.3

#   Image built with:
#       debian: buster-slim
#       python: 3.9.0

COPY requirements.txt /tmp
RUN set -x \
    && apt-get update --fix-missing \
    && apt-get install -y gcc \
    && apt-get install -y --no-install-recommends \
    	gettext \
    	libmariadb-dev-compat \
        libpq-dev \
    	sqlite3 \
        libffi6 \
        libfreetype6-dev \
        libjpeg-dev \
        libpng-dev  \
        openssl \
    \
#======== install django ========
    && pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple \
    && pip config set global.trusted-host https://mirrors.ustc.edu.cn/pypi/web/simple \
    && pip install --no-cache-dir \
                   -r /tmp/requirements.txt \
#======== clean cache ========
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

ENTRYPOINT ["bootstrap.sh"]
CMD ["/bin/bash"]

