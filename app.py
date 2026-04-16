import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import hashlib

# 页面配置
st.set_page_config(
    page_title="Nomad Apper - 数字游民应用推荐",
    page_icon="🌍",
    layout="wide"
)

# 初始化session state
if 'user_info' not in st.session_state:
    st.session_state.user_info = {}
if 'basic_analysis_done' not in st.session_state:
    st.session_state.basic_analysis_done = False
if 'payment_done' not in st.session_state:
    st.session_state.payment_done = False

# 应用数据库
APP_DATABASE = {
    "生产力": [
        {"name": "Notion", "type": "笔记管理", "price": "免费/付费", "rating": 4.8, "url": "https://notion.so", "description": "全能型笔记和项目管理工具"},
        {"name": "Obsidian", "type": "知识库", "price": "免费/付费", "rating": 4.7, "url": "https://obsidian.md", "description": "本地知识图谱笔记工具"},
        {"name": "Todoist", "type": "任务管理", "price": "免费/付费", "rating": 4.6, "url": "https://todoist.com", "description": "简洁高效的任务管理应用"},
    ],
    "设计创意": [
        {"name": "Figma", "type": "UI设计", "price": "免费/付费", "rating": 4.9, "url": "https://figma.com", "description": "协作式UI设计工具"},
        {"name": "Canva", "type": "平面设计", "price": "免费/付费", "rating": 4.7, "url": "https://canva.com", "description": "简单易用的设计平台"},
        {"name": "Adobe Creative Suite", "type": "专业设计", "price": "付费", "rating": 4.8, "url": "https://adobe.com", "description": "专业创意软件套件"},
    ],
    "开发工具": [
        {"name": "VS Code", "type": "代码编辑器", "price": "免费", "rating": 4.9, "url": "https://code.visualstudio.com", "description": "微软开发的轻量级代码编辑器"},
        {"name": "GitHub", "type": "代码托管", "price": "免费/付费", "rating": 4.8, "url": "https://github.com", "description": "代码托管和协作平台"},
        {"name": "Postman", "type": "API测试", "price": "免费/付费", "rating": 4.6, "url": "https://postman.com", "description": "API开发和测试工具"},
    ],
    "财务管理": [
        {"name": "QuickBooks", "type": "会计软件", "price": "付费", "rating": 4.5, "url": "https://quickbooks.intuit.com", "description": "中小企业会计解决方案"},
        {"name": "Expensify", "type": "费用报销", "price": "免费/付费", "rating": 4.4, "url": "https://expensify.com", "description": "智能费用管理工具"},
        {"name": "Wise", "type": "国际转账", "price": "按交易收费", "rating": 4.7, "url": "https://wise.com", "description": "低成本国际汇款服务"},
    ],
    "市场营销": [
        {"name": "Mailchimp", "type": "邮件营销", "price": "免费/付费", "rating": 4.5, "url": "https://mailchimp.com", "description": "电子邮件营销平台"},
        {"name": "Buffer", "type": "社交媒体", "price": "免费/付费", "rating": 4.4, "url": "https://buffer.com", "description": "社交媒体管理工具"},
        {"name": "SEMrush", "type": "SEO工具", "price": "付费", "rating": 4.6, "url": "https://semrush.com", "description": "全方位SEO和营销工具"},
    ]
}

def generate_user_id(email):
    """生成用户ID"""
    return hashlib.md5(email.encode()).hexdigest()[:10]

def basic_recommendation_analysis(user_info):
    """基础推荐分析（免费）"""
    profession = user_info.get('profession', '')
    budget = user_info.get('budget', '中等')

    recommendations = []

    # 根据职业推荐
    if '设计' in profession or '创意' in profession:
        recommendations.append({
            'category': '设计创意',
            'apps': APP_DATABASE['设计创意'][:2],
            'reason': '基于您的设计背景，推荐以下创意工具'
        })
    elif '开发' in profession or '程序员' in profession:
        recommendations.append({
            'category': '开发工具',
            'apps': APP_DATABASE['开发工具'][:2],
            'reason': '作为开发人员，这些工具将提高您的工作效率'
        })
    elif '营销' in profession or '市场' in profession:
        recommendations.append({
            'category': '市场营销',
            'apps': APP_DATABASE['市场营销'][:2],
            'reason': '针对营销工作，推荐以下专业工具'
        })
    else:
        recommendations.append({
            'category': '生产力',
            'apps': APP_DATABASE['生产力'][:2],
            'reason': '通用生产力工具推荐'
        })

    # 根据预算调整
    if budget == '低':
        for rec in recommendations:
            rec['apps'] = [app for app in rec['apps'] if '免费' in app['price']]

    return recommendations

