import matplotlib.pyplot as plt

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    total_sales = []

    for month in months:
        sales = float(input(f"Enter total sales for {month}: $"))
        total_sales.append(sales)

    plt.figure(figsize=(10, 6))
    plt.bar(months, total_sales, color='b', alpha=0.7)
    plt.xlabel('Months')
    plt.ylabel('Total Sales ($)')
    plt.title('Total Sales per Month')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()