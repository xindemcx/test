FROM redis:6.0.8-alpine

#   bootstrap.sh
#   supervisor.conf
COPY configs/ /tmp/

RUN set -xe \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \

#======== set timezone ========
    && apk add --no-cache \
        tzdata \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \
                    
#======== install supervisor ========
    && apk add --no-cache procps py3-pip \
    && pip3 install \
        -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
        --no-cache-dir \
        supervisor \

#======== nomal config ========
    && chmod +x /tmp/bootstrap.sh \
    && chown -R redis:redis /tmp/bootstrap.sh \
                            /tmp/supervisor.conf \
    && mv /tmp/bootstrap.sh /usr/local/bin/ \
    && mkdir -p /etc/supervisor.conf.d/include/ \
    && mv /tmp/supervisor.conf /etc/supervisor.conf.d/ \ 

#======== clean cache ========
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/* 
    && rm -rf /var/cache/apk/* /root/.cache /tmp/*         

USER redis
ENTRYPOINT ["bootstrap.sh"]
#CMD ["supervisord", "-c", "/etc/supervisor.conf.d/supervisor.conf"]
