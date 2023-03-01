from fpdf import FPDF

# Constants
PAGE_WIDTH = 210
PAGE_HEIGHT = 297

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.set_font('Helvetica', 'B', 28)
pdf.image('https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png', x=50, y=60, w=110)
pdf.cell(0, 30, 'CS50 Shirtificate', new_x="RIGHT", new_y="TOP", align='C')

name = input('Enter your name: ')
pdf.set_text_color(255, 255, 255)
pdf.text(PAGE_WIDTH / 2 - pdf.get_string_width(name) / 2, 90, name)

pdf.output('shirtificate.pdf')

