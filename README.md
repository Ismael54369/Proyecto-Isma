# 🐾 Refugidex - Proyecto Final Django

Refugidex es una aplicación web de gestión de adopciones de un refugio de animales, diseñada con una estética inmersiva inspirada en la clásica "Pokédex". Este proyecto no solo cumple con los requisitos de un CRUD tradicional, sino que añade una capa de diseño de usuario (UI/UX) premium para hacer la experiencia atractiva, moderna y completamente funcional.

----------

## 📸 Vistazo al Proyecto

<img width="1897" height="1041" alt="captura1_inicio" src="https://github.com/user-attachments/assets/a74caab8-4a67-48e0-8da4-e905a59ae85b" />

<img width="1895" height="1040" alt="captura2_principal" src="https://github.com/user-attachments/assets/e8f2373b-d6cd-48c1-9ef2-2bff0be8b782" />

<img width="1895" height="1012" alt="captura3_detalle" src="https://github.com/user-attachments/assets/39263a82-5c05-4d61-8c3f-c88f64e4ef79" />

----------

## ⭐ Características Principales y CRUD

El proyecto cumple con el modelo de operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) mediante vistas propias, garantizando que cada usuario solo pueda interactuar con sus propios registros:

-   **Crear (Create):** Los usuarios autenticados pueden enviar solicitudes de adopción detalladas (vivienda, horas en solitario, otras mascotas) para animales en estado de "Adopción".

<img width="1895" height="1040" alt="Captura de pantalla 2026-02-26 194942" src="https://github.com/user-attachments/assets/d4c01de2-ed5b-4735-9637-5f09eec90151" />
  
-   **Leer (Read):** Panel privado ("Ficha de Entrenador") donde el usuario visualiza el estado en tiempo real de sus solicitudes y su historial de donaciones económicas.

<img width="1897" height="1036" alt="captura4_perfil" src="https://github.com/user-attachments/assets/35aa5e19-b8cf-46c0-95ce-8c6644f4ba32" />
    
-   **Actualizar (Update):** Si la solicitud sigue "PENDIENTE", el usuario puede editar su formulario de adopción.

<img width="1896" height="1037" alt="Captura de pantalla 2026-02-26 194453" src="https://github.com/user-attachments/assets/214d92bd-6d61-4814-9fa8-a5d7c1d6f98f" />

-   **Eliminar (Delete):** Cancelación segura de la solicitud de adopción mediante una pantalla de confirmación, eliminando el registro de la base de datos.

<img width="1919" height="1036" alt="Captura de pantalla 2026-02-26 194647" src="https://github.com/user-attachments/assets/5c517ae6-7444-49d5-b2c5-b554e5152704" />

----------

## 🚀 Funcionalidades Extra (Valor Añadido)

Para dotar al proyecto de un acabado profesional, se han implementado las siguientes mejoras fuera de la rúbrica base:

1.  **Pasarela de Pago Simulada:** Interfaz de donaciones para animales en "Rehabilitación" con pestañas interactivas (Tarjeta, Bizum, PayPal) que demuestran el control del frontend, validando solo los datos necesarios en el backend por motivos de seguridad.

<img width="1897" height="1041" alt="captura5_pago" src="https://github.com/user-attachments/assets/7f65f468-c938-4dd9-bded-d26faf3cfdb0" />
    
2.  **Alertas Interactivas (SweetAlert2):** Integración de pop-ups dinámicos de éxito y error mediante JavaScript, sustituyendo las alertas estáticas de Bootstrap.

<img width="865" height="647" alt="captura6_alerta" src="https://github.com/user-attachments/assets/0f37aead-05c6-4262-8f5c-97fa677e6d06" />

3.  **Buscador Inteligente:** Motor de búsqueda integrado en la carcasa de la Pokédex que filtra la base de datos de animales por nombre (ignorando mayúsculas/minúsculas), complementando los filtros por categoría y estado.
    
4.  **Diseño Responsive:** Adaptabilidad total a dispositivos móviles usando la grilla y clases de Bootstrap 5.

----------

## 🛡️ Reglas de Negocio Implementadas (Backend)

Para garantizar la coherencia de los datos y evitar problemas operativos en el refugio, se han validado por código las siguientes reglas de negocio:

