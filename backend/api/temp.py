
# class DefaillanceSerializer(serializers.ModelSerializer):
#     interventions = serializers.SerializerMethodField()

#     class Meta:
#         model = Defaillance
#         fields = '__all__'

#     def get_interventions(self, obj):
#         from .serializers import InterventionSerializer
#         return InterventionSerializer(obj.intervention_set.all(), many=True).data
    

# class EquipementDetailSerializer(serializers.ModelSerializer):
#     lieu = LieuSerializer(read_only=True)
#     modeleEquipement = ModeleEquipementDetailSerializer(read_only=True)
#     fournisseur = FournisseurSerializer(read_only=True)
#     defaillances = serializers.SerializerMethodField()
#     consommables_compatibles = serializers.SerializerMethodField()
#     documents_techniques = serializers.SerializerMethodField()
#     documents_defaillance = serializers.SerializerMethodField()
#     documents_intervention = serializers.SerializerMethodField()
#     dernier_statut = InformationStatutSerializer(read_only=True)

#     class Meta:
#         model = Equipement
#         fields = ['reference', 'designation', 'lieu', 'modeleEquipement', 'fournisseur', 
#                   'defaillances', 'consommables_compatibles', 
#                   'documents_techniques', 'documents_defaillance', 'documents_intervention',
#                   'dernier_statut']

#     def get_interventions(self, obj):
#         return InterventionSerializer(obj.defaillance_set.all().prefetch_related('intervention_set'), many=True).data

#     def get_consommables_compatibles(self, obj):
#         return ConsommableSerializer(obj.modeleEquipement.estcompatible_set.all().select_related('consommable'), many=True).data

#     def get_documents_techniques(self, obj):
#         correspondances = Correspondre.objects.filter(modeleEquipement=obj.modeleEquipement)
#         documents_techniques = [correspondance.documentTechnique for correspondance in correspondances]
#         return DocumentTechniqueSerializer(documents_techniques, many=True).data

#     def get_documents_defaillance(self, obj):
#         return DocumentDefaillanceSerializer(DocumentDefaillance.objects.filter(defaillance__equipement=obj), many=True).data

#     def get_documents_intervention(self, obj):
#         return DocumentInterventionSerializer(DocumentIntervention.objects.filter(intervention__defaillance__equipement=obj), many=True).data

#     def get_defaillances(self, obj):
#         return DefaillanceSerializer(obj.defaillance_set.all().prefetch_related('intervention_set'), many=True).data

    
#     def get_dernier_statut(self, obj):
#         dernier_statut = obj.informationstatut_set.order_by('-dateChangement').first()
#         if dernier_statut:
#             return {
#                 'statutEquipement': dernier_statut.statutEquipement,
#                 'dateChangement': dernier_statut.dateChangement,
#                 'ModificateurStatut': dernier_statut.ModificateurStatut.username if dernier_statut.ModificateurStatut else None
#             }
#         return None








# class EquipementViewSet(viewsets.ModelViewSet):
#     queryset = Equipement.objects.all()
#     lookup_field = 'reference'
    
#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return EquipementDetailSerializer
#         return EquipementSerializer

#     def get_queryset(self):
#         if self.action == 'retrieve':
#             return Equipement.objects.select_related(
#                 'lieu', 
#                 'modeleEquipement__fabricant', 
#                 'fournisseur', 
#                 'createurEquipement'
#             ).prefetch_related(
#                 Prefetch('informationstatut_set', 
#                          queryset=InformationStatut.objects.order_by('-dateChangement'),
#                          to_attr='statuts'),
#                 Prefetch('defaillance_set', 
#                          queryset=Defaillance.objects.prefetch_related(
#                              'intervention_set',
#                              'documentdefaillance_set',
#                              'intervention_set__documentintervention_set'
#                          )),
#                 Prefetch('modeleEquipement__estcompatible_set__consommable', 
#                          queryset=Consommable.objects.all()),
#                 Prefetch('modeleEquipement__correspondre_set__documentTechnique',
#                          queryset=DocumentTechnique.objects.all()),
#             )
#         return Equipement.objects.all()

#     def get_object(self):
#         reference = self.kwargs.get('reference')
#         try:
#             obj = self.get_queryset().get(reference=reference)
#             if hasattr(obj, 'statuts') and obj.statuts:
#                 obj.dernier_statut = obj.statuts[0]
#             else:
#                 obj.dernier_statut = obj.informationstatut_set.order_by('-dateChangement').first()
#             return obj
#         except Equipement.DoesNotExist:
#             raise NotFound(f"Aucun équipement trouvé avec la référence {reference}")


#   path('equipements/<str:reference>/detail/', EquipementViewSet.as_view({'get': 'retrieve'}), name='equipement-detail'),
