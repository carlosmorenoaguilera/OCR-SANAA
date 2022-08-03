import tabula
file = ("HORARIOS AGUA POTABLE ABRIL2021.pdf")
tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)
tabula.convert_into(file, "agua.csv")