# Generated by Django 4.0.6 on 2022-08-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_reseña_film_reseña_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('image_url', models.URLField(default='https://image.shutterstock.com/image-vector/photo-album-picture-collection-line-260nw-256926565.jpg')),
                ('contains', models.ManyToManyField(blank=True, to='products.contenido')),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]