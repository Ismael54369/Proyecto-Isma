from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# 1. Modelo Auxiliar (Categoría / Tipo Pokémon)
class Especie(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# 2. Modelo Auxiliar para M2M (Etiquetas)
class Rasgo(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

# 3. Modelo Principal (El Animal)
class Animal(models.Model):
    OPCIONES_ESTADO = [
        ('ADOPCION', 'En Adopción'),
        ('REHAB', 'En Rehabilitación'),
        ('ADOPTADO', 'Adoptado'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.RESTRICT)
    rasgos = models.ManyToManyField(Rasgo, blank=True)
    
    foto = models.ImageField(upload_to='animales/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    historia = models.TextField()
    estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default='ADOPCION')
    
    def clean(self):
        if self.pk:
            antiguo_estado = Animal.objects.get(pk=self.pk).estado
            if antiguo_estado == 'ADOPTADO' and self.estado == 'REHAB':
                raise ValidationError("Un animal adoptado no puede pasar a rehabilitación directamente. Debe ser devuelto primero.")

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

# 4. Modelo: La Solicitud de Adopción (CRUD principal)
class SolicitudAdopcion(models.Model):
    ESTADOS_SOLICITUD = [
        ('PENDIENTE', 'Pendiente de revisión'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
    ]
    
    VIVIENDA_CHOICES = [
        ('PISO', 'Piso / Apartamento'),
        ('CASA', 'Casa con jardín / Adosado'),
        ('FINCA', 'Finca / Terreno rústico'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    telefono = models.CharField(max_length=15, default="")
    tipo_vivienda = models.CharField(max_length=20, choices=VIVIENDA_CHOICES, default='PISO')
    experiencia_previa = models.BooleanField(default=False, verbose_name="¿Tienes experiencia previa?")
    otras_mascotas = models.BooleanField(default=False, verbose_name="¿Tienes otras mascotas?")
    horas_solitario = models.IntegerField(default=0, help_text="¿Cuántas horas al día pasará solo?")
    motivo = models.TextField(help_text="Explica por qué serías un buen entrenador para este animal.")
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_SOLICITUD, default='PENDIENTE')

    def __str__(self):
        return f"Solicitud de {self.usuario.username} para {self.animal.nombre}"

# 5. Donaciones para Rehabilitación
class Donacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cantidad a donar (€)")
    mensaje = models.TextField(blank=True, help_text="Déjale un mensaje de ánimo (Opcional).")
    fecha_donacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad}€ de {self.usuario.username} para {self.animal.nombre}"
