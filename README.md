## runner

基于flask 的 api 脚手架框架，集成配置、log、sqlalchemy，目标就是快速能进行日常api开发。

api 风格： jsonschema



### use age

```shell
export PYTHONPATH=.
python scripts/web.py
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

