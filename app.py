import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tamil Cinema Representation", layout="wide", page_icon="🇮🇳")

@st.cache_data
def load_data():
    df = pd.read_csv('tamil_movies_clean.csv')
    try:
        labels = pd.read_csv('tamil_representation_labels.csv')
        df = df.merge(labels, on=['title', 'year'], how='left')
        st.success("✅ Representation labels loaded")
        return df
    except Exception as e:
        st.warning(f"⚠️ Labels CSV issue: {e}")
        return df

df = load_data()
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
df['num_votes'] = pd.to_numeric(df['num_votes'], errors='coerce')

st.markdown("# 🇮🇳 Tamil Cinema Representation Dashboard")

# Sidebar Filters
with st.sidebar:
    st.header("🔍 Filters")
    years = sorted(df['year'].dropna().unique())
    year_range = st.slider("📅 Year Range", int(min(years)), int(max(years)), (2011, 2019))
    
    col1, col2 = st.columns(2)
    with col1: female_filter = st.selectbox("👩 Female Lead", ["All", "Yes", "No"])
    with col2: working_filter = st.selectbox("💼 Working Woman", ["All", "Yes", "No"])

# Apply filters
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])].copy()
if female_filter != "All" and 'female_lead' in filtered.columns:
    filtered = filtered[filtered['female_lead'] == female_filter]
if working_filter != "All" and 'working_woman' in filtered.columns:
    filtered = filtered[filtered['working_woman'] == working_filter]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("🎬 Total Movies", len(filtered))
col2.metric("⭐ Avg Rating", f"{filtered['imdb_rating'].mean():.1f}")
col3.metric("👩 Female Leads", f"{filtered['female_lead'].eq('Yes').mean()*100:.0f}%" if 'female_lead' in filtered.columns else "N/A")
col4.metric("💼 Working Women", f"{filtered['working_woman'].eq('Yes').mean()*100:.0f}%" if 'working_woman' in filtered.columns else "N/A")

st.markdown("---")

# Charts - STREAMLIT NATIVE (NO PLOTLY!)
col1, col2 = st.columns(2)
with col1:
    st.subheader("👩 Female Lead Distribution")
    if 'female_lead' in filtered.columns:
        st.bar_chart(filtered['female_lead'].fillna('Unknown').value_counts())

with col2:
    st.subheader("💼 Working Women Distribution")
    if 'working_woman' in filtered.columns:
        st.bar_chart(filtered['working_woman'].fillna('Unknown').value_counts())

st.markdown("---")

st.subheader("🏆 Top 10 Movies by Rating")
top10 = filtered.dropna(subset=['imdb_rating']).nlargest(10, 'imdb_rating')
if len(top10) > 0:
    st.bar_chart(top10.set_index('title')['imdb_rating'])
    st.dataframe(top10[['title', 'year', 'imdb_rating', 'female_lead']], use_container_width=True)
else:
    st.info("No movies with ratings found")

st.subheader("📊 Movies per Year")
yearly_count = filtered['year'].value_counts().sort_index()
st.bar_chart(yearly_count)
