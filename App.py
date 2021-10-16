#setup
import os
if os.path.isdir('data')==False:
	os.system('mkdir data')
	os.system('mkdir media')
	with open('data/path','w') as f:
		f.write('media/')
	with open('data/file_type','w') as f:
		f.write('1')
try:	
	from pytube import YouTube
	from pytube.cli import on_progress
except:
	os.system('pip install pytube')
	from pytube import YouTube
	from pytube.cli import on_progress
	
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as msg
import time

#SETTING DATABASE??😀

setup={

'GUI_BG':'grey40',
'downloading_button_stream':'green',
'status_bar_bg':'white',
'settingpage_save_button':'light green',
'settingpage_cancel_button':'pink',
'Entry_box_bg':'light yellow'

}


number=0
root=Tk()
width='720'
height='1245'
root.geometry(f'{width}x{height}')
root.maxsize(width,height)
root.minsize(width,height)
bgnd=setup['GUI_BG']
Canvas(root,width=width,height=height,bg=bgnd).place(x=0,y=0)
		


class button:
	def exit_mode(self):
		self.value=msg.askquestion('Exit','Did you Want to exit !')
		if self.value=='yes':
			quit()
	def save_settings(self):
		l=['data/path','data/file_type']
		l2=[path.get(),(file_type.get())]
		j=0
		for i in l:
			with open(i,'w') as f:
				f.write(str(l2[j]))
				j+=1
		msg.showinfo('saved','Setting saved Sucessfully !')
	
	def author(self):
		msg.showinfo('author','Developer DURGESH RAWAT ')
	def cancel_settings(self):
		msg.showwarning('cancelled','Cancelled by USER !')
	def info(self):
		msg.showinfo('About','Hello There USER,\nwelcome in Yt Loader \nAn online utility for downloading\nYoutube videos.')	
	def download(self):
		global error
		error=False
		sc=Toplevel()
		sc.title('Processing')
		sc.geometry('600x600+20+500')
		Label(sc,text='Choice For Your Request ....').place(x=20,y=20)
			
		with open('data/livelink','w') as f:
			f.write(linkinput.get())
		
		intput = 'YouTube'
		with open('data/path','r') as r:
			pathh=r.readlines()
		with open('data/livelink','r') as r:
			link=r.readlines()
			
		url = link[0]	
		try:
			yt = YouTube(url,on_progress_callback = on_progress)
    		#video_title=yt.title
		except:
			msg.showwarning('error','Check your link\nand Try again !')
		
		with open('data/file_type','r') as f:
			d=f.readlines()
			
		if d[0]=='1':
			Z= yt.streams.filter(progressive=True,file_extension='mp4')
		else:
			Z=yt.streams.filter(only_audio=True)# for audio
		
		
		listbox=Listbox(sc)
		i=1
		for A in Z:
			listbox.insert(i,f'{i} - [{A.resolution,A.type,A.subtype}]')
			i+=1
		listbox.place(x=50,y=65)#
				
		def give():
			global error
			error=False
			value=listbox.curselection()
			
			no = value[0] - 1
			video = Z[no]
			file_size=(video.filesize)
				
			def down():
				video.download(pathh[0])
				status.set('status > Downloaded sucessfully !')
	
				
			if msg.askquestion('File Details',f'Title : file Size : {file_size//1024} kb\nDid you want to download it')=='yes':
				if True:
					status.set('status > Downloading Started ..')
				try:
					down()
				except:
					error=True
				if error==False:
					msg.showinfo('Notification','File Downloaded Sucessfully !')
				else:
					msg.showwarning('Failed','Downloading cancelled !')
			else:
				msg.showinfo('info','Downloading canclled by USER !')
				
		Button(sc,text='Download',command=give,bg=setup['downloading_button_stream']).place(x=55,y=470)		
	def clearentry(self):
		linkentry.delete(0,END)	

#initialise a object for buttons
b=button()

