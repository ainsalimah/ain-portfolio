# Ain — Portofolio Full Stack Developer

Portofolio statis berbahasa Indonesia untuk DevTrack, Stokita, Lumiere, NARA Atelier, dan Clinic Care. HTML, CSS, dan JavaScript native; tidak memakai backend atau database.

## Preview lokal

Dengan Python 3 dan Node.js yang sudah tersedia:

```powershell
npm run build
npm run dev
```

Buka http://127.0.0.1:4173. Tidak perlu menjalankan `npm install`.

## Memperbarui konten

- Edit `projects.json` untuk informasi proyek, urutan, dan galeri studi kasus.
- Edit `template.html` untuk bagian hero, tentang, kemampuan, dan kontak.
- Jalankan `npm run build` untuk menghasilkan ulang `index.html` dan `projects/<id>/index.html`. Jangan mengedit file hasil build langsung.
- `styles.css` menyimpan token warna, responsive layout, dan animasi. `app.js` menambahkan motion serta dukungan tautan lama ke studi kasus.

Seluruh konten dan studi kasus tetap tersedia tanpa JavaScript. Pengaturan reduced motion dihormati; tombol di footer dapat menjeda animasi. Gambar studi kasus dapat dibuka dalam ukuran penuh.

## Sumber

Informasi proyek berdasarkan README dan kode repositori:

- https://github.com/ainsalimah/clinic-care
- https://github.com/ainsalimah/lumiere
- https://github.com/ainsalimah/Stokita
- https://github.com/ainsalimah/devtrac

Screenshot DevTrack dan Clinic Care berasal dari `docs/screenshots` masing-masing repositori. Screenshot tambahan Stokita dan Lumiere diambil dari demo publik pada 17 Oktober 2026; Stokita memakai ruang demo pribadi dengan data fiktif. Preview lama tetap memakai aset yang sudah dijelaskan sebelumnya. Foto Ain berasal dari berkas pribadi yang diberikan pemilik portofolio. Logo teknologi disimpan lokal dari Devicon v2.17.0. Font Manrope disimpan lokal (SIL Open Font License).

Screenshot NARA Atelier diambil dari build lokal proyek pada 22 Oktober 2026. NARA Atelier dan seluruh karya arsitektur di dalamnya merupakan konsep demonstrasi; sumber visual dan lisensinya disimpan pada manifest proyek asal.

## Pemeriksaan

`npm run check` memeriksa sintaks JavaScript. Periksa halaman utama dan lima studi kasus pada ukuran desktop serta ponsel, tautan gambar penuh, keyboard, reduced motion, dan akses tanpa JavaScript.

## GitHub dan Vercel

Repositori: [ainsalimah/ain-portfolio](https://github.com/ainsalimah/ain-portfolio).
Situs: [ain-portfolio-zeta.vercel.app](https://ain-portfolio-zeta.vercel.app/).

Konfigurasi `vercel.json` menyajikan hasil HTML statis tanpa backend, install dependency, atau build di hosting. Sebelum push perubahan konten, jalankan `npm run build` dan `npm run check`, lalu commit halaman utama, kelima halaman detail, aset, dan sumbernya. `.vercelignore` membatasi upload ke file situs dan aset; file sumber dokumentasi serta hasil pengujian lokal tidak ikut disajikan.

Gambar sosial lokal tersedia di `assets/social-card.png`. Canonical, `og:url`, serta URL gambar sosial menggunakan domain situs di atas. Jika domain berubah, perbarui metadata di `template.html` lalu jalankan build.
