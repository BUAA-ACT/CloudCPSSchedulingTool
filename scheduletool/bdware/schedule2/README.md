# How to run

### Install packages

```
pip install flask
```
### Run server

```
python http_server.py
```

### Test

```shell
curl -H "Content-Type:application/json" -X POST -d '[{"NodeID": "n1(4,7)", "threshold": 0.5, "NodeFreeResourceInfo": {"freeMEM": "3.1 MiB", "freeCPU": "93.8%"}, "NodeContractResourceInfo": [{"id": "[1]_4", "cpu": "0.0%", "rss": "4 MiB"}, {"id": "[1]_7", "cpu": "0.0%", "rss": "7 MiB"}]}, {"NodeID": "n2(1,3,3)", "threshold": 0.5, "NodeFreeResourceInfo": {"freeMEM": "17 MiB", "freeCPU": "93.8%"}, "NodeContractResourceInfo": [{"id": "[2|4]_1", "cpu": "0.0%", "rss": "1 MiB"}, {"id": "[2]_3", "cpu": "0.0%", "rss": "3 MiB"}, {"id": "[2]_3-(2)", "cpu": "0.0%", "rss": "3 MiB"}]}]' http://127.0.0.1:9292/
```



# More

### Input format

```txt
[{
    "NodeID": "<str>",
    "threshold": <number>,
    "NodeFreeResourceInfo": {
        "freeMEM": "<number> MiB",
        "freeCPU": "<number>%"
    },
    "NodeContractResourceInfo": [{
        "id": "<str>",
        "cpu": "<number>%",
        "rss": "<number> MiB"
    }, {
        "id": "<str>",
        "cpu": "<number>%",
        "rss": "<number> MiB"
    }, {...}]
}, {...}]
```

### Output froamt

```
{
    "result": [{
        "DestinationNode": "<NodeID>",
        "NodeContractID": "<ContraceID>",
        "SourceNode": "<NodeID>"
    }, {...}]
}
```

### Algorithm

Refer to: https://oi-wiki.org/search/idastar/