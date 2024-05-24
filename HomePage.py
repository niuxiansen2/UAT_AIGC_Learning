import streamlit_antd_components as sac
import streamlit as st
from Bisheng_primary import *
from BIsheng_base import *
from openSource import *
from webLearning import *
from AIGC_Set import *
from TypicalCase import *
from api_file import *
from meetingLearning import *

st.set_page_config(page_title="UAT AIGC社区", page_icon="🌈", layout="wide")

with st.sidebar:
    st.image("imgSource/logo.png", use_column_width=True)
    sac.menu([
        sac.MenuItem('主页', icon='house-fill', ),
        # sac.MenuItem('业务运营智能审批要件', icon='box-fill'),
        sac.MenuItem("bisheng平台", icon='robot', children=[
            sac.MenuItem('基本介绍'),
            sac.MenuItem('快速入门'),
            sac.MenuItem('典型案例', children=[
                sac.MenuItem('角色对话'),
                sac.MenuItem('文件对话'),
                sac.MenuItem('文本分析Agent构建'),
            ]),
            sac.MenuItem('接口文档'),
        ]),
        sac.MenuItem('UI设计-Streamlit', icon='robot'),
        sac.MenuItem('AIGC应用合集', icon='git', ),
        sac.MenuItem("峰会分享", icon='google', children=[
            sac.MenuItem('人工智能'),
            sac.MenuItem('测试领域'),
            sac.MenuItem('其他')
        ]),
        sac.MenuItem('优秀开源案例', icon='gitlab'),
    ]
        , key="menu", size=18, open_index=[1])

