import subprocess
import shutil
import sys
import time
import os

# Paksa output Python langsung muncul di log
os.environ["PYTHONUNBUFFERED"] = "1"

def log(message):
    print(message, flush=True)

def main():
    log("=== VITA SERVERLESS STARTED ===")
    log("Python: " + sys.version)

    nvidia_smi = shutil.which("nvidia-smi")

    if nvidia_smi is None:
        log("ERROR: nvidia-smi tidak ditemukan")
        log("Periksa image dan konfigurasi GPU.")
        return

    log("nvidia-smi ditemukan: " + nvidia_smi)
    log("Menjalankan pemeriksaan GPU...")

    try:
        result = subprocess.run(
            [nvidia_smi],
            capture_output=True,
            text=True,
            timeout=60
        )

        log(result.stdout)

        if result.stderr:
            log("STDERR: " + result.stderr)

        log("Exit code: " + str(result.returncode))

    except Exception as e:
        log("ERROR: " + repr(e))

    log("=== SCRIPT SELESAI ===")

if __name__ == "__main__":
    main()
