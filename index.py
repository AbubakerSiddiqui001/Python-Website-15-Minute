import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.sidebar.title("🚀 Quick Settings")
username = st.sidebar.text_input("Enter your name", "Guest")
theme_color = st.sidebar.color_picker("Pick a theme color", "#00f900")
show_charts = st.sidebar.checkbox("Show Charts", value=True)

st.title(f"✨ Welcome, {username}!")
st.markdown(f"<hr style='border:1px solid {theme_color}'/>", unsafe_allow_html=True)

# Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["📊 Data Upload", "📈 Charts", "📚 About"])

with tab1:
    st.subheader("📁 Upload your CSV file")
    file = st.file_uploader("Choose a CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.success("File Uploaded Successfully!")
        st.dataframe(df.head())

with tab2:
    if file is not None and show_charts:
        st.subheader("📊 Visualize Your Data")
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if len(numeric_cols) >= 2:
            x_axis = st.selectbox("Choose X-axis", numeric_cols)
            y_axis = st.selectbox("Choose Y-axis", numeric_cols, index=1)

            fig = px.scatter(df, x=x_axis, y=y_axis, title="Scatter Plot")
            st.plotly_chart(fig)

            st.markdown("### Histogram")
            col = st.selectbox("Choose column for histogram", numeric_cols)
            fig2, ax = plt.subplots()
            ax.hist(df[col], bins=20, color='skyblue', edgecolor='black')
            st.pyplot(fig2)
        else:
            st.warning("Not enough numeric columns to display charts.")

    elif not file:
        st.info("Upload a CSV file to generate charts.")

with tab3:
    st.markdown("""
    ### 👨‍💻 About This App
    This is a more advanced Streamlit dashboard template that shows:
    - Sidebar inputs
    - Tabs navigation
    - CSV file upload and preview
    - Interactive charts using Plotly & Matplotlib
    
    You can expand it into a finance tracker, resume builder, or business dashboard!

    Made with ❤️ by Abubaker Siddiqui
    """)

# Footer
st.caption("🔗 Built with Streamlit | Advanced Example")
