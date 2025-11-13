import csv
from pathlib import Path

FILE = Path("transactions.csv")

def save_to_csv(entry_type, source, amount):
    """Save each credit/debit entry to CSV"""
    header = ["Type", "Source", "Amount"]
    write_header = not FILE.exists()
    with FILE.open("a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(header)
        writer.writerow([entry_type, source, amount])


def append_totals_to_csv(total_credit, total_debit, balance):
    """Append totals at the bottom of the CSV file"""
    with FILE.open("a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([])  # blank line
        writer.writerow(["Total Credit", "", total_credit])
        writer.writerow(["Total Debit", "", total_debit])
        writer.writerow(["Balance", "", balance])


# --- Lists to hold values in memory ---
mon_c = []
list_of_credit_sources = []
mon_d = []
list_of_debit_sources = []

while True:
    user = input("Credit 'C' or Debit 'D' (or 'list' to show report): ").lower()

    if user == "c":
        c_sources = input("Enter the source of income (or 'r' to return): ").lower()
        if c_sources == 'r':
            continue
        money = int(input("Enter the amount: "))
        mon_c.append(money)
        list_of_credit_sources.append(c_sources)
        save_to_csv("Credit", c_sources, money)
        print("✅ Credit added and saved!\n")

    elif user == "d":
        d_sources = input("Enter the source of expense (or 'r' to return): ").lower()
        if d_sources == 'r':
            continue
        money = int(input("Enter the amount: "))
        mon_d.append(money)
        list_of_debit_sources.append(d_sources)
        save_to_csv("Debit", d_sources, money)
        print("✅ Debit added and saved!\n")

    elif user == "list":
        print("\n📊--- Transaction Report ---📊")

        # Show credits
        print("\n💰 Credits:")
        for src, amt in zip(list_of_credit_sources, mon_c):
            print(f"  {src} : ₹{amt}")
        print(f"  ➕ Total Credit = ₹{sum(mon_c)}")

        # Show debits
        print("\n💸 Debits:")
        for src, amt in zip(list_of_debit_sources, mon_d):
            print(f"  {src} : ₹{amt}")
        print(f"  ➖ Total Debit = ₹{sum(mon_d)}")

        # Totals
        total_credit = sum(mon_c)
        total_debit = sum(mon_d)
        balance = total_credit - total_debit

        print(f"\n🧾 Balance: ₹{balance}")
        append_totals_to_csv(total_credit, total_debit, balance)
        print("\n✅ Totals added to 'transactions.csv'. Exiting...")
        break

    else:
        print(f"⚠️ '{user}' is invalid! Please enter 'C', 'D', or 'r'.\n")
