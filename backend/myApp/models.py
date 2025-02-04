# myApp/models.py
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError


# ------------------------- Creation of model validators -------------------------

# Validator for phone numbers
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Validator for the 'level' field in the 'Failure' table.
def validate_failure_level(value):
    valid_levels = ["Critical", "Major", "Minor"]
    
    if value not in valid_levels:
        raise ValidationError(f"The failure level must be one of the following values: {', '.join(valid_levels)}.")

def validate_equipment_status(value):
    valid_statuses = ["Scrapped", "Operational", "Degraded", "Stopped"]
    
    if value not in valid_statuses:
        raise ValidationError(f"The equipment status must be one of the following values: {', '.join(valid_statuses)}.")

# ------------------------- Creation of models -------------------------

class Manufacturer(models.Model):
    manufacturerName = models.CharField(
        max_length=50,
        help_text="Name of the manufacturer",
        error_messages={
            'unique': "This manufacturer name already exists.",
        }
    )

    manufacturerCountry = models.CharField(
        max_length=50,
        help_text="Country of the manufacturer"
    )

    manufacturerEmail = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        validators=[EmailValidator()],
        help_text="Email address of the manufacturer",
        error_messages={
            'invalid': "Enter a valid email address.",
        }
    )
    
    manufacturerPhoneNumber = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[phone_regex],
        help_text="Phone number of the manufacturer",
        error_messages={
            'invalid': "Enter a valid phone number.",
        }
    )
    afterSalesService = models.BooleanField(
        help_text="Indicates if the manufacturer offers after-sales service"
    )

    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of manufacturer deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.manufacturerName

class Supplier(models.Model):
    supplierName = models.CharField(max_length=50)
    streetNumber = models.SmallIntegerField()
    streetName = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    supplierCountry = models.CharField(max_length=50)
    supplierEmail = models.EmailField(max_length=50, null=True, blank=True, validators=[EmailValidator()])
    supplierPhoneNumber = models.CharField(max_length=15, null=True, blank=True, validators=[phone_regex])
    afterSalesService = models.BooleanField(
        help_text="Indicates if the supplier offers after-sales service",
    )

    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of supplier deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.supplierName

class Consumable(models.Model):
    designation = models.CharField(max_length=50)
    consumableImageLink = models.ImageField(upload_to='images/consumable', null=False) 
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of consumable deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.designation


class ConsumableStock(models.Model):
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchasePrice = models.DecimalField(max_digits=7, decimal_places=2)
    purchaseDate = models.DateField()
    consumableQuantity = models.SmallIntegerField()
    comment = models.CharField(
        max_length=1000, 
        null=True, 
        blank=True,
        help_text="Possible additional information to be provided",
        )

class EquipmentModel(models.Model):
    equipmentModelName = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of equipment model deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.equipmentModelName


class IsCompatible(models.Model):
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    equipmentModel = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE)

class Location(models.Model):
    locationName = models.CharField(max_length=50)
    locationType = models.CharField(
        max_length=50,
        help_text="Optional additional information about the type of location entered.")

    parentLocation = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="Pointer designating the structure (another location) where the element in question is located.")
    
    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of location deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.locationName

class Equipment(models.Model):
    reference = models.CharField(
        max_length=50,
        primary_key=True,
    )

    creationDate = models.DateTimeField()
    designation = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Name by which we refer to the machine."
    )
    commissioningDate = models.DateField()
    purchasePrice = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Price at which you purchased the batch"
    )
    equipmentImageLink = models.ImageField(upload_to='images/equipment', null=False)
    equipmentCreator = models.ForeignKey(User, related_name='equipmentCreator', on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    equipmentModel = models.ForeignKey('EquipmentModel', on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True)
    slidingPreventive = models.BooleanField(null=True, blank=True)
    maintenanceIntervalDays = models.SmallIntegerField()

    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of equipment deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.designation


class Constitute(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE)

class StatusInformation(models.Model):
    STATUT_CHOICES = [
        ('Scrapped', 'Scrapped'),
        ('Operational', 'Operational'),
        ('Degraded', 'Degradeds'),
        ('Stopped', 'Stopped'),
    ]
    equipmentStatus = models.CharField(
            max_length=50,
            choices=STATUS_CHOICES,
            null=True,
            blank=True
        )
    changeDate = models.DateTimeField(null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    parentStatusInformation = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    statusModifier = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Status of {self.equipment}: {self.equipmentStatus} (modified on {self.changeDate})"

class TechnicalDocument(models.Model):
    technicalDocumentName = models.CharField(max_length=50)
    technicalDocumentLink = models.FileField(upload_to='documents/technicalDocument', null=False) 

    deactivation_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time of technical document deactivation"
    )

    def deactivate(self):
        self.deactivation_date = timezone.now()
        self.save()

    def is_active(self):
        return self.deactivation_date is None

    def __str__(self):
        return self.technicalDocumentName

class Correspond(models.Model):
    technicalDocument = models.ForeignKey(TechnicalDocument, on_delete=models.CASCADE)
    equipmentModel = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE)


class InterventionRequest(models.Model):
    FAILURE_CHOICES = [
        ('Critical', 'Critical'),
        ('Major', 'Major'),
        ('Minor', 'Minor'),
    ]
    failureComment = models.CharField(max_length=1000, null=True, blank=True)
    failureLevel = models.CharField(
        max_length=50,
        choices=FAILURE_CHOICES, 
        validators=[validate_failure_level])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    requestProcessingDate = models.DateTimeField(null=True, blank=True)
    waitingDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.

class FailureDocument(models.Model):
    failureDocumentName = models.CharField(max_length=50)
    failureDocumentLink = models.FileField(upload_to='documents/failureDocument', null=False) 
    failure = models.ForeignKey(Failure, on_delete=models.CASCADE)

    def __str__(self):
        return self.failureDocumentName


class WorkOrder(models.Model):
    workOrderName = models.CharField(max_length=500, null=True, blank=True)
    workOrderCategory = models.BooleanField(
        help_text='The value is positive if it\'s a preventive intervention, otherwise it\'s a corrective intervention.',
        null=True, 
        blank=True)
    assignmentDate = models.DateTimeField()
    closureDate = models.DateTimeField(null=True, blank=True)
    estimatedTime = models.TimeField(null=True, blank=True)
    interventionComment = models.CharField(max_length=1000, null=True, blank=True)
    failure = models.ForeignKey(Failure, on_delete=models.CASCADE)
    interventionCreator = models.ForeignKey(User,
        related_name='interventionCreator', 
        on_delete=models.CASCADE,
        help_text="The person who creates the intervention")

    def __str__(self):
        return self.workOrderName

class Intervention(models.Model):
    instructions = models.CharField(max_length=1000, null=True, blank=True)
    attributionDate = models.DateTimeField()
    desiredDate = models.DateTimeField(null=True, blank=True)
    interventionStartDate = models.DateTimeField(null=True, blank=True)
    interventionEndDate = models.DateTimeField(null=True, blank=True)
    interventionComment = models.CharField(max_length=1000, null=True, blank=True)
    workOrder = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    technician = models.ForeignKey(User,
        related_name='Technician',  
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text="The person who performs the intervention"
    )

    def __str__(self):
        return self.interventionComment


class InterventionDocument(models.Model):
    interventionDocumentName = models.CharField(max_length=500)
    interventionDocumentLink = models.FileField(upload_to='documents/interventionDocument', null=False) 
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)

    def __str__(self):
        return self.interventionDocumentName