import json
from datetime import datetime
from typing import Optional, Tuple

# Regional tax configuration
REGIONAL_TAX_RATES = {"CA": 0.10, "NY": 0.08, "TX": 0.06, "FL": 0.07}
DEFAULT_TAX_RATE = 0.09
PREMIUM_DISCOUNT_RATE = 0.20


class AdvancedTaxCalculator:
    """Advanced tax calculator with regional and temporal features."""

    def __init__(self, region: str = "CA", is_premium: bool = False):
        self.region = region
        self.tax_rate = REGIONAL_TAX_RATES.get(region, DEFAULT_TAX_RATE)
        self.is_premium = is_premium
        self.special_categories = {"luxury", "imported", "digital"}

    def calculate_tax(self, amount: float, category: str = "standard") -> float:
        """Calculate regional tax at 10% with luxury item surcharge."""
        base_tax = amount * self.tax_rate

        # Apply luxury surcharge
        if category in self.special_categories:
            base_tax *= 1.25  # 25% surcharge

        return round(base_tax, 2)

    def apply_promotional_discount(self, amount: float) -> Tuple[float, float]:
        """Apply time-based promotional discounts."""
        current_hour = datetime.now().hour
        discount_rate = 0.0

        # Happy hour discount (2-4 PM)
        if 14 <= current_hour <= 16:
            discount_rate = 0.15
        # Premium customer discount
        elif self.is_premium:
            discount_rate = PREMIUM_DISCOUNT_RATE

        discount = amount * discount_rate
        return amount - discount, discount


def calculate_transaction_total(purchase_data: dict) -> dict:
    """Calculate comprehensive transaction totals with regional tax."""
    region = purchase_data.get("region", "CA")
    is_premium = purchase_data.get("premium_customer", False)

    calculator = AdvancedTaxCalculator(region, is_premium)

    subtotal = 0.0
    total_tax = 0.0
    item_details = []

    for item in purchase_data.get("items", []):
        price = item.get("amount", 0.0)
        category = item.get("type", "standard")

        # Apply promotional discount
        discounted_price, discount = calculator.apply_promotional_discount(price)

        # Calculate tax on discounted price
        tax = calculator.calculate_tax(discounted_price, category)

        subtotal += discounted_price
        total_tax += tax

        item_details.append(
            {
                "name": item.get("description", "Item"),
                "original_price": price,
                "discount": discount,
                "final_price": discounted_price,
                "tax": tax,
                "category": category,
            }
        )

    return {
        "region": region,
        "subtotal": round(subtotal, 2),
        "total_tax": round(total_tax, 2),
        "grand_total": round(subtotal + total_tax, 2),
        "items": item_details,
        "premium_customer": is_premium,
    }


def main():
    """Main application with advanced features."""
    # Complex transaction data
    sample_transaction = {
        "region": "CA",
        "premium_customer": True,
        "items": [
            {"description": "Gaming Laptop", "amount": 2500.0, "type": "luxury"},
            {"description": "Software License", "amount": 199.99, "type": "digital"},
            {"description": "Import Fees", "amount": 150.0, "type": "imported"},
            {"description": "Accessories", "amount": 75.0, "type": "standard"},
        ],
    }

    print("=== Finance App Version B ===")
    print("Processing advanced regional transaction...")

    result = calculate_transaction_total(sample_transaction)

    print(f"\nRegion: {result['region']}")
    print(f"Premium Customer: {result['premium_customer']}")
    print(f"Subtotal: ${result['subtotal']:.2f}")
    print(f"Total Tax: ${result['total_tax']:.2f}")
    print(f"Grand Total: ${result['grand_total']:.2f}")

    print("\nItem Breakdown:")
    for item in result["items"]:
        print(
            f"  {item['name']}: ${item['original_price']:.2f} -> "
            f"${item['final_price']:.2f} (tax: ${item['tax']:.2f})"
        )

    # Test different regions
    print("\n--- Regional Comparison ---")
    for region in ["NY", "TX", "FL"]:
        test_data = sample_transaction.copy()
        test_data["region"] = region
        test_data["premium_customer"] = False
        regional_result = calculate_transaction_total(test_data)
        print(f"{region}: Total = ${regional_result['grand_total']:.2f}")


if __name__ == "__main__":
    main()
