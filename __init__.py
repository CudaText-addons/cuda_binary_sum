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


    def base2tohex(self):
        '''
        E.g. I have a file with the following lines:
        00000000000000000000000000001000, 00000000000000000000000000000000, 00000000000000000000000000010000, 00000000000000000000000000111000, 00000000000000000000000000110000, 00000000000000000000000001000000,
        And I want to see them in hex representation:
        0000_0008, 0000_0000, 0000_0010, 0000_0038, 0000_0030, 0000_0040,
        '''

        def do_fmt(n):
            s = '%08x'%n
            s = s[:4] + '_' + s[4:]
            return s

        s = ed.get_text_all()

        s = s.replace(' ', ',')
        s = s.replace(';', ',')
        s = s.replace('\n', ',')
        s = s.replace('\t', ',')
        l = s.split(',')

        l = [int(s, 2) for s in l if s]
        l = [do_fmt(n) for n in l]

        out = ', '.join(l)+','

        #put to new tab
        file_open('')
        ed.set_text_all(out)


    def sort_by_len(self):
        text = ed.get_text_all()
        text = text.splitlines()
        text = [s for s in text if s]
        text = sorted(text, key = lambda x: '%5s'%len(x)+x)
        eol = '\n'
        text = eol.join(text)+eol
        ed.set_text_all(text)

