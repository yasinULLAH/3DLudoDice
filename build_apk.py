import os
import sys
import shutil
import subprocess

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ANDROID_DIR = os.path.join(PROJECT_DIR, "android_project")
ASSETS_WWW_DIR = os.path.join(ANDROID_DIR, "app", "src", "main", "assets", "www")
OUTPUT_APK_SRC = os.path.join(ANDROID_DIR, "app", "build", "outputs", "apk", "release", "app-release.apk")
OUTPUT_APK_DEST = os.path.join(PROJECT_DIR, "3DLudoDice.apk")

EXCLUDED_NAMES = {
    "android_project",
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    "3DLudoDice.apk",
}

EXCLUDED_EXTENSIONS = {
    ".py",
    ".pyw",
    ".apk",
}

def sync_assets():
    print("Syncing assets to Android project...")
    if os.path.exists(ASSETS_WWW_DIR):
        shutil.rmtree(ASSETS_WWW_DIR)
    os.makedirs(ASSETS_WWW_DIR, exist_ok=True)

    for item in os.listdir(PROJECT_DIR):
        if item in EXCLUDED_NAMES:
            continue
        _, ext = os.path.splitext(item)
        if ext.lower() in EXCLUDED_EXTENSIONS:
            continue

        src_path = os.path.join(PROJECT_DIR, item)
        dest_path = os.path.join(ASSETS_WWW_DIR, item)

        if os.path.isdir(src_path):
            shutil.copytree(
                src_path,
                dest_path,
                ignore=lambda d, files: [f for f in files if f in EXCLUDED_NAMES or os.path.splitext(f)[1].lower() in EXCLUDED_EXTENSIONS]
            )
        else:
            shutil.copy2(src_path, dest_path)
    print("Assets synchronized successfully.")

def build_apk():
    print("Running Gradle build (assembleRelease)...")
    gradlew_cmd = os.path.join(ANDROID_DIR, "gradlew.bat") if sys.platform == "win32" else os.path.join(ANDROID_DIR, "gradlew")
    
    if not os.path.exists(gradlew_cmd):
        print(f"Error: Gradle wrapper not found at {gradlew_cmd}")
        return False

    result = subprocess.run([gradlew_cmd, "assembleRelease"], cwd=ANDROID_DIR)
    if result.returncode != 0:
        print(f"Gradle build failed with exit code {result.returncode}")
        return False

    if os.path.exists(OUTPUT_APK_SRC):
        shutil.copy2(OUTPUT_APK_SRC, OUTPUT_APK_DEST)
        size_mb = os.path.getsize(OUTPUT_APK_DEST) / (1024 * 1024)
        print("========================================")
        print("BUILD SUCCESSFUL!")
        print(f"APK created at: {OUTPUT_APK_DEST}")
        print(f"APK Size: {size_mb:.2f} MB")
        print("========================================")
        return True
    else:
        print(f"Error: Generated APK not found at {OUTPUT_APK_SRC}")
        return False

if __name__ == "__main__":
    sync_assets()
    success = build_apk()
    if not success:
        sys.exit(1)

