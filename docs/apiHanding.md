## api 设计

runner的API不是REST风格，更接近于json-rpc风格。

### 使用jsonschema做参数校验

[jsonschema](https://json-schema.org/)

- 相比常见的各种http校验库，jsonschema更加简单、清晰、容易掌握。

### json-rpc风格的优势

- URL与函数名一致，不存在转化问题。
- 参数一律位于请求的json中，不存在歧义。
- 错误码位于输出的json中，可以表达无数种错误。
- URL是固定值，method只能是POST，参数只能是json，后端封装容易。
