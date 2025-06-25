# India's Development Report Dashboard (2000–2023)

This interactive **Streamlit dashboard** analyzes **India's development** across five major sectors i.e. **Economy, Education, Environment, Health, and Infrastructure** using data from the **World Bank’s World Development Indicators**.

The project distills thousands of raw indicators into intuitive visualizations to highlight trends, correlations, sector scores, and the best performing years, all at your fingertips.

---

## 📊 Key Features

✅ **Sectoral Score Trends (Line Chart)**  
✅ **Radar View for Yearly Sector Comparison**  
✅ **Total National Development Score YoY**  
✅ **Correlation Between Sectors (Heatmap)**  
✅ **Best Year Per Sector (Bar Plot)**  
✅ **Interactive Dropdowns, Buttons, and Chart Reveal Cards**

---

## 📁 Dataset Details

- **Source**: World Bank Development Indicators  
- **Rows Cleaned & Processed**: ~24,000  
- **Filtered** to 5 sectors using custom mapping  
- **Years Covered**: 2000 to 2023  
- **Final Data**: `df_scores.csv`

---

## 🧠 Insights

- Identify years with highest development scores for each sector
- Explore inter-sector correlations (e.g., health vs education)
- Analyze performance patterns and volatility across years
- Drill down year-wise with radar snapshots

---

## 🚀 How to Run Locally

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/india-sector-dashboard.git
cd india-sector-dashboard
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Run the app:**
```bash
streamlit run app.py
```

📸 Dashboard Preview

![image](https://github.com/user-attachments/assets/1b4ad664-2ee0-4eb3-9d90-e3ec5c3c9725)

![image](https://github.com/user-attachments/assets/20a979d6-97df-480d-a27c-eb2f4e07a369)

![image](https://github.com/user-attachments/assets/19213783-0d92-40d2-b477-94c9b8209dbe)

![image](https://github.com/user-attachments/assets/43b4c728-9fe1-4860-bed0-f9f5d272b580)

🧾 Files in This Repo

- app.py --> Streamlit application
- df_scores.csv --> Cleaned and scored dataset
- requirements.txt --> List of required Python libraries
- README.md --> Project overview

🙌 Credits
- Data: World Bank Open Data
- Visualization: Streamlit
- Designed by: **__Vivek Joshi__**
