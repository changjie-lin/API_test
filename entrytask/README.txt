# 环境配置

mkdir myproject
cd myproject/
python3 -m venv venv

. venv/bin/activate
pip install Flask
pip install httprunner


export FLASK_APP=api_server.py

flask run

## 生成接口测试报告
hrun testcases --html=report.html

## 压测
locusts -f testcase/test_api.yml


## 分布式压测

locusts -f testcases/cases_1.yml --master

启动多个 worker process
locusts -f testcases/cases_1.yml --worker --master-host=127.0.0.1



问题：
1. Charles, Fiddle 如何 capture 本地 (localhost, 127.0.0.1) 的流量？

2. test suite 和 test cases 的关系。简单的集合包含关系吗？ Test suite 可以做一些 setup teardown 的预处理？