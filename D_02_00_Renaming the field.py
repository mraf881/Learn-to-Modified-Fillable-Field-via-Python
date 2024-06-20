# Importing the module
import pdfrw

# Location of PDF file
input_pdf_path =  r"location"

# Output location of PDF file
output_pdf_path = r"location\output.pdf"

## Read the PDF file
read_pdf = pdfrw.PdfReader(input_pdf_path)

# Access annotations (Form Field)
annotations = read_pdf.pages[0]['/Annots']
print(True)

# Rename fillable fields by index
field_indices = range(32, 36)  # Indices of the fields you want to rename
new_field_names = ['NewFieldName1', 'NewFieldName2', 'NewFieldName3', 'NewFieldName4',]

for i, index in enumerate(field_indices):
    if 0 <= index < len(annotations):
        annotation = annotations[index]
        if annotation['/Subtype'] == '/Widget' and annotation.get('/T'):
            new_name = new_field_names[i]  # Use the correct index for new_field_names
            annotation.update(pdfrw.PdfDict(T='{}'.format(new_name)))

# Write the modified PDF to a new file
pdfrw.PdfWriter().write(output_pdf_path, read_pdf)

# Verify the change by reading the fields again
template_pdf_after = pdfrw.PdfReader(output_pdf_path)
annotations_after = template_pdf_after.pages[0]['/Annots']

fields_after_rename = []
for i, annotation in enumerate(annotations_after):
    if annotation['/Subtype'] == '/Widget':
        field = annotation.get('/T')
        if field:
            fields_after_rename.append((i, field[1:-1]))  # Remove parentheses from field name

print("\nFillable fields after renaming:")
for index, name in fields_after_rename:
    print(f"Index: {index}, Name: {name}")
