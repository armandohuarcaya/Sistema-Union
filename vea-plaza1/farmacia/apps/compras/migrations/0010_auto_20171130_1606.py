# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20151220_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecompra',
            old_name='medicamento',
            new_name='producto',
        ),
    ]
