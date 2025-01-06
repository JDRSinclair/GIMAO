
INSERT INTO myApp_role (nomRole) VALUES 
('Operateur'),
('Magasinier'),
('Technicien'),
('Responsable GMAO'),
('Administrateur');

INSERT INTO myApp_lieu (nomLieu, typeLieu, lieuParent_id) VALUES
-- Niveau 1 : Bâtiments principaux
('Bâtiment Principal', 'Bâtiment', NULL),
('Entrepôt Logistique', 'Entrepôt', NULL),
('Centre de Recherche', 'Laboratoire', NULL),
('Complexe Administratif', 'Bureau', NULL),

-- Niveau 2 : Zones dans le Bâtiment Principal
('Zone de Production A', 'Zone de production', 1),
('Zone de Production B', 'Zone de production', 1),
('Atelier de Maintenance', 'Atelier', 1),
('Salle de Contrôle Qualité', 'Laboratoire', 1),

-- Niveau 3 : Sous-zones dans la Zone de Production A
('Ligne d''Assemblage 1', 'Ligne de production', 5),
('Ligne d''Assemblage 2', 'Ligne de production', 5),
('Poste de Soudure', 'Poste de travail', 5),
('Zone de Test', 'Zone de test', 5),

-- Niveau 3 : Sous-zones dans la Zone de Production B
('Unité de Moulage', 'Unité de production', 6),
('Unité de Peinture', 'Unité de production', 6),
('Zone d''Emballage', 'Zone logistique', 6),

-- Niveau 2 : Zones dans l'Entrepôt Logistique
('Zone de Réception', 'Zone logistique', 2),
('Zone de Stockage A', 'Zone de stockage', 2),
('Zone de Stockage B', 'Zone de stockage', 2),
('Zone d''Expédition', 'Zone logistique', 2),

-- Niveau 3 : Sous-zones dans la Zone de Stockage A
('Rack de Stockage 1', 'Rack', 17),
('Rack de Stockage 2', 'Rack', 17),
('Zone de Préparation des Commandes', 'Zone de travail', 17),

-- Niveau 2 : Zones dans le Centre de Recherche
('Laboratoire de Chimie', 'Laboratoire', 3),
('Laboratoire de Physique', 'Laboratoire', 3),
('Salle de Prototypage', 'Atelier', 3),
('Salle de Conférence Scientifique', 'Salle de réunion', 3),

-- Niveau 3 : Sous-zones dans le Laboratoire de Chimie
('Salle d''Analyse Spectrale', 'Salle d''analyse', 22),
('Salle de Synthèse', 'Salle d''expérimentation', 22),

-- Niveau 2 : Zones dans le Complexe Administratif
('Département des Ressources Humaines', 'Bureau', 4),
('Département Financier', 'Bureau', 4),
('Salle de Conférence Principale', 'Salle de réunion', 4),
('Cafétéria', 'Zone de restauration', 4),

-- Niveau 3 : Sous-zones dans le Département des Ressources Humaines
('Bureau du Directeur RH', 'Bureau individuel', 26),
('Espace de Recrutement', 'Espace ouvert', 26),
('Salle de Formation', 'Salle de formation', 26);


INSERT INTO auth_user (
    password,
    last_login,
    is_superuser,
    username,
    first_name,
    last_name,
    email,
    is_staff,
    is_active,
    date_joined
) VALUES 
('pbkdf2_sha256$260000$JGwJdrWhq8cltnqkfAHWLm$d2Wnocq6bdcS09QEwab8NcgeN5KJNAe6h32qNGb3n1U=', NULL, 1, 'admin','admin','admin', 'admin@a.com',1, 1, '2024-12-22 14:02:29.239568' ),
('pbkdf2_sha256$260000$phb2aIcIzdG1lvJw1bl59D$ozBponKnswZsjxZnnVNdV2tcQk1TVz3CoLPc9b4IdZk=', NULL, 1, 'root','root','root', 'root@r.com',1, 1, '2024-12-22 14:02:58.710980' ),
('pbkdf2_sha256$260000$ILKUledv9DGixmggCi2G76$n2vIEsYTSIIqI9OFIxvcRyBRkuvsipe61akibvHXomo=', NULL, 1, 'dev','dev','dev', 'dev@d.com',1, 1, '2024-12-22 14:03:17.251897' );



INSERT INTO myApp_fabricant (nomFabricant, paysFabricant, mailFabricant, numTelephoneFabricant, serviceApresVente) VALUES
('Acme Corporation', 'USA', 'contact@acmecorp.com', '+1234567890', True),
('Beta Industries', 'France', 'support@betaindustries.fr', '+33987654321', False),
('Gamma Tech', 'Germany', 'info@gammatech.de', '+491234567890', True),
('Delta Solutions', 'Japan', 'sales@deltasolutions.jp', '+811234567890', True),
('Epsilon Innovations', 'UK', 'enquiries@epsiloninnovations.co.uk', '+441234567890', False);


INSERT INTO myApp_consommable (designation, lienImageConsommable, fabricant_id) VALUES
('Vis A', 'images/consomable/vis.jpg', 1),
('Ecrou B', 'images/consomable/ecrou.jpg', 2),
('Rondelle C', 'images/consomable/rondelle.jpg', 3),
('Boulon D', 'images/consomable/boulon.jpg', 4),
('Joint E', 'images/consomable/joint.jpg', 5);


INSERT INTO myApp_informationmaintenance (
    preventifGlissant,
    joursIntervalleMaintenance,
    dateCreation,
    dateChangement,
    informationMaintenanceParent_id,
    createurInformationMaintenance_id
) VALUES
(True, 30, '2023-01-01 00:00:00', NULL, NULL, 1),
(False, 60, '2023-02-01 00:00:00', NULL, NULL, 2),
(True, 90, '2023-03-01 00:00:00', NULL, NULL, 3),
(False, 120, '2023-04-01 00:00:00', NULL, NULL, 1),
(True, 180, '2023-05-01 00:00:00', NULL, NULL, 3);


