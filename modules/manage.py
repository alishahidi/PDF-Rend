from modules import loading

def rotate_pdf(path, deg, output, pages = 0):
    if pages == "0":
        pages = "all"
    pdf_writer = loading.PyPDF2.PdfFileWriter()
    pdf = loading.PyPDF2.PdfFileReader(path)
    pages_num = pdf.getNumPages()

    if pages == "all":
        for i in range(0, pages_num):
            page = pdf.getPage(i).rotateClockwise(int(deg))
            pdf_writer.addPage(page)
    else:
        for i in range(0, pages_num):
            if str(i + 1) in pages:
                page = pdf.getPage(i).rotateClockwise(int(deg))
                pdf_writer.addPage(page)
            else:
                page = pdf.getPage(i)
                pdf_writer.addPage(page)

    output = "result/pdf_rotate/" + output + ".pdf"
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Save [{output}]")


def merge_pdfs(paths, output):
    pdf_writer = loading.PyPDF2.PdfFileWriter()

    for path in paths:
        pdf_reader = loading.PyPDF2.PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    output = "result/pdf_merge/" + output + ".pdf"
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Save [{output}]")

def image_to_pdf(images, output):
    pdf = loading.FPDF()

    for x in images:
        x.replace(".pdf", "")

    for imageFile in images:
        cover = loading.Image.open(imageFile)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        # given we are working with A4 format size 
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

        # get page orientation from image size 
        orientation = 'P' if width < height else 'L'

        #  make sure image size is not greater than the pdf format size
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

        pdf.add_page(orientation=orientation)

        pdf.image(imageFile, 0, 0, width, height)
    output = f"result/images_to_pdf/{output}.pdf"
    pdf.output(output, "F")
    print(f"Save [{output}]")



def get_pages(path, pages, outname):
    pdf = loading.PyPDF2.PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = loading.PyPDF2.PdfFileWriter()
        for page in pages:
            pdf_writer.addPage(pdf.getPage(int(page) - 1))
        output = f'result/pdf_pages/{outname}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
    print(f"Save [{output}]")

def watermark(input_pdf, outname, watermark, pages = 0):
    if pages == "0":
        pages = "all"
    watermark_obj = loading.PyPDF2.PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = loading.PyPDF2.PdfFileReader(input_pdf)
    pdf_writer = loading.PyPDF2.PdfFileWriter()

    # Watermark all the pages
    pages_num = pdf_reader.getNumPages()
    if pages == "all":
        for i in range(0, pages_num):
            page = pdf_reader.getPage(i)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)
    else:
        for i in range(0, pages_num):
            for page in pages:
                if i == (int(page) - 1):
                    page = pdf_reader.getPage(int(page) - 1)
                    page.mergePage(watermark_page)
                    pdf_writer.addPage(page)
                else:
                    page = pdf_reader.getPage(i)
                    pdf_writer.addPage(page)

    output = f'result/pdf_watermark/{outname}.pdf'
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Save [{output}]")

def encrypt(input_pdf, outname, password):
    pdf_writer = loading.PyPDF2.PdfFileWriter()
    pdf_reader = loading.PyPDF2.PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)
    output = f'result/pdf_encrypt/{outname}.pdf'
    with open(output, 'wb') as fh:
        pdf_writer.write(fh)
    print(f"Save [{output}]")

def decrypt(path, outname, password):
    pdf_writer = loading.PyPDF2.PdfFileWriter()
    pdf = loading.PyPDF2.PdfFileReader(path)
    pdf.decrypt(password=password)
    pages_num = pdf.getNumPages()
    for i in range(0, pages_num):
        page = pdf.getPage(i)
        pdf_writer.addPage(page)

    output = f'result/pdf_decrypt/{outname}.pdf'
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Save [{output}]")


# Details

def details_pdf(path, outname):
    pdf = loading.PyPDF2.PdfFileReader(path)
    details  = pdf.getDocumentInfo()
    pages_num = pdf.getNumPages()
    content = f"""
Information about {path}: 

Author: {details.author}
Creator: {details.creator}
Producer: {details.producer}
Subject: {details.subject}
Title: {details.title}
Number of pages: {pages_num}
        """
    output = f'result/pdf_details/{outname}.txt'
    with open(output, 'w') as out:
        out.write(content)
    print(f"Save [{output}]")

def get_text(path, outname):
    pdfFileObj = open(path, 'rb') 
    pdf = loading.PyPDF2.PdfFileReader(pdfFileObj) 
    pageObj = pdf.getPage(0)
    pages_num = pdf.getNumPages()
    content = ""
    for i in range(0, pages_num):
        page = pdf.getPage(i).extractText()
        content+=f"\n\n--------------------PAGE {i + 1}--------------------\n\n" + page
    output = f'result/pdf_text/{outname}.txt'
    with open(output, 'w') as out:
        out.write(content)
    print(f"Save [{output}]")

def pdf_to_image(path, outname):
    images = loading.convert_from_path(path)
    dirName = path.split('/')[-1].split('.')[0]+"_"+outname
    loading.check_dir("result/pdf_to_images/"+dirName)
    dirName = "result/pdf_to_images/"+dirName
    i = 0
    for page in images:
        page.save(f"{dirName}/images_{i}.jpg", 'JPEG')
        i+=1
    print(f"Save [{dirName}]")

def get_images(path, outname):
    file = path
    pdf_file = loading.fitz.open(file)
    dirName = "result/pdf_extract_images/"+path.split('/')[-1].split('.')[0]+"_"+outname
    loading.check_dir(dirName)
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.getImageList()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = loading.Image.open(loading.io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open(f"{dirName}/image{page_index+1}_{image_index}.{image_ext}", "wb"))
    print(f"Save [{dirName}]")
