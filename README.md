# PDF-Rend
DESCRIPTION
    You can manage PDF files with this tool

    For example
    1- Turn them into photos
    2- Extract the photos inside the files
    3- Paste the PDFs together
    4- Convert photos to PDF
    5. Encrypt the PDF
    6. Decrypt encrypted PDFs
    7- Extract the texts inside the PDF
    8. Extract different pages
    9- Rotate the pages by 90
    
INSTALL

Run

<code>git clone https://github.com/Alishahidi/PDF-Rend.git</code>

<code>cd PDF-Rend</code>

<code>sudo chmod +x install.sh</code>

<code>sudo ./install.sh</code>


USAGE
       python3 pdf.py -f file-name [OPTIONS]

OPTIONS Help

       For merge pdfs

            python3 pdf.py -f file1.pdf file2.pdf --merge --outname yourname

       For convert pdf to images

            python3 pdf.py -f file.pdf --to_image --outname yourname

       For images to pdf

            python3 pdf.py -f file1.jpg file2.png --image_pdf --outname yourname

       For rotate pdf

          rotate All page

               python3 pdf.py -f file.pdf --rotate --deg 90 --outname yourname

          rotate selected page
               python3 pdf.py -f file.pdf --rotate --deg 90 --page 1 5 3 --outname yourname

       For get pdf page

            python3 pdf.py -f file.pdf --get_page --page 1 3 5 --outname yourname

       For encrypt pdfs

            python3 pdf.py -f file.pdf --encrypt --password yourSecretPassword --outname yourname

       For decrypt pdfs

            python3 pdf.py -f file.pdf --decrypt --password yourSecretPassword --outname yourname

       For get pdf pages text

            python3 pdf.py -f file.pdf --get_text --outname yourname

       For get pdf Details

            python3 pdf.py -f file.pdf --details --outname yourname

       For get images into pdf

           python3 pdf.py -f file.pdf --get_image --outname yourname

COPYRIGHT
       Copyright https://github.com/alishahidi 2021 Free Python Tools
