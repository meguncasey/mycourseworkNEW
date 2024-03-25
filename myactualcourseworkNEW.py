import wx
import re


def onUsernameMenu(evt):
    if evt.GetId() == window.menuIdCheck:
        print("Check Username")
        lbl.Show()
        txt.Show()
        btn.Show()
        lbl.SetLabel("Enter your username: ")
        
        window.Bind(wx.EVT_BUTTON, onCheckUsername, id=btn.GetId())


def onCheckUsername(evt):
    err.Hide()
    password = txt.GetValue()
    print("Checking Username")
    print(username)

    doUsernameCheck(username)
    


def doUsernameCheck(username):
    errorText = ""
    passed = True

    reg = re.compile('18004097')
    print(bool(reg.search(username)))

##    if len(username) == 18004097: 
##        passed
##
##    #if not bool(reg.search(username)):
##     #   errorText = "Must xxxxxxxx"
##     #   passed
##
##    if not passed:
##        lbl.SetLabel(errorText)
##        err.Show()

def onPasswordMenu(evt):
    if evt.GetId() == window.menuIdCheck:
        print("Check Password")
        lbl.Show()
        txt.Show()
        btn.Show()
        lbl.SetLabel("Enter your Password: ")
        
        window.Bind(wx.EVT_BUTTON, onCheckPassword, id=btn.GetId())


def onCheckPassword(evt):
    err.Hide()
    password = txt.GetValue()
    print("Checking Password")
    print(password)

    doPasswordCheck(password)
    


def doPasswordCheck(password):
    errorText = ""
    passed = True

    reg = re.compile('pass1')
    print(bool(reg.search(password)))

##    if len(username) == pass1: 
##        passed
##
##    #if not bool(reg.search(username)):
##     #   errorText = "Must xxxxxxxx"
##     #   passed
##
##    if not passed:
##        lbl.SetLabel(errorText)
##        err.Show()

def yourdetails(evt):
    if evt.GetId() == window.menuIdCheck:
        print("Check Username")
        lbl.Show()
        lbl.SetLabel("hello megan") 
        window.Bind(wx.EVT_BUTTON, yourdetails, id=btn.GetId())


app = wx.App()
window = wx.Frame(None, title="Login Program", size=(300, 200))
panel = wx.Panel(window)
lbl = wx.StaticText(panel, label="Login Program", pos=(150, 20))
txt = wx.TextCtrl(panel, pos=(50, 50), size=(150, 20))
btn = wx.Button(panel, wx.ID_ANY, "Check", pos=(50, 110))
err = wx.StaticText(panel, label="No error!", pos=(50, 110))


username = "18004097"
password = "pass1"

lbl.Hide()
txt.Hide()
btn.Hide()
err.Hide()

menubar = wx.MenuBar()
pwMenu = wx.Menu()

window.menuIdCheck = wx.NewId()
pwCheck = pwMenu.Append(window.menuIdCheck, "Username Menu")
window.Bind(wx.EVT_MENU, onUsernameMenu, pwCheck)

window.menuIdCheck = wx.NewId()
pwCheck = pwMenu.Append(window.menuIdCheck, "Password Menu")
window.Bind(wx.EVT_MENU, onPasswordMenu, pwCheck)

window.menuIdCheck = wx.NewId()
pwCheck = pwMenu.Append(window.menuIdCheck, "Your Deails")
window.Bind(wx.EVT_MENU, yourdetails, pwCheck)

menubar.Append(pwMenu, "Login")
window.SetMenuBar(menubar)

window.Show(True)
app.MainLoop()
