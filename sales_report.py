"""
Sales report generator.

Reads sales.csv and prints:
  - total revenue
  - revenue per region (highest first)
  - top 3 products by units sold
  - average ticket for one region
"""
import pandas as pd


def load_data(path):
    """Load the sales file and add a revenue column (units x price)."""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["units"] * df["price"]
    return df


def revenue_by_region(df):
    """Total revenue for each region, sorted from highest to lowest."""
    # CORREGIDO: Se cambió .mean() por .sum() para obtener el total de ingresos por región.
    result = df.groupby("region")["revenue"].sum().round(2)
    return result.sort_values(ascending=False)


def top_products(df, n=3):
    """The n products with the most units sold."""
    totals = df.groupby("product")["units"].sum()
    # CORREGIDO: Se agregó ascending=False para obtener los productos con más unidades vendidas (top 3).
    return totals.sort_values(ascending=False).head(n)


def average_ticket(df, region):
    """Average revenue per sale line for the given region."""
    # CORREGIDO: Se corrigió '=' (asignación) por '==' (comparación lógica).
    subset = df[df["region"] == region]
    return subset["revenue"].sum() / len(subset)


def main():
    df = load_data("sales.csv")

    print("=== SALES REPORT ===")
    print(f"Total revenue: {df['revenue'].sum():,.2f}")

    print("\nRevenue by region:")
    for region, value in revenue_by_region(df).items():
        print(f"  {region}: {value:,.2f}")

    print("\nTop 3 products by units sold:")
    for product, units in top_products(df).items():
        print(f"  {product}: {units}")

    print(f"\nAverage ticket (Norte): {average_ticket(df, 'Norte'):,.2f}")


if __name__ == "__main__":
    main()