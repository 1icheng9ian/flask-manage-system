# IoT Manage System
## By Li Chengqian
 
## 一、框架 
### 后端
+ Flask Nginx uWSGI  
### 数据库  
+ MongoDB  
`https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/`

## 二、部署
### uwsgi.ini 配置
```
[uwsgi]

socket = 127.0.0.1:5000

chdir = /home/your_name/flask-manage-system

wsgi-file = manage.py

buffer-size = 65536

callable = app

pidfile = %(chdir)/uwsgi.pid

daemonize = %(chdir)/uwsgi.log
```

### nginx配置 `/etc/nginx/sites-enabled/default`
```
server {
        listen 80;
        server_name your_ip;

        location / {
                include      uwsgi_params;
                uwsgi_pass   127.0.0.1:5000;
                uwsgi_param UWSGI_PYHOME /your_python_virtual_env_path;
                uwsgi_param UWSGI_CHDIR /home/your_name/flask-manage-system;
                uwsgi_param UWSGI_SCRIPT manage:app;
        }
}
```

### nginx配置更新
`sudo nginx -s reload`

### Start
`uwsgi --ini uwsgi.ini`

### Stop
`uwsgi --stop uwsgi.pid`

### 查看uwsgi进程
`ps aux | grep uwsgi`

### AEP平台推送地址
`http://your_ip/push_port`

### MongoDB

#### Start
`sudo systemctl enable mongod`

#### Stop
`sudo systemctl stop mongod`

#### Restart
`sudo systemctl restart mongod`