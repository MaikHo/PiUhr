# PiUhr
Steuerungssoftware für eine Uhr für Betriebsbahner

## Installation des Steuerungsskripts
Das Skript selbst muss nicht installiert werden. Um es zu starten, im entsprechenden Ordner den Befehl `sudo ./uhr.py` ausführen. Möglicherweise muss es davor noch mit `chmod a+x uhr.py` ausführbar gemacht werden.

## Installation des Webinterfaces
Zuerst muss der Webserver nginx installiert werden: `sudo apt-get install nginx`

Die Dateien aus dem Ordner `web/` werden nun in das Verzeichnis `/var/www/html` kopiert.

Die Datei `/etc/nginx/sites-available/default` muss mit der Datei `nginx-conf/default` ersetzt werden. Anschließnd muss, damit die Konfigurationsänderungen auch in Kraft treten, der Server mit `sudo service ngnix restart` neu gestartet werden.

Jetzt ist das Webinterface von jedem anderen Computer aus dem Heimnetz unter der IP-Adresse des Pis aufrufbar.

**Hinweis**: Damit das Webinterface korrekt funktionert, muss parallel das Steuerungsskript laufen! Dies gilt aber nicht umgekehrt.

## Standardwert für Zeitfaktor ändern
Dazu die Datei `uhr.py` in einem Texteditor öffnen und die Zeile `FACTOR = 6` nach Belieben anpassen. Der Maximalwert beträgt dabei 300! 6 bedeutet 6 simulierte Minuten pro "normaler" Minute. Eine Stunde dauert also 10 Minuten.
