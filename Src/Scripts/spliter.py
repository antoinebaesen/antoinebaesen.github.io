from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

def split_pages(input_pdf, output_pdf):
    with open(input_pdf, 'rb') as file:
        reader = PdfFileReader(file)
        writer = PdfFileWriter()

        for page_num in range(0, reader.numPages, 2):
            page = reader.getPage(page_num)
            # Récupérer les dimensions de la page A4 (en points)
            page_width = page.mediaBox.getUpperRight_x()
            page_height = page.mediaBox.getUpperRight_y()

            # Créer une page A3 à partir de 2 pages A4
            new_page = writer.addBlankPage(width=page_width, height=page_height)
            new_page.mergeTranslatedPage(page, 0, 0)
            
            if page_num + 1 < reader.numPages:
                page2 = reader.getPage(page_num + 1)
                new_page.mergeTranslatedPage(page2, page_width, 0)

        # Change les pages A3 en A4
        for page_num in range(0, writer.getNumPages()):
            page = writer.getPage(page_num)
            page.mediaBox.upperRight = (page_width, page_height)
            page.mediaBox.lowerLeft = (0, 0)

        # Enregistrer le résultat dans un nouveau fichier PDF
        with open(output_pdf, 'wb') as out_file:
            writer.write(out_file)

if __name__ == "__main__":
    args = sys.argv[1:]
    if(len(args) != 2):
        print("Usage: python spliter.py input.pdf output.pdf")
        sys.exit(1)

    input_pdf = args[0] # Chemin vers le fichier PDF d'entrée
    output_pdf = args[1] # Chemin vers le fichier PDF de sortie

    split_pages(input_pdf, output_pdf)
