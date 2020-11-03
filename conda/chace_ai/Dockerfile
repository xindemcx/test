FROM svr.base:v1.3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
#   ./.condarc
#   env.yaml
COPY ins/ /tmp
RUN set -xe \
#======== initialize environment ========
    && apt-get update --fix-missing \
    && apt-get install -y gcc \
    && apt-get install -y --no-install-recommends \
        bzip2 zlib1g xz-utils lzma \
        wget ca-certificates curl git \

#======== install miniconda ========
    && wget --quiet https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /root/miniconda.sh \
    && /bin/bash /root/miniconda.sh -b -p /opt/conda \
    && rm /root/miniconda.sh \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate base" >> ~/.bashrc \
#    && /opt/conda/bin/conda build purge-all \
    && /opt/conda/bin/conda config --set show_channel_urls yes \
    && mv -f /tmp/.condarc /root/ \
    && pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple \
    && pip config set global.trusted-host https://mirrors.ustc.edu.cn/pypi/web/simple \

#======== install chace_ai ========
    && /opt/conda/bin/conda env update -n base -f /tmp/env.yaml \

#======== clean cache ========
    && apt-get clean \
#    && /opt/conda/bin/conda clean -tipsy \
    && /opt/conda/bin/conda clean -y --all \
    && rm -rf /var/lib/apt/lists/* /root/.cache

ENTRYPOINT ["bootstrap.sh"]
CMD [ "/bin/bash" ]
