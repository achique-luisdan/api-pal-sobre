## Instalación (install)

### Paso 1. Crear entorno virtual

```
virtualenv env-palsobre
```

### Paso 2. Activar entorno virtual

```
env-palsobre\Scripts\activate
```

***Para desactivar el entorno virtual:***
```
deactivate
```

***Para eliminar entorno virtual***
```
rm -rf env-palsobre
```

**Ligera configuración del Windows PowerShell**

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

### Paso 3. Instalar paquetes necesario mediante PIP

```
pip install -r requirements/dev.txt
```

Para fijar o guardar un listado de los paquetes necesario de desarrollo:

```
pip freeze > requirements/dev.txt
```

### Paso 4.  Compilar Archivos Estáticos

```
python manage.py collectstatic
```

### Paso 5. Construir Esquema de Migraciones

```
python manage.py makemigrations
```

### Paso 6. Ejecutar Migraciones

```
python manage.py migrate
```