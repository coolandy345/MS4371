; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "MS4371 ������R����p�d�C�F"
#define MyAppVersion "1.2.1"
#define MyAppPublisher "������Ѓ��g���}"
#define MyAppURL "https://www.motoyama.co.jp/"
#define MyAppExeName "MS4371 ������R����p�d�C�F.exe"     


[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{FC8FA274-98AF-4D72-B1FF-C9457F22E673}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
AppCopyright=Copyright (C) 1997-2022 MOTOYAMA.co.,ltd
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application
OutputBaseFilename=MS4371 ������R����p�d�C�F installer 
SetupIconFile=C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\icon.ico   
ShowTasksTreeLines=yes



[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\libusb-1.0.dll"; DestDir: "{sys}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\error.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\warning.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\Database and Profile\*"; DestDir: "{app}\Database and Profile"; Flags: ignoreversion recursesubdirs createallsubdirs onlyifdoesntexist
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\gui_main\*"; DestDir: "{app}\gui_main"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\PyQt5.uic.widget-plugins\*"; DestDir: "{app}\PyQt5.uic.widget-plugins"; Flags: ignoreversion recursesubdirs createallsubdirs     
Source: "C:\Users\kou\source\repos\MS4371-Main Program Source Code\Application\execute file\�������\*"; DestDir: "{app}\�������"; Flags: ignoreversion recursesubdirs createallsubdirs

; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

