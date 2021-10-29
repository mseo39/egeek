from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb=Workbook()
ws=wb.active

img= Image('KakaoTalk_20210913_174428806.jpg')
img.height=100
img.width=100

ws.add_image(img, 'A2')
wb.save('image2.xlsx')