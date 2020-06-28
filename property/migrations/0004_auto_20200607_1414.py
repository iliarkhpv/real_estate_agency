# Generated by Django 2.2.4 on 2020-06-07 11:14

from django.db import migrations

def mark_all_new_buidings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_buiding = True
            flat.save()
        else:
            flat.new_buiding = False
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_buiding'),
    ]

    operations = [
        migrations.RunPython(mark_all_new_buidings)
    ]
