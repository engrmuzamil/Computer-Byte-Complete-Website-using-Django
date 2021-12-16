# Generated by Django 3.1 on 2021-07-02 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categories', '0003_auto_20210702_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=200, unique=True)),
                ('Slug', models.SlugField(max_length=200, unique=True)),
                ('Product_Description', models.TextField(blank=True, max_length=500)),
                ('Product_Image', models.ImageField(upload_to='photos/Products')),
                ('Product_Qty', models.IntegerField()),
                ('Product_Price', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('Created_Date', models.DateTimeField(auto_now_add=True)),
                ('Updated_Date', models.DateTimeField(auto_now=True)),
                ('Product_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Categories.category')),
            ],
        ),
    ]