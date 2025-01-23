# Nginx-QUIC Configuration

http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  logs/access.log  main;

    sendfile        on;
    tcp_nopush      on;
    tcp_nodelay     on;
    keepalive_timeout  65;
    types_hash_max_size 2048;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen       443 ssl http2;
        listen       [::]:443 ssl http2;
        server_name  localhost;

        ssl_certificate "/etc/nginx/ssl/nginx.crt";
        ssl_certificate_key "/etc/nginx/ssl/nginx.key";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page  404              /404.html;
        location = /40x.html {
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
        }
    }
}
