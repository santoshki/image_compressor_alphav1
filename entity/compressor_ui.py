import wx
from usecase.compressor import CompressionEngine


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Fx_Image Compressor Alphav1.0')
        panel = wx.Panel(self)
        self.browse_image_file_label = wx.StaticText(panel, id=1, label="Old Label.", pos=(150, 50),
                                                     size=wx.DefaultSize, style=0, name="statictext")
        self.browse_image_file_label.SetLabel("Browse Image file")
        self.image_browse_button = wx.Button(panel, label='Browse', pos=(25, 100))
        self.textbox = wx.TextCtrl(panel, size=(250, -1), pos=(100, 100))
        self.compress_action_button = wx.Button(panel, label='Compress', pos=(150, 140))
        self.progress_bar = wx.Gauge(panel, size=(180, 10), pos=(95, 180))
        self.image_browse_button.Bind(wx.EVT_BUTTON, self.on_click_image_browse)
        self.compress_action_button.Bind(wx.EVT_BUTTON, self.on_click_compress)
        self.Show()

    def on_click_image_browse(self, event):
        try:
            print("Image upload button pressed.\nOpening File selection dialog box...")
            self.select_file_dialog_ui = wx.FileDialog(frame, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
            self.select_file_dialog_ui.ShowModal()
            print("Image File selected")
            print("File name:", self.select_file_dialog_ui.GetFilename())
            self.filepath = self.select_file_dialog_ui.GetPath()
            self.filepath_str = str(self.filepath)
            self.filepath_addr = self.filepath_str.replace(str(self.select_file_dialog_ui.GetFilename()), '')
            print("File path:", self.filepath_addr)
            self.textbox.SetLabel(str(self.select_file_dialog_ui.GetPath()))
        except Exception as e:
            print("Exception occurred:", e)

    def on_click_compress(self, event):
        try:
            CompressionEngine.image_compression(self.filepath_addr, self.select_file_dialog_ui.GetFilename())
            self.select_file_dialog_ui.Destroy()
        except Exception as e:
            print("Exception occurred:", e)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
