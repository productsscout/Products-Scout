# Generated by Django 5.1.3 on 2024-12-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_conversation_delete_chathistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_name',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]