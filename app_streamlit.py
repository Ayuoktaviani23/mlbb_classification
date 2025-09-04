import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_mlbb.joblib")

st.title("Machine Learning Classification")
st.markdown("Aplikasi Machine Learning Sederhana")

kill = st.slider("Jumlah Kill",0,20)
asisst = st.slider("Jumlah Assist",0,20)
death = st.slider("Jumlah Death",0,20)
turret = st.slider("Jumlah Turret",0,20)

if st.button("Prediksi"):
	data_baru = pd.DataFrame([[kill,asisst,death,turet]], columns=["kill","asisst","death","turret"])
	hasil = model.predict(data_baru)[0]
	if hasil == "penyerang":
		st.success(f"Hasil Prediksinya : {hasil}")
	else:
		st.error(f"Hasil Prediksinya : {hasil}")
	
	st.balloons()

st.caption("Dibuat dengan :skull: dan :fire: oleh Ayu Oktaviani")