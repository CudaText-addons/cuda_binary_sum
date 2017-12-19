from cudatext import *

class Command:
    def show_sum(self):

        s = dlg_input('Enter decimal or hex (with 0x), to show its binary sum:', '')
        if not s: return
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
        for i in range(32):
            step = 1<<i
            if n & step == step:
                res += [str(step)]
                res2 += ['2^'+str(i)]

        res = ' + '.join(res)
        res2 = ' + '.join(res2)
        s10 = str(n)
        s16 = hex(n)

        msg_box('%s (%s)\n= %s\n= %s' % (s10, s16, res, res2), MB_OK+MB_ICONINFO)
