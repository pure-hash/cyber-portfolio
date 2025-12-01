FROM mcr.microsoft.com/windows/servercore:ltsc2022

# ---- Sysmon Install ----
ADD https://download.sysinternals.com/files/Sysmon.zip C:\\Sysmon.zip
RUN powershell -Command "Expand-Archive C:\\Sysmon.zip -DestinationPath C:\\Sysmon"

# ---- Atomic Red Team Install ----
RUN powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force"
RUN powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1 -OutFile install.ps1"
RUN powershell -File install.ps1

# ---- Copy Sysmon config ----
COPY ../config/sysmon_config.xml C:\\sysmon_config.xml

# ---- Install Sysmon with config ----
RUN C:\\Sysmon\\Sysmon64.exe -accepteula -i C:\\sysmon_config.xml

# ---- Entry ----
CMD ["powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass"]
