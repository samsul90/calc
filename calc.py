import streamlit as st

def main():
	st.title("kalkulator")

	num1 = st.number_input("Angka Pertama")
	num2 = st.number_input("Angka Kedua")

	operation = st.selectbox("Operasi:", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

	result = 0

	if operation == "Penjumlahan":
    	result = num1 + num2
	elif operation == "Pengurangan":
    	result = num1 - num2
	elif operation == "Perkalian":
    	result = num1 * num2
	elif operation == "Pembagian":
    	if num2 != 0:
        	result = num1 / num2
    	else:
        	st.error("Pembagian dengan 0 tidak valid!")
	
	st.write("Hasil:", result)

if __name__ == '__main__':
	main()
