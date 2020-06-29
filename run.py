# -*- encoding: utf-8 -*-

from app import app
from app.config import Config

# config.py 中的 debug 模式在正式平台上需要关闭
app.config.from_object(Config['base'])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)