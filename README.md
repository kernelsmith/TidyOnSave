TidyOnSave Sublime Text 2 Plugin
=====================================

This simple plugin runs msftidy (from the Metasploit Framework) on the saved file and
displays the output from it.

Installation
------------

**With the Package Control plugin** and the **Git Package installed** the easiest way to install TidyOnSave is by adding TidyOnSave's github repo to Sublime and then installing the package.  The 
full directions for the entire process are shown below, but you can skip to step 3 if you have 
package control and the git package already installed

1)  Install package control in sublime:  http://wbond.net/sublime_packages/package_control/installation.  For the impatient: 
 
2)  Install the git package (https://github.com/kemayo/sublime-text-2-git/wiki):  
 a) Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 b) Select "Package Control: Install Package" (it'll take a few seconds)
 c) Select Git when the list appears.
 
3)  Install various cool things like TidyOnSave by just pointing sublime to github repos:
 a) Reference http://wbond.net/sublime_packages/package_control/usage for more on this process
 b) Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 c) Type repo
 d) Find and click "Package Control: Add Repository"
 e) Paste https://github.com/kernelsmith/TidyOnSave and hit enter
 f) Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 g) Type TidyOnSave, select it
 h) Bask in glory

**Without Git:** Download the latest source from [GitHub](https://github.com/kernelsmith/TidyOnSave) and copy the TidyOnSave folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone git://github.com/kernelsmith/TidyOnSave.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/


Configuration
-------------

There aren't many configuration options available to customize the behavior of TidyOnSave. For the latest information on what options are available, select the menu item `Preferences->Package Settings->TidyOnSave->Settings - Default`.

Do **NOT** edit the default TidyOnSave settings. Your changes will be lost when TidyOnSave is updated. ALWAYS edit the user TidyOnSave settings by selecting `Preferences->Package Settings->TidyOnSave->Settings - User`.

 You need to edit the `tidy_on_save_cmd` setting to match your path to msftidy.rb which is typically
  <msf_install_dir>/tools/msftidy.rb, on most linux machines you can do 'locate msftidy.rb'.

### Per project

TidyOnSave supports per-project settings. This isn't likely to be very useful, maybe if you have different versions of msftidy you are trying out I guess, or maybe you want to test msftidy itself on different ruby interpreters for discrepancies.  To edit your project settings, select the menu item `Project->Edit Project`. If there is no `settings` object at the top level, add one and then add the `tidy_on_save_cmd` setting, like below.  I just made this example up, YMMV


    {
        "folders":
          [
              {
                  "path": "/home/ks/testing_msftidy/"
              }
          ],
          "settings":
          {
              "tidy_on_save_cmd": "/home/ks/.rvm/rubies/ruby-1.9.3-p194/bin/ruby /home/ks/testing_msftidy/msftidy.rb"
          }
    }
