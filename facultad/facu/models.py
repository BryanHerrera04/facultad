from django.db import models

# Create your models here.


class Decano(models.Model):
    nom_decano = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Nombre",
        help_text="Nombre del Decano",
    )

    ape_decano = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Apeliido",
        help_text="Apeliido del Decano"
    )

    cedula = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Cédula",
        help_text="Cédula del Decano"
    )

    cel_decano = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Celular",
        help_text="Celular del Decano"
    )

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # Nombre del modelo
        verbose_name = "Decano"
        # Nombre del modelo en plural
        verbose_name_plural = "Decano"

    def __str__(self):
        return self.nom_decano


class Facultad(models.Model):
    nom_facultad = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Nombre",
        help_text="Nombre del Facultad",
    )

    num_blo_facultad = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Número de bloque",
        help_text="Número de bloque de la Facultad",
    )

    ubi_facultad = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Ubicación",
        help_text="Ubicación de la Facultad",
    )

    decano = models.OneToOneField(
        Decano, null=False, on_delete=models.CASCADE, default="",
        verbose_name="Decano",
        help_text="Decano",
        unique=True,
    )

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # unique_together=('decano')
        # Nombre del modelo
        verbose_name = "Facultad"
        # Nombre del modelo en plural
        verbose_name_plural = "Facultad"

    def __str__(self):
        return self.nom_facultad


class Docente(models.Model):
    nom_docente = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Nombre",
        help_text="Nombre del Docente",
    )

    ape_docente = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Apellido",
        help_text="Apellido del Docente",
    )

    cc_docente = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Cédula",
        help_text="Cédula del Docente",
    )

    titulo_docente = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Titulo",
        help_text="Titulo del Docente",
    )

    facultad = models.ForeignKey(
        Facultad, on_delete=models.CASCADE, default="",
        verbose_name="Facultad",
        help_text="Facultad",
    )

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # unique_together=('facultad')
        # Nombre del modelo
        verbose_name = "Docente"
        # Nombre del modelo en plural
        verbose_name_plural = "Docente"

    def __str__(self):
        return self.nom_docente


class Asignatura(models.Model):
    nom_asig = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Nombre",
        help_text="Nombre de la Asignatura",
    )

    cod_asig = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Código",
        help_text="Código de la Asignatura",
    )

    num_cred_asig = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Creditos",
        help_text="Creditos de la Asignatura",
    )

    docente = models.ForeignKey(
        Docente, on_delete=models.CASCADE, default="",
        verbose_name="Docente",
        help_text="Docente",
    )

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # unique_together=('docente')
        # Nombre del modelo
        verbose_name = "Asignatura"
        # Nombre del modelo en plural
        verbose_name_plural = "Asignatura"

    def __str__(self):
        return self.nom_asig


class Estudiante(models.Model):
    nom_est = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Nombre",
        help_text="Nombre del Estudiante",
    )

    ape_est = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Apellido",
        help_text="Apellido del Estudiante",
    )

    cc_est = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Cédula",
        help_text="Cédula del Estudiante"
    )

    dir_est = models.CharField(
        null=False, blank=False, max_length=50, default="",
        verbose_name="Dirección",
        help_text="Dirección de Residencia"
    )

    asignatura = models.ForeignKey(
        Asignatura(), on_delete=models.CASCADE, default="",
        verbose_name="Asignatura",
        help_text="Asignatura",
    )

    class Meta:
        """ Atributos del modelo para el administrador """
        # Ordena por defecto por este campo
        ordering = ["id"]
        # unique_together=('asignatura')
        # Nombre del modelo
        verbose_name = "Estudiante"
        # Nombre del modelo en plural
        verbose_name_plural = "Estudiante"

    def __str__(self):
        return self.nom_est
