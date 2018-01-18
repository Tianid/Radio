import sys
import gi



gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
gi.require_version('GdkX11', '3.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import Gst, Gtk, Gdk, GLib, GdkX11, GstVideo,Gio


class ChangeRecordWindow(Gtk.Window):

    def __init__(self,main_win):
        self.old_value1=""
        self.old_value2=""
        self.old_value3=""
        self.main_win=main_win
        self.textarea1= ""
        self.textarea2= ""
        self.textarea3= ""

        Gtk.Window.__init__(self, title="Change record")
        self.set_size_request(200, 100)


        self.main_box = Gtk.VBox.new(False, 0)
        self.controls = Gtk.HBox.new(False, 0)


        self.label1=Gtk.Label("Enter the name of radio station")
        self.label2=Gtk.Label("Enter the URL-address")
        self.label3=Gtk.Label("Enter the site of radio station")
        self.label4=Gtk.Label("Fill all fields!")


        self.button1=Gtk.Button()
        self.button1.set_label("Apply")

        self.button2=Gtk.Button()
        self.button2.set_label("Cancel")




        self.controls.pack_start(self.button1, False, False, 2)
        self.controls.pack_start(self.button2, False, False, 2)



        self.entry1 = Gtk.Entry()
        self.entry1.set_text(self.main_win.deleteble_Name)
        self.entry1.set_size_request(20,5)
        self.entry2 = Gtk.Entry()
        self.entry2.set_text(self.main_win.deleteble_URL)
        self.entry2.set_size_request(20, 5)
        self.entry3 = Gtk.Entry()
        self.entry3.set_text(self.main_win.deleteble_All)
        self.entry3.set_size_request(20, 5)

        self.old_value1=self.entry1.get_text()
        self.old_value2=self.entry2.get_text()
        self.old_value3=self.entry3.get_text()


        self.entry1.connect("changed", self.set_disabled)
        self.entry2.connect("changed", self.set_disabled)
        self.entry3.connect("changed", self.set_disabled)


        self.button1.connect("clicked", self.change_record)
        self.button2.connect("clicked", self.cancel)

        self.main_box.pack_start(self.label1, False, False, 0)
        self.main_box.pack_start(self.entry1, False, False, 5)
        self.main_box.pack_start(self.label2, False, False, 0)
        self.main_box.pack_start(self.entry2, False, False, 0)
        self.main_box.pack_start(self.label3, False, False, 0)
        self.main_box.pack_start(self.entry3, False, False, 0)

        self.main_box.pack_start(self.controls, False, False, 2)
        self.main_box.pack_start(self.label4, False, False, 2)
        self.add(self.main_box)
        print(self.entry1.get_text(),"!!!")

        print(self.entry1.get_text())

        print(self.main_win.deleteble_All ,"old list")


    def cancel(self,widget):
        self.destroy()



    def change_record(self, widget):


        self.textarea1=self.entry1.get_text()
        self.textarea2=self.entry2.get_text()
        self.textarea3=self.entry3.get_text()

        self.indexData=self.main_win.data_list.index((self.old_value1,self.old_value2))
        self.indexInterf=self.main_win.interface_list.index((self.old_value1,self.old_value3))
        self.indexRadio_dic=self.main_win.radio_dic.index((self.old_value1,self.old_value2))

        self.main_win.data_list[self.indexData]=(self.textarea1,self.textarea2)
        self.main_win.interface_list[self.indexInterf]=(self.textarea1,self.textarea3)
        self.main_win.radio_dic[self.indexRadio_dic]=(self.textarea1,self.textarea2)





        self.main_win.list_radio.clear()
        for software_ref in self.main_win.interface_list:
             self.main_win.list_radio.append(list(software_ref))
        for i in range(len(self.main_win.data_list)):
            self.main_win.radio_dic.append(self.main_win.data_list[i])



    def set_disabled(self,widget):

        if self.entry1.get_text()!='' and self.entry2.get_text()!='' and self.entry3.get_text()!='':
            self.button1.set_sensitive(True)
        else:
            self.button1.set_sensitive(False)


class AddRecordWindow(Gtk.Window):

    def __init__(self,main_win):
        self.main_win=main_win
        self.textarea1= ""
        self.textarea2= ""
        self.textarea3= ""
        Gtk.Window.__init__(self, title="Add record")
        self.set_size_request(200, 100)

        self.timeout_id = None

        self.main_box = Gtk.VBox.new(False, 0)
        self.controls = Gtk.HBox.new(False, 0)


        self.label1=Gtk.Label("Enter the name of radio station")
        self.label2=Gtk.Label("Enter the URL-address")
        self.label3=Gtk.Label("Enter the site of radio station")
        self.label4=Gtk.Label("Fill all fields!")


        self.button1=Gtk.Button()
        self.button1.set_label("Apply")
        self.button1.set_sensitive(False)
        self.button2=Gtk.Button()
        self.button2.set_label("Cancel")




        self.controls.pack_start(self.button1, False, False, 2)
        self.controls.pack_start(self.button2, False, False, 2)



        self.entry1 = Gtk.Entry()
        self.entry1.set_text("")
        self.entry1.set_size_request(20,5)
        self.entry2 = Gtk.Entry()
        self.entry2.set_text("")
        self.entry2.set_size_request(20, 5)
        self.entry3 = Gtk.Entry()
        self.entry3.set_text("")
        self.entry3.set_size_request(20, 5)

        self.entry1.connect("changed", self.set_disabled)
        self.entry2.connect("changed", self.set_disabled)
        self.entry3.connect("changed", self.set_disabled)

        self.button1.connect("clicked", self.add_record)
        self.button2.connect("clicked", self.cancel)

        self.main_box.pack_start(self.label1, False, False, 0)
        self.main_box.pack_start(self.entry1, False, False, 5)
        self.main_box.pack_start(self.label2, False, False, 0)
        self.main_box.pack_start(self.entry2, False, False, 0)
        self.main_box.pack_start(self.label3, False, False, 0)
        self.main_box.pack_start(self.entry3, False, False, 0)

        self.main_box.pack_start(self.controls, False, False, 2)
        self.main_box.pack_start(self.label4, False, False, 2)
        self.add(self.main_box)
        print(self.entry1.get_text(),"!!!")

        print(self.entry1.get_text())

    def on_error_clicked(self):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.OK, "ERROR")
        dialog.format_secondary_text(
            "This name of radio is alredy exist.")
        dialog.run()
        print("ERROR dialog closed")

        dialog.destroy()
    def cancel(self,widget):
        self.destroy()



    def add_record(self, widget):

        self.textarea1=self.entry1.get_text()
        self.textarea2=self.entry2.get_text()
        self.textarea3=self.entry3.get_text()

        self.main_win.data_list.append((self.textarea1,self.textarea2))
        self.main_win.interface_list.append((self.textarea1,self.textarea3))
        self.main_win.radio_dic.append((self.textarea1,self.textarea2))
        print(self.main_win.radio_dic, "radidic")
        self.main_win.list_radio.clear()
        for software_ref in self.main_win.interface_list:
            self.main_win.list_radio.append(list(software_ref))


        print(self.main_win.data_list,"datalist")
        print(self.main_win.interface_list,"interface")
        print(self.main_win.radio_dic,"radidic")

    def set_disabled(self,widget):

        if self.entry1.get_text()!='' and self.entry2.get_text()!='' and self.entry3.get_text()!='':
            self.button1.set_sensitive(True)
        else:
            self.button1.set_sensitive(False)


