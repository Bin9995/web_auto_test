import os
# 配置cmd下执行命令
run_cmd = "allure generate ./report -o ./new_report --clean"
# 通过OS.system(run_cmd)方法运行终端命令
os.system(run_cmd)
# allure generate： 生成allure测试报告的命令
# ./report： 运行生成的临时报告文件路径
# -o ./new_report： 输出HTML的报告到report路径下
# --clean： 生成报告前清除之前的报告文件
