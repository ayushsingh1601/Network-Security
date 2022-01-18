from tkinter import * 
import string
import re
import operator

root = Tk()
root.title('ATBASH CIPHER')
root.geometry('500x300')

#menu bar


menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)

a = Label(root, text = 'Plain-text ->')
a.place(x=0,y=35)



# main driver function
def atbash(each):
	
	temp_string=""
	for val in each : 
		
		#reverses the english alphabet letters
		if val in string.ascii_lowercase or string.ascii_uppercase:
			reverse=0
			if val in string.ascii_lowercase:
				reverse=122-(ord(val)-97)
			else :
				reverse=90-(ord(val)-65)
			temp_string=temp_string+chr(reverse)
		else : 
			temp_string=temp_string + val
	
	return temp_string


count = 0
def clicked():
	global count
	if (count%2)==0 :
		result.configure(text = atbash(inp.get()))
		btn.configure(text = 'decrypt!')
	else :
		result.configure(text = inp.get())
		btn.configure(text = 'encrypt!')
	count+=1




inp = Entry(root, width=30)
inp.place(x=100,y=35)
btn = Button(root,bg = 'blue', text = 'encrypt!',
	bd = '5',command=clicked)
btn.place(x=200,y=60)



#just the layout part
lbl = Label(root, text = 'ATBASH ENCRYPTION',bg='blue')
lbl.place(x=100,y=0)

btin = Button(root,bd = '5', text = 'Exit', command = root.destroy)
btin.place(x=400,y=0) 

C = Canvas(root, background ="green", 
           height = 100, width = 300) 
C.place(x=100,y=100)


sim = Label(root,text='atbash cipher',bg='yellow')
sim.place(x=200,y=100)

encrypt = Label(root, text = 'Cipher Text!   ==>> ')
encrypt.place(x=180,y=120)


result = Label(root, text = 'dfgf',bg = 'yellow', fg = 'black')
result.place(x=180,y=150)

root.mainloop()
