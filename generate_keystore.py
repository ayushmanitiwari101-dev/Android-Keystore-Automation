import subprocess

def create_keystore():
    print("--- Android Debug Keystore Generator ---")
    
    keystore_name = input("Enter keystore filename (default: cyber_sec.jks): ") or "cyber_sec.jks"
    alias_name = input("Enter key alias (default: cyberalias): ") or "cyberalias"
    validity_days = input("Enter validity in days (default: 365): ") or "365"
    
    cmd = [
        "keytool", "-genkeypair", "-v",
        "-keystore", keystore_name,
        "-alias", alias_name,
        "-keyalg", "RSA",
        "-keysize", "2048",
        "-validity", validity_days
    ]
    
    print(f"\nGenerating keystore '{keystore_name}'...")
    try:
        subprocess.run(cmd, check=True)
        print(f"\n[Success] Keystore '{keystore_name}' generated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\n[Error] Failed to generate keystore: {e}")
    except FileNotFoundError:
        print("\n[Error] 'keytool' not found. Make sure OpenJDK is installed.")

if __name__ == "__main__":
    create_keystore()
