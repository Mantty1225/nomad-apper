#!/bin/bash
# Nomad Apper 快速启动脚本

echo "Starting Nomad Apper..."
echo "======================"

# 检查是否安装streamlit
if ! command -v streamlit &> /dev/null; then
    echo "Installing Streamlit..."
    pip install streamlit
fi

# 启动应用
echo "Launching application..."
streamlit run app.py
