@ECHO off

echo 获取Administrator权限
cacls.exe "%SystemDrive%\System Volume Information" >nul 2>nul
if %errorlevel%==0 goto Admin
if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"
echo Set RequestUAC = CreateObject^("Shell.Application"^)>"%temp%\getadmin.vbs"
echo RequestUAC.ShellExecute "%~s0","","","runas",1 >>"%temp%\getadmin.vbs"
echo WScript.Quit >>"%temp%\getadmin.vbs"
"%temp%\getadmin.vbs" /f
if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"
exit

:Admin

cd %~dp0
cd requestid

echo mitmproxy.cer
certmgr.exe -add mitmproxy.cer -s -r localMachine trustedpublisher
certmgr.exe -add mitmproxy.cer -s -r localMachine AuthRoot
echo .

echo Python37.msi
start /wait Python37.msi /quiet /passive
echo.


echo vc++2015.msi
start /wait vc_redist.x64.exe /q
echo.

