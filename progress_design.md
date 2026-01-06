# Desain Modul Progres

## Format Penyimpanan
Data akan disimpan dalam file `progress.json` untuk kemudahan pembacaan dan persistensi.

## Struktur Data
```json
{
    "lessons_completed": [],
    "typing_stats": {
        "best_wpm": 0.0,
        "average_accuracy": 0.0,
        "total_sessions": 0
    },
    "last_played": "YYYY-MM-DD HH:MM:SS"
}
```

## Fungsi Utama
- `load_progress()`: Membaca data dari file JSON.
- `save_progress(data)`: Menyimpan data ke file JSON.
- `update_lesson_status(lesson_title)`: Menandai materi yang sudah selesai.
- `update_typing_stats(wpm, accuracy)`: Memperbarui statistik mengetik.
- `display_progress()`: Menampilkan ringkasan progres di menu utama.
