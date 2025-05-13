import wx

class WxUtils(object):

    def set_font_size(label, size):
        font = label.GetFont()
        font.SetPointSize(size)
        label.SetFont(font)
        return font

    def set_font_bold(label):
        font = label.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)
        return font

    def set_font_size_and_bold(label, size):
        font = label.GetFont()
        font.SetPointSize(size)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)
        return font

    def set_font_size_and_bold_and_roman(label, size):
        font = label.GetFont()
        font.SetPointSize(size)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        font.SetFamily(wx.ROMAN)
        label.SetFont(font)
        return font
