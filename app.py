import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Pratik Sunar | Data Analyst",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# GLOBAL CSS (MOBILE & iOS SAFE)
# --------------------------------------------------
st.markdown("""
<style>
/* Base */
.stApp {
    background-color: #f9f5f0;
    font-family: "Segoe UI", sans-serif;
}
.main-container {
    max-width: 1200px;
    margin: auto;
    padding: 20px;
}

/* Section Card – SAFE */
.section-card {
    background-color: #ffffff !important;
    border-radius: 20px;
    padding: 30px;
    margin: 30px 0;
    box-shadow: 0 0 20px rgba(0, 191, 191, 0.35);
}

/* FORCE TEXT VISIBILITY (iOS FIX) */
.section-card,
.section-card * {
    color: #222 !important;
    opacity: 1 !important;
}

/* Headings */
h1 { color: #333; }
h2 {
    text-align: center;
    color: #00a0a0;
    margin-bottom: 20px;
}
h3 { color: #333; }

/* Intro */
.intro-text {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #444 !important;
}

/* Lists */
ul {
    max-width: 800px;
    margin: auto;
}
li {
    margin-bottom: 10px;
}

/* Social Icons */
.social-icons {
    display: flex;
    gap: 25px;
    margin-top: 25px;
}
.social-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #e0f7fa;
    padding: 8px;
    box-shadow: 0 0 10px rgba(0,191,191,0.3);
}

/* Contact Button */
.contact-btn {
    display: block;
    margin: 30px auto;
    width: 200px;
    text-align: center;
    padding: 14px;
    border-radius: 40px;
    background: linear-gradient(135deg, #0066cc, #004080);
    color: white !important;
    text-decoration: none;
    font-size: 1.1rem;
    box-shadow: 0 0 15px rgba(0,102,204,0.4);
}

/* Project Cards */
.project-card {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    overflow: hidden;
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
}
.project-card:hover {
    transform: translateY(-6px);
}
.project-header {
    height: 180px;
}
.project-header img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.project-title {
    position: absolute;
    margin: 10px;
    padding: 8px 14px;
    background: rgba(0,0,0,0.7);
    color: #fff;
    border-radius: 8px;
    font-weight: bold;
}
.project-body {
    padding: 16px;
    text-align: center;
    flex-grow: 1;
}
.project-desc {
    font-size: 0.9rem;
    margin: 10px 0;
}
.see-work-btn {
    background: #00a0a0;
    color: white;
    border-radius: 30px;
    padding: 8px 22px;
    border: none;
    cursor: pointer;
}

/* Skills */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 30px;
    margin-top: 30px;
    justify-items: center;
}
.skill-logo {
    width: 70px;
    margin-bottom: 10px;
}

/* Mobile */
@media (max-width: 768px) {
    .section-card { padding: 20px; }
    .intro-text { font-size: 1rem; }
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# HEADER
col1, col2 = st.columns([1, 3])
with col1:
    st.image(
        "https://raw.githubusercontent.com/890Pratik/pratik-portfolio/main/profile.png",
        width=220
    )

with col2:
    st.markdown("<h1>Pratik Sunar</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p class="intro-text">
    Data Analyst with hands-on experience in Data Science, Machine Learning, 
    Business Intelligence, Insurance and Pharmaceutical domains.
    </p>
    <p class="intro-text">
    Skilled in SQL, Python, Power BI, Excel, Streamlit and AWS. 
    Experienced in customer call analytics, claims outlier detection,
    PL/SQL automation and reporting solutions.
    </p>
    <p class="intro-text">
    Currently based in Ireland | Stamp 1G
    </p>
    """, unsafe_allow_html=True)

# SOCIALS
st.markdown("""
<div class="social-icons">
    <a href="https://www.linkedin.com/in/pratik-sunar-438323244/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="social-icon">
    </a>
    <a href="https://github.com/890Pratik" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" class="social-icon">
    </a>
    <a href="mailto:pratiksunar0899.ie@gmail.com">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" class="social-icon">
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('<a href="#contact" class="contact-btn">Contact Me</a>', unsafe_allow_html=True)

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------
st.markdown("""
<div class="section-card">
<h2>Experience</h2>

<h3><strong>VHI Group DAC – Data Analyst Intern (2025)</strong></h3>
<ul>
<li><strong>Analyzed 30k+ healthcare & drug claims to enhance Outlier Claims Model</strong></li>
<li><strong>Applied LLM (Haiku) via AWS Bedrock on 2,000+ customer calls</strong></li>
<li><strong>Built PL/SQL & VBA automation for reporting</strong></li>
</ul>

<h3><strong>Alembic Pharmaceutical – Market Data Analyst (2022–2023)</strong></h3>
<ul>
<li><strong>Analyzed prescription & sales data</strong></li>
<li><strong>Applied clustering & regression models</strong></li>
<li><strong>Contributed to 110% quarterly growth</strong></li>
</ul>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# EDUCATION
# --------------------------------------------------
st.markdown("""
<div class="section-card">
<h2>Education</h2>

<ul>
<li><strong>MSc Data Analytics – National College of Ireland (2024–2025)</strong></li>
<li><strong>BSc Statistics – St. Anthony’s College (2021)</strong></li>
</ul>

<h3><strong>Certifications</strong></h3>
<ul>
<li><strong>Data Analytics – Great Learning</strong></li>
<li><strong>Excel, SQL, Power BI – Codebasics</strong></li>
</ul>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# CONTACT
# --------------------------------------------------
st.markdown("""
<div class="section-card" id="contact">
<h2>Contact</h2>
<p><strong>📧 pratiksunar0899.ie@gmail.com</strong></p>
<p><strong>📞 +353 83 853 8913</strong></p>
<p><strong>📍 Dublin, Ireland</strong></p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown(
    "<p style='text-align:center;color:#666;margin-top:40px;'>© 2026 Pratik Sunar | Built with Streamlit</p>",
    unsafe_allow_html=True
)
