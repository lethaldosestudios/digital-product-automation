#!/usr/bin/env python3
"""
Order Fulfillment CLI
Simple command-line tool for manually generating customer orders

Usage:
  python3 order_fulfillment.py preschool --child "Emma" --numbers 1-5 --output ./customer_orders
  python3 order_fulfillment.py budget --family "Smith Family" --output ./customer_orders
"""

import argparse
import sys
import os
from datetime import datetime
from automation_server import AutomationServer

def main():
    parser = argparse.ArgumentParser(description="Generate digital product orders manually")
    subparsers = parser.add_subparsers(dest='product', required=True, help='Product type')

    # Preschool command
    preschool_parser = subparsers.add_parser('preschool', help='Generate preschool worksheets')
    preschool_parser.add_argument('--child', required=True, help='Child name (appears on worksheets)')
    preschool_parser.add_argument('--numbers', default='1-5',
                                   help='Numbers to include (e.g., "1-5" or "1,2,3,4,5,6,7,8,9,10")')
    preschool_parser.add_argument('--type', default='number_bundle',
                                   choices=['number_bundle', 'tracing_only', 'recognition_only'],
                                   help='Type of worksheet pack')
    preschool_parser.add_argument('--output', default='./customer_orders',
                                   help='Output directory for generated files')

    # Budget command
    budget_parser = subparsers.add_parser('budget', help='Generate budget spreadsheets')
    budget_parser.add_argument('--family', required=True, help='Family name (appears on spreadsheets)')
    budget_parser.add_argument('--type', default='full_bundle',
                               choices=['monthly_budget', 'annual_budget', 'full_bundle'],
                               help='Budget template type')
    budget_parser.add_argument('--year', type=int, default=datetime.now().year,
                               help='Year for budget (default: current year)')
    budget_parser.add_argument('--output', default='./customer_orders',
                               help='Output directory for generated files')

    # Global options
    parser.add_argument('--order-id', help='Custom order ID (auto-generated if not provided)')

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Initialize server
    server = AutomationServer()

    # Override output directories temporarily
    if args.product == 'preschool':
        # Parse numbers
        if '-' in args.numbers:
            start, end = map(int, args.numbers.split('-'))
            numbers = list(range(start, end + 1))
        else:
            numbers = [int(n) for n in args.numbers.split(',')]

        order_data = {
            "customer_name": "Customer",
            "child_name": args.child,
            "numbers": numbers,
            "product_type": args.type,
            "order_id": args.order_id or f"PRE-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        }

        print(f"Generating preschool order for {args.child} (numbers {args.numbers})...")
        result = server.generate_preschool_order(order_data)

        # Move files to output directory
        print(f"\nGenerated {len(result['files'])} files")
        for f in result['files']:
            print(f"  - {f}")
        print(f"\nFiles location: {args.output}/")

    elif args.product == 'budget':
        order_data = {
            "customer_name": "Customer",
            "family_name": args.family,
            "product_type": args.type,
            "year": args.year,
            "order_id": args.order_id or f"BUD-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        }

        print(f"Generating {args.type} for {args.family}...")
        result = server.generate_budget_order(order_data)

        print(f"\nGenerated {len(result['files'])} files")
        for f in result['files']:
            print(f"  - {f}")
        print(f"\nOrder ID: {result['order_id']}")
        print(f"Files location: {args.output}/")

    print("\n✅ Ready to deliver to customer.")
    print("Next: Upload files to Etsy order page, mark as complete, send message.")

if __name__ == "__main__":
    main()