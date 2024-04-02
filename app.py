import streamlit as st
from PIL import Image

# 设定页面布局
st.set_page_config(layout="wide")

# CSS 样式
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;700&display=swap');

body {
    font-family: 'Open Sans', sans-serif;
}

.vertical-text {
    text-align: right;
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    text-orientation: mixed;
    font-size: 720px; /* Adjust font-size as needed */
    font-weight: 700;
    margin: 0;
}

.divider {
    border-left: 2px solid #000000;
    height: 900px;
}

.section-heading {
    color: #808080;
    font-size: 1.25rem;
    font-weight: 400;
    margin-top: 2rem;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.detail-text {
    color: #000000;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.5;
}

.red-dot {
    height: 30px;
    width: 30px;
    background-color: #ff0000;
    border-radius: 50%;
    display: inline-block;
}

.black-dot {
    height: 10px;
    width: 10px;
    background-color: #000000;
    border-radius: 50%;
    display: inline-block;
    margin-right: 5px;
}

.column-space {
    margin-right: 50px;
}

.big-font {
    font-size: 200px;
    font-weight: 700;
}

.main-bg {
    background-color: #f5f5f5;
}

.contact-info {
    font-size: 0.875rem;
    margin-top: 3rem;
}

@media (max-width: 768px) {
    .divider {
        display: none;
    }

    .column-space {
        margin-right: 0;
    }
}
</style>
""", unsafe_allow_html=True)

# 加载图片
image = Image.open('images/img.png')

# 创建两个列
lEmtpy, col1, col2, col3, col4, rEmpty = st.columns([0.6, 1, 0.2, 1.5, 1.5, 0.5])

with lEmtpy:
    pass

with col1:
    st.markdown('<div class="vertical-text big-font">Dian Lyu</div>', unsafe_allow_html=True)
    # st.markdown('<div class="vertical-text">art director &<br>graphic designer</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="section-heading">product manager<br />&</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">operation</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-heading"> </div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading"> </div>', unsafe_allow_html=True)
    # Add the software tools part
    st.markdown('<div class="red-dot"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading">With six years of experience in the internet industry, where I have developed and managed both consumer and business-facing products. My career has spanned roles from design to product management and operations.</div>',
        unsafe_allow_html=True)
    st.markdown('<div class="section-heading"><u>SOFTWARE</u></div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Figma</div>', unsafe_allow_html=True)
    st.markdown('<div class="black-dot"></div>' * 5, unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Photoshop</div>', unsafe_allow_html=True)
    st.markdown('<div class="black-dot"></div>' * 5, unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Python</div>', unsafe_allow_html=True)
    st.markdown('<div class="black-dot"></div>' * 4, unsafe_allow_html=True)

    # Contact information
    st.markdown('<div class="contact-info">Watch my portfolio<br>lvdian1217gogo@gmail.com<br>425-624-8009</div>',
                unsafe_allow_html=True)

with col4:
    st.image(image, width=200)  # 根据实际情况调整宽度
    st.markdown('<div class="section-heading"><u><string>EDUCATION</strong></u></div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">MSTI - University of Washington<br>2023.09 - Now</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Information Design - Tsinghua University<br>2022.09 - 2023.09</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-heading"><u>CERTIFICATE</u></div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Certified UX/UI Design<br>2020</div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Certified Digital product management<br>2019</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading"><u>EXPERIENCE</u></div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Product Manger - Bytedance<br>2020 - 2022</div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Product Operations - Meituan<br>2016 - 2019</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading"><u>SKILLS</u></div>', unsafe_allow_html=True)
    st.markdown('<div class="detail-text">Coordination<br>Creativity<br>Vision</div>', unsafe_allow_html=True)

with rEmpty:
    pass

# Set the background color of the main page container
st.markdown('<style>.main {background-color: #f5f5f5;}</style>', unsafe_allow_html=True)

