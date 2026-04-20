from fpdf import FPDF

class BrochurePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 20)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, "TechNova Solutions", ln=True, align="C")
        self.set_font("Arial", "I", 12)
        self.cell(0, 10, "Innovating the Future of Fintech", ln=True, align="C")
        self.ln(10)

def generate_brochure():
    pdf = BrochurePDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    # Section: Company Overview
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "Company Overview", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 6, "TechNova Solutions is a leading global technology firm specializing in High-Frequency Trading (HFT) and AI-driven financial analytics. With an annual turnover exceeding $500 Million, we operate at the intersection of mathematics and high-performance computing.")
    pdf.ln(5)

    # Section: Job Description
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "Job Description", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, "Role: Machine Learning Intern", ln=True)
    pdf.cell(0, 6, "Type: 2-Month Summer Internship", ln=True)
    pdf.cell(0, 6, "Location: Bangalore (On-site)", ln=True)
    pdf.ln(5)

    # Section: Eligibility
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "Eligibility Criteria", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, "- Open to 2nd and 3rd-year B.Tech students.", ln=True)
    pdf.cell(0, 6, "- Eligible Branches: CSE, MnC, EE, and ECE.", ln=True)
    pdf.cell(0, 6, "- Minimum CGPA: 8.0 and above.", ln=True)
    pdf.ln(5)

    # Section: Compensation
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "Compensation & Benefits", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, "- Stipend: INR 60,000 per month.", ln=True)
    pdf.cell(0, 6, "- PPO Compensation: Up to 24 LPA.", ln=True)
    pdf.ln(5)

    # Section: Selection Process
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "Selection Process", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, "1. Resume Shortlisting", ln=True)
    pdf.cell(0, 6, "2. Online Technical Assessment (DSA & ML)", ln=True)
    pdf.cell(0, 6, "3. Deep Technical Interview (Math & Coding)", ln=True)
    pdf.ln(5)

    # Section: Contact
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Headquarters: 12th Floor, Cyber Plaza, Whitefield, Bangalore - 560066", ln=True)

    pdf.output("technova_brochure.pdf")
    print("PDF generated successfully: technova_brochure.pdf")

if __name__ == "__main__":
    generate_brochure()