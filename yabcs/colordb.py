from collections import defaultdict
import wx


class ColorDb(list):
    name = ''
    bcs = None
    image_list = None


color_db = ColorDb()