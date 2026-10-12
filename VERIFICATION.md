# Verifikasi lokal — 11 Oktober 2026

- `npm run build`: sukses, tiga proyek dirender ke HTML statis.
- `npm run check`: sukses, sintaks JavaScript valid.
- Preview `http://127.0.0.1:4173`: HTTP 200.
- Browser Chromium: lebar 375, 768, 1024, dan 1440 px tidak memiliki overflow horizontal; seluruh screenshot termuat.
- Ketiga studi kasus dibuka dan ditutup dengan Enter melalui fokus keyboard. Setiap studi kasus memiliki masalah, alur, keputusan teknis, dan batasan.
- Deep link `?studi=stokita` membuka detail Stokita.
- Skip link menjadi elemen pertama saat Tab, dengan outline terlihat.
- Reduced motion: CSS animation `none`, tidak ada animasi berjalan. Tombol jeda mengubah `aria-pressed` menjadi `true`.
- JavaScript dinonaktifkan: tiga proyek tetap tersedia dan detail Lumiere tetap bisa dibuka dengan kontrol native.
- Konteks browser baru: tidak ada page error atau console warning; font Manrope dan tiga gambar termuat.
- Tiga URL demo dan tiga URL repositori merespons HTTP 200. Tautan email memakai `mailto:nurainsalimah1@gmail.com`; pengiriman email tidak dilakukan.
- Kontras token ivory, bronze, dan muted pada charcoal berturut-turut 15,91:1, 7,12:1, dan 7,45:1.
- Screenshot teroptimasi total sekitar 227 KB. Font dan semua aset yang dipakai halaman disimpan lokal.

Screenshot hasil browser tersedia di `output/playwright/desktop.png`, `mobile.png`, dan `full-desktop.png`.

## Batasan

Pengujian dilakukan pada Chromium, bukan Safari/Firefox atau perangkat fisik. Respons HTTP 200 pada demo tidak menjamin seluruh fitur aplikasi demo berfungsi; tidak ada transaksi atau data demo yang dibuat saat verifikasi. Preview Lumiere menggunakan gambar hero dari Git LFS repositorinya karena URL gambar halaman publik tidak tersedia; rincian tercatat pada README. Metadata URL absolut untuk berbagi sosial menunggu alamat deployment.
