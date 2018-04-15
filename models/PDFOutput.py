
from Strategy import Strategy
from fpdf import FPDF

class PDFOutput(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """
    def output_interface(self, person):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, person.name)
        pdf.cell(40, 10, person.age)
        pdf.cell(40, 10, person.city)
        pdf.cell(40, 10, person.mob_num)        
        pdf.output('out.pdf', 'F')
