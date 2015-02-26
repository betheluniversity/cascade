BR = "<br />\n"
HR = "<hr class='thin width100 text_lightgray bg_lightgray' />"
E_H2 = "</h2>\n"
S_H2 = "<h2>"
E_LI = "</li>\n"
S_LI = "<li>\n"
E_PRE = "</pre>\n"
S_PRE = "<pre>\n"
SPACE = "&nbsp&nbsp&nbsp&nbsp"
E_STRONG = "</strong>\n"
S_STRONG = "<strong>\n"
E_UL = "</ul>\n"
S_UL = "<ul>\n"
S_SPAN = "<span style='color:redfont-weight:bold'>"
E_SPAN = "</span>"

import os
import glob
modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules]