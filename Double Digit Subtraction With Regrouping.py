from fpdf import FPDF
import random

def generate_problem():
    # Generate minuend with tens digit from 2 to 9 and ones digit from 0 to 8
    tens_m = random.randint(2, 9)
    ones_m = random.randint(0, 8)
    minuend = 10 * tens_m + ones_m
    # Generate ones digit of subtrahend greater than minuend's ones digit
    ones_s = random.randint(ones_m + 1, 9)
    # Generate tens digit of subtrahend from 1 to tens_m - 1
    tens_s = random.randint(1, tens_m - 1)
    subtrahend = 10 * tens_s + ones_s
    return minuend, subtrahend

def print_problem(pdf, x, y, minuend, subtrahend):
    pdf.set_xy(x, y)
    pdf.cell(0, 5, f" {str(minuend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 5)
    pdf.cell(0, 5, f"-{str(subtrahend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 10)
    pdf.cell(0, 5, "___", ln=True)

def print_answer(pdf, x, y, minuend, subtrahend, difference):
    pdf.set_xy(x, y)
    pdf.cell(0, 5, f" {str(minuend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 5)
    pdf.cell(0, 5, f"-{str(subtrahend).rjust(2)}", ln=True)
    pdf.set_xy(x, y + 10)
    pdf.cell(0, 5, f" {str(difference).rjust(2)}", ln=True)

def create_worksheet(num_problems=10):
    pdf = FPDF()
    
    # Worksheet page
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    pdf.cell(0, 10, "Double-Digit Subtraction with Regrouping", ln=True, align='C')
    pdf.ln(5)
    pdf.set_font("Courier", size=10)
    pdf.multi_cell(0, 5, "Solve the following subtraction problems. Remember to regroup when necessary.")
    pdf.ln(5)
    
    # Generate and store problems
    problems = [generate_problem() for _ in range(num_problems)]
    
    # Print problems in two columns
    col1_x = 10
    col2_x = 100
    y_start = pdf.get_y()
    for i in range(5):
        print_problem(pdf, col1_x, y_start + i * 15, problems[i][0], problems[i][1])
    for i in range(5, 10):
        print_problem(pdf, col2_x, y_start + (i - 5) * 15, problems[i][0], problems[i][1])
    
    # Answer key page
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    pdf.cell(0, 10, "Answer Key", ln=True, align='C')
    pdf.ln(5)
    y_start = pdf.get_y()
    for i in range(5):
        difference = problems[i][0] - problems[i][1]
        print_answer(pdf, col1_x, y_start + i * 15, problems[i][0], problems[i][1], difference)
    for i in range(5, 10):
        difference = problems[i][0] - problems[i][1]
        print_answer(pdf, col2_x, y_start + (i - 5) * 15, problems[i][0], problems[i][1], difference)
    
    # Save the PDF
    pdf.output("subtraction_worksheet.pdf")

if __name__ == "__main__":
    create_worksheet()
