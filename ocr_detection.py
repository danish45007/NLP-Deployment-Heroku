# Package importing into the code...
try:
    import PIL
    from PIL import Image
    import pytesseract
    import subprocess
    import os
except Exception as e:
    print("Some modules are missing {}".format(e))

#Code Starts Here
#subprocess.run(' ',shell=True)
#Importing the Image into the coden space
im = Image.open("C:\\Users\\DANISH\\PycharmProjects\\spam_detector\\NLP-Deployment-Heroku\\Zuck-Spam-Email.png")
im1 = Image.open("C:\\Users\\DANISH\\PycharmProjects\\spam_detector\\NLP-Deployment-Heroku\\ham.jpg")
#Converting the Image Character into the real Text.
text = pytesseract.image_to_string(im,lang='eng')
text2 = pytesseract.image_to_string(im1,lang='eng')
#with open("input_text.txt","w") as f:
    #f.write(text)
#with open("input_text.txt","r") as f:
    #print(f.read())
with open("ham_text.txt","w") as f:
    #Opening the file into the code space
    f.write(text)
with open("ham_text.txt","r") as f:
    # Reading the character present into the image.
    print(f.read())

###################################################################
