from django.db import models


class Adopcion(models.Model):
    id_adopcion = models.AutoField(db_column='Id_adopcion', primary_key=True)  # Field name made lowercase.
    id_animal = models.ForeignKey('Animal', models.DO_NOTHING, db_column='Id_animal', blank=True, null=True)  # Field name made lowercase.
    id_adoptante = models.ForeignKey('Adoptante', models.DO_NOTHING, db_column='Id_adoptante', blank=True, null=True)  # Field name made lowercase.
    id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='Id_empleado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Adopcion'


class Adoptante(models.Model):
    id_adoptante = models.AutoField(db_column='Id_adoptante', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Id_persona', blank=True, null=True)  # Field name made lowercase.
    id_contacto = models.ForeignKey('Contacto', models.DO_NOTHING, db_column='Id_contacto', blank=True, null=True)  # Field name made lowercase.
    id_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='Id_direccion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Adoptante'


class Animal(models.Model):
    id_animal = models.AutoField(db_column='Id_animal', primary_key=True)  # Field name made lowercase.
    nombre_animal = models.CharField(db_column='Nombre_animal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion_animal = models.TextField(db_column='Descripcion_animal', blank=True, null=True)  # Field name made lowercase.
    id_especie = models.ForeignKey('Especie', models.DO_NOTHING, db_column='Id_especie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Animal'


class Contacto(models.Model):
    id_contacto = models.AutoField(db_column='Id_contacto', primary_key=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Contacto'


class Direccion(models.Model):
    id_direccion = models.AutoField(db_column='Id_direccion', primary_key=True)  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_ext = models.CharField(db_column='Num_ext', max_length=10, blank=True, null=True)  # Field name made lowercase.
    num_int = models.CharField(db_column='Num_int', max_length=10, blank=True, null=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='Colonia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Direccion'


class Empleado(models.Model):
    id_empleado = models.AutoField(db_column='Id_empleado', primary_key=True)  # Field name made lowercase.
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Id_persona', blank=True, null=True)  # Field name made lowercase.
    id_contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='Id_contacto', blank=True, null=True)  # Field name made lowercase.
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='Id_direccion', blank=True, null=True)  # Field name made lowercase.
    id_puesto = models.ForeignKey('Puesto', models.DO_NOTHING, db_column='Id_puesto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Empleado'


class Especie(models.Model):
    id_especie = models.AutoField(db_column='Id_especie', primary_key=True)  # Field name made lowercase.
    nombre_comun = models.CharField(db_column='Nombre_comun', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre_cientifico = models.CharField(db_column='Nombre_cientifico', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcion_especie = models.TextField(db_column='Descripcion_especie', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Especie'


class Persona(models.Model):
    id_persona = models.AutoField(db_column='Id_persona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido_p = models.CharField(db_column='Apellido_p', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido_m = models.CharField(db_column='Apellido_m', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Persona'


class Puesto(models.Model):
    id_puesto = models.AutoField(db_column='Id_puesto', primary_key=True)  # Field name made lowercase.
    nombre_puesto = models.CharField(db_column='Nombre_puesto', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Puesto'


class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(db_column='Id_seguimiento', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    detalles = models.TextField(db_column='Detalles', blank=True, null=True)  # Field name made lowercase.
    id_adopcion = models.ForeignKey(Adopcion, models.DO_NOTHING, db_column='Id_adopcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Seguimiento'
