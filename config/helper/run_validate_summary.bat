@echo off
setlocal enabledelayedexpansion

:: Initialize a flag to check for the error string
set "error_found=false"

:: Run validate_jsons.py and capture the output
for /f "delims=" %%A in ('python validate_jsons.py 2^>^&1') do (
    set "line=%%A"
    echo !line!
    :: Check if the line contains the error string
    echo !line! | findstr /C:"JSON file format is invalid. Please fix all below error." >nul
    if !errorlevel! equ 0 (
        set "error_found=true"
    )
)

:: Check the flag and decide whether to run summary.py
if "!error_found!" == "true" (
    echo Some JSON files are invalid. Fix the errors to generate the updated summary file.
    pause
    exit /b 1
) else (
    python summary.py
    pause
)

endlocal
