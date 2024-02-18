import qrcode
from docx import Document
from datetime import datetime
from io import BytesIO
from docxtpl import DocxTemplate, InlineImage
import os
from docx.shared import Cm

def main(data, title, sub, source, tmpltpath):
    def generate_qr_code(subject, sub_bab, url):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        file_path = f"./source/{subject}_{sub_bab}_source.png"

        # Save the QR code image directly to the specified file path
        img.save(file_path, format="PNG")
        
        return file_path

    def building():
        subject = title
        sub_bab = sub
        url = source

        return subject, sub_bab, url

    def generate_docx(subject, sub_bab, url, file_path, data, tmpltpath):
        doc = DocxTemplate(f'{tmpltpath}')
        print(data)
        
        # qrsource = generate_qr_code(url)
        # Fill in template variables
        context = {
            'subject': subject.upper(),
            'sub_bab': sub_bab.capitalize(),
            'source': InlineImage(doc, file_path, width=Cm(1.5)),  
            'date': datetime.now().strftime("%d-%m-%Y"),
            'data': data,
        }

        # Apply context to the template
        doc.render(context)

        # Save the document
        name = f"{subject}-{sub_bab}"
        doc.save(f'./output/{name}.docx')

        print(f'File {name}.docx berhasil dibuat!')

    data = data
    subject, sub_bab, url = building()
    file_path = generate_qr_code(subject, sub_bab, url)
    generate_docx(subject, sub_bab, url, file_path, data, tmpltpath)