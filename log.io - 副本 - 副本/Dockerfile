FROM node:14.13.1-stretch

#
USER root
ENV LOGIO_SERVER_CONFIG_PATH /usr/local/log.io/server/server.json
ENV LOGIO_FILE_INPUT_CONFIG_PATH /usr/local/log.io/input/file.json

#   bootstrap.sh
#   sources.list
#   supervisor.conf
COPY ins/ /tmp/

RUN set -xe \
    && sed -i 's#http://deb.debian.org/#http://ftp.sjtu.edu.cn/#' /etc/apt/sources.list \
    && sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list \
    && apt-get update \

#======== set timezone ========
    && apt-get install -y --no-install-recommends \
        tzdata \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \

#======== install supervisor ========
    && apt-get install -y --no-install-recommends \
        procps \
        python3-pip \
    && pip3 install supervisor \
        -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
        --no-cache-dir  \
        supervisor \
        distribute \

#======== install log.io ========
    && npm config set registry https://registry.npm.taobao.org \
    && npm install -g bufferutil utf-8-validate \
    && npm install -g log.io log.io-file-input --user "root" \

#======== nomal config ========
    && rm -rf /usr/local/lib/node_modules/log.io/lib/ui/ \
    && mv /tmp/ui /usr/local/lib/node_modules/log.io/lib/ \
    && rm -rf /usr/local/lib/node_modules/log.io-file-input/lib/input.js \
    && mv /tmp/input.js /usr/local/lib/node_modules/log.io-file-input/lib/ \
    && mv /tmp/bootstrap.sh /usr/local/bin/ \
    && chmod +x /usr/local/bin/bootstrap.sh \
    && mkdir -p /var/log/log.io/server/ /var/log/log.io/input/ \
    && mkdir -p /usr/local/log.io/server /usr/local/log.io/input/ \
    && mkdir -p /etc/supervisor.conf.d/include/ \
    && mv /tmp/supervisor.conf /etc/supervisor.conf.d/ \

#======== clean cache ========
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache 

ENTRYPOINT ["bootstrap.sh"]
CMD ["/bin/bash"]
