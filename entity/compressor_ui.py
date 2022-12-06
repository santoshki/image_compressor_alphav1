import wx
from usecase.compressor import CompressionEngine


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Fx_Image Compressor Alphav1.0')
        panel = wx.Panel(self)
        image_upload_button = wx.Button(panel, label='Upload Image', pos=(150, 150))
        image_upload_button.Bind(wx.EVT_BUTTON, self.on_click())
        self.Show()

    def on_click(self, event):
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


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()