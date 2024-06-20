# For code history capturing


# Importing the library

import pdfrw

input_pdf_path = r"location"
output_pdf_path = r"location\output.pdf"

# Read the PDF file
template_pdf = pdfrw.PdfReader(input_pdf_path)

# Access annotations (Form Field)
annotations = template_pdf.pages[0]['/Annots']

# List filable fields with index number for easy trancking and modifying the fillable field
fields = []
for i, annotation in enumerate(annotations):
    if annotation['/Subtype'] == '/Widget':
        field = annotation.get('/T')
        if field:
            fields.append((i, field[1:-1]))  # Remove parentheses from field name

print("Fillable fields with index:")
for index, name in fields:
    print(f"Index: {index}, Name: {name}")

# Under development line
