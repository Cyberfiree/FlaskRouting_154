from flask import Flask, render_template, request, redirect, url_for  #Mengimpor Flask dan fungsi terkait
#from               # Mengimpor modul
#flask              # Modul yang menyediakan framework untuk aplikasi web
#import             # Kata kunci untuk mengimpor objek
#Flask              # Kelas utama dari Flask framework untuk membuat aplikasi
#render_template    # Fungsi untuk merender template HTML
#request            # Objek untuk menangani permintaan HTTP
#redirect           # Fungsi untuk mengarahkan pengguna ke halaman lain
# url_for           #Fungsi untuk menghasilkan URL berdasarkan nama route

app = Flask(__name__) # Membuat instance dari Flask app
#app =                  # Mendeklarasikan dan menginisialisasi instance aplikasi Flask
#Flask(__name__)        # Membuat objek Flask dengan nama modul sebagai argumen

@app.route('/') # Menangani route utama (login)/Mendeklarasikan route untuk halaman utama
def login():
    return render_template('login.html') # Render halaman login.html
#def                                        # Mendefinisikan fungsi untuk menangani permintaan HTTP
#login():                                   # Fungsi login untuk menangani permintaan di route '/'
#return                                     # Mengembalikan response atau halaman
#render_template('login.html')              # Merender template HTML login.html

@app.route('/home', methods=['POST']) # Menangani route untuk menerima data form / Mendeklarasikan route untuk '/home' hanya menerima POST
def home():
    name = request.form.get('name') # Mengambil nilai dari input nama
    age = request.form.get('age') # Mengambil nilai dari input usia
    return render_template('home.html', name=name, age=age) # Render halaman home.html dengan data nama dan usia
#def                        # Mendefinisikan fungsi untuk menangani permintaan HTTP
#home():                    # Fungsi home untuk menangani permintaan di route '/home'
#name =                     # Mengambil nilai dari form input 'name'
#request.form.get('name')   # Mengambil data 'name' dari form
#age =                      # Mengambil nilai dari form input 'age'
#request.form.get('age')    # Mengambil data 'age' dari form
#return                     # Mengembalikan response atau halaman
#render_template('home.html', name=name, age=age)  # Merender template home.html dengan data yang diterima

@app.route('/back', methods=['GET'])# Menangani route untuk kembali ke halaman login /Mendeklarasikan route untuk '/back' hanya menerima GET
def back_to_login():
    return redirect(url_for('login'))# Mengalihkan ke halaman login
#def                            # Mendefinisikan fungsi untuk menangani permintaan HTTP
#back_to_login():               # Fungsi untuk kembali ke halaman login
#return                         # Mengembalikan response atau redirect
#redirect(url_for('login'))     # Mengarahkan ke halaman login menggunakan URL yang dibuat oleh url_for

if __name__ == '__main__': # Memastikan aplikasi berjalan hanya jika dijalankan langsung
    app.run(debug=True) # Menjalankan aplikasi dengan mode debug
#if                         # Mengecek apakah modul dijalankan sebagai program utama
#__name__ == '__main__':    # Memastikan bahwa kode dijalankan dari modul ini
#app.run(debug=True)        # Menjalankan aplikasi Flask dalam mode debug