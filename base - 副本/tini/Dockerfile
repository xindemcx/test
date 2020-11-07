FROM debian:latest 

#
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

#   ./tini
#   sources.list
#   sysctl.conf 
COPY ins/ /tmp

RUN set -xe \

#======== initialize environment ========
    && sed -i 's#http://deb.debian.org/#http://ftp.sjtu.edu.cn/#' /etc/apt/sources.list \
    && sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list \
    && apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends \
        bzip2 zlib1g xz-utils \
        wget ca-certificates curl git \
        procps dialog \
    && mv -f /tmp/sources.list /etc/apt \
    && mv -f /tmp/sysctl.conf /etc/ \
    && apt-get update --fix-missing \

#======== install tini ========
#    && wget --quiet https://github.com/krallin/tini/releases/download/v0.19.0/tini -O /usr/bin/tini \
    && mv /tmp/tini /usr/bin/tini \
    && chmod +x /usr/bin/tini \

#======== clean cache ========
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
