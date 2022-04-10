Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run "cmd /K F: & CD F:\Progetti python\speedtester\ & file.cmd",0
Set WshShell = Nothing