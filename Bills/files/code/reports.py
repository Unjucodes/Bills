import webbrowser
import os

from fpdf import FPDF


class Pdfreport:
    """
    creates pdf file that contains data about
    the flatemates such as their names, their due amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        # generates a pdf file for the bill
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # adding an image
        pdf.image(name="cool_stuff/house.png", w=30, h=30)

        # adding title
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate's Bill", border=0, align="C", ln=1)

        # period label & value
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # how much the user1 pays
        pdf.cell(w=100, h=25, txt=flatmate1.name.title(), border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # how much user2 pays
        pdf.cell(w=100, h=25, txt=flatmate2.name.title(), border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # generating a name for the file

        os.chdir('cool_stuff')

        pdf.output(self.filename)

        # opens the pdf as soon as you fill out the input
        webbrowser.open(self.filename)
