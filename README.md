# CloudCPS-Scheduling

## 来源

@王旭

4. 系统工作

  （3）调度工具

## 使用

```shell
python setup.py bdist_wheel
pip install -U dist/scheduling_tool*
```

## 思路

默认的调度算法仅考虑实体间的包含关系，基于[匈牙利算法](https://zh.wikipedia.org/zh-hans/匈牙利算法)将复合实体视作一个抽象节点进行嵌套二分图匹配。

下面以`CloudLayer`为例，来展示算法逻辑。

`CloudLayer`的结构如下所示，`CloudLayer`包含若干`DataCenter`，`DataCentor`包含若干`CloudNode`，`CloudNode`包含若干`Container`：

```protobuf
message CloudLayer {
  repeated Datacenter datacenters = 2;
}

message Datacenter {
  optional string id = 1;
  required string location = 2;
  optional string name = 3;
  repeated CloudNode cloudnodes = 4;
}

message CloudNode {
  optional string name = 1;
  required string id = 2; // 对需求来说是有向图的ID，对资源来说是数据库ID
  optional string location = 3;
  optional double cpu = 4;
  optional double memory = 5;
  optional double store = 6;
  repeated Container containers = 7;
}
```

当需求端与资源端的`CloudLayer`进行匹配时，将`DataCenter`实体视作抽象节点，调度问题被转化为传统二分图匹配问题。下图中![](http://latex.codecogs.com/gif.latex?\\D_1%2cD_2%2cD_3) 表示需求描述`CloudLayer`中的所有`DataCenter`，![](http://latex.codecogs.com/gif.latex?\\d_1%2cd_2%2cd_3) 表示资源描述`CloudLayer`中所有的`DataCenter`。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1gdraorqt0rj30xe0u0who.jpg" alt="image-20200412210154856" style="zoom:33%;" />

此时，若![](http://latex.codecogs.com/gif.latex?\\D_1) 与![](http://latex.codecogs.com/gif.latex?\\d_1) 匹配，则需要满足![](http://latex.codecogs.com/gif.latex?\\D_1) 与 ![](http://latex.codecogs.com/gif.latex?\\d_1) 中的`CloudNode`能够匹配。

我们继续将`CloudNode`实体视作抽象节点进行二分图匹配。如下图所示，![](http://latex.codecogs.com/gif.latex?\\C_1%2c+C_2) 为`DataCenter`![](http://latex.codecogs.com/gif.latex?\\D_1) 中的`CloudNode`，![](http://latex.codecogs.com/gif.latex?\\c_1%2c+c_2%2c+c_3) 为`DataCenter` ![](http://latex.codecogs.com/gif.latex?\\d_1) 中的`CloudNode`。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1gdraykifwqj315w0u0gpc.jpg" alt="Snip20200412_9" style="zoom:33%;" />

如果能需求端`CloudNode` ![](http://latex.codecogs.com/gif.latex?\\C_x) 上的所有`Container`都能被部署到资源端`CloudNode` ![](http://latex.codecogs.com/gif.latex?\\c_y)上，则称作![](http://latex.codecogs.com/gif.latex?\\C_x) 与 ![](http://latex.codecogs.com/gif.latex?\\c_y) 匹配。

进一步，只有当需求端`DataCener` ![](http://latex.codecogs.com/gif.latex?\\D_x) 中所有`CloudNode`都能被部署到资源端`DataCenter` ![](http://latex.codecogs.com/gif.latex?\\d_y)的`CloudNode`上，即`CloudNode`的最大匹配为需求端的`CloudNode`数时，才称作![](http://latex.codecogs.com/gif.latex?\\D_1)与 ![](http://latex.codecogs.com/gif.latex?\\d_1) 匹配。

而只有当`DataCenter`的最大匹配为需求端的`DataCenter`数，才视作`CloudLayer`调度成功。

## 进展

本地读取需求描述 Json，查询数据库，做出匹配，将匹配写入数据库：

![image-20200329164704737](https://tva1.sinaimg.cn/large/00831rSTly1gdaw7p0fe0j30nc0kak55.jpg)

