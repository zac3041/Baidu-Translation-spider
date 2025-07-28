# Baidu-Translation-spider百度翻译补环境爬虫
Python使用execjs环境补全方案
需要下载nodejs

以下是测试接口，接口没问题的话，补环境方法就是没失效
## 多语言翻译API接口文档

### 请求接口
http://pyjk.daniuniu.top/translate

### 请求头
```http
Content-Type: application/json

python写法
headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
### 请求参数
{
    "text": "需要翻译的文本",
    "target_lang": "目标语言代码",
    "source_lang": "源语言代码(可选，不提供则自动检测)"
}
### 请求示例
带源语言指定
curl -X POST http://pyjk.daniuniu.top/translate \
-H "Content-Type: application/json" \
-d '{
    "text": "Hello world", 
    "source_lang": "en",
    "target_lang": "zh"
}'

自动检测源语言
curl -X POST http://pyjk.daniuniu.top/translate \
-H "Content-Type: application/json" \
-d '{
    "text": "こんにちは世界",
    "target_lang": "zh"
}'