def premium_analysis(user_info):
    """深度付费分析"""
    profession = user_info.get('profession', '')
    budget = user_info.get('budget', '中等')
    experience = user_info.get('experience', '中级')

    analysis = {
        'profile_score': 0,
        'recommendations': [],
        'workflow_suggestions': [],
        'cost_analysis': {},
        'learning_path': []
    }

    # 用户画像评分
    score = 50
    if experience == '高级':
        score += 20
    elif experience == '中级':
        score += 10

    if budget in ['高', '中等']:
        score += 15

    analysis['profile_score'] = min(score, 100)

    # 深度推荐（所有类别）
    for category, apps in APP_DATABASE.items():
        if category == '生产力':
            analysis['recommendations'].append({
                'category': category,
                'apps': apps,
                'priority': '高',
                'reason': '基础生产力工具是数字游民的必备'
            })
        elif '设计' in profession and category == '设计创意':
            analysis['recommendations'].append({
                'category': category,
                'apps': apps,
                'priority': '高',
                'reason': '专业设计工具套件'
            })
        elif '开发' in profession and category == '开发工具':
            analysis['recommendations'].append({
                'category': category,
                'apps': apps,
                'priority': '高',
                'reason': '开发工具链完整推荐'
            })
        elif '营销' in profession and category == '市场营销':
            analysis['recommendations'].append({
                'category': category,
                'apps': apps,
                'priority': '高',
                'reason': '营销工具完整方案'
            })
        else:
            analysis['recommendations'].append({
                'category': category,
                'apps': apps[:2],
                'priority': '中',
                'reason': f'{category}工具推荐'
            })

    # 工作流程建议
    analysis['workflow_suggestions'] = [
        {
            'phase': '调研阶段',
            'tasks': ['分析工作需求', '研究工具选项', '评估成本效益'],
            'duration': '1-2天'
        },
        {
            'phase': '试用阶段',
            'tasks': ['注册免费试用', '测试核心功能', '收集团队反馈'],
            'duration': '3-7天'
        },
        {
            'phase': '实施阶段',
            'tasks': ['购买付费版本', '配置工作环境', '导入历史数据'],
            'duration': '1-2周'
        },
        {
            'phase': '优化阶段',
            'tasks': ['建立工作流程', '培训团队成员', '监控使用效果'],
            'duration': '持续进行'
        }
    ]

    # 成本分析
    monthly_cost = 0
    yearly_cost = 0

    for rec in analysis['recommendations']:
        for app in rec['apps']:
            if '付费' in app['price']:
                if category == '生产力':
                    monthly_cost += 10
                    yearly_cost += 100
                elif category == '设计创意':
                    monthly_cost += 20
                    yearly_cost += 200
                elif category == '开发工具':
                    monthly_cost += 15
                    yearly_cost += 150

    analysis['cost_analysis'] = {
        'monthly': monthly_cost,
        'yearly': yearly_cost,
        'savings_tips': [
            '选择年付计划通常可节省20-30%',
            '利用教育优惠或初创企业折扣',
            '优先选择集成度高的工具套件',
            '定期评估工具使用率，取消不常用订阅'
        ]
    }

    # 学习路径
    analysis['learning_path'] = [
        {
            'phase': '基础设置',
            'focus': '熟悉工具界面和基础功能',
            'duration': '1-2周',
            'milestones': ['完成账号设置', '创建第一个项目', '导入测试数据']
        },
        {
            'phase': '工作流建立',
            'focus': '建立个人工作流程',
            'duration': '2-4周',
            'milestones': ['设计工作流程', '创建模板', '优化操作步骤']
        },
        {
            'phase': '高级功能',
            'focus': '掌握高级特性和集成',
            'duration': '1-2个月',
            'milestones': ['学习高级功能', '探索集成选项', '优化使用技巧']
        },
        {
            'phase': '优化自动化',
            'focus': '实现工作流自动化',
            'duration': '持续进行',
            'milestones': ['识别重复任务', '实施自动化方案', '持续监控改进']
        }
    ]

    return analysis

def display_basic_analysis(user_info):
    """显示基础分析结果"""
    st.success("✅ 基础分析完成！")

    recommendations = basic_recommendation_analysis(user_info)

    st.write("### 🎯 为您推荐的应用")

    for rec in recommendations:
        st.write(f"**{rec['category']}** - {rec['reason']}")

        for app in rec['apps']:
            with st.expander(f"**{app['name']}** ⭐ {app['rating']}"):
                st.write(f"**类型:** {app['type']}")
                st.write(f"**价格:** {app['price']}")
                st.write(f"**描述:** {app['description']}")
                st.link_button("访问官网", app['url'])

        st.divider()

