## runner

this is a web framework based on python Flask Framework

api style: jsonschema validate

### use age

```shell
export PYTHONPATH=.
python scripts/web.py
```

### docs

- [api handing](docs/apiHanding.md)

### demo request

```shell
curl --location --request POST 'http://127.0.0.1:5000/runner/domo_api/info' \
--header 'content-type: application/json' \
--data-raw '{
    "xdd": "ssdss"
}'

# method=>demoHandler.info 
```

