#!/usr/bin/env python3
"""
Preschool Number Worksheets Generator
Generates customizable PDF worksheets for numbers 1-20
Includes: tracing, counting, number recognition, fill-in-the-blank
"""

from fpdf import FPDF
from datetime import datetime
import os

class NumberWorksheetGenerator:
    def __init__(self, output_dir="./output worksheets"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_tracing_sheet(self, number, child_name=""):
        """Generate a number tracing worksheet for a specific number"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Number {number} Tracing Practice", ln=True, align='C')
        if child_name:
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 8, f"Name: {child_name}", ln=True, align='C')
        pdf.ln(10)

        # Large tracing number (outlined font would be better but using basic for now)
        pdf.set_font("Arial", 'B', 60)
        pdf.cell(0, 20, f"{number}", ln=True, align='C')
        pdf.ln(10)

        # Tracing lines
        pdf.set_font("Arial", size=12)
        for i in range(6):
            pdf.cell(0, 8, f"Trace the number {number}: _____", ln=True)
            pdf.ln(2)

        # Independent practice
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Now write the number by yourself:", ln=True)
        for i in range(3):
            pdf.cell(0, 8, "_____", ln=True)
            pdf.ln(2)

        # Counting practice
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Count and circle the correct number:", ln=True)
        pdf.set_font("Arial", size=12)
        # Simple placeholder - in full version would draw circles with numbers
        pdf.cell(0, 8, "[Visual: 3 apples, circle the number 3]", ln=True)

        filename = f"{self.output_dir}/number_{number}_tracing_{child_name or 'blank'}.pdf"
        pdf.output(filename)
        return filename

    def generate_counting_sheet(self, start_num=1, end_num=10):
        """Generate a counting worksheet with objects to count"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Counting Practice: {start_num} to {end_num}", ln=True, align='C')
        pdf.ln(10)

        # Grid of objects to count - simplified version
        pdf.set_font("Arial", size=12)
        items = ["*", "o", "+", "#", "@"]
        for row in range(5):
            line_items = []
            for col in range(5):
                idx = (row * 5 + col) % len(items)
                line_items.append(items[idx])
            pdf.cell(0, 10, "  ".join(line_items), ln=True, align='C')

        pdf.ln(10)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "How many stars (*)? ____", ln=True)
        pdf.cell(0, 10, "How many circles (o)? ____", ln=True)
        pdf.cell(0, 10, "How many pluses (+)? ____", ln=True)

        filename = f"{self.output_dir}/counting_{start_num}_to_{end_num}.pdf"
        pdf.output(filename)
        return filename

    def generate_number_recognition(self, target_number, range_start=1, range_end=20):
        """Generate a 'find the number' worksheet"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Find All the {target_number}s!", ln=True, align='C')
        pdf.ln(10)

        # Create a grid of numbers to circle
        pdf.set_font("Arial", size=14)
        numbers = list(range(range_start, range_end + 1))
        # Repeat to fill grid
        grid_numbers = numbers * 4
        import random
        random.shuffle(grid_numbers)

        per_row = 5
        for i in range(0, min(len(grid_numbers), 60), per_row):
            row = grid_numbers[i:i+per_row]
            line = "   ".join(str(n) for n in row)
            pdf.cell(0, 10, line, ln=True, align='C')

        pdf.ln(10)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, "Circle every number that equals the target number!", ln=True, align='C')

        filename = f"{self.output_dir}/find_number_{target_number}.pdf"
        pdf.output(filename)
        return filename

    def generate_bundle(self, numbers_list, child_name=""):
        """Generate a complete bundle of worksheets for a set of numbers"""
        files = []
        for num in numbers_list:
            files.append(self.generate_tracing_sheet(num, child_name))
            files.append(self.generate_number_recognition(num))

        files.append(self.generate_counting_sheet(1, 10))

        # Generate a cover sheet
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 20)
        pdf.cell(0, 15, "Number Learning Bundle", ln=True, align='C')
        pdf.set_font("Arial", size=14)
        if child_name:
            pdf.cell(0, 10, f"Made with love for {child_name}", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 8, f"Includes worksheets for numbers: {', '.join(map(str, numbers_list))}", ln=True, align='C')
        pdf.ln(15)
        pdf.set_font("Arial", 'I', 10)
        pdf.multi_cell(0, 6, "Tips for parents: Use these sheets to help your child recognize, trace, and write numbers. Practice daily for best results. Use pencils so children can erase and try again.", align='C')

        cover_file = f"{self.output_dir}/bundle_cover_{child_name or 'generic'}.pdf"
        pdf.output(cover_file)
        files.insert(0, cover_file)

        return files

if __name__ == "__main__":
    generator = NumberWorksheetGenerator()

    # Test generate a specific bundle
    numbers_to_generate = [1, 2, 3, 4, 5]
    bundle_files = generator.generate_bundle(numbers_to_generate, "TestChild")

    print(f"Generated {len(bundle_files)} worksheets:")
    for f in bundle_files:
        print(f"  - {f}")

    print(f"\nAll files saved to: {generator.output_dir}")