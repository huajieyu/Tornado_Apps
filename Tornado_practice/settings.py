# settings.py
from bkhandlers.MessageBuffer import MessageBuffer

def init():
    global global_message_buffer
    global_message_buffer = MessageBuffer()
    global sitectldict
    key_list = ["selsite", "selsubnet", "selcrb", "selcortex", "selaction", "seltdobj", "selcrbsec", "selcortexsec"]
    val_list = ["NONE", "NONE", "NONE", "NONE", "NONE", "NONE", "NONE", "NONE"]
    sitectldict = dict(zip(key_list, val_list))
