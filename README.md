# CloudCPS-Scheduling

## 来源

@王旭

4. 系统工作
（3）调度工具

## 思路

多层嵌套[匈牙利](https://zh.wikipedia.org/zh-hans/匈牙利算法)匹配。

下面是CloudLayer匹配示例：

![image-20200401170619671](https://tva1.sinaimg.cn/large/00831rSTly1gdedmo2grcj31gc0u0wsr.jpg)

## 进展

本地读取需求描述 Json，查询数据库，做出匹配，将匹配写入数据库：

![image-20200329164704737](https://tva1.sinaimg.cn/large/00831rSTly1gdaw7p0fe0j30nc0kak55.jpg)

