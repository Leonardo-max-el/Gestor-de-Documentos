@echo off
chcp 65001 >nul
echo ============================================================
echo   INSTALADOR - Sistema de Registros Academicos
echo ============================================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado.
    echo Descargalo desde: https://www.python.org/downloads/
    echo IMPORTANTE: Marca la casilla "Add Python to PATH"
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Crear entorno virtual
echo [1/5] Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] No se pudo crear el entorno virtual
    pause
    exit /b 1
)
echo [OK] Entorno virtual creado
echo.

REM Activar e instalar dependencias
echo [2/5] Instalando dependencias (puede tardar unos minutos)...
call venv\Scripts\activate.bat
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Error instalando dependencias
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas
echo.

REM Crear carpetas necesarias
echo [3/5] Creando carpetas del sistema...
if not exist "media" mkdir media
if not exist "media\expedientes" mkdir media\expedientes
if not exist "staticfiles" mkdir staticfiles
if not exist "plantillas_word" mkdir plantillas_word
echo [OK] Carpetas creadas
echo.

REM Migraciones
echo [4/5] Configurando base de datos...
python manage.py migrate --run-syncdb
if errorlevel 1 (
    echo [ERROR] Error en migraciones
    pause
    exit /b 1
)
echo [OK] Base de datos configurada
echo.

REM Crear superusuario
echo [5/5] Configurando usuario administrador...
echo.
echo Ingresa los datos para el usuario administrador:
python manage.py createsuperuser
echo.

echo ============================================================
echo   INSTALACION COMPLETADA EXITOSAMENTE
echo ============================================================
echo.
echo Para iniciar el sistema ejecuta: INICIAR.bat
echo O desde la consola: python manage.py runserver
echo Luego abre tu navegador en: http://127.0.0.1:8000
echo.
echo NOTA: La carpeta "plantillas_word" esta lista para agregar
echo       tu plantilla personalizada (plantilla_informe.docx)
echo.
pause
