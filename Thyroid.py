import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import streamlit as st 

@st.cache_data
def load_data():
    df = pd.read_csv("Thyroid_Diff.csv")
    return df

data = load_data()
st.title("Thyroid Cancer Dashboard")

st.write("The Thyroid Cancer datset provides a platform that guides patients treatments. This helps in preventing undertreatment and also spare patients from spending more in therapy especially in early stages")

# Display raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)

category = data['Physical Examination'].unique()
category_filter = st.multiselect("Physical Examination:", category, default=category)
filtered_data = data[data['Physical Examination'].isin(category_filter)]

st.subheader("Age distribution using histogram")
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True, color='#ffd8a7')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
st.pyplot(plt)

st.write("Majority of patients affected by Thyroid cancer are aged between 25 and 35 years of age")


st.subheader("Pie chart for thyroid cancer stages")
sns.set_palette("OrRd")
fig, axes = plt.subplots(1, 3, figsize=(20, 8))

Stage_of_Cancer = data['Stage'].value_counts()
Stage_of_Cancer.plot(kind='pie', autopct='%0.2f%%', labels=Stage_of_Cancer.index, explode=[0.1, 0.2, 0.3, 0.4, 0.9], shadow=True, ax=axes[1])
axes[0].set_title('Throid Cancer Stages in Percentage')
axes[0].set_ylabel('')

risk_data = data['Risk'].value_counts()
risk_data.plot(kind='pie', autopct='%0.2f%%', explode=[0.05, 0.08, 0.1], labels=risk_data.index, shadow=True, ax=axes[0])
axes[1].set_title('Risk involved in percentage')
axes[1].set_ylabel('')

aden = data['Adenopathy'].value_counts()
aden.value_counts().plot(kind='pie', autopct='%0.2f%%', labels=aden.index, shadow=True, ax=axes[2])
axes[2].set_title('Adenopathy in percentage')
axes[2].set_ylabel('')

st.pyplot(fig)


st.subheader("Patients count per gender, gender,smoking, & Response category")

fig, axes = plt.subplots(1, 3, figsize=(20, 8))

#Display the count of patients in each category.
sns.countplot(x='Gender', data=data, palette='OrRd', ax=axes[0])
axes[0].set_title('Gender Count')
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Count')

sns.countplot(x='Smoking', data=data, palette='OrRd', ax=axes[1])
axes[1].set_title('Smoking Count')
axes[1].set_xlabel('Smoking')
axes[1].set_ylabel('Count')

sns.countplot(x='Response', data=data, palette='OrRd',  ax=axes[2])
axes[2].set_title('Treatment Response Count')
axes[2].set_xlabel('Response')
axes[2].set_ylabel('Count')
axes[2].tick_params(axis='x', rotation=45)
st.pyplot(fig)


st.subheader("Relation Between Thyroid Stage and Recurrence")
plt.figure(figsize=(10, 6))
sns.countplot(x='Stage', hue='Recurred', data=data)

plt.title('Stage and Recurred')
plt.xlabel('Stage')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Recurred')
plt.tight_layout()

st.pyplot(plt)

st.subheader("Relation Between Physical Examination & Recurrence")

plt.figure(figsize=(10, 6))
sns.countplot(x='Physical Examination', hue='Recurred', data=data)

plt.title('Physical Examination and Recurred')
plt.xlabel('Physical Examination')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Recurred')
plt.tight_layout()

st.pyplot(plt)

fig, axes = plt.subplots(1, 2, figsize=(20, 5))

# Boxplot for Tumor by Age
sns.boxplot(x='T', y='Age', data=data, palette="OrRd", ax=axes[0])
axes[0].set_title('Boxplot of Age by Tumor Stage') 
axes[0].set_xlabel('Tumor Stage')
axes[0].set_ylabel('Age')
axes[0].tick_params(axis='x', rotation=45)

# Boxplot for cancer Stage by age
sns.boxplot(x='Stage', y='Age', data=data,palette="OrRd", ax=axes[1])
axes[1].set_title('Boxplot of Age by Cancer Stage')
axes[1].set_xlabel('Cancer Stage')
axes[1].set_ylabel('Age')
axes[1].tick_params(axis='x', rotation=0)
st.pyplot(plt)


st.subheader("Insights")
st.write("1. Females are the most affected with Thyroid cancer")
st.write("2. Smoking doesn't affect thyroid cancer that much")
st.write("3. Recovery rate from thryroid cancer is excellent")
st.write("4. Patients with multinodular goiter are at a higher risk of recurrent goiter")
st.write("5. Patients with diffuse goiter are not at risk of recurrent goiter")
st.write("6. Patients at the first stage have higher chance of recurrent goiter")
st.write("7. Patients who received structural incomplete treatment are at a higher risk of recurrent goiter")
st.write("The higher the stage  of thyroid cancer, the greater patients risk of recurrent thyroid cancer")




