# 🇮🇳 Tamil Cinema Representation Analysis Dashboard

[![Streamlit App](https://img.shields.io/badge/Streamlit-LIVE-brightgreen)](https://tamilcinemarepresentation-9shsvsvyssq2g7ppjqudpd.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-orange)](https://streamlit.io/)

## 🎬 **Project Overview**
Data science analysis of **Tamil cinema representation** - Female lead roles, working women characters, and movie ratings (2011-2019). Built with **Streamlit** + **Pandas** for interactive dashboard.

## 📊 **Key Features**
- 🔍 **Interactive Filters**: Year range, Female lead, Working women
- 📈 **Visual Analytics**: Female representation trends, rating comparisons  
- 🏆 **Top Movies**: Highest rated films with representation status
- 📱 **Responsive Design**: Mobile + Desktop friendly

## 🚀 **Live Demo**
[👉 View Dashboard](https://tamilcinemarepresentation-9shsvsvyssq2g7ppjqudpd.streamlit.app/)

## 📈 **Key Insights**
👩 Female Leads: ~25% of movies (2011-2019)
⭐ Avg Rating: 6.8/10
💼 Working Women: 18% representation
🏆 Highest Rated: Female-led films avg +0.3 rating points


## 🛠 **Tech Stack**
Frontend: Streamlit + Pandas
Data: Kaggle Tamil Movies Dataset (500+ films)
Deployment: Streamlit Cloud
Analytics: Female representation scoring system

## 📁 **Files**
├── app.py # Main dashboard
├── tamil_movies_clean.csv # Movie dataset (IMDB ratings)
├── tamil_representation_labels.csv # Manual labels (50+ films)
├── requirements.txt # Dependencies
└── runtime.txt # Python 3.11

## 🎯 **How to Run Locally**
git clone https://github.com/sajitha-shanmugam/tamil_cinema_representation
cd tamil_cinema_representation
pip install -r requirements.txt
streamlit run app.py


## 📊 **Sample Data**
| Title | Year | Rating | Female Lead | Working Woman |
|-------|------|--------|-------------|---------------|
| Kabali | 2016 | 6.5 | No | No |
| 96 | 2018 | 8.5 | Yes | Yes |

## 🔬 **Methodology**
1. **Data Collection**: Kaggle Tamil movies dataset
2. **Labeling**: Manual analysis of 50+ films (female lead, working woman)
3. **Visualization**: Interactive filters + KPI metrics
4. **Deployment**: Streamlit Cloud (auto-updates)

## 📈 **Future Enhancements**
- [ ] Director-wise analysis
- [ ] Genre correlation
- [ ] Bechdel test integration
- [ ] ML rating prediction

## 👩‍💻 **Author**
**Sajitha Shanmugam**  
Final Year CS Student | Data Science Enthusiast  
[LinkedIn](https://linkedin.com/in/sajithashanmugam) | [Portfolio](https://sajitha.streamlit.app)

## 📄 **License**
MIT License - Free to use & modify!

---

⭐ **Star this repo if helpful!**  
💬 **Issues/PRs welcome!**
