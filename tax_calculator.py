import math
from decimal import Decimal
from typing import Dict, List

# Configuration constants
TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 1000.0
MAX_DISCOUNT = 0.15


class TaxCalculator:
    """Handles tax calculations for financial transactions."""

    def __init__(self, base_rate: float = TAX_RATE):
        self.base_rate = base_rate
        self.exemptions = ["food", "medicine"]

    def calculate_tax(self, amount: float, category: str = "general") -> float:
        """Calculate sales tax at 8% with category exemptions."""
        if category in self.exemptions:
            return 0.0
        return amount * self.base_rate

    def calculate_with_discount(self, amount: float) -> Dict[str, float]:
        """Apply discount for large purchases."""
        discount = 0.0
        if amount >= DISCOUNT_THRESHOLD:
            discount = min(amount * 0.10, amount * MAX_DISCOUNT)

        discounted_amount = amount - discount
        tax = self.calculate_tax(discounted_amount)

        return {
            "original_amount": amount,
            "discount": discount,
            "discounted_amount": discounted_amount,
            "tax": tax,
            "total": discounted_amount + tax,
        }


def process_transaction(items: List[Dict]) -> float:
    """Process a list of items and calculate total with tax."""
    calculator = TaxCalculator()
    total = 0.0

    for item in items:
        amount = item.get("price", 0.0)
        category = item.get("category", "general")
        tax = calculator.calculate_tax(amount, category)
        total += amount + tax
        print(
            f"Item: {item.get('name', 'Unknown')} - Price: ${amount:.2f}, Tax: ${tax:.2f}"
        )

    return total


def main():
    """Main application entry point."""
    # Sample transaction data
    transaction_items = [
        {"name": "Laptop", "price": 1200.0, "category": "electronics"},
        {"name": "Groceries", "price": 85.0, "category": "food"},
        {"name": "Medicine", "price": 45.0, "category": "medicine"},
    ]

    print("=== Finance App Version A ===")
    print("Processing transaction with basic tax calculation...")

    total = process_transaction(transaction_items)
    print(f"\nTransaction Total: ${total:.2f}")

    # Test discount calculation
    calculator = TaxCalculator()
    large_purchase = calculator.calculate_with_discount(1500.0)
    print(f"\nLarge Purchase Analysis:")
    print(f"Original: ${large_purchase['original_amount']:.2f}")
    print(f"Discount: ${large_purchase['discount']:.2f}")
    print(f"Final Total: ${large_purchase['total']:.2f}")


if __name__ == "__main__":
    main()
