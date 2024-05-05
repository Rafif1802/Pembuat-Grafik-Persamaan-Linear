import streamlit as st
import numpy as np

# Fungsi untuk menghitung persamaan regresi linier dan koefisien korelasi
def calculate_regression_equation(X, Y):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    sum_x_squared = np.sum(X**2)

    # Menghitung koefisien regresi
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    # Menghitung koefisien korelasi
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x**2) * (n * np.sum(Y**2) - np.sum(Y)**2))

    equation = f'y = {a:.2f} + {b:.2f}x'
    regression_info = {'equation': equation, 'intercept': a, 'slope': b, 'r_value': r}
    return regression_info

# Halaman aplikasi Streamlit
def main():
    st.title('Penentuan Persamaan Regresi Linearlitas')
    st.subheader('Kelompok 3 (1E-PMIP)')
    st.write('Anggota:')
    st.write('1. Dhika Nurafliansyah (2320517)')
    st.write('2. Herni Khairunisa (2320528)')
    st.write('3. Ibnu Rafif (2320530)')
    st.write('4. Khaira Mutya Arrahman (2320533)')
    st.write('5. Marsya Kaila Avridita Mulyono (2320535)')

    st.write('Masukkan data X dan Y untuk menghitung persamaan regresi linier')

    # Input data X dan Y dari pengguna
    X_input = st.text_input('Masukkan nilai X (pisahkan dengan koma jika lebih dari satu):').strip()
    Y_input = st.text_input('Masukkan nilai Y (pisahkan dengan koma jika lebih dari satu):').strip()

    if X_input and Y_input:
        X = np.array([float(x) for x in X_input.split(',')])
        Y = np.array([float(y) for y in Y_input.split(',')])

        # Menghitung persamaan regresi linier dan koefisien korelasi
        regression_info = calculate_regression_equation(X, Y)

        # Menampilkan persamaan regresi linier, nilai slope (b), nilai intercept (a), dan nilai koefisien korelasi (r)
        st.markdown('### Persamaan Regresi Linier:')
        st.markdown(f'```{regression_info["equation"]}```', unsafe_allow_html=True)

        st.markdown('### Nilai Slope (b):')
        st.write(f'{regression_info["slope"]:.2f}')

        st.markdown('### Nilai Intercept (a):')
        st.write(f'{regression_info["intercept"]:.2f}')

        st.markdown('### Nilai Koefisien Korelasi (r):')
        st.write(f'{regression_info["r_value"]:.4f}')

if __name__ == '__main__':
    main()

