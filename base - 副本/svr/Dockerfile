FROM python:3.9.0-slim-buster

USER root
#   bootstrap.sh
#   sources.list
#   supervisor.conf
#   sysctl.conf
COPY ins/ /tmp/

RUN set -xe \
    && sed -i 's#http://deb.debian.org/#http://ftp.sjtu.edu.cn/#' /etc/apt/sources.list \
    && sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list \
    && apt-get update \

#======== set timezone ========
    && apt-get install -y --no-install-recommends \
        tzdata \
        apt-utils \
        procps \
        dialog \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \

#========   install supervisor ========
    && pip3 install supervisor \
        -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
        --no-cache-dir  \

#======== nomal config ========
    && mv -f /tmp/sysctl.conf /etc/ \
    && mv /tmp/bootstrap.sh /usr/local/bin/ \
    && chmod +x /usr/local/bin/bootstrap.sh \
    && mkdir -p /init.d \
    && mkdir -p /etc/supervisor.conf.d/include/ \
    && mv /tmp/supervisor.conf /etc/supervisor.conf.d/ \

#======== clean cache ========
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

ENTRYPOINT ["bootstrap.sh"]
CMD ["/bin/bash"]

