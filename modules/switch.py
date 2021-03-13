from modules import loading


argvs = loading.sys.argv[1:]


def argv_between(index):
    letIndex = argvs[index + 1]
    indexleft = argvs[index + 1:]
    indexOfitem = len(argvs)
    for item in indexleft:
        if item.startswith("-"):
            indexOfitem = argvs.index(item)
    newargv = argvs[index + 1:indexOfitem]
    return newargv

def outname_file():
    index = argvs.index("--outname")
    between = argv_between(index)
    outname = between[0]
    return outname

def get_file():
    index = argvs.index("-f")
    between = argv_between(index)
    fileName = ""
    if len(between) == 1:
        fileName = between[0]
    elif len(between) > 1:
        filename = between
    return fileName

def deg_pdf():
    index = argvs.index("--deg")
    between = argv_between(index)
    deg = between[0]
    return deg

def get_password():
    if "--pass" in argvs:
        index = argvs.index("--pass")
        between = argv_between(index)
        password = between[0]
    elif "--password" in argvs:
        index = argvs.index("--password")
        between = argv_between(index)
        password = between[0]
    return password

def details():
    with open("appData/details", "r") as details:
        detailsText = details.read()
        print(detailsText)

def pages_pdf():
    index = argvs.index("--page")
    between = argv_between(index)
    pages = between
    return pages

def merge(fileNames, outname):
    loading.manage.merge_pdfs(fileNames, outname)

def image_pdf(fileNames, outname):
    loading.manage.image_to_pdf(fileNames, outname)

def to_image(fileName, outname):
    loading.details.pdf_to_image(fileName, outname)

def rotate(fileName, deg, outname, pages = 0):
    loading.manage.rotate_pdf(fileName, deg, outname, pages)

def get_pages(fileName, pages, outname):
    loading.manage.get_pages(fileName, pages, outname)

def encrypt(fileName, outname, password):
    loading.manage.encrypt(fileName, outname, password)

def decrypt(fileName, outname, password):
    loading.manage.decrypt(fileName, outname, password)

def get_text(fileName, outname):
    loading.details.get_text(fileName, outname)

def details(fileName, outname):
    loading.details.details_pdf(fileName, outname)

def get_image(fileName, outname):
    loading.details.get_images(fileName, outname)