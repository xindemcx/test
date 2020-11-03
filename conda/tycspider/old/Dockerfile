FROM python:3.9.0-slim-buster 

USER root

#   bootstrap.sh
#   sources.list
#   supervisor.conf
COPY ins/ /tmp/

RUN set -xe \
    && mv /tmp/sources.list /etc/apt/ \
    && apt-get update \

#======== set timezone ========
    && apt-get install -y --no-install-recommends \
        tzdata \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \

#======== install scrapy ========
#   sys part
    && apt-get install -y gcc \
    && apt-get install -y --no-install-recommends \ 
        apt-transport-https \
        ca-certificates \
        dialog \
    && apt-get install -y --no-install-recommends \
        libfreetype6-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        lz4 \
        python3-olefile \
        openssl \
        python3-pil \
        sqlite3 \
        tk8.6 \
        python3-wheel \
        xz-utils \
        zlib1g \
        zstd \
        procps \
#   py part
    && python -m pip install \ 
        -U pip setuptools \
        -i https://mirrors.aliyun.com/pypi/simple/ \
        --no-cache-dir \
    && pip install \ 
        -i https://mirrors.aliyun.com/pypi/simple/ \
        --no-cache-dir \
		certifi \
		wincertstore \
		certifi \
		wincertstore \
		attrs \
		automat \
		cffi \
		constantly \
		cryptography \
		cssselect \
		fake-useragent \
		hyperlink \
		idna \
		incremental \
		itemadapter \
		itemloaders \
		jmespath \
		lxml \
		parsel \
		protego \
		pyasn1 \
		pyasn1-modules \
		pycparser \
		pydispatcher \
		pyhamcrest \
		pymysql \
		pyopenssl \
		pytz \
		queuelib \
		scrapy \
		selenium \
		service-identity \
		six \
		twisted \
		urllib3 \
		w3lib \
		xlrd \
		zope.interface \

#========   install supervisor ========
    && pip3 install \
        supervisor \
        -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
        --no-cache-dir  \

#======== nomal config ========
    && mv /tmp/bootstrap.sh /usr/local/bin/ \
    && chmod +x /usr/local/bin/bootstrap.sh \
    && mkdir -p /etc/supervisor.conf.d/include/ \
    && mv /tmp/supervisor.conf /etc/supervisor.conf.d/ \

#======== clean cache ========
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

ENTRYPOINT ["bootstrap.sh"]
CMD ["/bin/bash"]
