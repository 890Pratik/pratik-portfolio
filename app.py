import streamlit as st

# Page Config
st.set_page_config(page_title="Pratik Sunar | Data Analyst", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS (your original + enhanced Contact Me button + smooth scroll)
st.markdown("""
<style>
    .stApp {background-color: #f9f5f0;}
    .main-container {max-width: 1200px; margin: auto; padding: 20px;}
    .section-card {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 0 20px rgba(0, 191, 191, 0.5);
    }
    .social-icons {display: flex; justify-content: flex-start; gap: 30px; margin: 20px 0;}
    .social-icon {width: 40px; height: 40px; border-radius: 50%; background: #e0f7fa; padding: 10px; box-shadow: 0 0 10px rgba(0,191,191,0.3);}
    .contact-btn-container {
        text-align: center;
        margin: 40px 0;
    }
    .contact-btn {
        background: linear-gradient(135deg, #0066cc, #7b2cbf, #00a0a0);
        color: white !important;
        padding: 18px 60px;
        border-radius: 50px;
        font-size: 1.35rem;
        font-weight: bold;
        text-align: center;
        border: none;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0, 102, 204, 0.5);
        transition: all 0.4s ease;
        display: inline-block;
        min-width: 280px;
        letter-spacing: 1px;
        text-transform: uppercase;
        position: relative;
        overflow: hidden;
    }
    .contact-btn:hover {
        transform: translateY(-6px);
        box-shadow: 0 15px 40px rgba(0, 102, 204, 0.7);
        background: linear-gradient(135deg, #0077e6, #8a4fff, #00b3b3);
    }
    .contact-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: 0.6s;
    }
    .contact-btn:hover::before {
        left: 100%;
    }

    h1 {color: #333; margin-bottom: 10px;}
    h2 {text-align: center; color: #00a0a0; margin-bottom: 20px;}
    ul {text-align: left; max-width: 700px; margin: auto; list-style-type: disc;}
    li {margin-bottom: 10px;}
    .project-link {color: #00a0a0; text-decoration: none;}
    .intro-text {
        font-size: 1.1rem; 
        line-height: 1.6; 
        color: #555;
        word-wrap: break-word;
        overflow-wrap: break-word;
        hyphens: auto;
    }

    /* Smooth scroll behavior */
    html {
        scroll-behavior: smooth;
    }

    /* Skills Grid */
    .skills-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 20px; margin-top: 30px;}
    .skill-item {text-align: center;}
    .skill-logo {width: 60px; height: 60px; margin-bottom: 10px;}
    .skill-name {font-weight: bold; color: #333;}

    /* Project Card Styles - unchanged */
    .project-card {
        background: white;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        transition: transform 0.3s ease;
        height: 420px;
        display: flex;
        flex-direction: column;
    }
    .project-card:hover {
        transform: translateY(-8px);
    }
    .project-header {
        position: relative;
        height: 180px;
    }
    .project-header img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .project-title {
        position: absolute;
        top: 10px;
        left: 10px;
        background: rgba(0,0,0,0.7);
        color: white;
        padding: 8px 15px;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: bold;
    }
    .project-body {
        padding: 15px;
        text-align: center;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .project-subtitle {
        font-weight: bold;
        font-size: 0.95rem;
        margin-bottom: 8px;
    }
    .project-desc {
        font-size: 0.8rem;
        color: #555;
        line-height: 1.4;
        margin-bottom: 10px;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
        word-wrap: break-word;
        overflow-wrap: break-word;
        hyphens: auto;
    }
    .see-work-btn {
        background: #00a0a0;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 8px 25px;
        font-size: 0.9rem;
        cursor: pointer;
        margin: 10px auto 0;
    }
    .tool-icon {
        width: 40px;
        height: 40px;
        margin: 10px auto 0;
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .main-container {padding: 10px;}
        .section-card {padding: 20px;}
        .intro-text {font-size: 1rem;}
        .skills-grid {grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));}
        .project-card {height: auto; min-height: 420px;}
        .project-header {height: 150px;}
        .project-desc {-webkit-line-clamp: 3;}
        .contact-btn {width: 100%; max-width: 320px; padding: 14px 30px; font-size: 1.1rem;}
        [data-testid="stHorizontalBlock"] > div {flex-direction: column !important; gap: 20px !important;}
    }
</style>
""", unsafe_allow_html=True)

# Main Content
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Header with Professional Photo
col_photo, col_text = st.columns([1, 3], gap="large")

with col_photo:
    st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <img src="https://raw.githubusercontent.com/890Pratik/pratik-portfolio/main/profile.png" 
             alt="Pratik Sunar" 
             style="width: 220px; 
                    height: 220px; 
                    border-radius: 50%; 
                    object-fit: cover; 
                    border: 6px solid #e0f7fa; 
                    box-shadow: 0 10px 30px rgba(0,191,191,0.4);">
    </div>
    """, unsafe_allow_html=True)

with col_text:
    st.markdown("<h1 style='margin-top: 40px; color: #333;'>Pratik Sunar</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p class='intro-text'>
    Data Analyst with hands-on experience in Data science, Machine learning, and Business intelligence in Insurance and Pharmaceutical sectors.
    </p>
    <p class='intro-text'>
    Skilled in SQL, Python, Power BI, Excel, Streamlit and AWS. During recent Internship at VHI Group DAC gained experience in customer call analytics using AWS cloud services, enhancing logic for Outlier Claims model (OCM), implementing Oracle PL/SQL and VBA solutions that automated client reporting and enhanced operational efficiency.
    </p>
    <p class='intro-text'>
    Proven ability to query multi-million-row datasets and build interactive dashboards. An academic foundation in Statistics and Data Analytics, combined with practical exposure to real-world data challenges. Currently based in Ireland with Stamp 1G eligible to work in Ireland.
    </p>
    """, unsafe_allow_html=True)

