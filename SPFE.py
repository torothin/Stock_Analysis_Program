from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from datetime import datetime as dt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import SPBE as SP
import matplotlib.dates as mdates

class Window(object):

    def __init__(self,window):

        self.window = window
        self.window.wm_title("Stock Program")

        stock_L1=Label(window,text="Stock Symbol")
        stock_L1.grid(row=0,column=0)

        stock_L2=Label(window,text="Stock Value")
        stock_L2.grid(row=1,column=0)

        stock_L3=Label(window,text="Shares")
        stock_L3.grid(row=2,column=0)

        stock_L4=Label(window,text="Day Change")
        stock_L4.grid(row=3,column=0)

        stock_L5=Label(window,text="Cash")
        stock_L5.grid(row=0,column=2)

        stock_L6=Label(window,text="Cash Change")
        stock_L6.grid(row=2,column=2)

        stock_L7=Label(window,text="Buy Conditions")
        stock_L7.grid(row=5,column=1)

        stock_L8=Label(window,text="Sell Conditions")
        stock_L8.grid(row=5,column=2)

        stock_L9=Label(window,text="% Delta")
        stock_L9.grid(row=6,column=0)

        stock_L10=Label(window,text="Value Delta")
        stock_L10.grid(row=7,column=0)

        stock_L11=Label(window,text="Max Shares")
        stock_L11.grid(row=8,column=0)

        stock_L12=Label(window,text="Max Value")
        stock_L12.grid(row=9,column=0)

        stock_L13=Label(window,text="Trade Commision")
        stock_L13.grid(row=10,column=0)

        stock_L14=Label(window,text="Modeling Section")
        stock_L14.grid(row=12,column=0, columnspan=3)

        stock_L15=Label(window,text="Data File")
        stock_L15.grid(row=13,column=0)

        stock_L16=Label(window,text="Time Delay")
        stock_L16.grid(row=14,column=0)

        stock_L17=Label(window,text="Model Input File")
        stock_L17.grid(row=15,column=0)

        self.stock_symbol=StringVar()
        self.e1=Entry(window,textvariable=self.stock_symbol)
        self.e1.grid(row=0,column=1, padx=5, pady=5)

        self.stock_value=DoubleVar()
        self.e2=Entry(window,textvariable=self.stock_value)
        self.e2.grid(row=1,column=1, padx=5, pady=5)

        self.shares=IntVar()
        self.e3=Entry(window,textvariable=self.shares)
        self.e3.grid(row=2,column=1, padx=5, pady=5)

        self.day_change=DoubleVar()
        self.e4=Entry(window,textvariable=self.day_change)
        self.e4.grid(row=3,column=1, padx=5, pady=5)

        self.buy_perc_delta=DoubleVar()
        self.e5=Entry(window,textvariable=self.buy_perc_delta)
        self.e5.grid(row=6,column=1, padx=5, pady=5)

        self.buy_val_delta=DoubleVar()
        self.e6=Entry(window,textvariable=self.buy_val_delta)
        self.e6.grid(row=7,column=1, padx=5, pady=5)

        self.buy_max_shares=IntVar()
        self.e7=Entry(window,textvariable=self.buy_max_shares)
        self.e7.grid(row=8,column=1, padx=5, pady=5)

        self.buy_max_value=DoubleVar()
        self.e8=Entry(window,textvariable=self.buy_max_value)
        self.e8.grid(row=9,column=1, padx=5, pady=5)

        self.buy_trade_comm=DoubleVar()
        self.e9=Entry(window,textvariable=self.buy_trade_comm)
        self.e9.grid(row=10,column=1, padx=5, pady=5)

        self.sell_perc_delta=DoubleVar()
        self.e10=Entry(window,textvariable=self.sell_perc_delta)
        self.e10.grid(row=6,column=2, padx=5, pady=5)

        self.sell_val_delta=DoubleVar()
        self.e11=Entry(window,textvariable=self.sell_val_delta)
        self.e11.grid(row=7,column=2, padx=5, pady=5)

        self.sell_max_shares=IntVar()
        self.e12=Entry(window,textvariable=self.sell_max_shares)
        self.e12.grid(row=8,column=2, padx=5, pady=5)

        self.sell_max_value=DoubleVar()
        self.e13=Entry(window,textvariable=self.sell_max_value)
        self.e13.grid(row=9,column=2, padx=5, pady=5)

        self.sell_trade_comm=DoubleVar()
        self.e14=Entry(window,textvariable=self.sell_trade_comm)
        self.e14.grid(row=10,column=2, padx=5, pady=5)

        self.data_file=StringVar()
        self.e15=Entry(window,textvariable=self.data_file,width=42)
        self.e15.grid(row=13,column=1, columnspan=2, padx=5, pady=5)

        self.time_delay=DoubleVar()
        self.e16=Entry(window,textvariable=self.time_delay,width=42)
        self.e16.grid(row=14,column=1, columnspan=2, padx=5, pady=5)

        self.model_input_file=StringVar()
        self.e17=Entry(window,textvariable=self.model_input_file,width=42)
        self.e17.grid(row=15,column=1, columnspan=2, padx=5, pady=5)

        self.cash=DoubleVar()
        self.e18=Entry(window,textvariable=self.cash)
        self.e18.grid(row=1,column=2, padx=5, pady=5)

        self.cash_change=DoubleVar()
        self.e19=Entry(window,textvariable=self.cash_change)
        self.e19.grid(row=3,column=2, padx=5, pady=5)

        #Default Parameters,
        self.e5.delete(0,END), self.e5.insert(END,2)
        self.e6.delete(0,END), self.e6.insert(END,0.05)
        self.e7.delete(0,END), self.e7.insert(END,0)
        self.e8.delete(0,END), self.e8.insert(END,0)
        self.e9.delete(0,END), self.e9.insert(END,0)
        self.e10.delete(0,END), self.e10.insert(END,2)
        self.e11.delete(0,END), self.e11.insert(END,0.05)
        self.e12.delete(0,END), self.e12.insert(END,0)
        self.e13.delete(0,END), self.e13.insert(END,0)
        self.e14.delete(0,END), self.e14.insert(END,0)
        self.e18.delete(0,END), self.e18.insert(END,1000000)

        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Stock Input File", command=self.input_file)
        self.filemenu.add_command(label="Model Parameters Load", command=self.model_input_file_load)
        self.filemenu.add_command(label="Model Parameter Save As", command=self.model_input_file_save)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=window.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        '''
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        '''

        window.config(menu=self.menubar)

    def input_file(self):
        window.filename =  filedialog.askopenfilename(initialdir = "/Dropbox/Python Mega Course/App 9 Web Scraping/",
                                    title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.e15.delete(0,END)
        self.e15.insert(END,window.filename)

        SP.update_host(window.filename)

        f = Figure(figsize=(6,4), dpi=100)
        a = f.add_subplot(111)

        x = matplotlib.dates.date2num([dt.strptime(d,"%H-%M-%S") for d in SP.stock_time])
        a.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
        plt.setp(a.get_xticklabels(), rotation=45)
        a.plot(x,SP.stock_value)

        canvas = FigureCanvasTkAgg(f,window)
        canvas.show()
        canvas.get_tk_widget().grid(row=0,column=3, rowspan=18, padx=5, pady=5,sticky=N)

        toolbar_frame = Frame(window)
        toolbar_frame.grid(row=17,column=3, padx=5, pady=5)
        toolbar = NavigationToolbar2TkAgg( canvas, toolbar_frame )

        self.e4.delete(0,END)
        self.e4.insert(END,float("{0:.2f}".format(SP.stock_value[len(SP.stock_value)-1]-SP.stock_value[0])))

        self.e2.delete(0,END)
        self.e2.insert(END,float("{0:.2f}".format(SP.stock_value[len(SP.stock_value)-1])))

        self.e1.delete(0,END)
        self.e1.insert(END,SP.stock_symbol)

        self.simulation_Font = font.Font(family='Arial', size=24, weight='bold')
        self.b4=Button(window,text="Run Simulation",font=self.simulation_Font,width=18,command=self.run_sim)
        self.b4.grid(row=17,column=0, padx=5, pady=5, columnspan=3)

    def run_sim(self):
        input1=self.buy_perc_delta.get()/100
        input2=self.buy_val_delta.get()
        input3=self.buy_max_shares.get()
        input4=self.buy_max_value.get()
        input5=self.buy_trade_comm.get()
        input6=self.sell_perc_delta.get()/100
        input7=self.sell_val_delta.get()
        input8=self.sell_max_shares.get()
        input9=self.sell_max_value.get()
        input10=self.sell_trade_comm.get()
        input11=self.cash.get()
        SP.model_Run(input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11)

        self.e19.delete(0,END)
        self.e19.insert(END,float("{0:.2f}".format(SP.cash_model-input11)))

    def model_input_file_load(self):
        window.modelfilename =  filedialog.askopenfilename(initialdir = "/Dropbox/Python Mega Course/App 9 Web Scraping/",
                                    title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
        #might be better to try a loop at some point to clean up code
        self.e17.delete(0,END), self.e17.insert(END,window.modelfilename)
        SP.load_Model_Para(window.modelfilename)
        self.e5.delete(0,END), self.e5.insert(END,SP.para_buy_perc_delta)
        self.e6.delete(0,END), self.e6.insert(END,SP.para_buy_val_delta)
        self.e7.delete(0,END), self.e7.insert(END,SP.para_buy_max_shares)
        self.e8.delete(0,END), self.e8.insert(END,SP.para_buy_max_value)
        self.e9.delete(0,END), self.e9.insert(END,SP.para_buy_trade_comm)
        self.e10.delete(0,END), self.e10.insert(END,SP.para_sell_perc_delta)
        self.e11.delete(0,END), self.e11.insert(END,SP.para_sell_val_delta)
        self.e12.delete(0,END), self.e12.insert(END,SP.para_sell_max_shares)
        self.e13.delete(0,END), self.e13.insert(END,SP.para_sell_max_value)
        self.e14.delete(0,END), self.e14.insert(END,SP.para_sell_trade_comm)
        self.e18.delete(0,END), self.e18.insert(END,SP.para_cash)

    def model_input_file_save(self):
        input1=self.buy_perc_delta.get()
        input2=self.buy_val_delta.get()
        input3=self.buy_max_shares.get()
        input4=self.buy_max_value.get()
        input5=self.buy_trade_comm.get()
        input6=self.sell_perc_delta.get()
        input7=self.sell_val_delta.get()
        input8=self.sell_max_shares.get()
        input9=self.sell_max_value.get()
        input10=self.sell_trade_comm.get()
        input11=self.cash.get()

        window.modelfilename = filedialog.asksaveasfilename(initialdir = "/Dropbox/Python Mega Course/App 9 Web Scraping/",
                                    title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))

        SP.save_Model_Para(window.modelfilename,input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11)


window=Tk()
Window(window)
window.mainloop()
