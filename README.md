# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

Link Aplikasi Heroku =  `https://pbp-tugas2-ayu.herokuapp.com/katalog/`

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, diharapkan untuk dapat:

1. Mengerti bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya.
2. Mengetahui pentingnya *virtual environment* dalam membuat aplikasi *web* berbasis Django
3. Memahami cara buat sebuah fungsi pada `views.py` yang dapat melakukan pengambilan data dari *model* dan dikembalikan ke dalam sebuah HTML.
4. Membuat sebuah *routing* untuk memetakan fungsi yang telah kamu buat pada` views.py`.
5. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
6. Melakukan *deployment* aplikasi Django pada Heroku.

## Bagan Request Client ke Web Aplikasi Berbasis Django Beserta Responnya

![image.png](Gambar/Request.png)

`urls.py`     : Merupakan deklarasi URL* untuk project Django; Berisi konfigurasi URL pada project yang kita buat.

`views.py`    : Berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk

`models.py`   : Lebih difokuskan sebagai objek yang mendefinisikan entitas pada database beserta konfigurasinya

`berkas html` : Nantinya akan berisi pemetaan yang sudah didefinisikan sebelum akhirnya dikembalikan ke user sebagai response

###### Kaitan antara 4 file tersebut yaitu pada alur permintaan diproses Django :
   1. Permintaan yang masuk ke dalam *server* Django akan diproses melalui `urls` untuk diteruskan ke `view`s yang didefinisikan oleh pengembang untuk memproses permintaan tersebut.

   2. Apabila terdapat proses yang membutuhkan keterlibatan *database*, maka nantinya `views` akan memanggil *query* ke `models` dan *database* akan mengembalikan hasil dari query tersebut ke `views`

   3. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke pengguna sebagai *respons*.


## Pentingnya Virtual Environment

Suatu program apabila dijalankan dalam Virtual Environment, maka punya modul-modulnya sendiri yang program dari luar tidak dapat mengaksesnya. Dengan kata lain, Virtual Environment merupakan sebuah alat yang digunakan untuk membuat lingkungan python virtual yang tidak bisa diakses dari dunia luar atau terisolasi. 

###### Alasan mengapa kita butuh *virtual environment*

1. Agar masing-masing aplikasi punya modulnya sendiri 
2. Bisa spesifikasikan ingin memakai Django versi yang mana

Hal ini bermanfaat bila kita membuat proyek aplikasi menggunakan django 1.1 maka aplikasi tersebut akan berjalan sempurna menggunakan versi 1.1, namun jika kemudian hari rilis django versi terbaru maka harus melakukan upgrade modul. 

Tapi faktanya aplikasi yang sudah dibuat tidak berjalan dengan modul versi terbaru karena banyak perubahan fungsi dan ada juga proyek aplikasi lain yang diharuskan pakai modul versi terbaru tsb. Maka dibutuhkan virtual environment

###### Hal yang terjadi bila tidak mengaktifkan *virtual environment*

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun resikonya yaitu apabila kita mengupdate Django dan ternyata project yang kita buat tidak mensupport Django terbaru maka project kita bisa error.

   
## Tutorial: Implementasi Views Dasar

#### Membuat fungsi pada `views.py` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML

   1. Buka `views.py` yang ada pada folder `katalog` dan buatlah fungsi yang menerima parameter    `request` dan mengembalikan `render(request, "katalog.html")`. Contohnya adalah :

      ```shell
      def show_katalog(request):
         return render(request, "katalog.html")
      ```
   2. Buatlah folder bernama `templates` di dalam folder aplikasi `katalog` dan buatlah sebuah berkas bernama `katalog.html`. Isi dari `katalog.html` dapat diisi oleh *template* berikut.

      ```shell
      {% extends 'base.html' %}

      {% block content %}
      <h5>Nama: </h5>
      <p>Fill me!</p>

      <table>
         <tr>
         <th>Nama Barang</th>
         <th>Harga Barang</th>
         <th>Deskripsi</th>
         </tr>
         {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
      </table>

      {% endblock content %}
      ```

#### Membuat routing untuk memetakan fungsi yang telah dibuat pada `views.py`.
   
   1. Buatlah berkas di dalam folder aplikasi `katalog` bernama `urls.py` untuk melakukan *routing* terhadap fungsi `views` yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat *browser*-mu. Isi dari `urls.py` tersebut adalah sebagai berikut.

      ```shell
      from django.urls import path
      from katalog.views import show_katalog

      app_name = 'katalog'

      urlpatterns = [
         path('', show_katalog, name='show_katalog'),
      ]
      ```

   2. Daftarkan juga aplikasi `katalog` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`.

      ```shell
      path('katalog/', include('katalog.urls')),
      ```

   3. Jalankan proyek Django-mu dengan `perintah python manage.py runserver` dan bukalah `http://localhost:8000/katalog/` di browser untuk melihat halaman yang sudah dibuat.

