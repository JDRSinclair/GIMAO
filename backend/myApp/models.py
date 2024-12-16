from django.db import models
from django.core.validators import RegexValidator, EmailValidator

# Validateur pour les numéros de téléphone
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Numéro de téléphone non valide")

#Valideur pour le champ 'niveau' dans la table 'Defaillance'.
def validate_niveau_de_defaillance(value):
    valid_niveaux = ["Critique", "Majeur", "Mineur"]
    if value not in valid_niveaux:
        raise ValidationError(f"Le niveau de défaillance doit être l'une des valeurs suivantes: {', '.join(valid_niveaux)}.")

class Role(models.Model):
    nomRole = models.CharField(max_length=50)

    def __str__(self):
        return self.nomRole

class Utilisateur(models.Model):
    nomUtilisateur = models.CharField(max_length=50)
    motDePasse = models.CharField(max_length=100)
    mailUtilisateur = models.EmailField(max_length=50, validators=[EmailValidator()])
    numTelephoneUtilisateur = models.CharField(max_length=15, null=True, blank=True, validators=[phone_regex])
    actif = models.BooleanField()

    def __str__(self):
        return self.nomUtilisateur

class Avoir(models.Model):
    idRole = models.ForeignKey(Role, on_delete=models.CASCADE)
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Fabricant(models.Model):
    nomFabricant = models.CharField(max_length=50)
    paysFabricant = models.CharField(max_length=50)
    mailFabricant = models.EmailField(max_length=50, null=True, blank=True, validators=[EmailValidator()])
    numTelephoneFabricant = models.CharField(max_length=15, null=True, blank=True, validators=[phone_regex])
    serviceApresVente = models.BooleanField()

    def __str__(self):
        return self.nomFabricant

class Fournisseur(models.Model):
    nomFournisseur = models.CharField(max_length=50)
    numRue = models.SmallIntegerField()
    nomRue = models.CharField(max_length=50)
    codePostal = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    paysFournisseur = models.CharField(max_length=50)
    mailFournisseur = models.EmailField(max_length=50, null=True, blank=True, validators=[EmailValidator()])
    numTelephoneFournisseur = models.CharField(max_length=15, null=True, blank=True, validators=[phone_regex])
    serviceApresVente = models.BooleanField()

    def __str__(self):
        return self.nomFournisseur

class Consommable(models.Model):
    designation = models.CharField(max_length=50)
    lienImageConsommable = models.URLField(max_length=100, null=True, blank=True)
    idFabricant = models.ForeignKey(Fabricant, on_delete=models.CASCADE)

    def __str__(self):
        return self.designation

class StockConsommable(models.Model):
    idConsommable = models.ForeignKey(Consommable, on_delete=models.CASCADE)
    idFournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    prixAchat = models.DecimalField(max_digits=7, decimal_places=2)
    dateAchat = models.DateField()
    quantiteConsommable = models.SmallIntegerField()
    commentaire = models.CharField(max_length=1000, null=True, blank=True)

class ModeleEquipement(models.Model):
    nomModeleEquipement = models.CharField(max_length=50)
    idFabricant = models.ForeignKey(Fabricant, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomModeleEquipement

class EstCompatible(models.Model):
    idConsommable = models.ForeignKey(Consommable, on_delete=models.CASCADE)
    idModeleEquipement = models.ForeignKey(ModeleEquipement, on_delete=models.CASCADE)

class Lieu(models.Model):
    nomLieu = models.CharField(max_length=50)
    typeLieu = models.CharField(max_length=50)
    idLieuParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomLieu

class Equipement(models.Model):
    dateCreation = models.DateTimeField()
    designation = models.CharField(max_length=50, null=True, blank=True)
    dateMiseEnService = models.DateField()
    prixAchat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lienImageEquipement = models.URLField(max_length=100, null=True, blank=True)
    statutEquipement = models.CharField(max_length=50, null=True, blank=True)
    idCreateurEquipement = models.ForeignKey(Utilisateur, related_name='createurEquipement', on_delete=models.CASCADE, null=True, blank=True)
    idLieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, null=True, blank=True)
    idModeleEquipement = models.ForeignKey(ModeleEquipement, on_delete=models.CASCADE, null=True, blank=True)
    idFournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True, blank=True)
    idInformationMaintenance = models.ForeignKey('InformationMaintenance', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.designation

class Constituer(models.Model):
    idEquipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    idConsommable = models.ForeignKey(Consommable, on_delete=models.CASCADE)

class InformationMaintenance(models.Model):
    preventifGlissant = models.BooleanField(null=True, blank=True)
    joursIntervalleMaintenance = models.SmallIntegerField()
    dateCreation = models.DateTimeField()
    dateChangement = models.DateTimeField(null=True, blank=True)
    idInformationMaintenanceParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    idCreateurInformationMaintenance = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return f"InformationMaintenance {self.id}"

class DocumentTechnique(models.Model):
    nomDocumentTechnique = models.CharField(max_length=50)
    lienDocumentTechnique = models.URLField(max_length=100)

    def __str__(self):
        return self.nomDocumentTechnique

class Correspondre(models.Model):
    idDocumentTechnique = models.ForeignKey(DocumentTechnique, on_delete=models.CASCADE)
    idModeleEquipement = models.ForeignKey(ModeleEquipement, on_delete=models.CASCADE)

class Defaillance(models.Model):
    commentaireDefaillance = models.CharField(max_length=1000, null=True, blank=True)
    niveau = models.CharField(max_length=50, validators=[validate_niveau_de_defaillance])
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idEquipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def __str__(self):
        return self.commentaireDefaillance

class DocumentDefaillance(models.Model):
    nomDocumentDefaillance = models.CharField(max_length=50)
    lienDocumentDefaillance = models.URLField(max_length=100)
    idDefaillance = models.ForeignKey(Defaillance, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomDocumentDefaillance

class Intervention(models.Model):
    nomIntervention = models.CharField(max_length=50, null=True, blank=True)
    interventionCurative = models.BooleanField(null=True, blank=True)
    dateAssignation = models.DateTimeField()
    dateCloture = models.DateTimeField()
    dateDebutIntervention = models.DateTimeField(null=True, blank=True)
    dateFinIntervention = models.DateTimeField(null=True, blank=True)
    tempsEstime = models.TimeField(null=True, blank=True)
    commentaireIntervention = models.CharField(max_length=1000, null=True, blank=True)
    idDefaillance = models.ForeignKey(Defaillance, on_delete=models.CASCADE)
    idCreateurIntervention = models.ForeignKey(Utilisateur, related_name='createurIntervention', on_delete=models.CASCADE)
    idResponsable = models.ForeignKey(Utilisateur, related_name='responsable', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nomIntervention

class DocumentIntervention(models.Model):
    nomDocumentIntervention = models.CharField(max_length=50)
    lienDocumentIntervention = models.URLField(max_length=100)
    idIntervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomDocumentIntervention
