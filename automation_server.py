#!/usr/bin/env python3
"""
Digital Product Automation Server
Unified entry point for generating personalized products on-demand
Can be extended with webhook integration for Etsy/Gumroad
"""

import os
import json
from datetime import datetime
from preschool_number_generator import NumberWorksheetGenerator
from homeschool_budget_generator import BudgetSpreadsheetGenerator

class AutomationServer:
    def __init__(self):
        self.preschool_gen = NumberWorksheetGenerator("./output_worksheets")
        self.budget_gen = BudgetSpreadsheetGenerator("./output_budgets")

    def generate_preschool_order(self, order_data):
        """
        Generate preschool worksheets based on order parameters
        Expected order_data:
        {
            "customer_name": "John Doe",
            "child_name": " Emma",
            "numbers": [1,2,3,4,5,6,7,8,9,10],
            "product_type": "number_bundle",
            "order_id": "ORD123"
        }
        """
        print(f"[{datetime.now()}] Generating preschool order {order_data.get('order_id')}")

        child = order_data.get('child_name', '').strip()
        numbers = order_data.get('numbers', list(range(1, 6)))

        if order_data.get('product_type') == 'number_bundle':
            files = self.preschool_gen.generate_bundle(numbers, child)
        elif order_data.get('product_type') == 'tracing_only':
            files = []
            for n in numbers:
                files.append(self.preschool_gen.generate_tracing_sheet(n, child))
        elif order_data.get('product_type') == 'recognition_only':
            files = []
            for n in numbers:
                files.append(self.preschool_gen.generate_number_recognition(n))
        else:
            raise ValueError(f"Unknown product_type: {order_data.get('product_type')}")

        # Package files into a zip (would need zipfile module)
        output_dir = f"./orders/{order_data.get('order_id', 'unknown')}"
        os.makedirs(output_dir, exist_ok=True)

        # In full version, move files to output_dir and zip them
        print(f"Generated {len(files)} files")
        return {"order_id": order_data.get('order_id'), "files": files, "status": "generated"}

    def generate_budget_order(self, order_data):
        """
        Generate budget spreadsheets
        Expected order_data:
        {
            "customer_name": "Jane Smith",
            "family_name": "Smith Family",
            "product_type": "monthly_budget" | "annual_budget" | "full_bundle",
            "year": 2025,
            "order_id": "ORD456"
        }
        """
        print(f"[{datetime.now()}] Generating budget order {order_data.get('order_id')}")

        family = order_data.get('family_name', 'Homeschool Family')
        year = order_data.get('year', 2025)
        product = order_data.get('product_type', 'full_bundle')

        if product == 'monthly_budget':
            files = [self.budget_gen.create_monthly_budget(family, year)]
        elif product == 'annual_budget':
            files = [self.budget_gen.create_annual_budget(family, year)]
        elif product == 'full_bundle':
            files = self.budget_gen.generate_full_homeschool_bundle(family, year)
        else:
            raise ValueError(f"Unknown product_type: {product}")

        print(f"Generated {len(files)} files")
        return {"order_id": order_data.get('order_id'), "files": files, "status": "generated"}

    def webhook_handler(self, request_data):
        """
        Placeholder for webhook integration
        Will parse Etsy/Gumroad webhook payload and call appropriate generator
        """
        # TODO: Implement actual webhook parsing based on platform
        platform = request_data.get('platform', 'etsy')
        if platform == 'etsy':
            return self._handle_etsy_webhook(request_data)
        elif platform == 'gumroad':
            return self._handle_gumroad_webhook(request_data)
        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def _handle_etsy_webhook(self, payload):
        """Parse Etsy webhook and generate product"""
        # Etsy webhook structure will need to be mapped here
        # Extract: purchaser name, product SKU, customization options
        print("Etsy webhook received (not fully implemented)")
        print(f"Payload: {payload}")
        return {"status": "webhook_received", "message": "Implementation pending"}

    def _handle_gumroad_webhook(self, payload):
        """Parse Gumroad webhook and generate product"""
        print("Gumroad webhook received (not fully implemented)")
        print(f"Payload: {payload}")
        return {"status": "webhook_received", "message": "Implementation pending"}

if __name__ == "__main__":
    server = AutomationServer()

    # Test orders
    print("=== Testing Preschool Order ===")
    preschool_order = {
        "customer_name": "Test Parent",
        "child_name": " Emma",
        "numbers": [1, 2, 3, 4, 5],
        "product_type": "number_bundle",
        "order_id": "PRE-001"
    }
    result1 = server.generate_preschool_order(preschool_order)
    print(json.dumps(result1, indent=2))

    print("\n=== Testing Budget Order ===")
    budget_order = {
        "customer_name": "Test Homeschooler",
        "family_name": "Test Homeschool Family",
        "product_type": "full_bundle",
        "year": 2025,
        "order_id": "BUD-001"
    }
    result2 = server.generate_budget_order(budget_order)
    print(json.dumps(result2, indent=2))

    print("\n=== Automation Server Ready ===")
    print("To integrate with Etsy/Gumroad, set up webhook endpoints that call:")
    print("  server.generate_preschool_order({...})")
    print("  server.generate_budget_order({...})")