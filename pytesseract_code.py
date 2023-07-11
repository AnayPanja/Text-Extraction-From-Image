import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
import cv2


img = cv2.imread('student_card.png')
cv2.imshow('sample1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
#print(text)

s = text.split()
#print(s)

k=0
for i in s:
    k+=1
    if i=='Name:':
        name = s[k] + ' ' + s[k+1]
        
print('Name is : ',name)