import PyPDF2
import sys
from termcolor import colored
import os
import time
from modules import  manage
from getpass import getuser
from getpass import getpass
import platform
from PIL import Image
from pdf2image import convert_from_path
import fitz
import io
from fpdf import FPDF
import glob

colors = ("yellow", "cyan", "blue", "green")

def coloredBold(text, color):
    if color in colors:
       return colored(text, color = color, attrs = ["bold"])
    else:
        raise ValueError("color is not in exists color list")

def banner():
    with open(os.path.realpath("appData/banner"), "r") as banner:
        bannerText = banner.read()
    print(coloredBold("\n" + bannerText + "\n", "blue"))

def detailsShow():
    with open(os.path.realpath("appData/details"), "r") as heloFile:
        heloText = heloFile.read()
    print(f"\n{heloText}\n")

def loading():
    if os.name == "nt":
            print("Loading......")
            time.sleep(1)
            os.system("cls")
    elif os.name == "posix":
            print("Loading......")
            time.sleep(1)
            os.system("clear")
    banner()

def inputPlus(inputText, secret = False):
    if secret:
        secret = getpass(f"{colored('[', 'cyan')}{inputText}{colored(']', 'cyan')}$ ")
        print("\n") 
        return secret
    inputValue = input(f"{colored('[', 'cyan')}{inputText}{colored(']', 'cyan')}$ ")
    print("\n")
    return inputValue

def menu_creator(menuItems):
    menuContent = []
    count = 0
    for item in menuItems:
        content = f"{colored('[', 'cyan')}{count}{colored(']', 'cyan')} {colored(item, 'green', attrs = ['bold'])}"
        menuContent.append(content)
        count+=1
    return menuContent

def main_menu():
    print("\n")
    menus = menu_creator(["exit","app details", "merge", "image to pdf", "pdf to image", "rotate", "get pdf pages", "encrypt", "decrypt", "get pdf text", "pdf details", "get images from pdf", "watermark"])
    for item in menus:
        print (item)
        time.sleep(.1)
    print("\n")

def check_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def check_base_dirs():
    check_dir("temp")
    check_dir("result")
    check_dir("result/pdf_details")
    check_dir("result/pdf_to_images")
    check_dir("result/pdf_extract_images")
    check_dir("result/images_to_pdf")
    check_dir("result/pdf_managed")
    check_dir("result/pdf_merge")
    check_dir("result/pdf_encrypt")
    check_dir("result/pdf_decrypt")
    check_dir("result/pdf_pages")
    check_dir("result/pdf_rotate")
    check_dir("result/pdf_text")
    check_dir("result/pdf_watermark")

def delete_temp():
    if os.path.exists("Temp"):
        filesList = os.listdir("Temp")
        numReq = 0
        for file in filesList:
            path = f"Temp/{file}"
            if os.path.exists(path):
                os.remove(path)
                numReq = numReq + 1
    else:
        os.makedirs("Temp")

def run():
    check_base_dirs()
    main_menu()
    state = inputPlus("Select option")
    if state == "0":
        return False
    elif state == "1":
        detailsShow()
    elif state == "2":
        pdfs = inputPlus("Enter pdf Files path ex(file1.pdf file2.pdf ...)").split(" ")
        outname = inputPlus("Enter outname")
        manage.merge_pdfs(pdfs, outname)
    elif state == "3":
        images = inputPlus("Enter image Files path ex(image1.png image2.jpg ...)").split(" ")
        outname = inputPlus("Enter outname")
        manage.image_to_pdf(images, outname)
    elif state == "4":
        pdf = inputPlus("Enter pdf file path")
        outname = inputPlus("Enter outname")
        manage.pdf_to_image(pdf, outname)
    elif state == "5":
        pdf = inputPlus("Enter pdf file path")
        deg = inputPlus("Enter deg (90 | 180 | 270 | 360)")
        pages = inputPlus("Enter page numbers (0 = all)")
        outname = inputPlus("Enter outname")
        manage.rotate_pdf(pdf, deg, outname, pages)
    elif state == "6":
        pdf = inputPlus("Enter pdf file path")
        pages = inputPlus("Enter pdf pages ex(1 2 6 2 20) None = all | 0 = all").split(" ")
        if pages == "":
            pages = '0'
        outname = inputPlus("Enter outname")
        manage.get_pages(pdf, pages, outname)
    elif state == "7":
        pdf = inputPlus("Enter pdf file path")
        password = inputPlus("Enter password", True)
        outname = inputPlus("Enter outname")
        manage.encrypt(pdf, outname, password)
    elif state == "8":
        pdf = inputPlus("Enter pdf file path")
        password = inputPlus("Enter password", True)
        outname = inputPlus("Enter outname")
        manage.decrypt(pdf, outname, password)
    elif state == "9":
        pdf = inputPlus("Enter pdf file path")
        outname = inputPlus("Enter outname")
        manage.get_text(pdf, outname)
    elif state == "10":
        pdf = inputPlus("Enter pdf file path")
        outname = inputPlus("Enter outname")
        manage.details_pdf(pdf, outname)
    elif state == "11":
        pdf = inputPlus("Enter pdf file path")
        outname = inputPlus("Enter outname")
        manage.get_images(pdf, outname)
    elif state == "12":
        pdf = inputPlus("Enter pdf file path")
        watermark = inputPlus("Enter watermark file path")
        pages = inputPlus("Enter pdf pages ex(1 2 6 2 20) None = all | 0 = all").split(" ")
        if pages == "":
            pages = '0'
        outname = inputPlus("Enter outname")
        manage.watermark(pdf, outname, watermark, pages)