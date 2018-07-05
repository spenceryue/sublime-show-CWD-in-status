import sublime, sublime_plugin

class ShowCWDInStatus(sublime_plugin.EventListener):
    def on_activated_async(self, view):
       CWD = view.file_name()
       if CWD is None:
           # view.erase_status('_CWD')
           pass
       else:
           print (CWD)
           # view.set_status('_CWD', CWD)
