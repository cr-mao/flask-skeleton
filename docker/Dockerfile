# 基于官方 Python 3.10 镜像构建
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装应用程序依赖
RUN  pip install -r requirements.txt --index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 设置环境变量
ENV PYTHONPATH=.
ENV TZ "Asia/Shanghai"
EXPOSE 5000
# 运行应用程序
CMD [ "python", "scripts/web.py"]