from utils import clear_screen, print_header, Colors, slow_print, get_input
from lessons import PYTHON_LESSONS
from typing_engine import run_typing_test
from progress_tracker import update_lesson_status, display_progress

def show_lesson(lesson):
    clear_screen()
    print_header(f"MATERI: {lesson['title']}")
    slow_print(lesson['content'])
    
    print(f"\n{Colors.YELLOW}--- KUIS SINGKAT ---{Colors.ENDC}")
    print(lesson['quiz']['question'])
    for opt in lesson['quiz']['options']:
        print(opt)
        
    ans = get_input("\nJawaban Anda (A/B/C): ").upper()
    if ans == lesson['quiz']['answer']:
        print(f"\n{Colors.GREEN}Benar! Anda hebat.{Colors.ENDC}")
        update_lesson_status(lesson['title'])
    else:
        print(f"\n{Colors.FAIL}Salah. Jawaban yang benar adalah {lesson['quiz']['answer']}.{Colors.ENDC}")
    
    input(f"\n{Colors.WARNING}Tekan ENTER untuk lanjut...{Colors.ENDC}")

def main_menu():
    while True:
        clear_screen()
        print_header("PYTHON LEARNING & TYPING MASTER")
        print(f"{Colors.BLUE}Selamat datang! Pilih menu untuk memulai:{Colors.ENDC}")
        print("1. Belajar Dasar Python (Materi & Kuis)")
        print("2. Latihan Mengetik (Sintaks Python)")
        print("3. Lihat Progres Belajar")
        print("4. Tentang Program")
        print("5. Keluar")
        
        choice = get_input("\nPilihan Anda (1-5): ")
        
        if choice == '1':
            for lesson in PYTHON_LESSONS:
                show_lesson(lesson)
        elif choice == '2':
            run_typing_test()
        elif choice == '3':
            display_progress()
        elif choice == '4':
            clear_screen()
            print_header("TENTANG PROGRAM")
            print("Program ini dirancang untuk membantu pemula")
            print("menguasai dasar Python sambil melatih kecepatan mengetik.")
            print("Dibuat dengan cinta oleh Manus.")
            input(f"\n{Colors.WARNING}Tekan ENTER untuk kembali...{Colors.ENDC}")
        elif choice == '5':
            print(f"\n{Colors.GREEN}Terima kasih telah belajar! Sampai jumpa.{Colors.ENDC}")
            break
        else:
            print(f"\n{Colors.FAIL}Pilihan tidak valid!{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    import time
    main_menu()
