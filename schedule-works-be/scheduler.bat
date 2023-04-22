echo %*
@REM python -u "c:\Program Files\ScheduleWorks\schedule-works-be\scheduler.py" -m "CSC 3200 5"
python -u "C:\Program Files\ScheduleWorks\schedule-works-be\scheduler.py" "--courses" "%*"
@REM python manual_get_data.py --sid=%1 --passwd=%2