## Tutorial: Menghubungkan Models dengan Views dan Template

#### Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

   1. Pada fungsi *views* yang telah dibuat, import *models* yang sudah dibuat sebelumnya ke dalam file `views.py`. Kamu akan menggunakan *class* tersebut untuk melakukan pengambilan data dari *database*. Contohnya yaitu :

      ```shell
      from django.shortcuts import render
      from katalog.models import CatalogItem
      ```   

   2. Tambahkan potongan kode di bawah ini ke dalam fungsi `show_katalog` yang dibuat sebelumnya. Potongan kode ini berfungsi untuk memanggil fungsi *query* ke *model database* dan menyimpan hasil *query* tersebut ke dalam sebuah variabel.

      *Variable Kak Cinoy dapat kamu ganti sesuai nama yang diinginkan*

      ```shell
      data_barang_katalog = CatalogItem.objects.all()
      context = {
         'list_barang': data_barang_katalog,
         'nama': 'Kak Cinoy'
      }
      ```   

   3. Tambahkan `context` sebagai parameter ketiga pada pengembalian fungsi *render* di fungsi yang sudah kamu buat sebelumnya. Data yang ada pada variabel `context` tersebut akan ikut di-*render* oleh Django sehingga nantinya kamu dapat memunculkan data tersebut pada halaman HTML.
   
      ```shell
      return render(request, "katalog.html", context)
      ```   

 Untuk melakukan mapping tersebut, dapat menggunakan sintaks khusus template yang ada pada Django, yaitu `{{data}}`. 

   1. Bukalah file HTML yang sudah dibuat sebelumnya pada folder *templates* yang ada di dalam direktori katalog.

   2. `Ubah Fill me!` yang ada di dalam HTML tag `<p>` menjadi `{{nama}}` untuk menampilkan nama kamu di halaman HTML. Contohnya yaitu :

      ```shell
      <h5>Nama: </h5>
      <b>{{nama}}</b>
      ```   

   3. Untuk menampilkan daftar barang ke dalam tabel, kamu perlu melakukan iterasi terhadap variabel `list_barang` yang telah kamu ikut *render* ke dalam HTML. Perhatikan bahwa kamu tidak dapat memanggil daftar barang tersebut secara langsung seperti yang kamu lakukan pada langkah 2 sebab variabel `list_barang` merupakan sebuah kontainer yang berisikan objek. Kamu juga perlu memanggil nama variabel/atribut spesifik dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut. Contohny yaitu :

   ```shell
   {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
   {% for barang in list_barang %}
      <tr>
         <th>{{barang.nama_barang}}</th>
         <th>{{barang.harga_barang}}</th>
         <th>{{barang.deskripsi}}</th>
      </tr>
   {% endfor %}
   ```

Sekarang, cobalah untuk *refresh* halaman tersebut, Apabila sudah muncul perubahannya maka selamat! Kamu telah berhasil menyambungkan `models` dengan `views` dan `template` sekaligus mempelajari dasar dari sintaks *template* dari Django.

Selanjutnya, silakan lakukan `add`, `commit`, dan `push` perubahan yang sudah kamu lakukan untuk menyimpannya ke dalam repositori GitHub.


## Tutorial: Melakukan Deploy Aplikasi Django ke Heroku

#### Melakukan *deployment* ke Heroku terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

   1. Buat aplikasi Heroku dengan nama yang kamu inginkan

   2. Bukalah konfigurasi repositori GitHub kamu dan bukalah bagian Secrets untuk GitHub Actions (`Settings -> Secrets -> Actions`).
   
   3. Tambahkan variabel `repository secret` baru untuk melakukan *deployment*. Pasangan Name-Value dari variabel yang akan kamu buat dapat kamu ambil dari informasi yang kamu catat pada file teks sebelumnya. Contohnya adalah sebagai berikut.

   ```shell
   (NAME)HEROKU_APP_NAME
   (VALUE)APLIKASI-SAYA
   ```
   4. Masuk ke aplikasi Heroku yang telah dibuat lalu klik icon Deploy yang tersedia

   5. Scroll down dan klik *connect to Github* untuk menyambungkan aplikasi Heroku dengan Github kamu.\

   6. Klik deploy pada bagian bawah setelah *connect to Github*

   7. Bukalah tab GitHub Actions dan jalankan kembali workflow yang gagal.

Setelah workflow kamu jalankan kembali dan status deployment menjadi sukses (dapat kamu lihat terdapat simbol centang hijau pada repositori kamu), kamu dapat mengakses aplikasi milikmu di https://<nama-aplikasi-heroku>.herokuapp.com. Selamat! Sekarang aplikasi Django milikmu dapat diakses di Internet.

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage).

[Heroku]: https://www.heroku.com/
[Visual Studio Code]: https://code.visualstudio.com/
[PyCharm]: https://www.jetbrains.com/pycharm/