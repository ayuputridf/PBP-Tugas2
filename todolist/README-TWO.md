# Proyek Django PBP - Tugas 6

Nama    : Ayu Putri Dewi Fitriyani
NPM     : 2106654845

* [Link to App ](https://pbp-todolist-ayu.herokuapp.com/todolist/login/)

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

## Cara Implementasi Checklist 

* AJAX GET

 1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON.

```shell
def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

 2. Membuat path /todolist/json yang mengarah ke view yang baru dibuat.
```shell
path('json/', show_json, name='show_json'),
```

 3. Lakukan pengambilan task menggunakan AJAX GET.
 
 * AJAX POST

 1. Membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task. &  view baru untuk menambahkan task baru ke dalam database.

```shell
 def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = ToDoList(
            date=str(date.today()),
            title=title, 
            description=description,
            user=request.user,
        )
        new_task.save()
    return redirect('todolist:show_todolist_ajax')
```
 
 2. Membuat path /todolist/add yang mengarah ke view yang baru dibuat.

```shell
path('add/', add_task, name='add_task'),
```

 3. Menghubungkan form yang telah dibuat di dalam modal ke path /todolist/add

 Tutup modal setelah penambahan task telah berhasil dilakukan.

 4. Membentuk form penambahan Task pada modal dan button Create yang terhubung dengan AJAX
 
 5. Membuat fungsi yang bisa merespons event klik button Create dengan mengambil data dari form dan memanggil fungsi add_task
 
 6. Membuat fungsi fetchData & update untuk melakukan update template dengan GET data dari JSON yang memanfaatkan fungsi show_json

 