import streamlit as st
import pandas as pd
import numpy as np
import time





def complete_ai_dashboard():
    # Page config
    st.set_page_config(
        page_title="AI Command Center",
        page_icon="🤖",
        layout="wide"
    )
    
    # CSS for complete navbar
    st.markdown("""
    <style>
    .main-navbar {
        background: linear-gradient(135deg, #1a2a6c 0%, #b21f1f 50%, #fdbb2d 100%);
        padding: 1rem 3rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    .nav-main {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        fixed-top: 10px;
    }
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 15px;
        font-size: 1.6rem;
        font-weight: bold;
        fixed-top: 10px;
    }
    .nav-controls {
        display: flex;
        gap: 1.5rem;
        align-items: center;
        
    }
    .control-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 0.5rem 1rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .control-item:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    .user-profile {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0.5rem 1rem;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 25px;
    }
    .avatar {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Navbar HTML
    st.markdown("""
    <div class="main-navbar">
        <div class="nav-main">
            <div class="nav-brand">
                🧠 AI Command Center v2.0
            </div>
            <div class="nav-controls">
                <div class="control-item">
                    📊 Dashboard
                </div>
                <div class="control-item">
                    🤖 Models
                </div>
                <div class="control-item">
                    ⚡ Training
                </div>
                <div class="control-item">
                    📈 Analytics
                </div>
                <div class="user-profile">
                    <div class="avatar">AI</div>
                    <span>Admin User</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Active Models", "12", "3 new")
    
    with col2:
        st.metric("Training Jobs", "8", "-2 completed")
    
    with col3:
        st.metric("Accuracy", "94.2%", "1.5%")

complete_ai_dashboard()





def ai_sidebar_navigation():
    # Sidebar styling
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
    .sidebar-title {
        color: white;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar content
    with st.sidebar:
        st.markdown('<div class="sidebar-title">🧠 AI Studio</div>', unsafe_allow_html=True)
        
        # Navigation menu
        selected = st.radio(
            "Navigation",
            ["🏠 Dashboard", "🤖 AI Models", "📊 Data", "⚡ Training", "📈 Analytics", "⚙️ Settings"],
            index=0
        )
        
        st.markdown("---")
        
        # Quick actions
        st.subheader("Quick Actions")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Train"):
                st.success("Training started!")
        with col2:
            if st.button("📊 Analyze"):
                st.info("Analysis running...")
        
        # System status
        st.markdown("---")
        st.subheader("System Status")
        st.metric("CPU Usage", "42%", "2%")
        st.metric("Memory", "68%", "-5%")
        st.metric("GPU", "Active", "✓")

ai_sidebar_navigation()








st.title("Artificial Intelligence Engineering(Title)")
st.header("Artificial Intelligence Engineering(Header)")
st.subheader("Artificial Intelligence Engineering(Sub-Header)")
st.write("Artificial Intelligence Engineering(Text)")
st.markdown("Artificial Intelligence Engineering(Markdown)")
st.caption("Artificial Intelligence Engineering(Caption)")

st.image("AI.jpg")
st.image("igor.jpg")
st.audio("audio.mp3")
st.audio("artificial.mp3")
st.video("video1.mp4")
st.video("video4.mp4")
st.video("video2.mp4")

st.checkbox('checkbox')
st.button('Click button')
st.radio('Pick your city',['Pune','Mumbai','delhi','surat'])
st.selectbox('Pick your city',['Pune','Mumbai','delhi','surat'])
st.multiselect('Pick favourite sports',['cricket', 'football', 'basketball'])
st.select_slider('Give a Remark', ['Bad', 'Good', 'Excellent'])
st.slider('Your Marks', 0,100)

on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.number_input('Enter your marks', 0,100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Artificial Intelligence Engineering")
st.sidebar.image("AI.jpg")

st.sidebar.title("Artificial Intelligence Engineering")
st.sidebar.image("andrea.jpg")

st.sidebar.title("Artificial Intelligence Engineering")
st.sidebar.image("igor.jpg")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)


df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
    

with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

df = pd.DataFrame({
    "lat" : [123],
    "lon" : [456]
})
st.map(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

with st.chat_message("user"):
    st.write("Hello ji")
