# Generated by Django 3.2 on 2024-12-20 10:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import myApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consommable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('lienImageConsommable', models.ImageField(upload_to='images/consomable')),
            ],
        ),
        migrations.CreateModel(
            name='Defaillance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaireDefaillance', models.CharField(blank=True, max_length=1000, null=True)),
                ('niveau', models.CharField(choices=[('Critique', 'Critique'), ('Majeur', 'Majeur'), ('Mineur', 'Mineur')], max_length=50, validators=[myApp.models.validate_niveau_de_defaillance])),
            ],
        ),
        migrations.CreateModel(
            name='DocumentTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDocumentTechnique', models.CharField(max_length=50)),
                ('lienDocumentTechnique', models.FileField(upload_to='documents/documentTecnique')),
            ],
        ),
        migrations.CreateModel(
            name='Fabricant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFabricant', models.CharField(error_messages={'unique': 'Ce nom de fabricant existe déjà.'}, help_text='Nom du fabricant', max_length=50)),
                ('paysFabricant', models.CharField(help_text='Pays du fabricant', max_length=50)),
                ('mailFabricant', models.EmailField(blank=True, error_messages={'invalid': 'Entrez une adresse e-mail valide.'}, help_text='Adresse e-mail du fabricant', max_length=50, null=True, validators=[django.core.validators.EmailValidator()])),
                ('numTelephoneFabricant', models.CharField(blank=True, error_messages={'invalid': 'Entrez un numéro de téléphone valide.'}, help_text='Numéro de téléphone du fabricant', max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Le numéro de téléphone doit être entré au format: '+999999999'. Jusqu'à 15 chiffres autorisés.", regex='^\\+?1?\\d{9,15}$')])),
                ('serviceApresVente', models.BooleanField(help_text='Indique si le fabricant offre un service après-vente')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFournisseur', models.CharField(max_length=50)),
                ('numRue', models.SmallIntegerField()),
                ('nomRue', models.CharField(max_length=50)),
                ('codePostal', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('paysFournisseur', models.CharField(max_length=50)),
                ('mailFournisseur', models.EmailField(blank=True, max_length=50, null=True, validators=[django.core.validators.EmailValidator()])),
                ('numTelephoneFournisseur', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Le numéro de téléphone doit être entré au format: '+999999999'. Jusqu'à 15 chiffres autorisés.", regex='^\\+?1?\\d{9,15}$')])),
                ('serviceApresVente', models.BooleanField(help_text="Indique si le fournisseur propose un service d'aprés vente")),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRole', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StockConsommable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prixAchat', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dateAchat', models.DateField()),
                ('quantiteConsommable', models.SmallIntegerField()),
                ('commentaire', models.CharField(blank=True, help_text='Informations complémentaires possibles à renseigner', max_length=1000, null=True)),
                ('consommable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.consommable')),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='ModeleEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomModeleEquipement', models.CharField(max_length=50)),
                ('fabricant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.fabricant')),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomLieu', models.CharField(max_length=50)),
                ('typeLieu', models.CharField(help_text='Informations complémentaires optionnelles sur le type de lieu renseigné.', max_length=50)),
                ('lieuParent', models.ForeignKey(blank=True, help_text="Pointeur désignant la structure (un autre lieu) où se trouve l'élément en question.", null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomIntervention', models.CharField(blank=True, max_length=50, null=True)),
                ('interventionCurative', models.BooleanField(blank=True, null=True)),
                ('dateAssignation', models.DateTimeField()),
                ('dateCloture', models.DateTimeField()),
                ('dateDebutIntervention', models.DateTimeField(blank=True, null=True)),
                ('dateFinIntervention', models.DateTimeField(blank=True, null=True)),
                ('tempsEstime', models.TimeField(blank=True, null=True)),
                ('commentaireIntervention', models.CharField(blank=True, max_length=1000, null=True)),
                ('createurIntervention', models.ForeignKey(help_text="La personne qui crée l'intervention", on_delete=django.db.models.deletion.CASCADE, related_name='createurIntervention', to=settings.AUTH_USER_MODEL)),
                ('defaillance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.defaillance')),
                ('responsable', models.ForeignKey(blank=True, help_text="La personne qui réalise l'intervention", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InformationMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preventifGlissant', models.BooleanField(blank=True, null=True)),
                ('joursIntervalleMaintenance', models.SmallIntegerField()),
                ('dateCreation', models.DateTimeField()),
                ('dateChangement', models.DateTimeField(blank=True, null=True)),
                ('createurInformationMaintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('informationMaintenanceParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.informationmaintenance')),
            ],
        ),
        migrations.CreateModel(
            name='EstCompatible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consommable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.consommable')),
                ('modeleEquipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.modeleequipement')),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('reference', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dateCreation', models.DateTimeField()),
                ('designation', models.CharField(blank=True, help_text='Nom par lequel nous faisons référence à la machine.', max_length=50, null=True)),
                ('dateMiseEnService', models.DateField()),
                ('prixAchat', models.DecimalField(blank=True, decimal_places=2, help_text='Prix auquel vous avez acheté le lot', max_digits=10, null=True)),
                ('lienImageEquipement', models.ImageField(upload_to='images/equipement')),
                ('statutEquipement', models.CharField(blank=True, choices=[('Rebuté', 'Rebuté'), ('En fonctionnement', 'En fonctionnement'), ('Dégradé', 'Dégradé'), ("A l'arret", "A l'arret")], max_length=50, null=True)),
                ('createurEquipement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createurEquipement', to=settings.AUTH_USER_MODEL)),
                ('fournisseur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.fournisseur')),
                ('informationMaintenance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.informationmaintenance')),
                ('lieu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.lieu')),
                ('modeleEquipement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.modeleequipement')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentIntervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDocumentIntervention', models.CharField(max_length=50)),
                ('lienDocumentIntervention', models.FileField(upload_to='documents/documentIntervention')),
                ('intervention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.intervention')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDefaillance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDocumentDefaillance', models.CharField(max_length=50)),
                ('lienDocumentDefaillance', models.FileField(upload_to='documents/documentDefaillance')),
                ('defaillance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.defaillance')),
            ],
        ),
        migrations.AddField(
            model_name='defaillance',
            name='equipement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.equipement'),
        ),
        migrations.AddField(
            model_name='defaillance',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Correspondre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentTechnique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.documenttechnique')),
                ('modeleEquipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.modeleequipement')),
            ],
        ),
        migrations.CreateModel(
            name='Constituer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consommable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.consommable')),
                ('equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.equipement')),
            ],
        ),
        migrations.AddField(
            model_name='consommable',
            name='fabricant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.fabricant'),
        ),
        migrations.CreateModel(
            name='Avoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.role')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
