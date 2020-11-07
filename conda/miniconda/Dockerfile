FROM debian:buster-slim 

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
USER root

#   bootstrap.sh
#   sysctl.conf
#   supervisor.conf 
COPY ins/ /tmp

RUN set -xe \
    && sed -i 's#http://deb.debian.org/#http://ftp.sjtu.edu.cn/#' /etc/apt/sources.list     \
    && sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list  \
#======== set timezone ========
    && apt-get update --fix-missing    \
    && apt-get install -y --no-install-recommends \
        bzip2 zlib1g xz-utils   \
        wget ca-certificates curl git  \
#======== nomal config ========
    && apt-get install -y --no-install-recommends  \
        tzdata \
        procps \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone  \
    && mv -f /tmp/sysctl.conf /etc/  \
    && mv /tmp/bootstrap.sh  /usr/local/bin/ \
#======== nomal config ========
    && chmod +x /usr/local/bin/bootstrap.sh  \
    && mkdir -p /init.d  \
    && mkdir -p /etc/supervisor.conf.d/include/ \
    && mv /tmp/supervisor.conf /etc/supervisor.conf.d/  \
#======== clean cache ========
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

COPY ins/.condarc /tmp
RUN set -xe \
#======== install miniconda ========
    && wget --quiet \
        https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        -O /root/miniconda.sh  \
    && /bin/bash /root/miniconda.sh -b -p /opt/conda \
    && rm /root/miniconda.sh  \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc  \
    && echo "conda activate base" >> ~/.bashrc  \
    && /opt/conda/bin/conda config --set show_channel_urls yes \
    && pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple   \
    && pip config set global.trusted-host https://mirrors.ustc.edu.cn/pypi/web/simple  \
    && mv /tmp/.condarc /root/  \
#======== initialize supervisor ========
    && conda install -n base supervisor  \
#======== clean cache ========
    && /opt/conda/bin/conda clean -y --all

ENTRYPOINT ["bootstrap.sh"]
CMD [ "/bin/bash" ]
