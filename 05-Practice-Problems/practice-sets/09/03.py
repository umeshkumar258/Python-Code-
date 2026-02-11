import os

OUTPUT_DIR = "tables"
TABLE_RANGE = range(2, 21)


def generate_table(n: int) -> str:
    """Generate and return the multiplication table for n as a string."""
    lines = [f"{n} x {i} = {n * i}" for i in TABLE_RANGE]
    return "\n".join(lines)


def save_table(n: int, content: str) -> None:
    """Save a multiplication table to a file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"table_{n}.txt")
    with open(filepath, "w") as f:
        f.write(content)
    print(f"✅ Saved: {filepath}")


def generate_all_tables() -> None:
    """Generate and save multiplication tables for all numbers in TABLE_RANGE."""
    for i in TABLE_RANGE:
        table = generate_table(i)
        save_table(i, table)
    print(f"\n🎉 Done! {len(TABLE_RANGE)} tables saved to '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    generate_all_tables()
