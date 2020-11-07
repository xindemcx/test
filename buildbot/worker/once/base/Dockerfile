FROM python:3.9.0-slim-buster
#
ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

ENV NODE_VERSION 10.8.0
ENV YARN_VERSION 1.9.2

#======== set timezone ========
RUN set -xe \
    && sed -i 's#http://deb.debian.org/#http://ftp.sjtu.edu.cn/#' /etc/apt/sources.list \
    && sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list \
    && apt-get update \ 
    && apt-get install -y --no-install-recommends \
            tzdata \
            apt-utils \
            procps \
            dialog \
            xz-utils \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \ 
    && mkdir -p /init.d \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* 
ADD sysctl.conf /etc
    
#======== install node:10.8 && yarn:1.9.2 ========
#   node-v10.8.0-linux-x64.tar.xz
#   yarn-v1.9.2.tar.gz
#   docker-entrypoint.sh
COPY node/ /tmp

RUN set -xe \
    && groupadd --gid 1000 node \
    && useradd --uid 1000 \
               --gid node \
               --shell /bin/bash \
               --create-home node \
    && tar -xJf /tmp/node-v10.8.0-linux-x64.tar.xz \
           -C /usr/local \
           --strip-components=1 \ 
           --no-same-owner \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
    && mkdir -p /opt \
    && npm config set registry https://registry.npm.taobao.org \
    && tar -xzf /tmp/yarn-v1.9.2.tar.gz -C /opt/ \
    && ln -s /opt/yarn-v1.9.2/bin/yarn /usr/local/bin/yarn \
    && ln -s /opt/yarn-v1.9.2/bin/yarnpkg /usr/local/bin/yarnpkg \
    && mv /tmp/docker-entrypoint.sh /usr/local/bin \
    && chmod +x /usr/local/bin/docker-entrypoint.sh \
    && rm -rf /tmp/*

ENTRYPOINT ["docker-entrypoint.sh"]
CMD [ "node" ]
