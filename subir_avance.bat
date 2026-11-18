@echo off
chcp 65001 >nul
echo ==============================================
echo   Subir nuevo avance a GitHub - FlightTracker
echo ==============================================
echo.
set /p mensaje="Describe el avance o cambio realizado: "
if "%mensaje%"=="" set mensaje=Actualización y avances del proyecto

git add .
git commit -m "%mensaje%"
git push origin main

echo.
echo ==============================================
echo   ¡Avance subido a GitHub correctamente!
echo   Enlace: https://github.com/brostfm/proyecto_modulo
echo ==============================================
pause
