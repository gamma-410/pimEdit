# Create.main.py
# pim.main.py

import wx


def main():
    def clickSaveButton(event):
        saveFile = open(txtName.GetValue(), 'w')
        saveFile.write(text.GetValue())
        saveFile.close()

    if not __name__ == '__main__':  # Processing from this file.
        window = wx.App()
        frame = wx.Frame(None, -1, 'pim', size=(870, 700))

        panel = wx.Panel(frame, -1)  # createPanel
        saveButton = wx.Button(panel, -1, 'Save', pos=(120, 10))
        txtName = wx.TextCtrl(panel, -1, pos=(10, 10))
        text = wx.TextCtrl(panel, -1, pos=(10, 50), size=(850, 610), style=wx.TE_MULTILINE)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)  # fontSetting.
        text.SetFont(font)
        saveButton.Bind(wx.EVT_BUTTON, clickSaveButton)

        frame.Show()
        window.MainLoop()
