from cudatext import *

MAX_BITS = 64

class Command:
    def binarysum_msg(self):

        s = dlg_input('Enter decimal or hex (with 0x), to show its binary sum:', '')
        if not s: return
        s = self.binarysum_result(s)
        msg_box(s, MB_OK+MB_ICONINFO)

    def binarysum_editor(self):

        s = dlg_input('Enter decimal or hex (with 0x), to show its binary sum:', '')
        if not s: return
        s = self.binarysum_result(s)
        file_open('')
        ed.set_text_all(s)

    def binarysum_result(self, s):

        try:
            if s.startswith('0x'):
                n = int(s, 16)
            else:
                n = int(s)
        except:
            msg_box('Incorrect number: '+s, MB_OK+MB_ICONERROR)
            return

        res = []
        res2 = []
        for i in range(MAX_BITS):
            step = 1<<i
            if n & step == step:
                res += [str(step)]
                res2 += [str(i)]

        res = ' + '.join(res)
        res2 = ' '.join(res2)
        s10 = str(n)
        s16 = hex(n)

        return '%s (%s)\n= %s\nbits %s' % (s10, s16, res, res2)

