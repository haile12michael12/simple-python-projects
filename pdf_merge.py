import PyPDF2

def merge_pdfs(input_paths, output_path):
    pdf_merger = PyPDF2.PdfFileMerger()

    for path in input_paths:
        with open(path, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    # Replace these paths with the paths of your PDF files
    input_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
    output_file = 'merged_output.pdf'

    merge_pdfs(input_files, output_file)
