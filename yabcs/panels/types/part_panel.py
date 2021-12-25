from yabcs.panels.types import BasePanel
import wx


class PartPanel(BasePanel):
    def __init__(self, *args):
        BasePanel.__init__(self, *args)

        self.controls['name'] = self.add_text_entry(self.entry_page, 'Name', maxlen=3)
        self.controls['model'] = self.add_num_entry(self.entry_page, 'Model')
        self.controls['model2'] = self.add_num_entry(self.entry_page, 'Model2')
        self.controls['texture'] = self.add_num_entry(self.entry_page, 'Texture')
        self.controls['f_24'] = self.add_float_entry(self.entry_page, 'Left Eye Movement Strength')
        self.controls['f_28'] = self.add_float_entry(self.entry_page, 'Right Eye Movement Strength')
        self.controls['emd_name'] = self.add_text_entry(self.entry_page, 'EMD Name')
        self.controls['emm_name'] = self.add_text_entry(self.entry_page, 'EMM Name')
        self.controls['emb_name'] = self.add_text_entry(self.entry_page, 'EMB Name')
        self.controls['ean_name'] = self.add_text_entry(self.entry_page, 'EAN Name')
        self.controls['dyt_options'] = self.add_unknown_hex_entry(self.entry_page, 'DYT Options', showKnown=True, cols=4, knownValues={
            0x0: 'Standard',
            0x2: 'Model 2 DYT',
            0x4: 'Accessories',
            0xc: 'Green Scouter Overlay',
            0x14: 'Red Scouter Overlay',
            0x24: 'Blue Scouter Overlay',
            0x44: 'Purple Scouter Overlay',
            0x204: 'Orange Scouter Overlay',
        })
        self.controls['part_hiding'] = self.add_multiple_selection_entry(self.entry_page, 'Part Hiding', choices=[
            ('', ['Wrists', 'Boots'], True),
            ('', ['Face_ear', 'Hair', 'Bust', 'Pants'], True),
            ('', ['Face_base', 'Face_forehead', 'Face_eye', 'Face_nose'], True),
        ])

        self.controls['u_06'] = self.add_hex_entry(self.unknown_page, 'U_06', max=self.MAX_UINT16)
        self.controls['u_08'] = self.add_hex_entry(self.unknown_page, 'U_08', max=self.MAX_UINT16)
        self.controls['u_10'] = self.add_hex_entry(self.unknown_page, 'U_10', max=self.MAX_UINT64)
        self.controls['u_20'] = self.add_hex_entry(self.unknown_page, 'U_20')
        self.controls['u_2c'] = self.add_hex_entry(self.unknown_page, 'U_2C')
        self.controls['u_30'] = self.add_hex_entry(self.unknown_page, 'U_30')
        self.controls['u_48'] = self.add_hex_entry(self.unknown_page, 'U_48', max=self.MAX_UINT16)
        self.controls['u_50'] = self.add_hex_entry(self.unknown_page, 'U_50', max=self.MAX_UINT16)
