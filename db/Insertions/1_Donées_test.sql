
INSERT INTO myApp_role (nomRole) VALUES 
('Operateur'),
('Magasinier'),
('Technicien'),
('Responsable GMAO'),
('Administrateur');

INSERT INTO myApp_lieu (nomLieu, typeLieu, lieuParent_id) VALUES
('Atelier A', 'Atelier de production', NULL),
('Salle de stock', 'Salle de stockage', NULL),
('Bureau B', 'Bureau administratif', NULL),
('Laboratoire C', 'Laboratoire de recherche', NULL),
('Salle de réunion', 'Salle de réunion', NULL),
('Atelier D', 'Atelier de maintenance', NULL),
('Sous-atelier 1', 'Sous-atelier', 1),
('Sous-atelier 2', 'Sous-atelier', 1),
('Sous-atelier 3', 'Sous-atelier', 1),
('Sous-atelier 1', 'Sous-atelier', 4),
('Sous-atelier 2', 'Sous-atelier', 4);


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
('Machine à dynamiter', 1),
('Machine à plaques de fer', 2),
('Graveuse de bois', 3),
('Imprimante 3D', 4),
('Scanner géothermique', 5),
('Machine à fusée', 1);



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
('EQ001', '2023-01-15 10:00:00', 'Machine A', '2023-02-01', 10000.00, 'images/equipement/eq001.jpg', 'En fonctionnement', 1, 1, 1, 1, 1),
('EQ002', '2023-02-20 14:30:00', 'Machine B', '2023-03-01', 15000.00, 'images/equipement/eq002.jpg', 'En fonctionnement', 2, 2, 2, 2, 2),
('EQ003', '2023-03-25 09:45:00', 'Machine C', '2023-04-01', 20000.00, 'images/equipement/eq003.jpg', 'En fonctionnement', 3, 3, 3, 3, 3),
('EQ004', '2023-04-30 12:15:00', 'Machine D', '2023-05-01', 25000.00, 'images/equipement/eq004.jpg', 'En fonctionnement', 3, 4, 4, 4, 4),
('EQ005', '2023-05-10 16:00:00', 'Machine E', '2023-06-01', 30000.00, 'images/equipement/eq005.jpg', 'En fonctionnement', 2, 5, 5, 5, 5);



INSERT INTO myApp_constituer (equipement_id, consommable_id) VALUES
('EQ001', 1),
('EQ001', 2),
('EQ002', 3),
('EQ002', 4),
('EQ003', 5),
('EQ004', 1),
('EQ004', 3),
('EQ005', 2),
('EQ005', 4),
('EQ005', 5);