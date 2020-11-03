From nginx:1.19.2-alpine

RUN set -x \
#======== set timezone ========
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache procps tzdata \
    && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \
#    && /bin/mv -f /tmp/nginx.conf /etc/nginx/nginx.conf \
#    && groupadd -g 1001 ngx_mgr \
#    && useradd -g 1001 -u 1001 ngx_mgr -M -s /sbin/nologin \

#======== nomal config ========
    && /bin/mkdir -p /etc/nginx/vhosts \
    && /bin/mkdir /tmp/nginx \
#    && /bin/chown -R 1001:1001 /etc/nginx/vhosts

#======== clean cache ========
    && rm -rf /var/cache/apk/* /root/.cache 

#USER ngx_mgr

ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