# Social Icons + Enhanced Contact Me button
st.markdown("""
<div class='social-icons' style='margin-top: 30px;'>
    <a href="https://www.linkedin.com/in/pratik-sunar-438323244/"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="social-icon" alt="LinkedIn"></a>
    <a href="https://github.com/890Pratik"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" class="social-icon" alt="GitHub"></a>
    <a href="mailto:pratiksunar0899.ie@gmail.com"><img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" class="social-icon" alt="Mail"></a>
    <a href="#projects"><img src="https://cdn-icons-png.flaticon.com/512/3095/3095398.png" class="social-icon" alt="Projects"></a>
</div>
""", unsafe_allow_html=True)

# Enhanced centered Contact Me button with smooth scroll
st.markdown('<div class="contact-btn-container">', unsafe_allow_html=True)
if st.button("Contact Me", key="contact_btn_enhanced", help="Scroll to contact section"):
    st.markdown(
        """
        <script>
            const contactSection = document.getElementById('contact');
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: 'smooth' });
            }
        </script>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# Experience Section (unchanged)
st.markdown("""
<div class='section-card'>
    <h2>Experience</h2>
    <h3>VHI Group DAC – Data Analyst Intern | Dublin, Ireland | May 2025 – Aug 2025</h3>
    <ul>
        <li>Analyzed 30k healthcare and drug claims records to identify drug dosage anomalies across Hospitals in Ireland, enhancing the Outlier Claims Model</li>
        <li>Applied Anthropic’s Haiku LLM on 2,000+ customer call transcripts using AWS workflow (S3, Lambda, Transcribe, Bedrock), uncovering key insights for Cancellations and travel related calls</li>
        <li>Automated reporting using VBA and Oracle PL/SQL, improving workflow efficiency and maintaining strong data governance</li>
    </ul>
    <h3>Alembic Pharmaceutical – Market Data Analyst | Shillong, India | Dec 2022 – Jul 2023</h3>
    <ul>
        <li>Analyzed regional prescription and sales data for Azithral and Leveta-M to identify usage patterns, target segments, and high-potential prescribers</li>
        <li>Applied statistical analysis and machine learning techniques (clustering, regression) to evaluate prescription behavior and guide promotional strategies</li>
        <li>Collaborated with sales and marketing teams to align data-driven insights with business strategy, contributing to a 110% quarterly growth</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Projects Section - exactly your original layout (no changes here)
st.markdown("<div class='section-card' id='projects'><h2>Projects</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class='project-card'>
        <div class='project-header'>
            <img src="https://marketerkapoor.com/wp-content/uploads/2023/06/Business-Insights-360-Power-BI-Project-Executive-Page.png">
            <div class='project-title'>BUSINESS INSIGHT 360</div>
        </div>
        <div class='project-body'>
            <div class='project-subtitle'>Dashboard for Finance, Sales, Marketing & Supply Chain</div>
            <div class='project-desc'>AtliQ Hardware is a consumer electronics company expanding rapidly but is not able to compete with other...</div>
            <a href="https://app.powerbi.com/view?r=eyJrIjoiOWI0MjkyYzktNjNhYy00YWFlLWI1YTktYTc2NDBkNDU3ZWU5IiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9" target="_blank">
                <button class='see-work-btn'>See My Work</button>
            </a>
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" class="tool-icon" alt="Power BI">
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='project-card'>
        <div class='project-header'>
            <img src="https://i0.wp.com/amanxai.com/wp-content/uploads/2021/10/Health-Insurance-Premium-Prediction-with-Machine-Learning.png?fit=1920%2C1080&ssl=1">
            <div class='project-title'>HEALTH INSURANCE PREDICTOR</div>
        </div>
        <div class='project-body'>
            <div class='project-subtitle'>Machine Learning Web App</div>
            <div class='project-desc'>Predictive model deployed as interactive Streamlit app for real-time premium estimation.</div>
            <a href="https://ml-project-health-insurance-premium-predic.streamlit.app/" target="_blank">
                <button class='see-work-btn'>See My Work</button>
            </a>
            <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" class="tool-icon" alt="Streamlit">
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='project-card'>
        <div class='project-header'>
            <img src="https://raw.githubusercontent.com/890Pratik/AtliQ-Hardware-Business-Analytic-/main/Sqloutoutpic.png" alt="AtliQ Hardware SQL Analytics Output">
            <div class='project-title'>EXECUTIVE MANAGEMENT</div>
        </div>
        <div class='project-body'>
            <div class='project-subtitle'>AtliQ Hardware Business Analytics</div>
            <div class='project-desc'>Queried multi-million-row datasets using SQL to deliver ad-hoc insights on sales, markets, top customers, net sales, and region-wise market share for AtliQ Hardware.</div>
            <a href="https://github.com/890Pratik/AtliQ-Hardware-Business-Analytic-" target="_blank">
                <button class='see-work-btn'>See My Work</button>
            </a>
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" class="tool-icon" alt="PostgreSQL">
        </div>
    </div>
    """, unsafe_allow_html=True)

# Row 2 - unchanged
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(f"""
    <div class='project-card'>
        <div class='project-header'>
            <img src="https://nicolasboucher.online/wp-content/uploads/2024/12/Template-blue-40.png">
            <div class='project-title'>PYTHON ATIQ BANK</div>
        </div>
        <div class='project-body'>
            <div class='project-subtitle'>Banking Simulation</div>
            <div class='project-desc'>Banking data processing and analysis simulation using Python and Jupyter Notebook.</div>
            <a href="https://github.com/890Pratik/Python-AtilQ-Bank/blob/main/phase_1_atliqo_bank.ipynb" target="_blank">
                <button class='see-work-btn'>See My Work</button>
            </a>
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" class="tool-icon" alt="Python">
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class='project-card'>
        <div class='project-header'>
            <img src="https://i.ytimg.com/vi/bjLIA1vSqGs/maxresdefault.jpg">
            <div class='project-title'>EXCEL PROJECT</div>
        </div>
        <div class='project-body'>
            <div class='project-subtitle'>Sales Analytics (FMCG)</div>
            <div class='project-desc'>Created 2 reports for the sales team which will help them to evaluate customer performance and understand...</div>
            <a href="https://github.com/890Pratik/Excel-Sales-Analytics" target="_blank">
                <button class='see-work-btn'>See My Work</button>
            </a>
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_(2019–present).svg" class="tool-icon" alt="Excel">
        </div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class='project-card'>
        <div class='project-header'>
            <img src="https://via.placeholder.com/600x300/9370DB/FFFFFF?text=ONGOING+PROJECT">
            <div class='project-title'>ONGOING PROJECT</div>
        </div>
        <div class='project-body'>
            <div class='project-subtitle'>Coming Soon</div>
            <div class='project-desc'>Advanced analytics project in progress...</div>
            <a href="#" target="_blank">
                <button class='see-work-btn'>See My Work</button>
            </a>
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" class="tool-icon" alt="Power BI">
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Skills Section (unchanged)
st.markdown("""
<div class='section-card'>
    <h2>Skills</h2>
    <div class='skills-grid'>
        <div class='skill-item tooltip'>
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" class="skill-logo" alt="Python">
            <div class='skill-name'>Python</div>
            <span class='tooltiptext'>Advanced<br>Pandas, NumPy, Scikit-learn, Streamlit, ML Models</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" class="skill-logo" alt="PostgreSQL">
            <div class='skill-name'>PostgreSQL</div>
            <span class='tooltiptext'>Advanced<br>Complex queries, CTEs, Window functions, Joins</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" class="skill-logo" alt="Power BI">
            <div class='skill-name'>Power BI</div>
            <span class='tooltiptext'>Advanced<br>DAX, Power Query, Interactive Dashboards</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://www.logo.wine/a/logo/Amazon_Web_Services/Amazon_Web_Services-Logo.wine.svg" class="skill-logo" alt="AWS">
            <div class='skill-name'>AWS</div>
            <span class='tooltiptext'>Proficient<br>S3, Lambda, Bedrock, Transcribe, Step Functions</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Amazon-S3-Logo.svg" class="skill-logo" alt="Amazon S3">
            <div class='skill-name'>Amazon S3</div>
            <span class='tooltiptext'>Proficient<br>Data storage & retrieval for analytics</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://cdn.worldvectorlogo.com/logos/aws-lambda-1.svg" class="skill-logo" alt="AWS Lambda">
            <div class='skill-name'>AWS Lambda</div>
            <span class='tooltiptext'>Proficient<br>Serverless functions for automation</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://cms.article-factory.ai/wp-content/uploads/2023/04/amazon-bedrock.png" class="skill-logo" alt="Amazon Bedrock">
            <div class='skill-name'>Amazon Bedrock</div>
            <span class='tooltiptext'>Proficient<br>LLM integration (Haiku) for call analytics</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://logos-world.net/wp-content/uploads/2022/02/Microsoft-Excel-Logo.png" class="skill-logo" alt="Excel">
            <div class='skill-name'>Excel & VBA</div>
            <span class='tooltiptext'>Advanced<br>Pivot tables, advanced formulas, VBA automation</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" class="skill-logo" alt="Streamlit">
            <div class='skill-name'>Streamlit</div>
            <span class='tooltiptext'>Advanced<br>Interactive web apps & dashboards</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Git-logo.svg" class="skill-logo" alt="Git">
            <div class='skill-name'>Git</div>
            <span class='tooltiptext'>Proficient<br>Version control & collaboration</span>
        </div>
        <div class='skill-item tooltip'>
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" class="skill-logo" alt="Docker">
            <div class='skill-name'>Docker</div>
            <span class='tooltiptext'>Intermediate<br>Containerization for deployment</span>
        </div>
    </div>
</div>

<style>
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 30px;
        margin-top: 30px;
        justify-items: center;
    }
    .skill-item {
        text-align: center;
        transition: transform 0.3s ease;
    }
    .skill-item:hover {
        transform: translateY(-8px);
    }
    .skill-logo {
        width: 80px;
        height: 80px;
        margin-bottom: 12px;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
        transition: transform 0.3s ease;
    }
    .skill-item:hover .skill-logo {
        transform: scale(1.15);
    }
    .skill-name {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1rem;
    }
    .tooltip {
        position: relative;
        display: inline-block;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 240px;
        background-color: #2c3e50;
        color: #fff;
        text-align: center;
        border-radius: 10px;
        padding: 12px;
        position: absolute;
        z-index: 10;
        bottom: 125%;
        left: 50%;
        margin-left: -120px;
        opacity: 0;
        transition: opacity 0.4s ease;
        font-size: 0.95rem;
        line-height: 1.6;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -10px;
        border-width: 10px;
        border-style: solid;
        border-color: #2c3e50 transparent transparent transparent;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# Education Section (unchanged)
st.markdown("""
<div class='section-card'>
    <h2>Education</h2>
    <ul>
        <h3>MSc in Data Analytics</h3>
        <li>National College of Ireland | Sept 2024 – Oct 2025</li>
        <li>Modules: Statistics, Data Governance, Business Intelligence, Machine Learning, Deep Learning, Generative AI</li>
        <li>Research: Enhancing Short-Term Solar Irradiance Prediction Accuracy with SARIMA-LSTM and XGBoost: A Case Study Using the UNISOLAR Dataset</li>
    </ul>
    <ul>
        <h3>BSc in Statistics (Hons)</h3>
        <li>St. Anthony’s College | Graduated 2021</li>
    </ul>
    <h3>Certifications</h3>
    <ul>
        <li>Data Analytics Bootcamp | Great Learning | Feb 2024</li>
        <li>Excel, SQL and Power BI | Codebasics | Sep 2023 - Apr 2024</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class='section-card' id='contact'>
    <h2>Contact</h2>
    <p>📧 pratiksunar0899.ie@gmail.com</p>
    <p>📞 +353 83 853 8913</p>
    <p>📍 Dublin, Ireland | Stamp 1G</p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align:center; color:#666; margin-top:50px;'>© 2026 Pratik Sunar | Built with Streamlit</p>", unsafe_allow_html=True)
