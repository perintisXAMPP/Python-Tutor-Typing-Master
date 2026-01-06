import json
import os
from datetime import datetime
from utils import Colors, print_header

PROGRESS_FILE = "progress.json"

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {
            "lessons_completed": [],
            "typing_stats": {
                "best_wpm": 0.0,
                "average_accuracy": 0.0,
                "total_sessions": 0
            },
            "last_played": None
        }
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    except:
        return load_progress()

def save_progress(data):
    data["last_played"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def update_lesson_status(lesson_title):
    data = load_progress()
    if lesson_title not in data["lessons_completed"]:
        data["lessons_completed"].append(lesson_title)
        save_progress(data)

def update_typing_stats(wpm, accuracy):
    data = load_progress()
    stats = data["typing_stats"]
    
    # Update Best WPM
    if wpm > stats["best_wpm"]:
        stats["best_wpm"] = wpm
        
    # Update Average Accuracy
    total = stats["total_sessions"]
    current_avg = stats["average_accuracy"]
    new_avg = ((current_avg * total) + accuracy) / (total + 1)
    
    stats["average_accuracy"] = new_avg
    stats["total_sessions"] += 1
    
    save_progress(data)

def display_progress():
    data = load_progress()
    print_header("PROGRES BELAJAR ANDA")
    
    print(f"{Colors.CYAN}Materi Selesai:{Colors.ENDC} {len(data['lessons_completed'])} materi")
    for lesson in data["lessons_completed"]:
        print(f" - {lesson}")
        
    print(f"\n{Colors.CYAN}Statistik Mengetik:{Colors.ENDC}")
    stats = data["typing_stats"]
    print(f" - Best WPM       : {stats['best_wpm']:.2f}")
    print(f" - Rata-rata Akurasi: {stats['average_accuracy']:.2f}%")
    print(f" - Total Sesi     : {stats['total_sessions']}")
    
    if data["last_played"]:
        print(f"\n{Colors.WARNING}Terakhir Belajar: {data['last_played']}{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")
