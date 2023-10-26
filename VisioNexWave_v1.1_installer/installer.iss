[Setup]
AppName=VisionexWave
AppVersion=1.1
DefaultDirName={pf}\VisionexWave
OutputDir=Output
OutputBaseFilename=VisioNex_Wave_v1.1
;Modificar/automatizar próximamente

[Dirs]
Name: "{pf}\VisionexWave"

[Files]
; Copia los archivos y directorios necesarios desde las carpetas build y dist
Source: "dist*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "build*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Añade aquí cualquier otro archivo o recurso necesario para tu aplicación

[Tasks]
Name: desktopicon; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Opciones adicionales"
Name: autostart; Description: "Agregar al inicio"; GroupDescription: "Opciones adicionales"

[Icons]
Name: "{group}\VisionexWave"; Filename: "{app}\TuEjecutable.exe"; Tasks: desktopicon
Name: "{commonstartup}\VisionexWave"; Filename: "{app}\TuEjecutable.exe"; Tasks: autostart

[Code]
procedure CurPageChanged(CurPageID: Integer);
begin
  if CurPageID = wpInstalling then
  begin
    // Muestra un mensaje acceso a pagina web y github
    MsgBox('Gracias por instalar Visionex Wave. Para más información, visita nuestra wiki: "http://visionexwave.wikidot.com/start", o a nuestro repositorio en GitHub: "https://github.com/Nisamov/VisioNexWave".', mbInformation, MB_OK);
  end;
end;