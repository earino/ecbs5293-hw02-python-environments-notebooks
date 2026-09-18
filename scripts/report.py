"""Print a table of revenue per product.

Run from the project folder:  uv run python scripts/report.py
"""

from pathlib import Path

import pandas as pd

DATA = Path("data/raw/sales_2024.csv")


def main() -> None:
    df = pd.read_csv(DATA).dropna(subset=["units"])
    df["revenue"] = df["units"] * df["unit_price"]
    table = df.groupby("product")["revenue"].sum().round(2).reset_index()
    print(table.to_string(index=False))


if __name__ == "__main__":
    main()
