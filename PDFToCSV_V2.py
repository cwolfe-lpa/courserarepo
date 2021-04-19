# Import Module
import tabula

# Read PDF File
#df = tabula.read_pdf("C:\Temp\history_forecast4744257.pdf", pages = 1)[0]

# Convert to Excel
#df.to_csv("C:\Users\cwolfe\OneDrive - LPA Software Solutions LLC\Documents\Expotel\Attachment")

tabula.convert_into("C:\Temp\history_forecast4744257.pdf", "C:\Temp\history_forecast4744257.csv", output_format="csv", pages='all')
