
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
                'reason': '营销自动化工具组合'
            })
    
    # 工作流程建议
    analysis['workflow_suggestions'] = [
        {"step": 1, "action": "建立核心生产力系统", "tools": ["Notion", "Todoist"], "time": "1-2周"},
        {"step": 2, "action": "设置专业工具链", "tools": ["根据职业选择"], "time": "2-4周"},
        {"step": 3, "action": "整合财务管理", "tools": ["QuickBooks", "Wise"], "time": "1周"},
        {"step": 4, "action": "优化和自动化", "tools": ["Zapier", "API集成"], "time": "持续"}
    ]
    
    # 成本分析
    monthly_cost = 0
    yearly_cost = 0
    for rec in analysis['recommendations']:
        for app in rec['apps']:
            if app['price'] == '付费':
                monthly_cost += 20  # 估算平均月费
                yearly_cost += 200  # 估算平均年费
    
    analysis['cost_analysis'] = {
        'monthly': monthly_cost,
        'yearly': yearly_cost,
        'savings_tips': [
            '选择年付计划通常可节省20-30%',
            '利用教育优惠或早期用户折扣',
            '优先使用免费版本，按需升级'
        ]
    }
    
    # 学习路径
    analysis['learning_path'] = [
        {"phase": "基础设置", "duration": "1周", "focus": "熟悉核心工具"},
        {"phase": "工作流建立", "duration": "2-3周", "focus": "构建个人工作系统"},
        {"phase": "高级功能", "duration": "1个月", "focus": "掌握高级特性"},
        {"phase": "优化自动化", "duration": "持续", "focus": "提升效率"}
    ]
    
    return analysis

# 主界面
def main():
    st.title("🌍 Nomad Apper")
    st.subheader("数字游民应用推荐系统")
    
    # 用户输入表单
    if not st.session_state.basic_analysis_done:
        with st.form("user_info_form"):
            st.write("### 请填写您的信息")
            
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("姓名")
                email = st.text_input("邮箱")
                profession = st.text_input("职业")
            with col2:
                budget = st.selectbox("预算范围", ["低", "中等", "高"])
                experience = st.selectbox("经验水平", ["初级", "中级", "高级"])
                goals = st.text_area("主要目标（用逗号分隔）")
            
            submitted = st.form_submit_button("获取基础分析", type="primary")
            
            if submitted:
                if not all([name, email, profession]):
                    st.error("请填写所有必填字段")
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
        st.success("✅ 基础分析完成！")
        
        user_info = st.session_state.user_info
        basic_recs = basic_recommendation_analysis(user_info)
        
        st.write(f"### 您好，{user_info['name']}！")
        st.write(f"用户ID: `{user_info['user_id']}`")
        
        # 显示基础推荐
        for rec in basic_recs:
            with st.expander(f"📊 {rec['category']} - {rec['reason']}", expanded=True):
                for app in rec['apps']:
                    col1, col2, col3 = st.columns([3, 2, 1])
                    with col1:
                        st.markdown(f"**[{app['name']}]({app['url']})** - {app['description']}")
                    with col2:
                        st.caption(f"类型: {app['type']} | 价格: {app['price']}")
                    with col3:
                        st.caption(f"⭐ {app['rating']}")
        
        # 付费升级提示
        st.divider()
        st.write("### 🔒 深度付费分析")
        st.info("基础分析已完成！解锁深度分析获取更多价值：")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("应用推荐", "5个类别", "+15个深度推荐")
        with col2:
            st.metric("工作流方案", "基础推荐", "+完整实施路径")
        with col3:
            st.metric("成本分析", "无", "详细预算规划")
        
        # 模拟支付按钮
        if st.button("💳 解锁深度分析（¥99）", type="primary"):
            st.session_state.payment_done = True
            st.rerun()
    
    # 显示付费分析结果
    elif st.session_state.payment_done:
        st.success("🎉 付费分析已解锁！")
        
        user_info = st.session_state.user_info
        premium_data = premium_analysis(user_info)
        
        # 用户画像评分
        st.write("### 📈 用户画像分析")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.metric("匹配度评分", f"{premium_data['profile_score']}/100")
        with col2:
            if premium_data['profile_score'] >= 80:
                st.success("🌟 您具备优秀的数字游民潜质！")
            elif premium_data['profile_score'] >= 60:
                st.info("💪 良好的基础，继续优化！")
            else:
                st.warning("📚 建议从基础工具开始建立工作流")
        
        # 深度推荐
        st.write("### 🎯 深度应用推荐")
        for rec in premium_data['recommendations']:
            with st.expander(f"**{rec['category']}** - {rec['reason']} (优先级: {rec['priority']})"):
                for app in rec['apps']:
                    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
                    with col1:
                        st.markdown(f"**[{app['name']}]({app['url']})**")
                        st.caption(app['description'])
                    with col2:
                        st.caption(f"类型: {app['type']}")
                    with col3:
                        st.caption(f"价格: {app['price']}")
                    with col4:
                        st.caption(f"⭐ {app['rating']}")
        
        # 工作流程建议
        st.write("### 🔄 工作流程实施方案")
        for step in premium_data['workflow_suggestions']:
            with st.expander(f"步骤 {step['step']}: {step['action']}（预计时间: {step['time']}）"):
                st.write("**推荐工具:**", ", ".join(step['tools']))
                st.write("**实施要点:**")
                if step['step'] == 1:
                    st.write("""- 建立项目管理系统
- 设置任务分类
- 创建模板和工作流""")
                elif step['step'] == 2:
                    st.write("""- 选择专业工具
- 学习核心功能
- 整合到日常工作""")
                elif step['step'] == 3:
                    st.write("""- 设置账单系统
- 建立客户管理系统
- 优化收款流程""")
                elif step['step'] == 4:
                    st.write("""- 探索自动化工具
- 建立API集成
- 持续优化效率""")
        
        # 成本分析
        st.write("### 💰 成本效益分析")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("预估月费用", f"¥{premium_data['cost_analysis']['monthly']}")
        with col2:
            st.metric("预估年费用", f"¥{premium_data['cost_analysis']['yearly']}")
        
        with st.expander("💡 省钱小贴士"):
            for tip in premium_data['cost_analysis']['savings_tips']:
                st.write(f"• {tip}")
        
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
- 测试和调优")
                elif phase['phase'] == "高级功能":
                    st.write("- 学习高级特性
- 探索集成选项
- 优化使用技巧")
                elif phase['phase'] == "优化自动化":
                    st.write("- 识别重复任务
- 实施自动化方案
- 持续监控改进")
        
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

if __name__ == "__main__":
    main()
