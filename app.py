import streamlit as st

# Page Config
st.set_page_config(page_title="Pratik Sunar | Data Analyst", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS - Improved for mobile visibility & button fix
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
    .social-icons {display: flex; justify-content: flex-start; gap: 30px; margin: 20px 0; flex-wrap: wrap;}
    .social-icon {width: 40px; height: 40px; border-radius: 50%; background: #e0f7fa; padding: 10px; box-shadow: 0 0 10px rgba(0,191,191,0.3);}
    .contact-btn {
        background: linear-gradient(135deg, #0066cc, #004080);
        color: white !important;
        padding: 15px 40px;
        border-radius: 50px;
        font-size: 1.2rem;
        text-align: center;
        display: block;
        width: 200px;
        max-width: 100%;
        margin: 30px auto;
        text-decoration: none;
        box-shadow: 0 0 15px rgba(0,102,204,0.4);
        transition: all 0.3s ease;
        z-index: 10;
        box-sizing: border-box;
    }
    .contact-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(0,102,204,0.6);
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

    /* Skills Grid */
    .skills-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 20px; margin-top: 30px;}
    .skill-item {text-align: center;}
    .skill-logo {width: 60px; height: 60px; margin-bottom: 10px;}
    .skill-name {font-weight: bold; color: #333;}

    /* Project Card Styles */
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
        .contact-btn {
            width: 100%;
            max-width: 300px;
            padding: 12px 20px;
            font-size: 1.1rem;
        }
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

# Social Icons + Contact Button (fixed visibility)
st.markdown("""
<div class='social-icons' style='margin-top: 30px;'>
    <a href="https://www.linkedin.com/in/pratik-sunar-438323244/"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="social-icon" alt="LinkedIn"></a>
    <a href="https://github.com/890Pratik"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" class="social-icon" alt="GitHub"></a>
    <a href="mailto:pratiksunar0899.ie@gmail.com"><img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" class="social-icon" alt="Mail"></a>
    <a href="#projects"><img src="https://cdn-icons-png.flaticon.com/512/3095/3095398.png" class="social-icon" alt="Projects"></a>
</div>
""", unsafe_allow_html=True)

st.markdown('<a href="#contact" class="contact-btn">Contact Me</a>', unsafe_allow_html=True)

# Experience Section
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

# Projects Section (your current setup - no change needed here)
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

# (rest of your projects code remains unchanged - col2, col3, row 2)

st.markdown("</div>", unsafe_allow_html=True)

# Skills Section (unchanged)
# ... (your skills code here)

# Education Section (unchanged)
# ... (your education code here)

# Contact Section (unchanged)
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
