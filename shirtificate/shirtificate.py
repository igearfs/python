from fpdf import FPDF
from fpdf import Align

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self._name = name
        super().add_page()
        super().set_font("helvetica", "B", 50)
        super().cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN",  align=Align.C)
        super().image("shirtificate.png", w = super().epw, y = 70)

        super().set_font_size(30)
        super().set_text_color(255,255,255)
        super().set_x(50)
        super().set_y(140)
        super().cell(h=5.0, align='C', w=0, text=f"{name} took CS50", border=0)


name = input("Name: ")
pdf = PDF(name)
pdf.output("shirtificate.pdf")