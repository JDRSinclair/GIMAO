-- Insert pour EQ-006
INSERT INTO myApp_informationstatut (
    statutEquipement,
    dateChangement,
    equipement_id,
    informationStatutParent_id,
    ModificateurStatut_id
) 
SELECT 
    'Dégradé',
    CURRENT_TIMESTAMP,
    'EQ-006',
    (SELECT id FROM (SELECT id FROM myApp_informationstatut WHERE equipement_id = 'EQ-006' ORDER BY dateChangement DESC LIMIT 1) AS temp),
    3;

-- Insert pour EQ-009
INSERT INTO myApp_informationstatut (
    statutEquipement,
    dateChangement,
    equipement_id,
    informationStatutParent_id,
    ModificateurStatut_id
) 
SELECT 
    'A l''arret',
    CURRENT_TIMESTAMP,
    'EQ-009',
    (SELECT id FROM (SELECT id FROM myApp_informationstatut WHERE equipement_id = 'EQ-009' ORDER BY dateChangement DESC LIMIT 1) AS temp),
    3;