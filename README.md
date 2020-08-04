# Tools
把自己的一些想法写出来

## parseMan
解析burp截取的数据包，用法如下：  
```
pm = parseMan('packet.txt')
print('url: ' + pm.request_url)
print('get_data: ' + pm.get_data)
print('post_data: ' + pm.post_data)
...
```
