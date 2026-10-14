# Ain — Portofolio Full Stack Developer

Portofolio statis berbahasa Indonesia untuk DevTrack, Stokita, dan Lumiere. HTML, CSS, dan JavaScript native; tidak memakai backend atau database.

## Preview lokal

Dengan Python 3 dan Node.js yang sudah tersedia:

```powershell
npm run build
npm run dev
```

Buka http://127.0.0.1:4173. Tidak perlu menjalankan `npm install`.

## Memperbarui konten

- Edit `projects.json` untuk informasi proyek dan studi kasus.
- Edit `template.html` untuk bagian hero, tentang, kemampuan, dan kontak.
- Jalankan `npm run build` untuk menghasilkan ulang `index.html`. Jangan mengedit konten proyek langsung di file hasil build.
- `styles.css` menyimpan token warna, responsive layout, dan animasi. `app.js` menambahkan motion serta deep link studi kasus.

Seluruh konten dan studi kasus tetap tersedia tanpa JavaScript. Pengaturan reduced motion dihormati; tombol di footer dapat menjeda animasi.

## Sumber

Informasi proyek berdasarkan README dan kode repositori:

- https://github.com/ainsalimah/devtrac
- https://github.com/ainsalimah/Stokita
- https://github.com/ainsalimah/lumiere

Screenshot DevTrack berasal dari `docs/screenshots/board.png` di repositori DevTrack dengan data demo fiktif. Stokita diambil dari halaman demo publik pada 11 Oktober 2026 tanpa membuat data baru. Preview Lumiere memakai halaman demo publik dengan gambar hero `public/images/hero/hero_1.png` dari repositori: URL gambar asli `/images/about/about-1.jpg` tidak tersedia, sehingga permintaan gambar tersebut diganti hanya di browser pengambilan screenshot. Preview ini diberi label aset repositori; deployment aslinya tidak diubah. Font Manrope disimpan lokal (SIL Open Font License).

## Pemeriksaan

`npm run check` memeriksa sintaks JavaScript. Pemeriksaan browser mencakup ukuran 375, 768, 1024, dan 1440 piksel, studi kasus, keyboard, reduced motion, dan akses tanpa JavaScript.

## GitHub dan Vercel

Repositori: [ainsalimah/ain-portfolio](https://github.com/ainsalimah/ain-portfolio).
Situs: [ain-portfolio-zeta.vercel.app](https://ain-portfolio-zeta.vercel.app/).

Konfigurasi `vercel.json` menyajikan hasil HTML statis tanpa backend, install dependency, atau build di hosting. Sebelum push perubahan konten, jalankan `npm run build` dan `npm run check`, lalu commit `index.html` beserta sumbernya. `.vercelignore` membatasi upload ke file situs dan aset; file sumber dokumentasi serta hasil pengujian lokal tidak ikut disajikan.

Gambar sosial lokal tersedia di `assets/social-card.png`. Canonical, `og:url`, serta URL gambar sosial menggunakan domain situs di atas. Jika domain berubah, perbarui metadata di `template.html` lalu jalankan build.
