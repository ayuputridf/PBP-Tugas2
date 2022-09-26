# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

[Link to App (login)](https://pbp-tugas4-ayu.herokuapp.com/todolist/login/)
[Link to App (register)](https://pbp-tugas4-ayu.herokuapp.com/todolist/login/)
[Link to App (create-task)](https://pbp-tugas4-ayu.herokuapp.com/todolist/register/create-task/)
[Link to App (logout)](https://pbp-tugas4-ayu.herokuapp.com/todolist/logout/)


## Fungsionalitas {% csrf_token %} pada elemen <form>
CSRF Token merupakan value yang unik, rahasia, dan tidak terduga sehingga dihasilkan oleh aplikasi di bagian sisi server kemudian dikirimkan ke klien dalam permintaan HTTP berikutnya yang nantinya dibuat di sisi klien.

Apabila tidak ada potongan kode tersebut pada elemen <form> maka saat permintaan selanjutnya dibuat, akan menolak permintaan tersebut. Hal ini terjadi ketika aplikasi di bagian sisi server melakukan validasi permintaan tersebut yang diharapkan.

## Gambara Besar Cara Membuat <form> Secara Manual

Sebuah form dalam HTML harus berada di dalam tag form, yang diawali dengan <form> dan diakhiri dengan </form>. Tag form akan membutuhkan beberapa atribut untuk dapat berfungsi dengan seharusnya. Attribut yang dibutuhkan yaitu :
1. action : untuk menjelaskan kemana data form akan dikirimkan.
2. method : untuk menjelaskan bagaimana data isian form akan dikirim oleh web browser. Terdapat nilai
    - method get 
    - method post

Struktur dasar form akan terlihat sebagai berikut:
    ```shell
    <form action="prosesdata.php" method="post">
    ...isi form...
    </form>
    ```

## Proses Alur Data
Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form , formulir HTML diperlukan, apabila ingin mengumpulkan beberapa data dari pengunjung situs. Misalnya, selama pendaftaran user, kita ingin mengumpulkan informasi seperti nama, alamat email, dll.

Pada dasarnya, web menggunakan arsitektur klien/server yang dapat diringkas sebagai berikut: klien (biasanya browser web) mengirimkan permintaan ke server (sebagian besar waktu server web seperti Apache, Nginx, IIS, Tomcat , dll.), menggunakan protokol HTTP. Server menjawab permintaan menggunakan protokol yang sama. 

Elemen <form> mendefinisikan bagaimana data akan dikirim. Semua atributnya dirancang untuk memungkinkan Anda mengonfigurasi permintaan untuk dikirim saat pengguna menekan tombol kirim. Dua atribut yang paling penting adalah tindakan dan metode.

Atribut action menentukan kemana data dikirim. Nilainya harus berupa URL relatif atau absolut yang valid. Jika atribut ini tidak tersedia, data akan dikirim ke URL halaman yang berisi formulir — halaman saat ini.

Selanjutnya terjadi penyimpanan data pada database dan munculnya data yang telah disimpan pada template HTML.

## Cara Pengimplementasian
### A. Menyalakan Virtual Environment

1. Membuka directory yang dimau pada cmd 
2. Menjalankan perintah berikut pada cmd. `python -m venv env` 
3. Menyalakan virtual env dengan `env\Scripts\activate.bat`
4. Install dependencies yang diperlukan untuk menjalankan proyek Django dengan `pip install -r requirements.txt`

## B. Membuat Aplikasi Django todolist & Konfigurasi Model

   1. Jalankan perintah `python manage.py startapp todolist` pada cmd yang masih dibuka
   2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang sudah  dibuat ke dalam proyek Django-mu. 
   3. Buka file `models.py` yang ada di folder `todolist` dan tambahkan class model yang diinginkan.
   4. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
   5. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

### C. Implementasi Views Dasar

   1. Buka `views.py` yang ada pada folder `todolist` dan buatlah fungsi yang menerima parameter    `request` dan mengembalikan `render(request, "todolist.html")`. 
   2. Buatlah folder bernama `templates` di dalam folder aplikasi `todolist` dan buatlah sebuah berkas bernama `todolist.html`. 
   3. Buatlah sebuah berkas di dalam folder aplikasi `todolist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang telah kamu buat sehingga nantinya halaman `HTML` dapat ditampilkan lewat browser-mu.
   4. Daftarkan juga aplikasi todolist ke dalam `urls.py` yang ada pada folder `project_django`

    #### Membuat Form Registrasi, Login, Logout Sekaligus Membuat Routing

    1. Tambahkan import 

    ```shell
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    from django.contrib.auth import authenticate, login
    from django.contrib.auth import logout
    ``` 

    2. Buatlah fungsi dengan nama register yang menerima parameter request dan mengisi fungsi tersebut.
    3. Buatlah berkas `HTML` baru dengan nama register.html pada folder `todolist/templates`dan mengisi berkas tersebut.
    4. Buatlah fungsi dengan nama `login `yang menerima parameter request dan mengisi fungsi tersebut.
    5. Buatlah berkas `HTML` baru dengan nama register.html pada folder `login/templates`dan mengisi berkas tersebut.
    4. Buatlah fungsi dengan nama `logout` yang menerima parameter request dan mengisi fungsi tersebut.

    5. Tambahkan potongan kode di bawah ini setelah end tag table (</table>) pada berkas todolist.html. Potongan kode ini berfungsi untuk menambahkan tombol logout.

    ```shell
    <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
    ```

    6. Buka `urls.py` yang ada pada folder todolist dan impor fungsi yang sudah kamu buat tadi.
    ```shell
        from todolist.views import register 
        from todolist.views import login_user 
        from todolist.views import logout_user

    ```
    7. Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
    ```shell
        path('register/', register, name='register'), 
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ```

    #### Merestriksi Akses Halaman todolist
    
    1. Buka views.py yang ada pada folder todolist dan tambahkan import login_required pada bagian paling atas.
    2. Tambahkan kode @login_required(login_url='/todolist/login/') di atas fungsi show_todolist agar halaman todolist hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

    #### Membuat Task Baru  Sekaligus Membuat Routing
    
    1. Buatlah fungsi dengan nama `create-task` yang menerima parameter `request` dan isinya sebagai berikut.
    2. Buatlah berkas `HTML` baru dengan nama register.html pada folder `create-task/templates`dan mengisi berkas tersebut.
    3. Tambahkan potongan kode di bawah ini setelah end tag table (</table>) pada berkas todolist.html. Potongan kode ini berfungsi untuk menambahkan tombol logout.

    ```shell
    <button><a href="{% url 'todolist:create-task' %}">Add New Task</a></button>
    ```
   4. Jangan lupa untuk jalankan perintah `git add.`lalu `git commit -m <Kalimat sesukamu>` dan `git push origin main` 

### Melakukan Deploy Aplikasi Django ke Heroku

   1. Buat aplikasi Heroku dengan nama yang kamu inginkan
   2. Bukalah konfigurasi repositori GitHub kamu dan bukalah bagian Secrets untuk GitHub Actions (`Settings -> Secrets -> Actions`).
   3. Tambahkan variabel `repository secret` baru untuk melakukan *deployment*. Pasangan Name-Value dari variabel yang akan kamu buat dapat kamu ambil dari informasi yang kamu catat pada file teks sebelumnya. 
   4. Masuk ke aplikasi Heroku yang telah dibuat lalu klik icon Deploy yang tersedia
   5. Scroll down dan klik *connect to Github* untuk menyambungkan aplikasi Heroku dengan Github kamu.\
   6. Klik deploy pada bagian bawah setelah *connect to Github*
   7. Bukalah tab GitHub Actions dan jalankan kembali workflow yang gagal.`


[Heroku]: https://www.heroku.com/
[Visual Studio Code]: https://code.visualstudio.com/
[PyCharm]: https://www.jetbrains.com/pycharm/