class homepage:
	def __init__(self):
		self.bg='white'

	def home(self):
		#menubar
		self.main_menubar=Menu(root)
		self.main_menubar.add_command(label='Home',font='default 7')
		self.main_menubar.add_command(label='Downloads',font='default 7',command=downloadpage)
		self.main_menubar.add_command(label='Setting',font='default 7',command=settingpage)
		root.config(menu=self.main_menubar)

		#helpmenu
		self.help_menu=Menu(self.main_menubar)
		self.help_menu.add_command(label='About',font='default 7',command=b.info)
		self.help_menu.add_command(label='Developer',font='default 7',command=b.author)
		self.help_menu.add_command(label='Exit',font='default 7',command=b.exit_mode)

		root.config(menu=self.main_menubar)
		self.main_menubar.add_cascade(label='Help',font='default 7',menu=self.help_menu)

		#designing
		Label(root,text='Welcome in YT downloader',font='default 8',bg=bgnd).place(x=20,y=20)
		Label(root,text='• Download your favourit videos Very easily. ',bg=bgnd,font='default 5').place(x=50,y=60)
		Label(root,text='• Step 1 paste Your link in entry Box',bg=bgnd,font='default 5').place(x=50,y=90)
		Label(root,text='• step 2 Then click on Download Now to Download Video/audio',bg=bgnd,font='default 5').place(x=50,y=122)
		Label(root,text='• For More intresting Features see setting',font='default 5',bg=bgnd).place(x=50,y=154)		
		Label(root,text='____________________________________________________________',bg=bgnd,font='default 5').place(x=20,y=200)
		

		#link input
		global linkinput
		global linkentry
		linkinput=StringVar()
		linkinput.set('paste your link here ')
		#link_address_notation=Label(root,text='PASTE HERE',padx=40)
		#link_address_notation.place()
		#link_address_notation.place(x=238,y=290)
		linkentry=Entry(root,textvariable=linkinput,width=27,bd=1,relief='flat',fg='dodger blue',bg=setup['Entry_box_bg'],font='default 8')
		#linkentry=Entry(root,textvariable=linkinput,bd=1,font=('Arial',9),highlightthickness=0,insertbackground='red',relief='flat',width=25)
		linkentry.bind('<Button-1>',self.linkentry__)
		linkentry.place(x=116,y=250)
		global status
		status=StringVar()
		sb=Label(root,textvariable=status,bg=setup['status_bar_bg'],anchor='sw',padx=20,relief=SUNKEN).pack(side=BOTTOM,fill=X)
		status.set('status > ready')
	def linkentry__(self,event):
		global linkentry,linkinput
		global number
		number+=1
		if number==1:
			linkinput.set('')
			
		

class downloadpage:
	def __init__(self):
		with open('data/path','r') as f:
			self.path=f.readlines()
		self.download_window=Toplevel()
		self.download_window.title('Downloads')
		self.download_window.geometry('500x600+100+100')
		directories=os.listdir(self.path[0])
		n=1
		j=''
		for i in directories:
			if len(i)>40:
				j=i
				i=j[0:30]+j[len(j)-4:len(j)]
			Label(self.download_window,text=f'[{n}] {i}',font='default 5').pack(anchor='sw')
			n+=1
			
class settingpage:
	def __init__(self):
		self.setting_window=Toplevel()
		self.setting_window.geometry('500x700+100+200')
		self.setting_window.title('Settings')
		Label(self.setting_window,text='Downloading Path ',font='default 7').place(x=20,y=10)
		
		global path
		global file_type
		path=StringVar()
		pathentry=Entry(self.setting_window,textvariable=path).place(x=24,y=50)
		f=open('data/path')
		p=f.readlines()
		f.close()
		path.set(p[0])
		
		
		file_type=IntVar()
		Label(self.setting_window,text='Media Type For Downloading ').place(x=20,y=100)
		with open('data/file_type','r') as f:
			d=f.readlines()
		if d[0]=='1':
			file_type.set('1')
		else:
			file_type.set('2')
		but1=Radiobutton(self.setting_window,text='Video',variable=file_type,value=1).place(x=20,y=160)
		but2=Radiobutton(self.setting_window,text='Audio',variable=file_type,value=2).place(x=20,y=200)

		Button(self.setting_window,text='save',bg=setup['settingpage_save_button'],command=b.save_settings).place(x=20,y=620)
		Button(self.setting_window,text='cancel',bg=setup['settingpage_cancel_button'],command=b.cancel_settings).place(x=190,y=620)




#graphics
if True:
	"""
	bgpic=PhotoImage(file='data/assets/bg.png')
	l=Label(root,image=bgpic)
	l.image=bgpic
	l.place(x=0,y=0)
	"""
	download_icon=PhotoImage(file = r'data/assets/dbblack.png')#rpath
	downloadicon = download_icon.subsample(4,4) 
	reset_option=PhotoImage(file=r'data/assets/reset1.png')
	reset_option=reset_option.subsample(14,14)

	link_icon=PhotoImage(file=r'data/assets/link.png')
	link_icon=link_icon.subsample(1,1)

	Button(root,image=downloadicon,command=b.download,bg=bgnd).place(x=290,y=300)
	Button(root,image=reset_option,command=b.clearentry,bg=bgnd).place(x=220,y=300)
	Label(root,image=link_icon,bg=bgnd).place(x=70,y=260)

App=homepage()
App.home()
root.mainloop()
#DURGESH-RAWAT
