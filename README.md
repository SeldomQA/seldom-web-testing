# seldom-web-testing

> seldom Web 自动化测试项目.

## 安装

```shell
> git clone https://github.com/SeldomQA/seldom-web-testing
> cd seldom-web-testing
> pip install -r requirements.txt
```

## 运行

目录结构：

```shell
mypro/
├── pages/
│   ├── xxx_page.py
├── reports/
├── test_data/
│   ├── xx_data.json
├── test_dir/
│   ├── test_xxx_xxx.py
└── run.py
```

* `pages/` page层封装目录。
* `reports/` 测试报告目录。
* `test_data/` 测试数据目录。
* `test_dir/` 测试用例目录。
* `run.py` 运行测试用例主文件。

运行用例：

```shell
> python run.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.10.2
-----------------------------------------
                             @itest.info

[WDM] -

[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 96.0.4664
[WDM] - Get LATEST driver version for 96.0.4664
[WDM] - Driver [C:\Users\fnngj\.wdm\drivers\chromedriver\win32\96.0.4664.35\chromedriver.exe] found in cache

DevTools listening on ws://127.0.0.1:61378/devtools/browser/46d8e0b7-1a8f-4444-9089-060008cee591
...
Generating HTML reports...
.202022-06-26 11:51:35 log.py | SUCCESS | generated html file: file:///D:\github\seldom-web-testing\reports\2022_06_26_11_49_34_result.html
2022-06-26 11:51:35 log.py | SUCCESS | generated log file: file:///D:\github\seldom-web-testing\reports\seldom_log.log
```

## 测试报告

![](report.png)
