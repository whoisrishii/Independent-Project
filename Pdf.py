import os
import comtypes.client
from tkinter import filedialog, Tk

def ppt_to_pdf(input_ppt, output_pdf):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    ppt_file = powerpoint.Presentations.Open(input_ppt)
    ppt_file.SaveAs(output_pdf, FileFormat=32)
    ppt_file.Close()
    powerpoint.Quit()

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the main window

    # Ask user to select input PowerPoint file
    input_ppt = filedialog.askopenfilename(title="Select PowerPoint file", filetypes=[("PowerPoint files", "*.pptx;*.ppt")])

    # Ask user to select output PDF file
    output_pdf = filedialog.asksaveasfilename(title="Save PDF as", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if input_ppt and output_pdf:
        # Convert PPT to PDF
        ppt_to_pdf(input_ppt, output_pdf)

        print("Conversion completed!")
    else:
        print("No input or output file selected.")
