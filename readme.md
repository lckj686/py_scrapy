### 1、准备库

    Lxml
    zope.interface
    twisted(现在可以用pip3安装了，之前要weel 方式)
    pyOpenSSL
    Scrapy

### 2、创建工程
    scrapy startproject xiaozhu

### 3、目标解释
    scrapy.cfg: 顶级目录配置
    items.py:定义字段
    pipelines.py:数据清理，和入库
    settings.py：配置
    xiaozhuspiders.py：自己的爬虫逻辑