FROM node:10.8-py386-tz 

USER root
COPY known_hosts /home/buildbot/.ssh/
#======== install buildbot-worker ========
RUN set -xe \
    && groupadd --gid 1001 buildbot \
    && useradd --uid 1001 \
        --gid buildbot \
        --shell /bin/bash \
        --create-home buildbot \
    && apt-get update \ 
    && apt-get install -y gcc \
    && apt-get install -y --no-install-recommends \
        git \
        subversion \
        libffi-dev \
        libssl-dev \
        openssh-client \
    && pip3 install buildbot-worker \
        -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
        --no-cache-dir  \
    && mkdir -p /var/log/bdtworker/ \ 
    && mkdir -p /home/buildbot/.ssh/ \
    && mkdir -p /home/buildbot/.npm \
    && chown -R buildbot:buildbot /home/buildbot/ \
    && sed -i 's/HashKnownHosts yes/HashKnownHosts no/' /etc/ssh/ssh_config \
    && npm config -g set registry https://registry.npm.taobao.org \
#======== clean cache ========
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*


WORKDIR /buildbot
USER buildbot

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["twistd", "--pidfile=", "--nodaemon", "--python=buildbot.tac"]
