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
        self.compress_action_button = wx.Button(panel, label='Compress', pos=(150, 150))
        self.progress_bar = wx.Gauge(panel, size=(150, 25), pos=(200, 300))
        self.image_browse_button.Bind(wx.EVT_BUTTON, self.on_click_image_browse)
        self.compress_action_button.Bind(wx.EVT_BUTTON, self.on_click_compress)
        self.Show()

    def on_click_image_browse(self, event):
        try:
            print("Image upload button pressed.\nOpening File selection dialog box...")
            select_file_dialog_ui = wx.FileDialog(frame, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
            select_file_dialog_ui.ShowModal()
            print("Image File selected")
            print("File name:", select_file_dialog_ui.GetFilename())
            filepath = select_file_dialog_ui.GetPath()
            filepath_str = str(filepath)
            filepath_addr = filepath_str.replace(str(select_file_dialog_ui.GetFilename()), '')
            print("File path:", filepath_addr)
            CompressionEngine.image_compression(filepath_addr, select_file_dialog_ui.GetFilename())
            select_file_dialog_ui.Destroy()
        except Exception as e:
            print("Exception occurred:", e)

    def on_click_compress(self, event):
        try:
            pass
        except Exception as e:
            print("Exception occurred:", e)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()