INSERT INTO myApp_fournisseur (nomFournisseur, numRue, nomRue, codePostal, ville, paysFournisseur, mailFournisseur, numTelephoneFournisseur, serviceApresVente) VALUES
('Alpha Supplies', 123, 'Main Street', '12345', 'New York', 'USA', 'orders@alphasupplies.com', '+1987654321', True),
('Bravo Parts', 456, 'Elm Street', '67890', 'Los Angeles', 'USA', 'sales@bravoparts.com', '+1234567890', False),
('Charlie Components', 789, 'Oak Avenue', '12345', 'Chicago', 'USA', 'info@charliecomponents.com', '+1345678901', True),
('Delta Distributors', 101, 'Pine Road', '67890', 'Houston', 'USA', 'support@deltadistributors.com', '+1456789012', True),
('Echo Equipment', 112, 'Maple Lane', '12345', 'Miami', 'USA', 'enquiries@echoequipment.com', '+1567890123', False);



INSERT INTO myApp_modeleequipement (
    nomModeleEquipement,
    fabricant_id
) VALUES
-- Alpha Corp (id: 1)
('Excavatrice Quantique XQ-1000', 1),
('Foreuse Moléculaire FM-500', 1),
('Compresseur Gravitationnel CG-750', 1),

-- Beta Industries (id: 2)
('Laminoir Magnétique LM-2000', 2),
('Presse Hydrostatique PH-3000', 2),
('Extrudeuse à Plasma EP-1500', 2),

-- Gamma Tech (id: 3)
('Laser de Précision Nanométrique LPN-X', 3),
('Scanner Holographique SH-4D', 3),
('Imprimante Biomoléculaire IB-3000', 3),

-- Delta Solutions (id: 4)
('Robot Assembleur Intelligent RAI-5000', 4),
('Drone de Maintenance Autonome DMA-X1', 4),
('Système d Inspection Quantique SIQ-2000', 4),

-- Epsilon Innovations (id: 5)
('Générateur de Champ de Force GCF-X', 5),
('Stabilisateur Temporel ST-1000', 5),
('Analyseur de Matière Noire AMN-500', 5),

-- Additional entries for variety
('Synthétiseur de Matériaux SM-3000', 1),
('Tour à Commande Neuronale TCN-X', 2),
('Recycleur Moléculaire RM-2000', 3),
('Fabricateur Quantique FQ-5000', 4),
('Téléporteur de Particules TP-X1', 5);


INSERT INTO myApp_equipement (
    reference,
    dateCreation,
    designation,
    dateMiseEnService,
    prixAchat,
    lienImageEquipement,
    statutEquipement,
    createurEquipement_id,
    lieu_id,
    modeleEquipement_id,
    fournisseur_id,
    informationMaintenance_id
) VALUES
('EQ-001', '2023-01-15 09:00:00', 'Excavatrice Quantique XQ-1000', '2023-01-20', 500000.00, 'images/equipement/excavatrice.jpg', 'En fonctionnement', 1, 9, 1, 1, 1),
('EQ-002', '2023-02-01 10:30:00', 'Foreuse Moléculaire FM-500', '2023-02-05', 350000.00, 'images/equipement/foreuse.jpg', 'En fonctionnement', 2, 10, 2, 2, 2),
('EQ-003', '2023-03-10 11:45:00', 'Compresseur Gravitationnel CG-750', '2023-03-15', 420000.00, 'images/equipement/compresseur.jpg', 'En fonctionnement', 3, 11, 3, 3, 3),
('EQ-004', '2023-04-05 14:00:00', 'Laminoir Magnétique LM-2000', '2023-04-10', 380000.00, 'images/equipement/laminoir.jpg', 'En fonctionnement', 1, 13, 4, 4, 4),
('EQ-005', '2023-05-20 16:15:00', 'Presse Hydrostatique PH-3000', '2023-05-25', 450000.00, 'images/equipement/presse.jpg', 'En fonctionnement', 2, 14, 5, 5, 5),
('EQ-006', '2023-06-07 08:30:00', 'Extrudeuse à Plasma EP-1500', '2023-06-12', 320000.00, 'images/equipement/extrudeuse.jpg', 'Dégradé', 3, 15, 6, 1, 1),
('EQ-007', '2023-07-18 13:45:00', 'Laser de Précision Nanométrique LPN-X', '2023-07-23', 550000.00, 'images/equipement/laser.jpg', 'En fonctionnement', 1, 22, 7, 2, 2),
('EQ-008', '2023-08-30 11:00:00', 'Scanner Holographique SH-4D', '2023-09-04', 480000.00, 'images/equipement/scanner.jpg', 'En fonctionnement', 2, 23, 8, 3, 3),
('EQ-009', '2023-09-12 15:30:00', 'Imprimante Biomoléculaire IB-3000', '2023-09-17', 620000.00, 'images/equipement/imprimante.jpg', 'A l arret', 3, 24, 9, 4, 4),
('EQ-010', '2023-10-25 10:15:00', 'Robot Assembleur Intelligent RAI-5000', '2023-10-30', 700000.00, 'images/equipement/robot.jpg', 'En fonctionnement', 1, 25, 10, 5, 5);

INSERT INTO myApp_constituer (equipement_id, consommable_id) VALUES
('EQ-001', 1),
('EQ-001', 2),
('EQ-002', 3),
('EQ-002', 4),
('EQ-003', 5),
('EQ-004', 1),
('EQ-004', 3),
('EQ-005', 2),
('EQ-005', 4),
('EQ-005', 5);