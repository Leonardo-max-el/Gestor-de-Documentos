# 📚 Sistema de Gestión de Registros Académicos

Sistema web local para la gestión de expedientes académicos de estudiantes.

---

## ⚙️ INSTALACIÓN EN WINDOWS

### Requisitos previos
- **Python 3.10 o superior** — https://www.python.org/downloads/
  - ⚠️ Durante la instalación marca la casilla **"Add Python to PATH"**
- Conexión a internet (solo para la instalación)

### Pasos de instalación

1. **Descarga y descomprime** el archivo del sistema en una carpeta de tu PC  
   Ejemplo: `C:\RegistrosAcademicos\`

2. **Doble clic en `INSTALAR.bat`**  
   Esto hará automáticamente:
   - Crear el entorno virtual de Python
   - Instalar todas las librerías necesarias
   - Crear la base de datos SQLite
   - Pedirte crear un usuario administrador (tu login)

3. **Doble clic en `INICIAR.bat`** para arrancar el sistema

4. Abre tu navegador en: **http://127.0.0.1:8000**

---

## 🚀 USO DIARIO

Para usar el sistema cada día:
1. Doble clic en `INICIAR.bat`
2. Abrir navegador → `http://127.0.0.1:8000`
3. Al terminar: cierra la ventana negra del servidor

---

## 🖥️ FUNCIONALIDADES

### Dashboard (pantalla principal)
- Lista de todos los estudiantes con semáforo de estado
- 🟢 **Verde** = Todos los archivos entregados
- 🔴 **Rojo** = Faltan archivos
- Badges por archivo: DNI · SOL · FOTO · PAG · RSC · CERT · PROY · ADEU
- Buscador en tiempo real
- Botón para crear nuevo estudiante

### Vista de Expediente
**Panel izquierdo (30%):** Formulario del estudiante
- Apellidos y Nombres
- DNI
- N° Expediente (manual)
- Proveído
- Escuela Profesional (desplegable con 21 opciones)
- Celular y Correo
- Indicadores visuales de archivos entregados/pendientes

**Panel derecho (70%):** Visor de documentos
- Sección **Expediente 1**: DNI, Solicitud, Fotografía, Recibo, Registro de Graduados
- Sección **Expediente 2**: Certificado de Notas, Const. Proyección, Const. No Adeudo
- Sección **Resoluciones adicionales**

### Para cada documento:
- 📂 Subir por clic o arrastrando el archivo
- 👁️ Ver el documento completo desplegando el acordeón
- 🔍 Zoom + y - en PDFs e imágenes
- ✋ Arrastre con el mouse para moverse en la imagen
- 🗑️ Botón eliminar

### Renombrado automático
Al guardar los datos del estudiante, los nombres correctos aparecen debajo de cada archivo:

**Expediente 1:**
| Archivo | Nombre final |
|---------|-------------|
| DNI | R05_[DNI]_DNI.pdf |
| Solicitud | R04_[DNI]_SOL.pdf |
| Recibo | R03_[DNI]_PAG.pdf |
| Registro Graduados | R01_[DNI]_RSC.pdf |
| Fotografía | Cmatricula_[ApellidosNombres].jpg |

**Expediente 2:**
| Archivo | Nombre final |
|---------|-------------|
| Cert. Notas | 1 Certificado de Notas [Nombre].pdf |
| Const. Proyección | 2° Constancia de Proyección Social [Nombre].pdf |
| Const. No Adeudo | 3° Constancia NO Adeudo [Nombre].pdf |

### Descargas
- **Descargar Exp.1 (ZIP)** → Carpeta `Informe_R06_[DNI]_FAC.zip` con los 5 archivos renombrados
- **Descargar PDF unido** → `R07-FAC-[DNI]-2026-PRUEBA.pdf` con los 3 archivos del Exp.2 fusionados
- **Informe Word** → `INFORME_[NExpediente]_[DNI].docx` — te pedirá la fecha

---

## 📄 PLANTILLA WORD PERSONALIZADA

Para usar tu propio diseño de informe:

1. Crea un archivo Word llamado exactamente: `plantilla_informe.docx`
2. Guárdalo en la carpeta: `plantillas_word\`
3. Usa estas variables en tu plantilla (se reemplazarán automáticamente):

| Variable | Se reemplaza con |
|----------|-----------------|
| `{{FECHA}}` | Fecha seleccionada |
| `{{NOMBRE}}` | Apellidos y Nombres |
| `{{DNI}}` | Número de DNI |
| `{{EXPEDIENTE}}` | N° de Expediente |
| `{{PROVEIDO}}` | Proveído |
| `{{ESCUELA}}` | Escuela Profesional |
| `{{CELULAR}}` | Celular |
| `{{CORREO}}` | Correo electrónico |

Si no hay plantilla, el sistema genera un informe por defecto.

---

## 🔒 SEGURIDAD

- El sistema requiere usuario y contraseña para acceder
- Solo funciona en tu computadora local (no es accesible desde internet)
- Los archivos se guardan en la carpeta `media\` del sistema

---

## 📁 ESTRUCTURA DE ARCHIVOS

```
RegistrosAcademicos/
├── INSTALAR.bat          ← Ejecutar primero (una sola vez)
├── INICIAR.bat           ← Ejecutar cada vez para usar
├── manage.py
├── requirements.txt
├── plantillas_word\      ← Aquí va tu plantilla Word personalizada
├── media\                ← Aquí se guardan los archivos subidos
│   └── expedientes\
│       └── [DNI]\
│           ├── exp1\
│           ├── exp2\
│           └── resoluciones\
├── db.sqlite3            ← Base de datos (se crea sola)
├── registros_academicos\ ← Configuración del sistema
└── expedientes\          ← Código de la aplicación
```

---

## 🛠️ SOLUCIÓN DE PROBLEMAS

**"Python no está instalado"**
→ Descarga Python desde python.org y marca "Add Python to PATH"

**"No se puede subir archivo PDF"**
→ Verifica que el archivo no esté abierto en otro programa

**"Error al unir PDFs"**
→ El sistema instalará pypdf automáticamente. Si falla, los descargará en ZIP

**El sistema no abre**
→ Ejecuta `INICIAR.bat` como administrador (clic derecho → Ejecutar como administrador)

---

## 📞 SOPORTE

Sistema desarrollado para el Área de Registros Académicos.
Para cambiar la contraseña: http://127.0.0.1:8000/admin/
