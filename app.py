import streamlit as st
import pandas as pd


st.set_page_config(page_title="Tamil Cinema Representation", layout="wide", page_icon="🇮🇳")

@st.cache_data
def load_data():
    df = pd.read_csv('tamil_movies_clean.csv')
    try:
        labels = pd.read_csv('tamil_representation_labels.csv')
        df = df.merge(labels, on=['title', 'year'], how='left')
        return df
    except:
        return df

df = load_data()
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
df['num_votes'] = pd.to_numeric(df['num_votes'], errors='coerce')

st.markdown("# 🇮🇳 Tamil Cinema Representation Analysis")

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
if female_filter != "All": filtered = filtered[filtered['female_lead'] == female_filter]
if working_filter != "All": filtered = filtered[filtered['working_woman'] == working_filter]

# === KPI CARDS ===
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("🎬 Total Movies", len(filtered))
with col2: st.metric("⭐ Avg Rating", f"{filtered['imdb_rating'].mean():.1f}")
with col3: 
    female_pct = filtered['female_lead'].eq('Yes').mean()*100 if 'female_lead' in filtered.columns else 0
    st.metric("👩 Female Leads", f"{female_pct:.0f}%")
with col4:
    working_pct = filtered['working_woman'].eq('Yes').mean()*100 if 'working_woman' in filtered.columns else 0
    st.metric("💼 Working Women", f"{working_pct:.0f}%")

st.markdown("---")

# === CHART 1: Female Lead Pie ===
col1, col2 = st.columns(2)
with col1:
    st.subheader("👩 Female Lead Distribution")
    if 'female_lead' in filtered.columns:
        female_data = filtered['female_lead'].fillna('Unknown').value_counts()
        fig = px.pie(values=female_data.values, names=female_data.index, hole=0.4)
        fig.update_traces(textposition='inside')
        st.plotly_chart(fig, use_container_width=True)

# === CHART 2: Working Women Pie ===
with col2:
    st.subheader("💼 Working Women Distribution")
    if 'working_woman' in filtered.columns:
        working_data = filtered['working_woman'].fillna('Unknown').value_counts()
        fig = px.pie(values=working_data.values, names=working_data.index, hole=0.4)
        st.plotly_chart(fig, use_container_width=True)

# === CHART 3: Female Lead Trend ===
st.markdown("---")
col1, col2 = st.columns([2,1])
with col1:
    st.subheader("📈 Female Lead Trend Over Years")
    if 'female_lead' in filtered.columns:
        trend = filtered.dropna(subset=['year','female_lead']).groupby('year')['female_lead'].apply(lambda x: (x=='Yes').mean()*100)
        fig = px.line(x=trend.index, y=trend.values, markers=True, 
                     line_shape='spline', color_discrete_sequence=['#ff6b6b'])
        fig.update_layout(yaxis_title="Female Lead %", xaxis_title="Year", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# === CHART 4: Rating vs Female Lead ===
with col2:
    st.subheader("⭐ Rating Comparison")
    if 'female_lead' in filtered.columns:
        fig = px.box(filtered, x='female_lead', y='imdb_rating', 
                    color='female_lead', title="Rating: Female Lead vs Others")
        st.plotly_chart(fig, use_container_width=True)

# === PERFECT TOP 10 - REMOVE DEBUG ===
st.markdown("---")
st.subheader("🏆 Top 10 Movies by Rating")

top10 = filtered.dropna(subset=['imdb_rating']).nlargest(10, 'imdb_rating')

# CHART 1: Streamlit bar_chart (movie titles visible!)
top10_plot = top10.set_index('title')['imdb_rating'].sort_values(ascending=False)
st.bar_chart(top10_plot, height=400)

# CHART 2: Color-coded table below
st.subheader("📊 Top 10 with Female Lead Status")
display_df = top10[['title', 'year', 'imdb_rating', 'female_lead', 'working_woman']].head(10)
st.dataframe(display_df, use_container_width=True, hide_index=True)

# === CHART 6: Year-wise Movie Count ===
col1, col2 = st.columns(2)
with col1:
    st.subheader("📊 Movies per Year")
    yearly_count = filtered.groupby('year').size().reset_index(name='count')
    fig = px.bar(yearly_count, x='year', y='count', color='count', 
                color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

# === CHART 7: Rating Distribution ===
with col2:
    st.subheader("📈 Rating Distribution")
    fig = px.histogram(filtered, x='imdb_rating', nbins=20, 
                      title="IMDB Rating Histogram")
    st.plotly_chart(fig, use_container_width=True)

# === DATA TABLE ===
st.markdown("---")
st.subheader("📋 Filtered Movies Table")
st.dataframe(filtered[['title', 'year', 'imdb_rating', 'num_votes', 
                      'female_lead', 'working_woman']].head(20), 
            use_container_width=True, hide_index=True)

