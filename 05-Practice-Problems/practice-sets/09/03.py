from pathlib import Path

OUTPUT_DIR = Path("tables")
TABLE_RANGE = range(2, 21)


def generate_table(number):
    """Return multiplication table as a string."""
    
    return "\n".join(
        f"{number} x {i} = {number * i}"
        for i in TABLE_RANGE
    )


def save_table(number, content):
    """Save table to a text file."""

    OUTPUT_DIR.mkdir(exist_ok=True)

    filepath = OUTPUT_DIR / f"table_{number}.txt"

    with open(filepath, "w") as file:
        file.write(content)

    print(f"✅ Saved: {filepath}")


def generate_all_tables():
    """Generate and save all tables."""

    for number in TABLE_RANGE:
        save_table(number, generate_table(number))

    print(f"\n🎉 {len(TABLE_RANGE)} tables saved successfully!")


if __name__ == "__main__":
    generate_all_tables()
