# import customtkinter as ctk
from tkinter import *
# import AppearanceModeTracker
from customtkinter import *
from PIL import ImageTk,Image

# from tkinter import ttk
from customtkinter import filedialog
# from packaging import version
import os,shutil
from tkinter import messagebox
class SortingApp:
    def __init__(self,root):    
        self.root = root
        self.root.title("Sorting Application | Developed By Kamlesh")
        self.root.geometry("1520x800+0+0")
        setback = set_appearance_mode("light")
        # self.photo_image = ImageTk.PhotoImage(file="back.jpg")
        # self.lbl_phone_image = Label(self.root,image=self.photo_image,bd=0).place(x=2,y=0)
        self.logo = ImageTk.PhotoImage(file="64x64.png") 
        title = CTkLabel(master=self.root,text="FILE  SORTING  APPLICATION",font=("Inter",40,"bold"),anchor="w",image=self.logo, compound=LEFT,padx=23,pady=12)
        # title.place(x=0,y=0,relwidth=1)
        title.pack(fill=X,side=TOP)


        #=============section1==================================
        self.var_foldername = StringVar()
        lbl_select_folder = CTkLabel(self.root,text="Select Folder :",font=("Inter",25,"bold"))
        lbl_select_folder.place(x=22,y=100)

        txt_folder_name = CTkEntry(self.root,placeholder_text="Select Folder",width=700,border_width=3,state='readonly',textvariable=self.var_foldername)
        txt_folder_name.place(x=190,y=102)

        btn_browse = CTkButton(self.root,text="Browse",font=("Inter",20,"bold"),hover_color="#FFB760",cursor="hand2",command=self.browse_function)
        btn_browse.place(x=920,y=100)
 
        # hr = Label(self.root,bg="light gray")
        # hr.place(x=25,y=190,width=1300,height=2)

        #===============section 2+++=================================
        lbl_support_extension = CTkLabel(self.root,text="Various Support Extension :",font=("Inter",25,"bold"))
        lbl_support_extension.place(x=22,y=170)


        self.image_extensions = ["Image Extensions",".png",".jpg",'.psd','.ai'] 
        self.audio_extensions = ["Audio Extensions",".amr",".mp3"] 
        self.video_extensions = ["Video Extensions",".mp4",".avi",".mpeg4"] 
        self.doc_extensions = ["Document Extensions",".doc",".xlsx"] 
        self.prog_extensions = ["Programming Extensions",".cpp",".c","pl"]

        self.folders = {
             'videos':self.video_extensions,
             'audios':self.audio_extensions,
             'images':self.image_extensions,
             'documents':self.doc_extensions,
             'software':self.prog_extensions
        }
        
        




        self.image = CTkComboBox(self.root,values=self.image_extensions,font=("Inter",15,"bold"),width=200,dropdown_hover_color="white",state='readonly',justify=CENTER)
        self.image.place(x=22,y=240)
        self.image.set("Image Extension")
        # ==============================================
        self.image = CTkComboBox(self.root,values=self.video_extensions,font=("Inter",15,"bold"),width=200,dropdown_hover_color="white",state='readonly',justify=CENTER)
        self.image.place(x=300,y=240)
        self.image.set("Video Extensions")

        self.image = CTkComboBox(self.root,values=self.audio_extensions,font=("Inter",15,"bold"),width=200,dropdown_hover_color="white",state='readonly',justify=CENTER)
        self.image.place(x=600,y=240)
        self.image.set("Audio Extensions")

        self.image = CTkComboBox(self.root,values=self.doc_extensions,font=("Inter",15,"bold"),width=200,dropdown_hover_color="white",state='readonly',justify=CENTER)
        self.image.place(x=900,y=240)
        self.image.set("Document Extensions")

        self.image = CTkComboBox(self.root,values=self.prog_extensions,font=("Inter",15,"bold"),width=200,dropdown_hover_color="white",state='readonly',justify=CENTER)
        self.image.place(x=1200,y=240)
        self.image.set("Others")



        #=============section 3=====================
        #==============all images==============================
        image1 = Image.open("images/final_images.png")
        resize_image1 = image1.resize((300,300))
        image2 = Image.open("images/finalfinal_video.png")
        resize_image2 = image2.resize((300,300))
        image3 = Image.open("images/final_music.png")
        resize_image3 = image3.resize((300,300))
        image4 = Image.open("images/512x512.png")
        resize_image4 = image4.resize((300,300))
        image5 = Image.open("images/final_prog.png")
        resize_image5 = image5.resize((300,300))
        

        self.image_icon = ImageTk.PhotoImage(resize_image1)
        self.audio_icon = ImageTk.PhotoImage(resize_image2)
        self.video_icon = ImageTk.PhotoImage(resize_image3)
        self.doc_icon = ImageTk.PhotoImage(resize_image4)
        self.other_icon = ImageTk.PhotoImage(resize_image5)

        frame1 = CTkFrame(self.root,width=1470,height=370,border_color="black",border_width=2)
        frame1.place(x=22,y=300)  

        self.lbl_total_files = CTkLabel(frame1,text="Total Files : ",font=("Inter",25,"bold"))
        self.lbl_total_files.place(x=22,y=11)

        self.lbl_image = CTkLabel(master=frame1,image=self.image_icon,text="",compound=TOP,font=("Intern",20,"bold"))
        self.lbl_image.place(x=22,y=50)

        self.lbl_audio = CTkLabel(master=frame1,image=self.audio_icon,text="",compound=TOP,font=("Inter",20,"bold"))
        self.lbl_audio.place(x=300,y=50)

        self.lbl_video = CTkLabel(master=frame1,image=self.video_icon,text="",compound=TOP,font=("Inter",20,"bold"))
        self.lbl_video.place(x=600,y=50)

        self.lbl_doc = CTkLabel(master=frame1,image=self.doc_icon,text="",compound=TOP,font=("Inter",20,"bold"))
        self.lbl_doc.place(x=900,y=50)

        self.lbl_other = CTkLabel(master=frame1,image=self.other_icon,text="",compound=TOP,font=("Inter",20,"bold"))
        self.lbl_other.place(x=1200,y=50)

        #======================section 3(buttons) =============================
        self.lbl_status = CTkLabel(self.root,text="STATUS : ",font=("Inter",25,"bold"))
        self.lbl_status.place(x=20,y=700)

        self.lbl_total = CTkLabel(self.root,text="",font=("Inter",25,"bold"))
        self.lbl_total.place(x=200,y=700)

        self.lbl_moved = CTkLabel(self.root,text="",font=("Inter",25,"bold"))
        self.lbl_moved.place(x=400,y=700)

        self.lbl_left = CTkLabel(self.root,text="",font=("Inter",25,"bold"))
        self.lbl_left.place(x=600,y=700)
        

        # =====BUTTONS=====================================
        self.btn_clear = CTkButton(self.root,text="CLEAR",font=("Inter",20,"bold"),hover_color="#FF5721",cursor="hand2",fg_color="#FF0400",border_width=3,command=self.clear)
        self.btn_clear.place(x=990,y=700)

        self.btn_execute = CTkButton(self.root,text="EXECUTE",font=("Inter",20,"bold"),hover_color="#FF5721",cursor="hand2",fg_color="#000000",text_color="#000000",border_width=3,command=self.start_function,state=DISABLED)
        self.btn_execute.place(x=1230,y=700)


    def Total_count(self):
        images =0
        audios =0
        videos =0
        documents =0
        others =0
        self.count =0
        cmbine_list =[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                self.count+=1
                ext='.'+i.split(".")[-1]
                for folder_name in self.folders.items():
                    # print(folder_name)   
                    for x in folder_name[1]:
                        cmbine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=='images':
                        images+=1          
                    if ext.lower() in folder_name[1] and folder_name[0]=='audios':
                        audios+=1          
                    if ext.lower() in folder_name[1] and folder_name[0]=='videos':
                        videos+=1          
                    if ext.lower() in folder_name[1] and folder_name[0]=='documents':
                        documents+=1          
                    # if ext.lower() in folder_name[1] and folder_name[0]=='others':
                    #     others+=1          
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                ext='.'+i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    others+=1
        self.lbl_image.configure(text="Total Images\n"+str(images))
        self.lbl_audio.configure(text="Total Audios\n"+str(audios))
        self.lbl_video.configure(text="Total Videos\n"+str(videos))
        self.lbl_doc.configure(text="Total Documents\n"+str(documents))
        self.lbl_other.configure(text="Total Others\n"+str(others))
        self.lbl_total_files.configure(text="Total Files :"+str(self.count))    
    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING") 
        if op!=None:
            self.var_foldername.set(str(op))
            self.directory =self.var_foldername.get()
            self.other_name ='others'
            self.rename_folder()
            self.all_files=os.listdir(self.directory)
            length =len(self.all_files)
            count=1
            self.Total_count()
            self.btn_execute.configure(state=NORMAL)
            # for i in self.all_files:
            #     if os.path.isfile(os.path.join(self.directory,i))==True:
            #         self.create_move(i.split(".")[-1],i)
                # print(f"Total Files :{length}|Done:{count}")   
                # count+=1 
    def start_function(self):
            if self.var_foldername.get()!="":
                self.btn_clear.configure(state=DISABLED)
                c=0
                for i in self.all_files:
                    if os.path.isfile(os.path.join(self.directory,i))==True:
                        c+=1  
                        self.create_move(i.split(".")[-1],i)  
                        self.lbl_total.configure(text="TOTAL :"+str(self.count))
                        self.lbl_moved.configure(text="MOVED :"+str(c))
                        self.lbl_left.configure(text="LEFT :"+str(self.count-c)) 

                        self.lbl_total.update()
                        self.lbl_moved.update()
                        self.lbl_left.update() 
                          
                messagebox.showinfo("Success","All Files has been Moved Successfully!....")    
                self.btn_execute.configure(state=DISABLED) 
                self.btn_clear.configure(state=NORMAL)   
            else:
                messagebox.showerror("Error","Please select the Directory!!..")             
    
    def clear(self):
        self.btn_execute.configure(state=DISABLED) 
        self.var_foldername.set("")
        self.lbl_total.configure(text="")
        self.lbl_moved.configure(text="")
        self.lbl_left.configure(text="") 
        self.lbl_image.configure(text="")
        self.lbl_audio.configure(text="")
        self.lbl_video.configure(text="")
        self.lbl_doc.configure(text="")
        self.lbl_other.configure(text="")
        self.lbl_total_files.configure(text="Total Files : ")    
 
    
    
    
    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,self.other_name))

    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))    
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directory):    
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))    

   


if __name__=='__main__':
    root = CTk()
    obj = SortingApp(root)
    root.mainloop()        
