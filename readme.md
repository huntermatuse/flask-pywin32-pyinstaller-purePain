for reference later or you do not need to feel my pain

https://stackoverflow.com/questions/41200068/python-windows-service-error-starting-service-the-service-did-not-respond-to-t
if len(sys.argv) > 1:
       # Called by Windows shell. Handling arguments such as: Install, Remove, etc.
       win32serviceutil.HandleCommandLine(JobManager)
else:
    # Called by Windows Service. Initialize the service to communicate with the system operator
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(JobManager)
    servicemanager.StartServiceCtrlDispatcher()

https://pypi.org/project/pywin32/

https://stackoverflow.com/questions/55677165/python-flask-as-windows-service

https://github.com/top2topii/FlaskServiceWin32/blob/master/README.md

https://stackoverflow.com/questions/50590796/having-several-issues-with-a-python-service-for-windows

https://stackoverflow.com/questions/23550067/deploy-flask-app-as-windows-service

python .\env\Scripts\pywin32_postinstall.py --install