USE mercearia;

-- popular o banco de dados para fins de desenvolvimento

INSERT INTO product (name, description, price) VALUES ('Banana', 'bananas amarelas fresquinhas', 2.0);
INSERT INTO product (name, description, price) VALUES ('Beterraba', 'beterrabas roxas fresquinhas', 3.0);
INSERT INTO product (name, description, price) VALUES ('Leite em pó', 'leite em pó integral instantâneo', 5.0);
INSERT INTO product (name, description, price) VALUES ('Achocolatado', 'achocolatado marrom', 4.0);
INSERT INTO product (name, description, price) VALUES ('Uvas redondinhas', 'uvas rendondas', 1.0);

INSERT INTO cart (user_id) VALUES (0);
