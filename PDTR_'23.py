''' 
    NSYS-102 Programming 1 Final Exam

    by Group 3

    Python-based Date & Time Recorder (PDTR)

'''
# importing tkinter module for GUI
import tkinter as tk 
from tkinter import messagebox
from tkinter import *

# importing time module for time & date feature
import time

# fpdf modules need to be installed first (pip install fpdf) in the terminal
from fpdf import FPDF 


# resets PDTR
def reset_window():
    display.destroy() # destroys currents window
    print("Status: Program Reset!") # verifies that the program has reset
    main() # re-runs the main code
    

# main code for PDTR
def main():

    global display # convert to global variable

    # displays frame we want to see
    def show_frame(frame):
        frame.tkraise()

    #display = ttk.Window(themename = 'darkly')  # to create GUI
    display = tk.Tk()
    display.title("Digital Date & Time Record (Python) ver. 2023") # display window title and background
    

    # window size
    width = 550 # Width 
    height = 450 # Height

    screen_width = display.winfo_screenwidth()  # Width of the screen
    screen_height = display.winfo_screenheight() # Height of the screen
    
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    display.geometry('%dx%d+%d+%d' % (width, height, x, y)) # keeps the window centered

    pictures = [PhotoImage(file = "whiteicon.png"), PhotoImage(file = "button_login.png")
                , PhotoImage(file = "button_check-in_e.png"), PhotoImage(file = "button_check-out_e.png")
                , PhotoImage(file = "button_check-in_d.png"), PhotoImage(file = "button_check-out_d.png")
                , PhotoImage(file = "button_print-record_e.png"), PhotoImage(file = "button_print-record_d.png")
                , PhotoImage(file = "button_end-session.png")] # instantiate and store images

    display.iconphoto(False, pictures[0]) # display frame icon

    # gives permission to show up in the window
    # expanding the window means that the frame will too
    display.rowconfigure(0, weight = 1)
    display.columnconfigure(0, weight = 1)

    # instantiates all existing frames
    frame1 = tk.Frame(display)
    frame1.config(bg = "black")
    frame2 = tk.Frame(display)
    frame2.config(bg = "black")
    

    # to constantly add the frames in the window
    # layered on top of each other
    '''
    frame 3 will pop up in the screen after looping, 
    thus frame 1 needs to displayed first 
    (refer to def show_frame(frame))
    '''
    for frame in (frame1, frame2):
        frame.grid(row = 0, column = 0, sticky = 'nsew') # sticky (mold to the size of the window)


    # mock database
    def source():

        global username_1, username_2, username_3, username_4, username_5 # convert to global variable
        global password_1, password_2, password_3, password_4, password_5 # convert to global variable

        # stored data
        username_1 = "john"
        password_1 = "wow_"

        username_2 = "drey"
        password_2 = "6969"

        username_3 = "carol"
        password_3 = "iloveshawarma12"

        username_4 = "mark"
        password_4 = "chillihotdog144"

        username_5 = "eroy"
        password_5 = "12psits_"

        

        # if username and password matches or not
        if username_entry.get() == username_1 and password_entry.get() == password_1:
            show_frame(frame2)

        elif username_entry.get() == username_2 and password_entry.get() == password_2:
            show_frame(frame2)

        elif username_entry.get() == username_3 and password_entry.get() == password_3:
            show_frame(frame2)

        elif username_entry.get() == username_4 and password_entry.get() == password_4:
            show_frame(frame2)

        elif username_entry.get() == username_5 and password_entry.get() == password_5:
            show_frame(frame2)

        else:
            messagebox.showinfo(title = " ", message = "Invalid Username or Password: Please Try Again!")



    #=========================================================================================FRAME1
    # (log in) frame title
    title = tk.Label(frame1, text = "元気 Inc.", font = 'Calibri 40 bold', fg = "white" ,bg = "black")
    title.pack(pady = 60)

    # widget frame
    widget_frame = tk.Frame(frame1, width = 350, height = 250, borderwidth = 0, relief = tk.FLAT, bg = "black")
    widget_frame.pack_propagate(True)
    widget_frame.pack()

    # username label
    username_label = tk.Label(widget_frame, text = "Username", font = 'Calibri 15 bold', fg = "white" ,bg = "black")
    username_label.grid(row = 1, column = 0, padx = 10, pady = 5)
    
    # entry field for username
    global username_entry # to convert to global variable
    username_entry = tk.Entry(master = widget_frame, bd = 0, fg = "black", bg = "white", font = 'Calibri 12', width = 15)
    username_entry.grid(row = 1, column = 1, pady = 15)

    # password label
    password_label = tk.Label(widget_frame, text = "Password", font = 'Calibri 15 bold', fg = "white" ,bg = "black")
    password_label.grid(row = 2, column = 0, padx = 10)

    # entry field for password
    password_entry = tk.Entry(master = widget_frame, show = "*", bd = 0, fg = "black", bg = "white", font = 'Calibri 12', width = 15)
    password_entry.grid(row = 2, column = 1)

    # login button
    frame1_btn = tk.Button(frame1, bg = "black", activebackground = "black", borderwidth = 0, image = pictures[1], text = 'LOGIN', font = 'Calibri 13 bold' , command = source)
    frame1_btn.pack(pady = 30)
    #=========================================================================================FRAME1


    #=========================================================================================FRAME2
    # label for frame 2
    title_f2 = tk.Label(frame2, text = "元気 Inc.", font = 'Calibri 24 bold', fg = "white" ,bg = "black")
    title_f2.pack(pady = 20)

    # widget frame
    widget_frame_f2 = tk.Frame(frame2, width = 350, height = 250, borderwidth = 0, relief = tk.FLAT, bg = "black")
    widget_frame_f2.pack_propagate(True)
    widget_frame_f2.pack()

    # displaying label that welcomes employee
    employee_info = Label(widget_frame_f2,  font = ("calibri", 30, "bold"), text = "Welcome Employee", fg = "white" ,bg = "black")
    employee_info.grid(row = 1, column = 0, columnspan = 2)

    # displaying date
    Label(widget_frame_f2, font = ("calibri", 13, "bold"), text = "Date: ", fg = "white" ,bg = "black").grid(row = 2, column = 0)

    # displaying time
    Label(widget_frame_f2, font = ("calibri", 13, "bold"), text = "Current Time: ", fg = "white" ,bg = "black").grid(row = 3, column = 0)

    # date and clock mechanics
    def clock():
        clock_time = time.strftime('%H:%M:%S %p')
        current_time.config(text = clock_time)
        current_time.after(1000, clock)

        date = time.strftime('%D %A')
        current_date.config(text = date)
        
    
    # displaying date info
    current_date = Label(widget_frame_f2, font = ("calibri", 13, "bold"), text = " ", fg = "white" ,bg = "black")
    current_date.grid(row = 2, column = 1)

    #displaying time info
    current_time = Label(widget_frame_f2, font = ("calibri", 13, "bold"), text = " ", fg = "white" ,bg = "black")
    current_time.grid(row = 3, column = 1)

    # calling clock function
    clock()

    # checkin time functionality
    def checkin():

        global clock_date_time_in # convert to global variable

        # generating date and time
        clock_date_time_in = time.strftime('%H:%M:%S %p  %m/%d %a')
    
        # time in label
        time_in_label = Label(widget_frame_f2, font = ("calibri", 12, "bold"), text = "TIME IN: ", fg = "white" ,bg = "black")
        time_in_label.grid(row = 6, column = 0, pady = 10)

        # displaying time and date
        check_in_label = Label(widget_frame_f2, font = ("calibri", 12, "bold"), text = clock_date_time_in, fg = "red" ,bg = "black")
        check_in_label.grid(row = 6, column = 1, columnspan = 2, pady = 10)
        print("Check-in time: ", clock_date_time_in)

        check_in_btn.config(state = tk.DISABLED, image = pictures[4]) # disables check-in button once clicked
        check_out_btn.config(state = tk.NORMAL, image = pictures[3]) # enables check-out button once check in is clicked
        
    # checkin button and functionality
    check_in_btn = tk.Button(widget_frame_f2, bg = "black", activebackground = "black", borderwidth = 0, image = pictures[2], text = 'Check-in', font = 'Calibri 13' , command = checkin)
    check_in_btn.grid(row = 4, column = 0, pady = 15)


    # checkout time functionality
    def checkout():

        global clock_date_time_out # convert to global variable

        # generating date and time
        clock_date_time_out = time.strftime('%H:%M:%S %p  %m/%d %a')
        
        # time in label
        time_out_label = Label(widget_frame_f2, font = ("calibri", 12, "bold"), text = "TIME OUT: ", fg = "white" ,bg = "black")
        time_out_label.grid(row = 7, column = 0)

        # displaying time and date
        check_out_label = Label(widget_frame_f2, font = ("calibri", 12, "bold"), text = clock_date_time_out, fg = "red" ,bg = "black")
        check_out_label.grid(row = 7, column = 1, columnspan = 2)
        print("Check-out time:", clock_date_time_out)

        # disables check-out button once clicked
        check_out_btn.config(state = tk.DISABLED, image = pictures[5])

    # checkout button and functionality
    check_out_btn = tk.Button(widget_frame_f2, bg = "black", activebackground = "black",
     borderwidth = 0, image = pictures[5], text = 'Check-out', font = 'Calibri 13', command = checkout, state = tk.DISABLED)
    check_out_btn.grid(row = 4, column = 1, pady = 15)

    # displaying warning note
    display_label = Label(widget_frame_f2,  font = ("calibri", 11, "italic"), text = "*Clicking Check-Out will Record your Time", fg = "white" ,bg = "black")
    display_label.grid(row = 5, column = 0, columnspan = 2)

    # records time and date of employee
    def record():

        # data will be added to the file depending on who is logged in
        if username_entry.get() == username_1 and password_entry.get() == password_1:
            # opens (creates if none) file and appends data
            with open(f'{username_1}.txt', "a") as employee_dtr:
                print(45 * "=", file = employee_dtr) # border
                print("GENKI INC. CHECK-IN AND OUT RECORD", file = employee_dtr) # record details
                print(f"Employee Username: {username_1}", file = employee_dtr)
                print(" ", file = employee_dtr)
                print("Check-in time: ",clock_date_time_in, file = employee_dtr) # check-in time data
                print("Check-out time: ",clock_date_time_out, file = employee_dtr) # check-out time data
                print(45 * "=", file = employee_dtr) # border
                messagebox.showinfo(title = " ", message = "        Record Saved!        ") # prompts user that the record is saved
            
            # function that converts txt file to pdf file
            def pdf():

                pdf = FPDF() # save FPDF() class into a variable pdf

                pdf.add_page() # Add a page

                pdf.set_font("Arial", size = 15) # set style and size of font of text in pdf

                f = open(f"{username_1}.txt", "r") # open the text file in read mode

                # insert the texts in pdf
                

                for x in f:
                    pdf.cell(200, 10, txt = x, ln = 2, align = 'C')

                pdf.output(f"{username_1}_record.pdf") # save the pdf

                # verifies if conversion is finished
                print("Status: PDF Converted!")

            # calling pdf converter function
            pdf()
                
        if username_entry.get() == username_2 and password_entry.get() == password_2:
            # opens (creates if none) file and appends data
            with open(f'{username_2}.txt', "a") as employee_dtr:
                print(45 * "=", file = employee_dtr) # border
                print("GENKI INC. CHECK-IN AND OUT RECORD", file = employee_dtr) # record details
                print(f"Employee Username: {username_2}", file = employee_dtr)
                print(" ", file = employee_dtr)
                print("Check-in time: ",clock_date_time_in, file = employee_dtr) # check-in time data
                print("Check-out time: ",clock_date_time_out, file = employee_dtr) # check-out time data
                print(45 * "=", file = employee_dtr) # border
                messagebox.showinfo(title = " ", message = "        Record Saved!        ") # prompts user that the record is saved

           # function that converts txt file to pdf file
            def pdf():

                pdf = FPDF() # save FPDF() class into a variable pdf

                pdf.add_page() # Add a page

                pdf.set_font("Arial", size = 15) # set style and size of font of text in pdf

                f = open(f"{username_2}.txt", "r") # open the text file in read mode

                # insert the texts in pdf
                for x in f:
                    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

                pdf.output(f"{username_2}_record.pdf") # save the pdf

                # verifies if conversion is finished
                print("Status: PDF Converted!")

            # calling pdf converter function
            pdf()

        if username_entry.get() == username_3 and password_entry.get() == password_3:
            # opens (creates if none) file and appends data
            with open(f'{username_3}.txt', "a") as employee_dtr:
                print(45 * "=", file = employee_dtr) # border
                print("GENKI INC. CHECK-IN AND OUT RECORD", file = employee_dtr) # record details
                print(f"Employee Username: {username_3}", file = employee_dtr)
                print(" ", file = employee_dtr)
                print("Check-in time: ",clock_date_time_in, file = employee_dtr) # check-in time data
                print("Check-out time: ",clock_date_time_out, file = employee_dtr) # check-out time data
                print(45 * "=", file = employee_dtr) # border
                messagebox.showinfo(title = " ", message = "        Record Saved!        ") # prompts user that the record is saved

           # function that converts txt file to pdf file
            def pdf():

                pdf = FPDF() # save FPDF() class into a variable pdf

                pdf.add_page() # Add a page

                pdf.set_font("Arial", size = 15) # set style and size of font of text in pdf

                f = open(f"{username_3}.txt", "r") # open the text file in read mode

                # insert the texts in pdf
                for x in f:
                    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

                pdf.output(f"{username_3}_record.pdf") # save the pdf

                # verifies if conversion is finished
                print("Status: PDF Converted!")

            # calling pdf converter function
            pdf()

        if username_entry.get() == username_4 and password_entry.get() == password_4:
            # opens (creates if none) file and appends data
            with open(f'{username_4}.txt', "a") as employee_dtr:
                print(45 * "=", file = employee_dtr) # border
                print("GENKI INC. CHECK-IN AND OUT RECORD", file = employee_dtr) # record details
                print(f"Employee Username: {username_4}", file = employee_dtr)
                print(" ", file = employee_dtr)
                print("Check-in time: ",clock_date_time_in, file = employee_dtr) # check-in time data
                print("Check-out time: ",clock_date_time_out, file = employee_dtr) # check-out time data
                print(45 * "=", file = employee_dtr) # border
                messagebox.showinfo(title = " ", message = "        Record Saved!        ") # prompts user that the record is saved

            # function that converts txt file to pdf file
            def pdf():

                pdf = FPDF() # save FPDF() class into a variable pdf

                pdf.add_page() # Add a page

                pdf.set_font("Arial", size = 15) # set style and size of font of text in pdf

                f = open(f"{username_4}.txt", "r") # open the text file in read mode

                # insert the texts in pdf
                for x in f:
                    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

                pdf.output(f"{username_4}_record.pdf") # save the pdf

                # verifies if conversion is finished
                print("Status: PDF Converted!")

            # calling pdf converter function
            pdf()

        if username_entry.get() == username_5 and password_entry.get() == password_5:
            # opens (creates if none) file and appends data
            with open(f'{username_5}.txt', "a") as employee_dtr:
                print(45 * "=", file = employee_dtr) # border
                print("GENKI INC. CHECK-IN AND OUT RECORD", file = employee_dtr) # record details
                print(f"Employee Username: {username_5}", file = employee_dtr)
                print(" ", file = employee_dtr)
                print("Check-in time: ",clock_date_time_in, file = employee_dtr) # check-in time data
                print("Check-out time: ",clock_date_time_out, file = employee_dtr) # check-out time data
                print(45 * "=", file = employee_dtr) # border
                messagebox.showinfo(title = " ", message = "        Record Saved!        ") # prompts user that the record is saved

            # function that converts txt file to pdf file
            def pdf():

                pdf = FPDF() # save FPDF() class into a variable pdf

                pdf.add_page() # Add a page

                pdf.set_font("Arial", size = 15) # set style and size of font of text in pdf

                f = open(f"{username_5}.txt", "r") # open the text file in read mode

                # insert the texts in pdf
                for x in f:
                    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

                pdf.output(f"{username_5}_record.pdf") # save the pdf

                # verifies if conversion is finished
                print("Status: PDF Converted!")

            # calling pdf converter function
            pdf()

        # disables button after clicking
        print_btn.config(state = tk.DISABLED, image = pictures[7])


    # ends session and resets window
    endsesh_btn = tk.Button(frame2, bg = "black", activebackground = "black", borderwidth = 0, image = pictures[8], text = 'End Session', font = 'Calibri 12' ,command = reset_window)
    endsesh_btn.pack(side = 'bottom', pady = 10)

    # prints data and adds to record
    print_btn = tk.Button(frame2, bg = "black", activebackground = "black", borderwidth = 0, image = pictures[6], text = 'Print Record', font = 'Calibri 12' ,command = record)
    print_btn.pack(side = 'bottom', pady = 5)
    #=========================================================================================FRAME2


    show_frame(frame1)  # calling function that displays frame

    display.mainloop()  # to loop GUI


# calling function to run the program
main()
