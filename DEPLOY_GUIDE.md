# Nomad Apper - 部署指南

## 项目介绍

Nomad Apper是一个为数字游民提供专业应用推荐的Streamlit应用。

## 完成的功能

### 免费基础分析
- 用户信息收集（姓名、邮箱、职业、预算等）
- 基础应用推荐（4-6个）
- 应用评分和描述

### 付费99元深度分析
- 用户画像评分（0-100分）
- 完整应用推荐（5个类别，20+个应用）
- 工作流程建议（4个阶段）
- 成本分析（月费/年费 + 省钱小贴士）
- 学习路径规划（4个阶段）

## 部署步骤

### 方式1: Streamlit Cloud（推荐）

1. 访问 https://github.com/new
2. 创建仓库 `nomad-apper`
3. 上传所有文件（或解压部署包）
4. 访问 https://share.streamlit.io
5. 登录并选择 `nomad-apper` 仓库
6. 点击 Deploy

### 方式2: Railway.app（更快）

1. 访问 https://railway.app
2. 使用GitHub账号登录
3. 点击 New Project
4. 选择 Deploy from GitHub repo
5. 选择 nomad-apper
6. 等待1-2分钟部署完成

### 方式3: 本地运行

1. 安装Python 3.8+
2. 安装依赖: `pip install streamlit pandas numpy`
3. 运行: `streamlit run app.py`
4. 访问: http://localhost:8501

## 项目文件说明

- `app.py` - 主应用程序（376行）
- `requirements.txt` - Python依赖包
- `README.md` - 项目文档
- `deploy.sh` - 部署脚本
- `start.sh` - 本地启动脚本

## 测试清单

部署后请检查:

- [ ] 用户表单可以正常提交
- [ ] 基础应用推荐显示正确
- [ ] 点击付趙解锁深度分析
- [ ] 用户画像评分显示
- [ ] 完整应用推荐显示
- [ ] 工作流程建议显示
- [ ] 成本分析显示
- [ ] 学习路径显示

## 支持

如有问题，请联系支持。