-   **Regla 1 (Antispam de Solicitudes):** Un usuario **no puede** enviar una nueva solicitud de adopción para un animal si ya tiene una solicitud previa en estado `PENDIENTE` o `APROBADA` para ese mismo animal. El backend intercepta la petición, bloquea el guardado en base de datos y redirige al usuario con un mensaje de error. _(Validado en views.py)_.
    
-   **Regla 2 (Flujo de Estados de Salud):** Un animal que se encuentra en estado `ADOPTADO` no puede pasar directamente al estado `REHAB` (En rehabilitación) desde el panel de administración. Requiere un proceso de devolución previo. _(Validado mediante ValidationError en el método clean del modelo Animal)_.
    
-   **Regla 3 (Donaciones restringidas):** El sistema bloquea los intentos de donación económica hacia animales que ya están sanos y listos para adopción. Solo se permiten fondos para la categoría "En Rehabilitación".
    

----------

## 💻 Tecnologías Utilizadas

**Categoría**

**Tecnología**

**Uso en el Proyecto**

**Backend**

Django 6.x (Python)

Lógica de negocio, ORM, Autenticación, Vistas, Modelos.

**Frontend**

HTML5, CSS3

Estructuración, diseño de la interfaz y customización estilo Pokédex.

**Framework CSS**

Bootstrap 5

Sistema de grid, tarjetas, botones, navbars y diseño responsive.

**Librerías JS**

SweetAlert2

Generación de modales y alertas de sistema atractivas.

**Base de Datos**

SQLite3

Almacenamiento local para desarrollo (Animales, Usuarios, Solicitudes).

----------

## ⚙️ Instrucciones de Instalación y Ejecución

Para desplegar este proyecto en un entorno local, sigue estos pasos desde la terminal de tu sistema:

**1. Clonar el repositorio:**

```
git clone https://github.com/Ismael54369/Proyecto-Isma
cd proyecto_refugio
```

**2. Crear y activar el entorno virtual:**

-   En **Windows**:
    
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
    
-   En **Mac/Linux**:
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    

**3. Instalar las dependencias necesarias:**

```
pip install django pillow

```

**4. Aplicar las migraciones a la base de datos:**

```
python manage.py makemigrations
python manage.py migrate
```

**5. Crear un superusuario (para acceder al panel de administración):**

```
python manage.py createsuperuser
```

**6. Levantar el servidor de desarrollo:**


```
python manage.py runserver
```

_La aplicación estará disponible en `http://127.0.0.1:8000` y el panel de administración en `http://127.0.0.1:8000/admin`._

----------

## 🧪 Guía Rápida de Pruebas (Para el Evaluador)

Dado que la base de datos se entrega vacía por defecto, se recomienda seguir este flujo para testear todas las funcionalidades:

1.  **Poblar la base de datos:** Accede a `/admin` con tu superusuario. Crea 2 "Especies", 3 "Rasgos" y al menos 2 "Animales" (uno en estado _Adopción_ y otro en _Rehabilitación_). Sube una imagen para cada uno.
    
2.  **Registro de usuario:** Ve a la web principal (`/`), haz clic en "Registrarse" y crea una cuenta de Entrenador (usuario normal).
    
3.  **Probar CRUD (C):** Entra al detalle del animal en "Adopción" e intenta adoptarlo rellenando el formulario.
    
4.  **Probar Regla de Negocio:** Vuelve a intentar adoptar al mismo animal. El sistema te bloqueará el acceso.
    
5.  **Probar CRUD (R y U):** Ve a "Mi Perfil", revisa que tu solicitud aparece listada y haz clic en "Editar" para modificar tus datos.
    
6.  **Probar Donaciones:** Entra al detalle del animal en "Rehabilitación", usa la pasarela de pago y verifica que la transacción aparece en tu Ficha de Entrenador (Mi Perfil).
    
7.  **Probar CRUD (D):** Cancela tu solicitud de adopción desde tu perfil y verifica que desaparece.

--- 
*Desarrollado por Ismael González Tempa.*
 
*"El vínculo entre un Entrenador y su compañero es para siempre. ¡Tenemos que adoptarlos a todos!"* 🔴⚪

 ---
