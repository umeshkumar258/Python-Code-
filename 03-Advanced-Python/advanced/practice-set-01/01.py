files = ["9.txt", "0.txt", "6.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"\n📄 Reading {file}:")
            print(f.read())
    except FileNotFoundError:
        print(f"❌ {file} not found")
    except Exception as e:
        print(f"⚠ Error in {file}: {e}")

print("\n🙏 Thanks")
