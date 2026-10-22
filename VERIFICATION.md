# Verifikasi lokal — 22 Oktober 2026

- `npm run build`: sukses; menghasilkan beranda dan lima halaman studi kasus statis.
- `npm run check`: sukses; sintaks `app.js` valid.
- `git diff --check`: tidak menemukan kesalahan whitespace.
- Kelima URL `/projects/<id>/` merespons HTTP 200 dari server lokal.
- Chromium: kartu NARA Atelier tampil sebagai proyek 04 dari 05; halaman studi kasus dan galeri dapat dibuka tanpa error console pada desktop 1280 px dan mobile 360 px.
- Urutan proyek di beranda: DevTrack, Stokita, Lumiere, NARA Atelier, Clinic Care.
- Halaman NARA memiliki heading berurutan, teks alternatif pada seluruh gambar, navigasi kembali, serta tautan ke proyek berikutnya.
- Screenshot beranda NARA, case study proyek, tampilan mobile, dan kartu sosial diperiksa secara visual.

Screenshot verifikasi lokal tersimpan di `output/` dan tidak ikut diunggah ke hosting.

## Batasan

Verifikasi visual dilakukan di Chromium, bukan Safari/Firefox atau perangkat fisik. Alur penuh dari tiap demo eksternal tidak diuji. Preview NARA di Vercel masih memakai Deployment Protection sehingga pengunjung publik memerlukan akses Vercel sampai deployment produksi dipublikasikan. Konten halaman studi kasus disajikan dalam HTML statis dan dapat dibaca tanpa JavaScript, tetapi sesi browser tanpa JavaScript belum diuji terpisah.
