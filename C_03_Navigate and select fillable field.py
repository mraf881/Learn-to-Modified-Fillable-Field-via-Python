from PyPDF2 import PdfReader


# Reading the text file
pdf_file = r"PDF File location"

# Reading the field

#Reading and display the PDF file
reading_pdf = PdfReader(pdf_file)
detect_field =reading_pdf.get_fields()
print("Fillable field and field value detected ✓")

#Displaying the fillable field and field value
if detect_field:
    for read_field in detect_field:
        print(f"{read_field}: {detect_field[read_field].get('/v')}") #to retrieve fillable fill value if entered, preffered to be "None"

else:
    print("No fillable field detected")
