import PIL
from PIL import Image
import pytesseract
import subprocess


#subprocess.run('start microsoft.windows.camera:',shell=True)
im = Image.open("C:\\Users\\DANISH\\PycharmProjects\\spam_detector\\NLP-Deployment-Heroku\\Zuck-Spam-Email.png")
im1 = Image.open("C:\\Users\\DANISH\\PycharmProjects\\spam_detector\\NLP-Deployment-Heroku\\ham.jpg")
text = pytesseract.image_to_string(im,lang='eng')
text2 = pytesseract.image_to_string(im1,lang='eng')
#with open("input_text.txt","w") as f:
    #f.write(text)
#with open("input_text.txt","r") as f:
    #print(f.read())
with open("ham_text.txt","w") as f:
    f.write(text2)
with open("ham_text.txt","r") as f:
    print(f.read())
