# Verifikasi lokal — 17 Oktober 2026

- `npm run build`: sukses; menghasilkan beranda dan empat halaman studi kasus statis.
- `npm run check`: sukses; sintaks `app.js` valid.
- `git diff --check`: tidak menemukan kesalahan whitespace.
- Pemeriksaan semua tautan dan aset lokal pada lima halaman HTML: 0 target hilang.
- Keempat URL `/projects/<id>/` merespons HTTP 200. Galeri berisi 3 gambar untuk DevTrack, 2 untuk Stokita, 2 untuk Lumiere, dan 3 untuk Clinic Care; setiap gambar galeri dapat dibuka penuh.
- Chromium: beranda dan DevTrack pada lebar 375, 768, 1024, dan 1440 px tidak memiliki overflow horizontal. Keempat halaman detail pada 375 dan 1440 px juga tidak memiliki overflow horizontal; gambar cover termuat.
- Urutan proyek di beranda: DevTrack, Stokita, Lumiere, Clinic Care. Sembilan teknologi pada strip memiliki logo lokal.
- Tombol Tab pertama memfokuskan skip link dan outline terlihat. Saat `prefers-reduced-motion: reduce`, tombol jeda menunjukkan `aria-pressed=true` dan animasi CSS tidak berjalan.
- Foto pada bagian Tentang, galeri, dan kartu sosial diperiksa secara visual di browser atau dari aset lokal.

Screenshot verifikasi lokal tersimpan di `output/` dan tidak ikut diunggah ke hosting.

## Batasan

Verifikasi visual dilakukan di Chromium, bukan Safari/Firefox atau perangkat fisik. Alur penuh dari tiap demo eksternal tidak diuji; Stokita dan Lumiere hanya dibuka untuk mengambil screenshot fitur yang terlihat. Konten halaman studi kasus disajikan dalam HTML statis dan dapat dibaca tanpa JavaScript, tetapi sesi browser tanpa JavaScript belum diuji terpisah.
