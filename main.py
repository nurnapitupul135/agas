
import subprocess
import shutil
import os

def main():
    print("=== NVIDIA GPU CHECK ===")

    # Periksa apakah nvidia-smi tersedia
    nvidia_smi = shutil.which("nvidia-smi")

    if not nvidia_smi:
        print("nvidia-smi tidak ditemukan.")
        print("Pastikan environment Vita Serverless")
        print("memiliki GPU NVIDIA dan driver NVIDIA.")
        return

    # Jalankan pemeriksaan GPU
    commands = [
        [nvidia_smi],
        [nvidia_smi, "-L"],
        [
            nvidia_smi,
            "--query-gpu=name,driver_version,memory.total,memory.free,utilization.gpu",
            "--format=csv"
        ]
    ]

    for command in commands:
        print("\n$", " ".join(command))
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=30
            )
            print(result.stdout or result.stderr)
            print("Exit code:", result.returncode)
        except subprocess.TimeoutExpired:
            print("Perintah timeout.")

    print("\n=== SELESAI ===")

if __name__ == "__main__":
    main()
