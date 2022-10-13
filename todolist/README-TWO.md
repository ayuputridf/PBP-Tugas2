# Proyek Django PBP - Tugas 6

Nama    : Ayu Putri Dewi Fitriyani
NPM     : 2106654845

[Link to App (login)](https://pbp-todolist-ayu.herokuapp.com/todolist/login/)
[Link to App (register)](https://pbp-todolist-ayu.herokuapp.com/todolist/login/)
[Link to App (create-task)](https://pbp-todolist-ayu.herokuapp.com/todolist/register/create-task/)
[Link to App (logout)](https://pbp-todolist-ayu.herokuapp.com/todolist/logout/)


## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

* Asynchronous Programming
- Asynchronous programming sering digunakan. Jadi proses jalannya program secara bersamaan & gaharus nunggu proses antrian
- Code yg ditulis akan dieksekusi di belakang main thrad & gaakan membloking proses runtime/ nunggu hingga proses selesai => nah sambil nunggu, compiler bakal eksekusi perintah code selanjutnya
- Ada untuk hampir semua programming language kecuali PHP
-  pendekatan pemrograman yang tidak terikat pada input output (I/O)  protocol.
- melakukan pekerjaannya tanpa harus terikat dengan proses lain

* Synchronous Programming
- Synchronous programming sama saja kita membuat code yang dijalankan secara berurut/ sequential (ada berdasarkan antrian eksekusi program)
- Ada di programming language PHP
- memiliki pendekatan yang lebih old style
- Task akan dieksekusi satu persatu sesuai dengan urutan dan prioritas task.
Kekurangan : lama waktu eksekusi (harus nunggu task lain selesai), gabisa buat workload yg berat, jadi deri segi ux kurang baik

##  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

1. Penerapan paradigma Event-Driven Programming
 paradigma Event-Driven Programming merupakan : paradigma programming yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan output atau tindakan pengguna / bisa berupa pesan dari program lainnya.

2. Contoh penerapan pada tugas 


## Penerapan asynchronous programming pada AJAX

* AJAX sendiri berasal dari kata Asynchronous JavaScript and XMLHTTP (salah satu konsep yg menerapkan asynchronous programming)

* Fungsi AJAX : utk melakukan request data & handling response -> response dlm btk XML, Javascript, ataupun JSON dari sebuah Rest API

* Jadi ketika menerapkan AJAX, ada bnyk metode yg bisa dipakai salah satunya : XHR (XMLHTTPRequest), JQuery, Fetch
Untuk contoh penerapannya bisa dilihat dari source berikut : [Contoh Penerapan](https://www.dicoding.com/blog/mengenal-fungsi-asynchronous-request-pada-javascript/)  

## Cara Implementasi
