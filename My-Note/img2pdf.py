import os
from PIL import Image
from io import BytesIO
from PyPDF2 import PdfMerger

# 定义文件夹路径和PDF文件名
folder_path = 'C:\\Users\\cumth\\Pictures\\xw-excrise'
pdf_file_name = 'xw-excrise.pdf'

# 获取文件夹中的所有图片
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

# 创建一个PdfFileMerger对象
merger = PdfMerger()

# 遍历所有图片并将其添加到PdfFileMerger对象中
for image_file in image_files:
    # 打开图片文件并将其转换为PDF格式
    image = Image.open(os.path.join(folder_path, image_file))
    with BytesIO() as f:
        image.save(f, format='PDF')
        pdf_bytes = f.getvalue()
    # 将PDF字节流添加到PdfFileMerger对象中
    merger.append(BytesIO(pdf_bytes))

# 将所有PDF合并为一个文件
with open(pdf_file_name, 'wb') as f:
    merger.write(f)