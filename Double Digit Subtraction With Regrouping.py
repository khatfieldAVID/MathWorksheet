from fpdf import FPDF
import random

def generate_problem():
    """Generate a double-digit subtraction problem requiring regrouping."""
    tens_m = random.randint(2, 9)
    ones_m = random.randint(0, 8)
    minuend = 10 * tens_m + ones_m
    ones_s = random.randint(ones_m + 1, 9)
    tens_s = random.randint(1, tens_m - 1)
    subtrahend = 10 * tens_s + ones_s
    return minuend, subtrahend

def print_problem(pdf, x, y, minuend, subtrahend):
    """Print a subtraction problem at the specified x, y position with 8mm line spacing."""
    pdf.set_xy(x, y)
    pdf.cell(0, 8, f" {str(minuend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 8)
    pdf.cell(0, 8, f"-{str(subtrahend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 16)
    pdf.cell(0, 8, "___", ln=True)

def print_answer(pdf, x, y, minuend, subtrahend, difference):
    """Print a subtraction problem with its answer at the specified x, y position."""
    pdf.set_xy(x, y)
    pdf.cell(0, 12, f" {str(minuend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 12)
    pdf.cell(0, 12, f"-{str(subtrahend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 24)
    pdf.cell(0, 12, f" {str(difference).rjust(2)}", ln=True)

def create_worksheet(num_problems=10):
    """Create a worksheet and answer key with increased padding and spacing."""
    pdf = FPDF()
    
    # Worksheet page
    pdf.add_page()
    pdf.set_font("Courier", size=14)
    pdf.set_xy(0, 15)
    pdf.cell(210, 10, "Double-Digit Subtraction with Regrouping", ln=True, align='C')
    pdf.set_font("Courier", size=12)
    pdf.set_xy(20, 25)
    pdf.multi_cell(170, 5, "Solve the following subtraction problems. Remember to regroup when necessary.")
    pdf.ln(10)
    y_start = pdf.get_y()
    
    # Generate problems
    problems = [generate_problem() for _ in range(num_problems)]
    
    # Print problems in two columns
    col1_x = 20
    col2_x = 110
    for i in range(5):
        print_problem(pdf, col1_x, y_start + i * 25, problems[i][0], problems[i][1])
    for i in range(5, 10):
        print_problem(pdf, col2_x, y_start + (i - 5) * 25, problems[i][0], problems[i][1])
    
    # Answer key page
    pdf.add_page()
    pdf.set_font("Courier", size=14)
    pdf.set_xy(0, 15)
    pdf.cell(210, 10, "Answer Key", ln=True, align='C')
    pdf.set_font("Courier", size=12)
    y_start = pdf.get_y() + 10
    for i in range(5):
        difference = problems[i][0] - problems[i][1]
        print_answer(pdf, col1_x, y_start + i * 36, problems[i][0], problems[i][1], difference)
    for i in range(5, 10):
        difference = problems[i][0] - problems[i][1]
        print_answer(pdf, col2_x, y_start + (i - 5) * 36, problems[i][0], problems[i][1], difference)
    
    pdf.output("subtraction_worksheet.pdf")

if __name__ == "__main__":
    create_worksheet()
