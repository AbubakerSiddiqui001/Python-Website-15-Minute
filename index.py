import streamlit as st
import pandas as pd
import plotly.express as px

# Sidebar settings
st.sidebar.title("🚀 Quick Settings")
username = st.sidebar.text_input("Enter your name", "Guest")
theme_color = st.sidebar.color_picker("Pick a theme color", "#00f900")
show_charts = st.sidebar.checkbox("Show Charts", value=True)

# Main title
st.title(f"✨ Welcome, {username}!")
st.markdown(f"<hr style='border:1px solid {theme_color}'/>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📁 Data Upload", "📊 Charts", "ℹ️ About"])

with tab1:
    st.subheader("📁 Upload your CSV file")
    file = st.file_uploader("Choose a CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.success("✅ File Uploaded Successfully!")
        st.dataframe(df.head())

with tab2:
    if file is not None and show_charts:
        st.subheader("📊 Visualize Your Data")
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if len(numeric_cols) >= 2:
            x_axis = st.selectbox("Choose X-axis", numeric_cols)
            y_axis = st.selectbox("Choose Y-axis", numeric_cols, index=1)

            scatter_fig = px.scatter(df, x=x_axis, y=y_axis, title="Scatter Plot")
            st.plotly_chart(scatter_fig)

            st.markdown("### 📊 Histogram")
            hist_col = st.selectbox("Choose column for histogram", numeric_cols)
            hist_fig = px.histogram(df, x=hist_col, nbins=20, title="Histogram")
            st.plotly_chart(hist_fig)
        else:
            st.warning("⚠️ Not enough numeric columns to display charts.")
    elif not file:
        st.info("ℹ️ Upload a CSV file to generate charts.")

with tab3:
    st.markdown("""
    ### 👨‍💻 About This App
    This is a Streamlit dashboard template with:
    
    - CSV file upload and preview  
    - Interactive charts using Plotly  
    - Tab navigation & sidebar customization
    
    Expand this into a resume builder, finance tracker, or any dashboard idea!

    Made with ❤️ by Abubaker Siddiqui
    """)

# Footer
st.caption("🔗 Built with Streamlit | Custom Dashboard")