class FileChooserWindowOpen(Gtk.Window):

    def on_file_clicked(self):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        self.filename=dialog.get_filename()


        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def return_filename(self):

        return self.filename
    def __del__(self):
        print("window deleted")


class FileChooserWindowSave(Gtk.Window):
    filename=""


    def add_filters(self, dialog):
        # Add text file filter
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
    def button_pressed(self,list,dict):

        dialog = Gtk.FileChooserDialog("Save your text file", self,
                                       Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
        dialog.set_default_size(800, 400)

        self.add_filters(dialog)
        Gtk.FileChooser.set_do_overwrite_confirmation(dialog, True)
        Gtk.FileChooser.set_current_name(dialog, "Untitled document")
        response = dialog.run()

        if response == Gtk.ResponseType.ACCEPT:
            filename = Gtk.FileChooser.get_filename(dialog)
            print(
                "This is the filename: " + filename)
            self.save_to_file(filename,list, dict)


        dialog.destroy()
    def save_to_file(self,filename,list,dict):
        save_list=[]
        str=""
        file = open(filename, "w")
        for i in range(len(list)):
            save_list.append(list[i][0]+","+dict[i][1]+","+list[i][1])

        for i in range(len(save_list)):
            str=str+save_list[i]+"\n"

        file.write(str)
        file.close()
        print(save_list)

        pass

    def return_filename(self):

        return self.filename
    def __del__(self):
        print("window deleted")


class RadioConnect():

    def __init__(self, URL, StartVolume):

        Gst.init(sys.argv)

        self.state = Gst.State.NULL
        self.duration = Gst.CLOCK_TIME_NONE
        self.playbin = Gst.ElementFactory.make("playbin", "playbin")
        if not self.playbin:
            print("ERROR: Could not create playbin.")
            sys.exit(1)

        # set up URI
        self.playbin.set_property(
            "uri", URL)

        self.playbin.set_property("volume", StartVolume)



    def play(self):
        self.playbin.set_state(Gst.State.PLAYING)

    def pause(self):
        self.playbin.set_state(Gst.State.PAUSED)

    def stop(self):
        self.playbin.set_state(Gst.State.READY)

    def on_slider_changed(self, value):

        self.playbin.set_property("volume", value)

    def __del__(self):
        print("deleted")


class RadioWindow(Gtk.Window):
    data_list = []
    interface_list = []


    def __init__(self):


        main_window = Gtk.Window.new(Gtk.WindowType.TOPLEVEL)
        main_window.connect("delete-event", self.on_delete_event)
        main_window.set_title("Hero-Radio")
        main_window.set_name('pam')


        self.obj = ""
        self.radio_dic=[]

        self.button1 = Gtk.Button.new_from_stock(Gtk.STOCK_MEDIA_PLAY)

        self.button1.connect("clicked", self.start)
        self.button1.set_name("lal")
        self.button2 = Gtk.Button.new_from_stock(Gtk.STOCK_MEDIA_PAUSE)
        self.button2.set_name("lal")
        self.button2.connect("clicked", self.on_pause)

        self.button3 = Gtk.Button.new_from_stock(Gtk.STOCK_MEDIA_STOP)
        self.button3.connect("clicked", self.on_stop)
        self.button3.set_name("lal")

        self.slider = Gtk.HScale.new_with_range(0, 3, 0.01)
        self.slider.set_draw_value(False)
        self.slider.set_name("lals")

        self.slider_update_signal_id = self.slider.connect(
            "value-changed", self.on_slider_changed)




        self.list_radio = Gtk.ListStore(str, str)
        for software_ref in self.interface_list:
            self.list_radio.append(list(software_ref))


        self.software_TreeStore = Gtk.TreeView(self.list_radio)

        for i, column_title in enumerate(["Название", "Сайт"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.software_TreeStore.append_column(column)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.add(self.software_TreeStore)




        controls = Gtk.HBox.new(False, 0)
        controls.pack_start(self.button1, False, False, 2)
        controls.pack_start(self.button2, False, False, 2)
        controls.pack_start(self.button3, False, False, 2)
        controls.pack_start(self.slider, True, True, 0)

        self.main_hbox = Gtk.HBox.new(False, 0)
        self.main_hbox.pack_start(self.scrollable_treelist, True, True, 2)

        grid=Gtk.Grid()

        mb=Gtk.MenuBar()
        mb.set_name('ram')
        file=Gtk.MenuItem("File")
        file_open=Gtk.MenuItem("Open file")
        file_save=Gtk.MenuItem("Save file")
        file_close=Gtk.MenuItem("Close file")
        exit = Gtk.MenuItem("Exit")

        edit=Gtk.MenuItem("Edit")
        add_record=Gtk.MenuItem("Add record")
        add_record.set_name('pam')
        delete_record=Gtk.MenuItem("Delete record")
        delete_record.set_name('pam')
        change_record=Gtk.MenuItem("Change record")
        change_record.set_name('pam')

        about = Gtk.MenuItem("About")


        file_open.connect("activate", self.open_file)
        file_open.set_name('pam')
        file_save.connect("activate", self.window_save)
        file_save.set_name('pam')
        file_close.connect("activate",self.clear_ui)
        file_close.set_name('pam')
        exit.connect("activate", self.exit)
        exit.set_name('pam')
        about.connect("activate",self.call_about)


        add_record.connect("activate",self.create_add_record_window)
        delete_record.connect("activate",self.delete_record)
        change_record.connect("activate",self.create_change_record_window)




        filemenu=Gtk.Menu()
        filemenu.set_name('pam')
        filemenu.append(file_open)
        filemenu.append(file_save)
        filemenu.append(file_close)
        filemenu.append(exit)
        file.set_submenu(filemenu)

        editmenu=Gtk.Menu()
        editmenu.set_name('pam')
        editmenu.append(add_record)
        editmenu.append(delete_record)
        editmenu.append(change_record)
        edit.set_submenu(editmenu)


        mb.append(file)
        mb.append(edit)
        mb.append(about)

        grid.attach(mb, 0, 0, 1, 1)



        self.main_box = Gtk.VBox.new(False, 0)
        self.main_box.pack_start(grid,False,False,0)
        self.main_box.pack_start(self.main_hbox, True, True, 0)
        self.main_box.pack_start(controls, False, False, 0)
        print(type(main_window))

        main_window.add(self.main_box)
        main_window.set_default_size(640, 480)
        main_window.show_all()

        self.selected_row = self.software_TreeStore.get_selection()
        self.selected_row.connect("changed", self.item_selected)




    def delete_record(self):
        print(self.list_radio)
        print(self.deleteble_URL,"!!")
        print(self.deleteble_Name,"!!")
        print(self.deleteble_All,"!!")
       # print(self.data_list)
        print(self.interface_list)
        self.data_list.remove((self.deleteble_Name,self.deleteble_URL))
        self.interface_list.remove((self.deleteble_Name,self.deleteble_All))
      #  print(self.data_list)
        print(self.interface_list)
        self.list_radio.clear()
        for software_ref in self.interface_list:
            self.list_radio.append(list(software_ref))
        for i in range(len(self.data_list)):
            self.radio_dic.append(self.data_list[i])
        self.URL=""
        self.deleteble_All = ""
        self.deleteble_Name = ""
        self.deleteble_URL = ""






    def create_add_record_window(self,widget):
        self.record = []
        winF=AddRecordWindow(self)
        winF.set_name('pam')
        winF.show_all()

    def create_change_record_window(self,widget):
        winF=ChangeRecordWindow(self)
        winF.show_all()
        winF.set_name('pam')

        pass




    def window_open(self):

        self.filename=""
        winF=FileChooserWindowOpen()
        winF.on_file_clicked()
        self.filename=winF.return_filename()
        print(self.filename)

        winF.__del__()
        return self.filename

    def window_save(self,widget):
        winF=FileChooserWindowSave()
        winF.button_pressed(self.interface_list,self.radio_dic)
        winF.__del__()

    def open_file(self, widget):
        self.filename=self.window_open()
        if self.filename!=None:
            self.get_data_from_file(self.filename)

    def clear_ui(self,widget):
        self.list_radio.clear()
        self.interface_list=[]
        self.data_list=[]
        self.radio_dic=[]
        self.URL=""
        self.deleteble_Name=""
        self.deleteble_URL=""

        self.on_stop(self.button1)

    def exit(self,widget):
        Gtk.main_quit()

    def get_url_from_dic(self, model):
        print(model,"model@#@##@@#@")
        print(self.radio_dic)
        for i in self.radio_dic:
            if i[0]==model:
                self.result=i[1]
            #print(i)
        return self.result


    def item_selected(self, selection):
        model, row = selection.get_selected()
        print(row,"it'srow")
        if row is not None:
            print(model[row][0],"ride")
            print(model[row][1],"ride")


            print(model[row][0],"ride!!!!")
            print(self.get_url_from_dic(model[row][0]), "ride URL")

            self.URL = self.get_url_from_dic(model[row][0])
            self.deleteble_URL=self.get_url_from_dic(model[row][0])
            self.deleteble_Name=model[row][0]
            self.deleteble_All=model[row][1]

            print(model[row][1])
            print(self.URL, "new!!!!!!!!!!")
            print(model[row][0])

    def on_slider_changed(self, widget):
        value = self.slider.get_value()
        if self.obj != "":
            self.obj.on_slider_changed(value)



    def on_play(self):

        self.obj.play()


        pass

    def on_pause(self, button):

        if self.obj != "":
            print(button)
            self.obj.pause()

        pass

    def on_stop(self, button):

        if self.obj != "":
            self.obj.stop()
            self.obj = ""

        print(self.obj, "))))))")



    def start(self, widget):
        print(widget, "@4344")
        print(self.data_list)
        if self.obj == "":
            self.obj = RadioConnect(self.URL, 0.5)
            self.BuffUrl = self.URL
            self.obj.play()
            print("kek2")
        elif self.obj != "" and self.BuffUrl != self.URL:
            self.on_stop(self.button3)
            self.obj = RadioConnect(self.URL, 0.5)
            self.BuffUrl = self.URL
            self.obj.play()
            print("kek3")
        elif self.obj != "" and self.BuffUrl == self.URL:
            self.obj.play()
            print("kek4")

    def on_delete_event(self, widget, event):
        self.on_stop(None)
        Gtk.main_quit()




    def get_data_from_file(self, filename):

        file = open(filename)
        str = file.read()
        print(str)
        str = str.split("\n")
        self.list_radio.clear()
        self.radio_dic=[]
        self.data_list=[]
        self.interface_list=[]


        for i in range(len(str) - 1):
            str2 = str[i].split(",")
            print(str2)
            if str2!=['']:
                self.interface_list.append((str2[0], str2[2]))
                self.data_list.append((str2[0], str2[1]))

        print(self.data_list, "1111111")
        # self.URL = self.data_list[5][1]
        for software_ref in self.interface_list:
            self.list_radio.append(list(software_ref))
        for i in range(len(self.data_list)):
            self.radio_dic.append(self.data_list[i])


    def call_about(self,widjet):
        self.button_callback()

    def about(self):
        Gtk.MessageDialog.__init__(self, "HERO-RADIO v0.1")
        self.format_secondary_text(
            "Supe Duper Hyper Radio EVER!!!!!1111")
        self.run()
        self.destroy()

    def button_callback(self):
        self.dialog = Gtk.MessageDialog(None,0, Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.OK, "HERO-RADIO v0.1")
        self.dialog.set_name('pam')
        self.dialog.format_secondary_text(
            "Supe Duper Hyper Radio EVER!!!!!1111")
        self.dialog.run()
        print("ERROR dialog closed")
       # dialog.set_title("MessageDialog Example")

        self.dialog.destroy()


if __name__ == '__main__':
    win = RadioWindow()
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path("test.css")
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    Gtk.main()
