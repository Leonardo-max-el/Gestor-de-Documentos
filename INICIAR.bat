@echo off
chcp 65001 >nul
echo ============================================================
echo   Sistema de Registros Academicos - Iniciando...
echo ============================================================
echo.

REM Activar entorno virtual
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Entorno virtual no encontrado.
    echo Ejecuta primero: INSTALAR.bat
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo [OK] Sistema iniciado
echo.
echo Abre tu navegador en:
echo   http://127.0.0.1:8000
echo.
echo Presiona Ctrl+C para detener el servidor
echo ============================================================
echo.

python manage.py runserver 127.0.0.1:8000
pause
