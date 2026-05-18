import base64
import os
import subprocess

def decode_and_run():
    # Путь к файлу bs64.txt в той же папке, что и скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "bs64.txt")
    exe_path = os.path.join(script_dir, "decoded_program.exe")
    
    try:
        # Проверка существования файла
        if not os.path.exists(input_file):
            print(f"[-] Ошибка: Файл '{input_file}' не найден!")
            print(f"    Убедитесь, что файл bs64.txt находится в папке: {script_dir}")
            return
        
        # Чтение Base64 из файла
        with open(input_file, 'r', encoding='utf-8') as f:
            base64_content = f.read().strip()
        
        if not base64_content:
            print("[-] Ошибка: Файл bs64.txt пуст!")
            return
        
        print(f"[+] Файл bs64.txt найден. Размер: {len(base64_content)} символов")
        
        # Декодирование Base64
        print("[+] Декодирование Base64...")
        exe_data = base64.b64decode(base64_content)
        
        print(f"[+] Размер декодированных данных: {len(exe_data)} байт")
        
        # Запись в exe-файл
        with open(exe_path, 'wb') as exe_file:
            exe_file.write(exe_data)
        
        print(f"[+] Файл сохранён как: {exe_path}")
        
        # Запуск exe-файла
        print("[+] Запуск программы...")
        subprocess.run([exe_path], check=True)
        print("[+] Программа завершила работу")
        
    except base64.binascii.Error as e:
        print(f"[-] Ошибка декодирования Base64: {e}")
        print("    Проверьте, что файл содержит корректные данные Base64")
    except PermissionError:
        print("[-] Ошибка: Нет прав на запись или выполнение файла")
        print("    Попробуйте запустить программу от имени администратора")
    except subprocess.CalledProcessError as e:
        print(f"[-] Ошибка при запуске exe-файла: {e}")
    except Exception as e:
        print(f"[-] Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    decode_and_run()