# Mock Server

Sebuah aplikasi untuk membuat mockserver dari CSV.

## Persiapan

Siapkan file CSV dan simpan di folder `mock_blueprint`. Contoh file ada di sana. Lalu ganti nama di `config.cfg`.

Ada empat kolom dan contohnya: 
```
path  , method, response                , wait
/hello, GET   , "{""hello"":""world""}" , 0
```

* Pro tips 1: Gunakan google sheets lalu import ke csv untuk awalnya.
* Pro tips 2: Jika menggunakan VS Code, cari extension yang berhubungan dengan CSV. (Saya menggunakan: `janisdd.vscode-edit-csv`)

## Install dan Jalankan

```
pip3 install -r requirements.txt
python3 run.py
```

Lalu buka http://localhost:5000/<PATH yang sudah di define pada CSV>