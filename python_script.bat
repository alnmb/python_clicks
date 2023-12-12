@echo off
echo Activating the virtual environment...
call .\python_clicks\Scripts\activate
pause
echo Running the Python script...
call python .\python_clicks.py
@echo off
call \python_clicks\Scripts\deactivate
