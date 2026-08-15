import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = "../data/expenses_august_2026.csv"
CHART_DIR = Path("../outputs/charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)

def load_data(file_path):
    """Load expense data from a CSV file."""
    return pd.read_csv(file_path)


def analyze_expenses(df):
    """Calculate key expense statistics."""

    total_expense = df["Amount"].sum()
    average_expense = df["Amount"].mean()
    highest_expense = df["Amount"].max()
    lowest_expense = df["Amount"].min()

    return {
        "total_expense": total_expense,
        "average_expense": average_expense,
        "highest_expense": highest_expense,
        "lowest_expense": lowest_expense
    }

def analyze_categories(df):
    """Analyze expenses by category."""

    category_expense = df.groupby("Category")["Amount"].sum()
    category_count = df["Category"].value_counts()

    highest_category = category_expense.idxmax()
    lowest_category = category_expense.idxmin()

    return {
        "category_expense": category_expense,
        "category_count": category_count,
        "highest_category": highest_category,
        "lowest_category": lowest_category
    }

def analyze_daily_expenses(df):
    """Analyze expenses by date."""

    daily_expense = df.groupby("Date")["Amount"].sum()

    daily_average = daily_expense.mean()
    highest_spending_date = daily_expense.idxmax()
    highest_daily_expense = daily_expense.max()

    return {
        "daily_expense": daily_expense,
        "daily_average": daily_average,
        "highest_spending_date": highest_spending_date,
        "highest_daily_expense": highest_daily_expense
    }

def analyze_descriptions(df):
    """Analyze total spending by description."""

    description_expense = (
        df.groupby("Description")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    top_5_descriptions = description_expense.head(5)

    highest_description = description_expense.idxmax()
    highest_description_amount = description_expense.max()

    return {
        "description_expense": description_expense,
        "top_5_descriptions": top_5_descriptions,
        "highest_description": highest_description,
        "highest_description_amount": highest_description_amount
    }

def plot_category_expenses(category_expense):
    """Create and save a bar chart of spending by category."""

    category_expense.sort_values(ascending=False).plot(
        kind="bar",
        figsize=(10, 6)
    )

    plt.title("Total Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "category_spending.png",
        dpi=300
    )

    plt.show()
    plt.close()

def plot_daily_expenses(daily_expense):
    """Create and save a line chart of daily expenses."""

    daily_expense.plot(
        kind="line",
        figsize=(12, 6),
        marker="o"
    )

    plt.title("Daily Expense Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "daily_expense_trend.png",
        dpi=300
    )

    plt.show()
    plt.close()
def plot_top_5_descriptions(top_5_descriptions):
    """Create and save a bar chart of the top 5 spending descriptions."""

    top_5_descriptions.sort_values().plot(
        kind="barh",
        figsize=(10, 6)
    )

    plt.title("Top 5 Spending Descriptions")
    plt.xlabel("Amount")
    plt.ylabel("Description")
    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "top_5_spending.png",
        dpi=300
    )

    plt.show()
    plt.close()


def main():
    """Run the complete expense analysis."""

    # Load data
    df = load_data(DATA_FILE)

    # Prepare date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Analyze expenses
    stats = analyze_expenses(df)

    # Analyze categories
    category_stats = analyze_categories(df)

    # Analyze daily expenses
    daily_stats = analyze_daily_expenses(df)

    # Analyze descriptions
    description_stats = analyze_descriptions(df)

    # Print summary
    print("=" * 50)
    print("       PERSONAL EXPENSE ANALYZER")
    print("=" * 50)

    print(f"Total Expense: {stats['total_expense']:.2f}")
    print(f"Average Transaction: {stats['average_expense']:.2f}")
    print(f"Average Daily Expense: {daily_stats['daily_average']:.2f}")
    print(f"Highest Transaction: {stats['highest_expense']:.2f}")
    print(f"Lowest Transaction: {stats['lowest_expense']:.2f}")

    print(
        "Highest Spending Category:",
        category_stats["highest_category"]
    )

    print(
        "Highest Spending Description:",
        description_stats["highest_description"]
    )

    print(
        "Highest Description Amount:",
        description_stats["highest_description_amount"]
    )

    # Create charts
    plot_category_expenses(
        category_stats["category_expense"]
    )

    plot_daily_expenses(
        daily_stats["daily_expense"]
    )

    plot_top_5_descriptions(
        description_stats["top_5_descriptions"]
    )
if __name__ == "__main__":
    main()