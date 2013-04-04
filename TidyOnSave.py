import sublime, sublime_plugin

class TidyOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if view.file_name()[-3:] == '.rb':
            view.window().run_command("tidy_on_save", {"saving": True})

class TidyOnSaveCommand(sublime_plugin.TextCommand):
    def run(self, edit, saving=False):
        view = self.view
        global_settings = sublime.load_settings(__name__ + '.sublime-settings')
        cmd_setting = 'tidy_on_save_cmd'
        tidy = view.settings().get(cmd_setting, global_settings.get(cmd_setting))
        view.window().run_command("exec", {"cmd": [tidy, view.file_name()]})