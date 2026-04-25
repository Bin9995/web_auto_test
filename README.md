# Web 自动化测试项目 - 金融平台

## 项目介绍
本项目使用 **Python + Pytest + Selenium + Page Object Model (POM)** 框架，对**传智播客金融理财平台**进行 Web 自动化测试。  
覆盖**前台会员交易系统**（注册、登录、开通账户、借款申请、额度申请等）和**后台管理系统**（管理员登录、额度审核等核心业务流程）。

**目标**：提升测试效率，减少手动重复操作，实现核心业务的回归测试自动化。

## 技术栈
- **语言**：Python 3
- **测试框架**：Pytest
- **自动化工具**：Selenium WebDriver
- **设计模式**：Page Object Model (POM)
- **报告工具**：Allure
- **数据生成**：Faker
- **其他**：Git

## 项目结构

```text
web_auto_test/
├── base/                  # 基础工具类（浏览器驱动封装、公共方法等）
├── data/                  # 测试数据文件（Excel、JSON 等）
├── img/                   # 测试过程中自动截图存放目录
├── page/                  # 页面对象层（Page Object Model）
│   ├── page_back_login.py # 后台登录页面
│   ├── page_borrow.py
│   ├── page_credit_application.py
│   ├── page_credit_review.py
│   ├── page_login.py
│   ├── page_open_account.py
│   └── page_register.py
├── script/                # 测试用例脚本层
├── conftest.py            # pytest 全局 fixtures（浏览器、登录前置等）
├── config.py              # 项目配置（URL、测试数据生成等）
├── tools.py               # 工具类（DriverTools、截图等）
├── pytest.ini             # pytest 配置文件
├── cmd_allure.py          # Allure 报告生成脚本
├── .gitignore
└── requirements.txt       # 项目依赖（推荐添加）

说明：

采用经典的 分层设计：Page Object Model（页面对象） + 测试用例分离，提高代码可维护性和可读性。
每个页面对应一个 Page 类，封装元素定位和业务操作方法，符合企业自动化测试开发规范。
