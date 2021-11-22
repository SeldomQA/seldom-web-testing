# seldom-web-testing

## 安装

```shell
> pip install seldom==2.3.3
> pip install poium==1.0.4
```

## 运行

目录结构：

```shell
mypro/
├── pages/
│   ├── xxx_page.py
├── test_data/
│   ├── data.json
├── reports/
└── run.py
```

* `pages/` page层封装目录。
* `test_dir/` 测试用例目录。
* `reports/` 测试报告目录。
* `run.py` 运行测试用例主文件。

运行用例：

```shell
> python run.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.3.3
-----------------------------------------
                             @itest.info

[WDM] -

[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 96.0.4664
[WDM] - Get LATEST driver version for 96.0.4664
[WDM] - Driver [C:\Users\fnngj\.wdm\drivers\chromedriver\win32\96.0.4664.35\chromedriver.exe] found in cache

DevTools listening on ws://127.0.0.1:61378/devtools/browser/46d8e0b7-1a8f-4444-9089-060008cee591
2021-11-22 23:35:50 [INFO] 📖 https://sahitest.com/demo/iframesTest.htm
2021-11-22 23:35:51,197  [INFO] ✅ Find element: id=checkRecord
2021-11-22 23:35:52,146  [INFO] clear element: input Text
2021-11-22 23:35:52,181  [INFO] ✅ Find element: id=checkRecord
2021-11-22 23:35:53,122  [INFO] 🖋 input element: input Text
2021-11-22 23:35:53,199  [INFO] ✅ Find element: css selector=input[value='Click me']
2021-11-22 23:35:54,143  [INFO] 🖱 click element: input button
2021-11-22 23:35:54 [INFO] 📖 https://sahitest.com/demo/
2021-11-22 23:35:54,398  [INFO] ✅ Find element: link text=Link Test
2021-11-22 23:35:55,364  [INFO] 🖱 click element: Link Test
2021-11-22 23:35:56 [PRINT] generated html file: file:///D:\github\seldom-web-testing\reports\2021_11_22_23_35_48_result.html
2021-11-22 23:35:56 [PRINT] generated log file: file:///D:\github\seldom-web-testing\reports\2021_11_22_23_35_48_log.log
.1.2
```

## 测试报告

![](report.png)
