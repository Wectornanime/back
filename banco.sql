-- Active: 1686500747749@@127.0.0.1@3306@banco_teste


CREATE database if NOT EXISTS banco_teste;

USE banco_teste;

CREATE TABLE if NOT EXISTS meds (
cod INT NOT NULL AUTO_INCREMENT,
farmaco VARCHAR(30),
detentor VARCHAR(30),
medicamento VARCHAR(30),
concentracao VARCHAR(30),
PRIMARY KEY (cod)
);

INSERT INTO meds (farmaco, detentor, medicamento, concentracao)
VALUES
('abacavir (sulfato)', 'Glaxosmithkline', 'ZIAGENAVIR', '20 mg/mL'),
('abacavir (sulfato)', 'Glaxosmithkline', 'ZIAGENAVIR', '300 mg'),
('abemaciclibe', 'Eli Lilly', 'VERZENIOS', '50mg'),
('abemaciclibe', 'Eli Lilly', 'VERZENIOS', '100mg'),
('abemaciclibe', 'Eli Lilly', 'VERZENIOS', '150mg'),
('abemaciclibe', 'Eli Lilly', 'VERZENIOS', '200mg'),
('abiraterona (acetato)', 'Janssen-Cilag', 'ZYTIGA' , '250mg' ),
('abiraterona (acetato)', 'Janssen-Cilag', 'ZYTIGA' , '500mg' ),
('acalabrutinibe', 'Astrazeneca', 'CALQUENCE', '100mg'),
('acebrofilina', 'Aché', 'BRONDILAT', '5mg/mL'),
('acebrofilina', 'Aché', 'BRONDILAT', '10 mg/mL'),
('acebrofilina', 'Eurofarma', 'FILINAR G', '5mg/ml'),
('aceclofenaco', 'Eurofarma', 'PROFLAM', '100mg'),
('aceclofenaco', 'Eurofarma', 'PROFLAM', '15mg/g'),
('acetato de fluormetolona', 'Novartis Biociências', 'FLORATE', '1mg/ mL'),
('acetato de glatiramer', 'Teva Farmacêutica', 'COPAXONE', '20mg/mL'),
('acetato de glatiramer', 'Teva Farmacêutica', 'COPAXONE', '40mg/mL'),
('acetazolamida', 'União Química', 'meto', '250 mg'),
('acetilcisteína', 'Eurofarma', 'ACETILCISTEÍNA', '100mg'),
('acetilcisteína', 'União Química', 'FLUCISTEIN', '40mg/g'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '120mg/g'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '11,5mg/ml'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '20 mg/ml'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '40mg/ml'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '600mg'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '100mg/ml'),
('acetilcisteína', 'Zambon', 'FLUIMUCIL', '200mg'),
('aciclovir', 'Merck', 'ACICLOVIR', '400 mg'),
('aciclovir', 'Glaxosmithkline', 'ZOVIRAX', '200 mg'),
('aciclovir', 'Glaxosmithkline', 'ZOVIRAX', '250mg/10mL'),
('aciclovir', 'Glaxosmithkline', 'ZOVIRAX', '50 mg/g');