if st.session_state["menu"] == "主页":
    st.header("📂AIGC信息汇总", divider="rainbow")
    with st.container(height=900):
        st.markdown("""
        ### 本周（0518-0524）行业发展近况： 

#### （1）微软昨夜AI全家桶狂飙：GPT-4o上云，纳德拉现场表白OpenAI，Altman剧透新模型（05月22日） 

--> 目前，微软已经建造了三个平台：首先是Microsoft Copilot，成为用户的日常助理，帮助用户采取行动；第二个是Copilot堆栈，帮助开发者更快构建AI应用、解决方案；第三个是Copilot+PC，第一台AI PC。 

#### （2）国内各大模型厂商相继降价及免费 

--> 百度宣布文心大模型 ENIRE Speed、ENIRE Lite 全面免费，即刻生效 

--> 通义千问宣布“GPT-4 级”主力模型 Qwen-Long 降价 97%，一元 200 万 tokens

 --> 讯飞星火 Lite API 能力免费开放：在线联网搜索、低算力推理场景 

--> 腾讯混元大模型全面降价，混元-lite 即日起免费







### 本周（0511-0517）行业发展近况（重点关注）： 

#### **（1）谷歌反击OpenAI！连夜发布十几款新品，喊了121次AI，最新长文本模型问鼎全球最强（05月15日）**

 --> 发布支持200万token长文本的Gemini 1.5 Pro和Gemini 1.5 Flash，谷歌版Sora技术Veo（可生成1分钟1080P的视频模型），最强开源模型Gemma2，支持生成式搜索的AI Overviews，第六代TPU等。 

#### **（2）OpenAI推出新的AI模型GPT-4o和ChatGPT桌面版（05月14日）** 

--> GPT-4o，大幅度降低延迟，感知用户情绪，具备不同情绪的声音，理解音调、背景噪声等不同情绪表达因素。实时视觉功能，更即时的语音交互，在多语言、音频和视觉功能方面表现分数创下新高。 

#### **（3）字节跳动发布豆包大模型，主力模型比行业价格低99.3%（05月15日）** 

--> 从0.12元/千Tokens降低至0.0008元/千Tokens 

#### **（4）零一万物千亿参数模型Yi-Large发布，基准测试登顶国产大模型，新MoE模型对打GPT-5（05月13日）**

 --> Yi-Large在斯坦福英语测评中位居第二，仅次于GPT-4-Turbo，中文SuperCLUE结果中，位于国产大模型榜首 

#### **（5）腾讯宣布混元文生图大模型对外开源（05月14日）**

 --> 15亿参数量，DiT架构，业内首个中文原生DiT架构文生图开源模型
        """)
    with st.container(height=900):
        col = st.columns(3)
        with col[1]:
            st.subheader("大模型基础知识")
        st.markdown(
            """
            **基础**：
    - 【ChatGPT提示工程师&AI大神吴恩达教你写提示词｜prompt engineering【完整中字九集全】-哔哩哔哩】 https://b23.tv/yBqBnA1
    -  吴恩达最新《LLM应用程序开发的LangChain》1_LangChain_Intro_v02.zh_gpt_subtitled_哔哩哔哩_bilibili
    - 【合集·LangChain in Action-哔哩哔哩】 https://space.bilibili.com/28357052/channel/collectiondetail?sid=1611560
    - 《解读 ChatGPT 背后的技术重点：RLHF、IFT、CoT、红蓝对抗》https://blog.csdn.net/HuggingFace/article/details/128843029


    **推荐文章：**
    - 《LangChain：Model as a Service粘合剂，被ChatGPT插件干掉了吗？》https://mp.weixin.qq.com/s/3coFhAdzr40tozn8f9Dc-w
    - 《AI Agent的千亿美金问题：如何重构10亿知识工作职业，掀起软件生产革命？》https://mp.weixin.qq.com/s/JYu_oXWbWbasT1fcBRo-cA
    - 《GitHub首席工程师：别再逼着用户跟AI聊天了！》https://mp.weixin.qq.com/s/wm__hW1rQSbZEBQchx-q4g
    - 《万字长文带你深入了解向量数据库》https://mp.weixin.qq.com/s/6IPMIYch3rA7DEJKm9xUmg
    - 投身LLM的道路https://mp.weixin.qq.com/s/vfsB5t3r5dBACKQx6FshVw
      - 向下走：去搞基模型预训练、部署、或者去做大模型基建；
      - 向上走：去做对齐工作，做 Agents，做应用；
      - 艰难之路：去搞大模型理论研究，可解释性，短期基本看不到回报，但这块成果对前两个都会有帮助。
    - 【注意，“人工智障”系列是大模型时代之前的文章，但问题值得持续思考】
      - 《为什么现在的人工智能助理都像人工智障？》https://mp.weixin.qq.com/s/_jyBZtp_43vTgtjcHsSlHQ
      - 《人工智障 2 : 你看到的AI与智能无关》https://mp.weixin.qq.com/s/KF4DgF9FPYW2D_M-uacNaw


    **进阶：**
    - 《Large Language Model in Action》https://wangwei1237.github.io/LLM_in_Action/
    - 【langchain官方文档】https://python.langchain.com/docs/get_started/introduction
    - 【OpenAI官方文档】https://cookbook.openai.com/
    - 《Building LLM applications for production》https://huyenchip.com/2023/04/11/llm-engineering.html
    - 《LLM Powered Autonomous Agents》https://lilianweng.github.io/posts/2023-06-23-agent/
            """
        )

if st.session_state["menu"] == "基本介绍":  # 使用markdown
    baseKnowledge2()
    # base2()

if st.session_state["menu"] == "快速入门":
    primaryLearning()

if st.session_state["menu"] == "优秀开源案例":
    openSourceUrl()

if st.session_state["menu"] == "AIGC应用合集":
    AIGC_SET()

if st.session_state["menu"] == "UI设计-Streamlit":
    main()

if st.session_state["menu"] == "角色对话":
    case_base_talk()
if st.session_state["menu"] == "文件对话":
    case_file_talk()
if st.session_state["menu"] == "文本分析Agent构建":
    case_analyze_agent()
if st.session_state["menu"] == "接口文档":
    apiShow()
if st.session_state["menu"] == "人工智能":
    meetingFile_AI()

if st.session_state["menu"] == "测试领域":
    meetingFile_softTest()
