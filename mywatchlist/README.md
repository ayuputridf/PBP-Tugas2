# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

[Link to HTML](https://pbp-tugas3-ayu.herokuapp.com/mywatchlist/html/) ,
[Link to JSON](https://pbp-tugas3-ayu.herokuapp.com/mywatchlist/json/) ,
[Link to XML](https://pbp-tugas3-ayu.herokuapp.com/mywatchlist/xml/) ,


## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, diharapkan untuk dapat:

1. Mengerti perbedaan antara JSON, XML, dan HTML.
2. Mengetahui pentingnya memerlukan data delivery dalam pengimplementasian sebuah platform.
3. Mengetahui cara mengimplementasikan :
   - Pembuatan aplikasi baru yaitu mywatchlist di proyek Django Tugas 2
   - Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
   - Membuat sebuah model MyWatchList yang memiliki atribut 
   - Menambahkan minimal 10 data untuk objek MyWatchList
   - Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format HTML, XML, JSON
   - Membuat routing sehingga data di atas dapat diakses melalui URL
   - Melakukan deployment ke Heroku


## Perbedaan antara JSON, XML, dan HTML.


`JSON`   : JSON merupakan format yang digunakan untuk menyimpan, membaca, dan menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Biasanya, file JSON berisikan teks dan file berekstensi .json. 
    - Json menyimpan elemen secara efisien tapi tidak rapi jika diliat
    - Digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet

`XML`    : bahasa markup untuk menyederhanakan proses penyimpanan dan pengiriman data antarserver.
    - XML menyimpan elemen secara terstruktur mudah dibaca manusia dan mesin, tapi kurang efisien
    -Punya data yang lebih terstruktur dan user dapat menggunakannya untuk menambahkan catatan


`HTML`   : Kode HTML memastikan format teks dan gambar yang tepat untuk browser Internet. Tanpa HTML, browser tidak akan tahu bagaimana menampilkan teks sebagai elemen atau memuat gambar atau elemen lainnya. Terdapa perbedaan tag dengan JSON & XML 

## Keperluan Data Delivery dalam Pengimplementasian sebuah Platform

Data Delivery diperlukan untuk mempermudah proses pengiriman data dari satu stack ke stack yang lainnya ketika mengimplenemtasikan platform. Contoh beberapa datanya yaitu HTML, JSON, XML.  

## Tutorial: Menyalakan Virtual Environment

1. Membuka directory yang dimau pada cmd 
2. Menjalankan perintah berikut pada cmd. `python -m venv env` 
3. Menyalakan virtual env dengan `env\Scripts\activate.bat`
4. Install dependencies yang diperlukan untuk menjalankan proyek Django dengan `pip install -r requirements.txt`

## Tutorial: Membuat Aplikasi Django MyWatchList & Konfigurasi Model

   1. Jalankan perintah `python manage.py startapp wishlist` pada cmd yang masih dibuka
   2. Buka `settings.py` di folder `project_django` dan tambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang sudah  dibuat ke dalam proyek Django-mu. 
   3. Buka file `models.py` yang ada di folder `mywatchlist` dan tambahkan class model yang diinginkan.
   4. Lakukan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
   5. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
   6. Buatlah sebuah folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `initial_wishlist_data.json` yang berisi kode isi dari model yang ingin ditampilkan.
   7. Jalankan perintah python `manage.py loaddata initial_wishlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.   


## Tutorial : Implementasi Views Dasar

   1. Buka `views.py` yang ada pada folder `mywatchlist` dan buatlah fungsi yang menerima parameter    `request` dan mengembalikan `render(request, "mywatchlist.html")`. Contohnya adalah :
      ```shell
      def show_mywatchlist(request):
         return render(request, "mywatchlist.html")
      ```
   2. Buatlah folder bernama `templates` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `mywatchlist.html`. Isi dari `mywatchlist.html` dapat diisi oleh *template* berikut.
      ```shell
      {% extends 'base.html' %}

      {% block content %}
      <h5>Nama: </h5>
      <p>Fill me!</p>

      <tr>
         <th>Movie Watched?</th>
         <th>Movie Title</th>
         <th>Rating</th>
         <th>Release Date</th>
         <th>Review</th>
      </tr>
         {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
      </table>

      {% endblock content %}
      ```

#### Membuat routing untuk memetakan fungsi yang telah dibuat pada `views.py`.
   
   1. Buatlah berkas di dalam folder aplikasi `mywatchlist` bernama `urls.py` untuk melakukan *routing* terhadap fungsi `views` yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat *browser*-mu. Isi dari `urls.py` tersebut adalah sebagai berikut.

      ```shell
      from django.urls import path
      from mywatchlist.views import show_mywatchlist

      app_name = 'mywatchlist'

      urlpatterns = [
         path('', show_mywatchlist, name='show_mywatchlist'),
      ]
      ```

   2. Daftarkan juga aplikasi `mywatchlist` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`.

      ```shell
      path('mywatchlist/', include('mywatchlist.urls')),
      ```

   3. Jalankan proyek Django-mu dengan `perintah python manage.py runserver` dan bukalah `http://localhost:8000/mywatchlist/` di browser untuk melihat halaman yang sudah dibuat.

## Tutorial: Menghubungkan Models dengan Views dan Template

   1. Pada fungsi *views* yang telah dibuat, import *models* yang sudah dibuat sebelumnya ke dalam file `views.py`. Kamu akan menggunakan *class* tersebut untuk melakukan pengambilan data dari *database*. Contohnya yaitu :

      ```shell
      from django.shortcuts import render
      from mywatchlist.models import MyWatchList
      ```   
   2. Tambahkan potongan kode di bawah ini ke dalam fungsi `show_mywatchlist` yang dibuat sebelumnya. Potongan kode ini berfungsi untuk memanggil fungsi *query* ke *model database* dan menyimpan hasil *query* tersebut ke dalam sebuah variabel.
      ```shell
      data_movie = MyWatchList.objects.all()
      context = {
         'list_movie': data_movie,
         'nama': 'Ayu Putri Dewi Fitriyani',
         'id' : '2106654845'
      }
      ```   
   3. Tambahkan `context` sebagai parameter ketiga pada pengembalian fungsi *render* di fungsi yang sudah kamu buat sebelumnya. Data yang ada pada variabel `context` tersebut akan ikut di-*render* oleh Django sehingga nantinya kamu dapat memunculkan data tersebut pada halaman HTML.
   
      ```shell
      return render(request, "mywatchlist.html", context)
      ```   
   3. Untuk menampilkan daftar movie ke dalam tabel, kamu perlu melakukan iterasi terhadap variabel `list_movie` yang telah kamu ikut *render* ke dalam HTML. Perhatikan bahwa kamu tidak dapat memanggil daftar movie tersebut secara langsung seperti yang kamu lakukan pada langkah 2 sebab variabel `list_movie` merupakan sebuah kontainer yang berisikan objek. Kamu juga perlu memanggil nama variabel/atribut spesifik dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut. Contohny yaitu :

   ```shell
         <tr>
            <th>{{movie.watched}}</th>
            <th>{{movie.title}}</th>
            <th>{{movie.rating}}</th>
            <th>{{movie.release_date}}</th>
            <th>{{movie.review}}</th>
            </th>
         </tr>
      {% endfor %}
      </table>
      {% endfor %}
   ```
## Tutorial: Mengembalikan Data dalam Bentuk XML dan JSON

   1. Membuat fungsi `show_mywatchlist_xml(request)` pada `views.py` untuk melakukan pengembalian data dalam bentuk `XML`
   2. Membuat fungsi `show_mywatchlist_json(request)` pada `views.py` untuk melakukan pengembalian data dalam bentuk `JSON`
   3. Melakukan routing terhadap fungsi `show_mywatchlist_xml(request)`, dan `show_mywatchlist_json(request)` pada `views.py` dengan memanggil method `path()`

## Tutorial: Melakukan Deploy Aplikasi Django ke Heroku

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

## Tutorial: Menambah Unit Test pada `tests.py` untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon `HTTP 200 OK`

   1. Membuat Unit Test
   2. Membuat berkas `tests.py`
   3. Mengimport TestCase
   4. Membentuk class baru yang merupakan anak kelas dari TestCase
   5. Membuat fungsi untuk mengecek apakah URL `html`, `xml`, dan `json` yang telah dibuat mengembalikan respon `HTTP 200` atau tidak
   6. Melakukan testing dengan perintah `python manage.py test`
   7. Jangan lupa untuk jalankan perintah `git add.`lalu `git commit -m <Kalimat sesukamu>` dan `git push origin main` 


## Postman
![image.jpg](/mywatchlist/assets_postman/POSTMAN_html.jpg)
![image.jpg](/mywatchlist/assets_postman/POSTMAN_json.jpg)
![image.jpg](/mywatchlist/assets_postman/POSTMAN_xml.jpg)

[Heroku]: https://www.heroku.com/
[Visual Studio Code]: https://code.visualstudio.com/
[PyCharm]: https://www.jetbrains.com/pycharm/