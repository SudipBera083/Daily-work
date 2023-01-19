from tkinter import* 
from tkinter import messagebox
from PIL import ImageTk, Image
import bonggoQuery
import time
import AppOpener
import webbrowser

from itertools import count, cycle
class ImageLabel(Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 



def wordResizer(sentence):
    data =str(sentence).split(" ")
    q =""
    coun =0
    for i in data:
        if coun<=8:
            q+=" "+i
            coun+=1
        else:
            q+="\n"
            coun=0

    return q




def HomepageGUI():

    

    root =Tk()
    
    root.title("Home  page")
    
    root.geometry("1200x700")
    root.maxsize(1200,700)
    root.minsize(1200,700)

    
    image = Image.open(".\\Daily\\src\\data.png")
 
    # Resize the image using resize() method
    resize_image = image.resize((1200, 700))
 
    img = ImageTk.PhotoImage(resize_image)

    # Create Canvas
    canvas1 = Canvas( root, width = 400,
                 height = 400)
  
    canvas1.pack(fill = "both", expand = True)
  
    # Display image
    canvas1.create_image( 0, 0, image = img, 
                     anchor = "nw")
  
    # Add Text
    # canvas1.create_text( 200, 250, text = "Welcome")
    Label(canvas1,text="Welcome to Daily Work", font="lucida 18", fg="#091F42").place(y=35, x =430)





    # Button(canvas1, text="Read News").place(x=280,y =80)
    # Button(canvas1, text="1").place(x=280,y =120)
    # Button(canvas1, text="2").place(x=280,y =160)
    # Button(canvas1, text="3").place(x=280,y =200)
    # Button(canvas1, text="4").place(x=280,y =240)
    # Button(canvas1, text="5").place(x=280,y =280)

    

# Creating A portion for Location checking Automatically
    def LOcation_Access(canvas1):
        #Creating a Frame 
        location = Frame(canvas1)
        location.pack()
        location.place(x =710, y =415)
        # Creating a Location
        canvas_location = Canvas( location, width = 200,
                     height = 200)
  
        canvas_location.pack(fill = "both", expand = True)
  
        lbl = ImageLabel(canvas_location)
    
        lbl.pack()
        lbl.load('.\\Daily\\src\\location.gif')
    
        # Label(location, text="Check").pack()
        data = bonggoQuery.Query.normal_query.printing("my location")
    
    
        update_data = Label(location,text="")
        update_data.pack()
        update_data.config(text=f"{data}")


    def ContentShowing(canvas1, query):
        content_layout = Frame(canvas1,)
        content_layout.pack()
        content_layout.place(x =135, y= 495)
        canvas_content = Canvas( content_layout, width = 200,
                     height = 200)
  
        canvas_content.pack(fill = "both", expand = True)
        show_result=  Label(canvas_content, text="")
        show_result.pack()
        
        result = bonggoQuery.Query.normal_query.printing(query)
        result1 = wordResizer(result)
        show_result.config(text=result1)


    image3 = Image.open(".\\Daily\\src\\bd.png")
 
    # Resize the image using resize() method
    resize_image3 = image3.resize((550, 200))
 
    img3 = ImageTk.PhotoImage(resize_image3)
    content_layout1 = Frame(canvas1,)
    content_layout1.pack()
    content_layout1.place(x =99, y= 435)
    canvas_content1 = Canvas( content_layout1, width = 550,
                     height = 200)
  
    canvas_content1.pack(fill = "both", expand = True)
   
    canvas_content1.create_image( 0, 0, image = img3, 
                     anchor = "nw")
   
    Label(canvas1, text="Your Query will appear on this pannel...", font="lucida 12", fg="blue").place(x =110, y =390)


  
    
  
    # WORKING ON SERACH PANNEL
    question = StringVar()  
    def serachIcon():
        

        query1 = question.get()

        ContentShowing(canvas1, query1)
       
        
    Entry(canvas1,width=80,textvariable= question).place(x =110, y =645)
        
    image2 = Image.open(".\\Daily\\src\\search.png")
    resize_image2 = image2.resize((30, 22))
    serach = ImageTk.PhotoImage(resize_image2)
        # Label(canvas1,image=serach).pack()
    # Label(canvas1, image=serach).place(x=510, y=455)
    Button(canvas1, image=serach, command=serachIcon).place(x=600, y =640)


    # ContentShowing(canvas1,"weather report")  



    # showing the location after a time interval
    LOcation_Access(canvas1)


    def groupedBoxes(x1,y1, con):
        social_media_frame =Frame(canvas1)
        social_media_frame.pack()
        social_media_frame.place(x = x1, y= y1)
        Label(social_media_frame, text=con, fg="blue", font ="lucida 10").pack()


        image4 = Image.open(".\\Daily\\src\\shadow_bg.png")
        resize_image4 = image4.resize((280, 220))
 
        img4 = ImageTk.PhotoImage(resize_image4)
       
        social_media_canvas = Canvas( social_media_frame, width = 280,
                     height = 220)
  
        social_media_canvas.pack(fill = "both", expand = True)
   
        social_media_canvas.create_image( 0, 0, image = img4, 
                     anchor = "nw")
        social_media_canvas.image = img4


    def Social_Media():
        data ="Check your Social media Applications"
        groupedBoxes(250,100, data)
        

        # ADDING FACEBOOK Isocial_media
        def faceBook():
            webbrowser.open("https://www.facebook.com/")

        social_frame = Frame(canvas1)
        social_frame.pack()
        social_frame.place(x= 290, y =150)


        image5 = Image.open(".\\Daily\\src\\fb.png")
        resize_image5 = image5.resize((80, 70))
        img5 = ImageTk.PhotoImage(resize_image5)
       
        facebook_btn = Button(social_frame, image=img5, command=faceBook)
        facebook_btn.pack()
        facebook_btn.image = img5

        # ======================================


        
        # ADDING InstagramIsocial_media
        def Instagram():
            webbrowser.open("https://www.instagram.com/")

        social_frame2 = Frame(canvas1)
        social_frame2.pack()
        social_frame2.place(x= 390, y =150)


        image6 = Image.open(".\\Daily\\src\\insta.png")
        resize_image6 = image6.resize((80, 70))
        img6 = ImageTk.PhotoImage(resize_image6)
       
        instagram_btn = Button(social_frame2, image=img6,  command=Instagram)
        instagram_btn.pack()
        instagram_btn.image = img6

        # ======================================



        # ADDING Linkedin Isocial_media
        def linkedIn():
            webbrowser.open("https://www.linkedin.com/feed/")
        social_frame3 = Frame(canvas1)
        social_frame3.pack()
        social_frame3.place(x= 290, y =240)


        image7 = Image.open(".\\Daily\\src\\ln.png")
        resize_image7 = image7.resize((80, 70))
        img7 = ImageTk.PhotoImage(resize_image7)
       
        linkedin_btn = Button(social_frame3, image=img7,command=linkedIn)
        linkedin_btn.pack()
        linkedin_btn.image = img7

        # ======================================


        
        # ADDING Github Isocial_media
        def github():
            webbrowser.open("https://github.com/")
        social_frame4 = Frame(canvas1)
        social_frame4.pack()
        social_frame4.place(x= 390, y =240)


        image8 = Image.open(".\\Daily\\src\\gb.png")
        resize_image8 = image8.resize((80, 70))
        img8 = ImageTk.PhotoImage(resize_image8)
       
        github_btn = Button(social_frame4, image=img8, command=github)
        github_btn.pack()
        github_btn.image = img8

        # ======================================
    


# CREATING THE GROUP OF OTHERS ESSENTIAL APPS

    def Essential_Works():
        data ="Check your Essential Applications"
        groupedBoxes(600, 100, data)

        # ADDING THE FUNCTIONALITIES OF YOUTUBE
        def youtube():
            webbrowser.open("https://www.youtube.com/")
        es_frame = Frame(canvas1)
        es_frame.pack()
        es_frame.place(x= 640, y =150)


        image_youtube = Image.open(".\\Daily\\src\\you.png")
        resize_image_youtube = image_youtube.resize((80, 70))
        img_youtube = ImageTk.PhotoImage(resize_image_youtube)
       
        youtube_btn = Button(es_frame, image=img_youtube, command=youtube)
        youtube_btn.pack()
        youtube_btn.image = img_youtube
        # =====================================

        # ADDING THE FUNCTIONALITIES OF VS CODE
        def vsCode():
            AppOpener.open("Visual Studio Code")

        es_frame1 = Frame(canvas1)
        es_frame1.pack()
        es_frame1.place(x= 740, y =150)


        image_vscode = Image.open(".\\Daily\\src\\vs.png")
        resize_image_vscode = image_vscode.resize((80, 70))
        img_vscode = ImageTk.PhotoImage(resize_image_vscode)
       
        vscode_btn = Button(es_frame1, image=img_vscode, command=vsCode)
        vscode_btn.pack()
        vscode_btn.image = img_vscode
        # =====================================

        # ADDING THE FUNCTIONALITIES OF NEWS READER
        def news_update():
                bonggoQuery.Query.normal_query.speaking("latest news in india")

        es_frame2 = Frame(canvas1)
        es_frame2.pack()
        es_frame2.place(x= 640, y =240)


        image_news = Image.open(".\\Daily\\src\\news.png")
        resize_image_news = image_news.resize((80, 70))
        img_news = ImageTk.PhotoImage(resize_image_news)
       
        news_btn = Button(es_frame2, image=img_news,  command=news_update)
        news_btn.pack()
        news_btn.image = img_news
        # =========================================

        # ADDING THE FUNCTIONALITY OF WEATHER BROADCASTING
        

        def weather():
            bonggoQuery.Query.normal_query.speaking("weather report")

        es_frame3 = Frame(canvas1)
        es_frame3.pack()
        es_frame3.place(x= 740, y =240)


        image_weather = Image.open(".\\Daily\\src\\weather.png")
        resize_image_weather = image_weather.resize((80, 70))
        img_weather = ImageTk.PhotoImage(resize_image_weather)
       
        weather_btn = Button(es_frame3, image=img_weather, command=weather)
        weather_btn.pack()
        weather_btn.image = img_weather
        # ================================================

# =============================================================================

    # adding the left side design img
    # *****************************************************************************
    side_frame = Frame(canvas1)
    side_frame.pack()
    side_frame.place(x = 900, y =100)

    Label(canvas1, text="About Developer", font="lucida 12 bold").place(x =930, y =90)

    image_side = Image.open(".\\Daily\\src\\fm.png")
 
    # Resize the image using resize() method
    resize_image_side = image_side.resize((200, 200))
 
    img_side = ImageTk.PhotoImage(resize_image_side)
    side_canvas = Canvas( side_frame, width = 200,
                     height = 200)
  
    side_canvas.pack(fill = "both", expand = True)
   
    side_canvas.create_image( 0, 0, image = img_side, 
                     anchor = "nw")
    side_canvas.image = img_side
   


    # =============================================================================

    Social_Media()

    Essential_Works()



    root.mainloop()







if __name__== '__main__':
    HomepageGUI()