def display_premium_analysis(user_info):
    """显示付费深度分析"""
    st.success("✅ 深度分析已解锁！")

    premium_data = premium_analysis(user_info)

    # 用户画像评分
    st.write("### 👤 用户画像分析")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("匹配度评分", f"{premium_data['profile_score']}/100")
    with col2:
        st.metric("推荐应用数", len(premium_data['recommendations']) * 3)
    with col3:
        st.metric("预计节省", "20-30%")

    # 完整应用推荐
    st.write("### 🎯 完整应用推荐")

    for rec in premium_data['recommendations']:
        priority_color = "🟢" if rec['priority'] == '高' else "🟡"
        st.write(f"#### {priority_color} {rec['category']}（优先级：{rec['priority']}）")
        st.write(f"*{rec['reason']}*")

        cols = st.columns(3)
        for idx, app in enumerate(rec['apps']):
            with cols[idx % 3]:
                st.write(f"**{app['name']}**")
                st.write(f"⭐ {app['rating']} | {app['price']}")
                st.link_button("访问", app['url'])

        st.divider()

    # 工作流程建议
    st.write("### 🔄 工作流程建议")
    for workflow in premium_data['workflow_suggestions']:
        with st.expander(f"**{workflow['phase']}** - {workflow['duration']}"):
            for task in workflow['tasks']:
                st.write(f"- {task}")

    # 成本分析
    st.write("### 💰 成本分析")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**月度成本:** ¥{premium_data['cost_analysis']['monthly']}")
        st.write(f"**年度成本:** ¥{premium_data['cost_analysis']['yearly']}")
    with col2:
        st.write("**省钱小贴士:**")
        for tip in premium_data['cost_analysis']['savings_tips']:
            st.write(f"- {tip}")

    # 学习路径
    st.write("### 📚 学习路径规划")
    for phase in premium_data['learning_path']:
        with st.expander(f"**{phase['phase']}** - {phase['focus']}（{phase['duration']}）"):
            if phase['phase'] == "基础设置":
                st.write("""- 观看官方教程
- 完成基础设置
- 导入示例数据""")
            elif phase['phase'] == "工作流建立":
                st.write("""- 设计个人工作流
- 建立项目模板
- 测试和调优""")
            elif phase['phase'] == "高级功能":
                st.write("""- 学习高级特性
- 探索集成选项
- 优化使用技巧""")
            elif phase['phase'] == "优化自动化":
                st.write("""- 识别重复任务
- 实施自动化方案
- 持续监控改进""")

    # 导出报告
    st.divider()
    st.write("### 📄 导出分析报告")
    if st.button("生成PDF报告"):
        st.success("报告生成中...（功能开发中）")

    if st.button("重新开始"):
        st.session_state.basic_analysis_done = False
        st.session_state.payment_done = False
        st.session_state.user_info = {}
        st.rerun()

def main():
    """主函数"""
    st.title("🌍 Nomad Apper")
    st.subtitle("数字游民应用推荐系统")

    # 侧边栏
    with st.sidebar:
        st.write("### 关于")
        st.write("为数字游民量身定制的应用推荐系统")
        st.divider()
        st.write("### 定价")
        st.write("**基础分析** - 免费")
        st.write("- 基础应用推荐")
        st.write("- 简单使用建议")
        st.divider()
        st.write("**深度分析** - ¥99")
        st.write("- 完整应用推荐")
        st.write("- 工作流程建议")
        st.write("- 成本分析")
        st.write("- 学习路径规划")

    # 用户信息收集
    if not st.session_state.basic_analysis_done:
        st.write("### 📝 请告诉我们一些关于您的信息")

        with st.form("user_info_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("姓名", placeholder="请输入您的姓名")
                email = st.text_input("邮箱", placeholder="your@email.com")
                profession = st.text_input("职业", placeholder="如：设计师、开发者、营销人员")
            with col2:
                budget = st.selectbox("预算范围", ["低", "中等", "高"])
                experience = st.selectbox("数字游民经验", ["初级", "中级", "高级"])
                goals = st.text_area("主要目标", placeholder="请简述您的主要工作目标")

            submitted = st.form_submit_button("开始基础分析", type="primary")

            if submitted:
                if not name or not email:
                    st.error("请填写姓名和邮箱")
                else:
                    st.session_state.user_info = {
                        'name': name,
                        'email': email,
                        'profession': profession,
                        'budget': budget,
                        'experience': experience,
                        'goals': goals,
                        'user_id': generate_user_id(email)
                    }
                    st.session_state.basic_analysis_done = True
                    st.rerun()

    # 显示基础分析结果
    elif st.session_state.basic_analysis_done and not st.session_state.payment_done:
        display_basic_analysis(st.session_state.user_info)

        st.divider()
        st.write("### 🔓 解锁深度分析")
        st.write("获取完整应用推荐、工作流程建议、成本分析和学习路径规划")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("支付 ¥99 解锁深度分析", type="primary"):
                st.session_state.payment_done = True
                st.rerun()

    # 显示付费深度分析
    elif st.session_state.payment_done:
        display_premium_analysis(st.session_state.user_info)

if __name__ == "__main__":
    main()
