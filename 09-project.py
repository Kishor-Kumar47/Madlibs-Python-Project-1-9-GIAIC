#  project number 9 

import streamlit as st 
import pandas as pd
import random
st.set_page_config(page_title='Student Data Generator', layout='wide',page_icon='👨‍💻')
st.title("👨‍💻 Student CSV Generator")

names = ["Kishor", "Gotam", "Dolat","BhagChand","Ahmed","Ali","Sunnel","Ajay","Usama","Hina","Sara","Zara","Zoya"]

students = []
for i in range(1,13):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A","B","C","D","E","F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("Generate Student Data")
st.dataframe(df)

csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file)
st.success("Students Record Generated Successfully!✔️")