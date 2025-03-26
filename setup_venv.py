import os
import sys
import subprocess

def setup_virtualenv():
    """Создает виртуальное окружение и устанавливает зависимости"""
    venv_dir = "venv"

    # Создаем venv, если его нет
    if not os.path.exists(venv_dir):
        print("🔄 Создаем виртуальное окружение...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir])

    # Устанавливаем зависимости
    pip_path = os.path.join(venv_dir, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_dir, "bin", "pip")
    print("📦 Устанавливаем зависимости...")
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])

    print("✅ Окружение настроено! Активируйте его перед работой.")

if __name__ == "__main__":
    setup_virtualenv()
