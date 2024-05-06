def main():
    st.title('Penentuan Persamaan Regresi Linearlitas')

    # Membuat sidebar dengan pilihan menu
    menu = st.sidebar.radio("Menu", ('Utama', 'Perkenalan Kelompok'))

    if menu == 'Utama':
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

    elif menu == 'Perkenalan Kelompok':
        st.subheader('Kelompok 3 (1E-PMIP)')
        st.write('Anggota:')
        st.write('1. Dhika Nurafliansyah (2320517)')
        st.write('2. Herni Khairunisa (2320528)')
        st.write('3. Ibnu Rafif (2320530)')
        st.write('4. Khaira Mutya Arrahman (2320533)')
        st.write('5. Marsya Kaila Avridita Mulyono (2320535)')
