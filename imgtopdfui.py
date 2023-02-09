import PySimpleGUI as sg
import img2pdf as im
from PIL import Image
import os

def img_to_pdf(file_path, pdf_name, output_path):

    img_path = file_path
    pdf_path_name = '{}/{}.pdf'.format(output_path,pdf_name)

    image = Image.open(img_path)
    pdf_bytes = im.convert(image.filename)
    file = open(pdf_path_name, "wb")
    file.write(pdf_bytes)

    image.close()
    file.close()
    sg.popup("PDF criado com sucesso!")

def img_to_pdf_window():
    imgtopdf_layout = [
        [sg.Text("Efetue os seguintes comandos:")],
        [sg.Text("Selecione o arquivo a ser transformado:"), sg.Input(),sg.FilesBrowse("Buscar", key="-IMAGE_FILE-")],
        [sg.Text("Nome do pdf a ser criado: "), sg.InputText(key="-PDF_NAME-")],
        [sg.Text("Destino: "),sg.Input(), sg.FolderBrowse("Escolher", key="-PDF_PATH-")],
        [sg.Ok(),sg.Cancel()]
    ]

    imgToPdfwindow = sg.Window("Image to PDF", imgtopdf_layout)

    while True:
        event, values = imgToPdfwindow.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Ok":
            img_to_pdf(
                file_path = values["-IMAGE_FILE-"],
                pdf_name = values["-PDF_NAME-"],
                output_path=values["-PDF_PATH-"]
            )
            break
    imgToPdfwindow.close()

img_to_pdf_window()
