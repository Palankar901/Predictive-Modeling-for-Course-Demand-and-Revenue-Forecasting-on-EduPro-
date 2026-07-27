import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="EduPro Forecasting",layout="wide")
st.title("EduPro | Course Demand & Revenue Analytics")
st.caption("Decision-support baseline. Upload a refreshed course metrics CSV or use the prepared dataset.")
def load_data(upload):
    return pd.read_csv(upload) if upload else pd.read_csv(Path(__file__).parent/"edupro_course_metrics.csv")
upload=st.sidebar.file_uploader("Refresh with course metrics CSV",type="csv")
df=load_data(upload)
st.sidebar.header("Scenario inputs")
price=st.sidebar.number_input("Course price",0.0,5000.0,float(df.CoursePrice.median()))
duration=st.sidebar.number_input("Duration (hours)",0.1,500.0,float(df.CourseDuration.median()))
level=st.sidebar.selectbox("Level",sorted(df.CourseLevel.dropna().unique()))
category=st.sidebar.selectbox("Category",sorted(df.CourseCategory.dropna().unique()))
base=df[(df.CourseCategory==category)&(df.CourseLevel==level)]
base=base if len(base) else df
# Transparent scenario, not a trained production score: historical comparable-course average scaled by price ratio.
base_price=max(base.CoursePrice.mean(),1); demand=max(0,base.EnrollmentCount.mean()*(1-0.20*(price/base_price-1))); forecast_revenue=demand*price
c1,c2,c3=st.columns(3); c1.metric("Observed catalog revenue",f"${df.CourseRevenue.sum():,.0f}"); c2.metric("Scenario demand",f"{demand:,.0f} enrollments"); c3.metric("Scenario revenue",f"${forecast_revenue:,.0f}")
st.info("Scenario figures are transparent planning estimates based on comparable historical courses. Production predictions should load a validated serialized model after additional time-series data is collected.")
st.subheader("Category demand and revenue")
cat=df.groupby('CourseCategory').agg(Enrollments=('EnrollmentCount','sum'),Revenue=('CourseRevenue','sum')).sort_values('Revenue',ascending=False)
st.bar_chart(cat[['Revenue']]); st.dataframe(cat,use_container_width=True)
st.subheader("Price vs. realized revenue")
st.scatter_chart(df,x='CoursePrice',y='CourseRevenue',color='CourseCategory')
st.subheader("Feature importance explorer")
imp_path=Path(__file__).parent/'feature_importance.csv'
if imp_path.exists():
    imp=pd.read_csv(imp_path).set_index('Feature'); st.bar_chart(imp)
st.subheader("Course-level data")
st.dataframe(df[['CourseName','CourseCategory','CourseLevel','CoursePrice','EnrollmentCount','CourseRevenue','CourseRating']],use_container_width=True)
