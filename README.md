## runner

基于flask 的 api 脚手架框架，集成配置、log、sqlalchemy，目标就是快速能进行日常api开发。

api 风格： jsonschema



### use age

```shell
export PYTHONPATH=.
# 启动web api服务
python scripts/web.py

# demo job服务, 如一次性运行脚本
python scripts/demo_job.py

# 守护进程 job服务
python scripts/daemon_job_demo.py
```

### docs

- [api处理](docs/apiHanding.md)

### demo request

```shell
curl --location --request POST 'http://127.0.0.1:5000/runner/domo_api/info' \
--header 'content-type: application/json' \
--data-raw '{
    "arg1": "abcdefghi"
}'

# method=>demoHandler.info 
```

