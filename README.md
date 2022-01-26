# Data-visualization-project
基于 Python+Flask+Echarts 的疫情爬虫&amp;数据可视化项目



## 步骤

> - Python 网络爬虫
> - 使用 Python 与 MySQL 数据库交互
> - 使用 Flask 构建 web 项目
> - 基于 Echarts 数据可视化展示
> - 在 Linux 上部署 web 项目及爬虫



## 项目环境

> - Linux 上:
>> - 阿里云 CentOS 7.8 64 位
>> - Python3.6
>> - MySQL 5.7
> > - Flask 1.1.1

## IDE

> Pycharm







## 文件说明

> - app.py 是 flask 的运行程序，整体项目也是运行它
> - spider.py 是爬取各种数据并存入数据库的，定时爬虫就是定时运行它
> - utils.py 是数据库的相关操作的封装，spider.py 中会调用它的函数
> - templates/中
>   > - index.html 和 test.html 是写项目过程中用于测试用的，和项目运行无关，可删
>   > - main.html 是前端页面

## 运行方式：

> ### **本地 win10 上:**

    在mysql数据库中新建cov数据库，并在其中新建3张表details,history,hotsearch——具体见博客
    在utils.py和spider.py中更改get_conn函数中的数据库连接，host,user,password，db
    运行spider.py爬取数据写入到mysql中
    运行app.py

##具体介绍及项目过程
https://blog.csdn.net/hxxjxw/article/details/105336981
# 在其中遇到的问题解决：

## 关于 ChromeDriver 下载及配置环境变量（Linux)

- 1.定位 ChromeDriver 的路径 可以用 ps -qa |grep chromdriver 也可以借助宝塔 linux 管理面版(建议使用后者，毕竟我们是 java 开发，又不是运维，可能不需要掌握这么多命令)

```java
可以从此网站下载相应的驱动:http://chromedriver.storage.googleapis.com/index.html
```

- 2.在命令行中中进入下载文件所在路径，将其移动到/usr/bin

```java
sudo mv chromedriver /usr/bin
```
## ChromeDriver（windos）思路是一致的，在这里就不赘述了！
## 反向代理之 nginx.cof 配置

```java
1.cd /usr/local/nginx/conf
2.vim nginx.cnf
3.以下是关键配置（如果没有配置经验，请不要改动和删改）
	http {

		.......省略

    upstream covid_19{
    server     127.0.0.1:8080 weight=1;
    }
    # 默认主页
     server {

      .......省略

        server_name  127.0.0.1;

		.......省略

        location / {
        proxy_pass http://covid_19;
        }

       .......省略

        }
    }
	为什么这么配，可以自行查阅相关资料。

```
## Flask 端口配置及外网访问
```java
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

	#0.0.0.0就是不限制任何ip地址

	# 通过 xxx.xxx.xxx.xxx或 绑点的域名
```
