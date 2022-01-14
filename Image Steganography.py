# To programma auto asxoleite me tin steagongrafia eikonon, tin apokripsi minimaton mesa se eikones kai tin emfanisi auton
# Aksiologa site pou eksigoun tin steganografia eikonon einai ta eksis:
# https://www.geeksforgeeks.org/image-steganography-in-cryptography/
# https://www.mygreatlearning.com/blog/image-steganography-explained/
# mesa stin bibliothiki stepic dinontai epipleon plirofories gia to pos ginete i apokripsi kai i emfanisi minimaton se kai apo eikones


# oi apariaitites bibliothikes

# tkninter gia GUI
# PIL (pillow) gia eisagogi kai eksagogi eikonon
# stepic gia encoding kai decoding
from tkinter import *
from PIL import Image
import stepic


# To programma exei treis basikes sinartisis oi opoies antiprosopeuoun ena parathiro
# H encode_image antiprosopeuei to parathiro "Encode an Image"
def encode_image():
    # GUI ftiagmeno me tkinter
    # ftiaxnei to onoma tou parathirou, to megethos tou, to xroma tou kai keimeno pano sto parathiro
    encode_wn = Toplevel(root)
    encode_wn.title("Encode an Image")
    encode_wn.geometry('600x260')
    encode_wn.resizable(0, 0)
    encode_wn.config(bg='Gray')
    Label(encode_wn, text='Encode an Image', font=("Comic Sans MS", 15), bg='Gray').place(x=220, rely=0)

    Label(encode_wn, text='Enter the path to the image with extension:', font=("Times New Roman", 13),
          bg='Gray').place(x=10, y=45)
    Label(encode_wn, text='Enter the data to be encoded:', font=("Times New Roman", 13), bg='Gray').place(
        x=10, y=90)
    Label(encode_wn, text='Enter the new image path with extension (only .png images can be decoded):', font=("Times New Roman", 13), bg='Gray').place(x=10, y=135)

    # Mpares gia eisagogi onomaton tis iparxousas eikonas, to krifou minimatos kai tis neas kodikopoiimenis eikonas
    img_path = Entry(encode_wn, width=70)
    img_path.place(x=10, y=70)

    text_to_be_encoded = Entry(encode_wn, width=70, show="*")
    text_to_be_encoded.place(x=10, y=115)
    
    new_img = Entry(encode_wn, width=70)
    new_img.place(x=10, y=160)
    
    # meso tis encode tis stepic tropopoieitai to minima kai to anamigniei sta pixels tis eikonas
    def encode(img, message):
        # meso tis PIL eisagete to onoma mias eikonas apo ton ipologisti
        img = Image.open(img, 'r')     
        # eisagoume to minima kai i stepic to kodikopoiei stin eikona
        message = text_to_be_encoded.get()
        message = message.encode()
        # H PIL ftiaxnei mia nea eikona sxedon oloeidia me tin arxiki, alla exontas to kodikopiimeno minima mesa
        encoded_img = stepic.encode(img, message)
        encoded_img.save(new_img.get())
        
    # otan patite to koumpi pirodotite i sinartisi encode
    Button(encode_wn, text='Encode the Image', font=('Helvetica', 12), bg='LightGray', command=lambda:encode(img_path.get(), text_to_be_encoded.get())).place(x=220, y=195)


#H decode_image antiprosopeuei to parathiro "Decode an Image"
def decode_image():
    # GUI ftiagmeno me tkinter
    # omoios me tkinter
    decode_wn = Toplevel(root)
    decode_wn.title("Decode an Image")
    decode_wn.geometry('600x330')
    decode_wn.resizable(0, 0)
    decode_wn.config(bg='Grey')

    Label(decode_wn, text='Decode an Image', font=("Comic Sans MS", 17), bg='Grey').place(x=220, rely=0)

    Label(decode_wn, text='Enter the path to the image with extension (works only with .png format):', font=("Times New Roman", 14),
          bg='Grey').place(x=10, y=50)

    # eisodos onomatos tis kodikopiimenis eikonas
    img_entry = Entry(decode_wn, width=72)
    img_entry.place(x=10, y=85)

    # meso tis decode tis stepic apokodikopoieitai to minima apo mia eikona
    def decode(img):
        # H PIL anoigei tin eikona me to krifo minima kai i stepic apokodikopoiei to minima kai to emfanizei
        img = Image.open(img, 'r')
        decoded_msg = stepic.decode(img)
    
        Label(decode_wn, text='The hidden message is:', font=("Times New Roman", 14), bg='Gray').place(x=215, y=160)
        
        Label(decode_wn, text=decoded_msg, font=("Times New Roman", 14), bg='Silver', wraplength=580).place(x=10, y=190)
    
    # otan patite to koumpi pirodotite i sinartisi decode    
    Button(decode_wn, text='Decode the Image', font=('Helvetica', 12), bg='LightGrey', command=lambda:decode(img_entry.get())).place(x=220, y=120)

    


# Kentriko parathiro, antiprosopeuei to "Image Steganography Application"
# omoios me tkinter
root = Tk()
root.title('Image Steganography Application')
root.geometry('350x150')
root.resizable(0, 0)
root.config(bg='Gray')

Label(root, text='Image Steganography Application', font=('Comic Sans MS', 15), bg='Gray',
      wraplength=300).place(x=80, y=0)

# Otan patite to koumpi anoigei to parathiro "Encode an Image"
Button(root, text='Encode an Image', width=12, font=('Helvetica', 12), bg='LightGray', command=encode_image).place(
    x=30, y=80)

# Otan patite to koumpi anoigei to parathiro "Decode an Image"
Button(root, text='Decode an Image', width=12, font=('Helvetica', 12), bg='LightGray', command=decode_image).place(
    x=190, y=80)

# Emfanizei to kentriko parathiro
root.update()
root.mainloop()





# Liges apantiseis se erotisis pou akoustikan peri tou programmatos

# An kodikopiisoume mia eikona pano apo mia fora to minima pou tha emfanistei einai to teleutaio pou eisixthei
# An to minima pou tha emfanistei sto parathiro "Decode an Image" einai poli megalo sinexizei stis epomens apo kato grammes
# Ama ginei paralili apokodikopoiisi dio i parapano eikonon xoris na kleisoume kai na ksananiksoume to parathiro to neo minima the emfanizete pano apo to palio
#    An to kainourio einai mikrotero apo to palio, anakateuontai
# Otan eisagoume ena minima gia na kodikopoieithei se mia eikona mporoume na baloume keno
#    To minima antikathistate me "*" gia na min mporei na diabastei apo eksoterikous paratirites
