FROM svr.base:v1.0 

#   install buildbot-worker
RUN set -xe \
    && apt-get update \
    && apt-get install -y gcc \
    && apt-get install -y --no-install-recommends \
        git \
        subversion \
        libffi-dev \
        libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install buildbot-worker \
        -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
        --no-cache-dir  \
    && mkdir -p /var/log/bdtworker/ 

WORKDIR /buildbot
ENTRYPOINT ["bootstrap.sh"]
CMD ["/bin/bash"]
