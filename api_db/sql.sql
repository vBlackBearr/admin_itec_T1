

-- Creación de la tabla partners
CREATE TABLE partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    details VARCHAR(255),
    direction VARCHAR(255),
    api_endpoint VARCHAR(255),
    props JSON,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla partners
INSERT INTO partners (name, details, direction, api_endpoint, props, enabled)
VALUES
    ('Partner 1', 'Details 1', 'Direction 1', 'http://api.example.com/', '{"key": "value1"}', 1),
    ('Partner 2', 'Details 2', 'Direction 2', 'http://api.example.com/', '{"key": "value2"}', 1),
    ('Partner 3', 'Details 3', 'Direction 3', 'http://api.example.com/', '{"key": "value3"}', 1);

-- Creación de la tabla raw_materials
CREATE TABLE raw_materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    stock INT,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla raw_materials
INSERT INTO raw_materials (name, description, props, stock, enabled)
VALUES
    ('Raw Material 1', 'Description 1', '{"key": "value1"}', 100, 1),
    ('Raw Material 2', 'Description 2', '{"key": "value2"}', 200, 1),
    ('Raw Material 3', 'Description 3', '{"key": "value3"}', 150, 1);

-- Creación de la tabla products
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    props JSON,
    stock INT,
    price FLOAT,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla products
INSERT INTO products (id, name, description, props, stock, price, enabled)
VALUES
    (17, 'iPhone 14 Azul', 'Description 1', '
{"color": "Azul",
"images": [
        {
          "alt": "",
          "src": "static/img/IPHONE14/Azul/iphone-14-finish-select-202209-6-1inch-blue.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Azul/iphone-14-finish-select-202209-6-1inch-blue_AV1.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Azul/iphone-14-finish-select-202209-6-1inch-blue_AV2.jpeg"
        }
    ]
}', 500, 949.99, 1),
    (18, 'iPhone 14 Morado', 'Description 2', '
{"color": "Morado",
"images": [
        {
          "alt": "",
          "src": "static/img/IPHONE14/Morado/iphone-14-finish-select-202209-6-1inch-purple.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Morado/iphone-14-finish-select-202209-6-1inch-purple_AV1.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Morado/iphone-14-finish-select-202209-6-1inch-purple_AV2.jpeg"
        }
    ]
}', 75, 949.99, 1),
    (19, 'iPhone 14 Amarillo', 'Description 3', '
{"color": "Amarillo",
"images": [
        {
          "alt": "",
          "src": "static/img/IPHONE14/Amarillo/iphone-14-finish-select-202209-6-1inch-yellow.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Amarillo/iphone-14-finish-select-202209-6-1inch-yellow_AV1.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Amarillo/iphone-14-finish-select-202209-6-1inch-yellow_AV2.jpeg"
        }
    ]
}', 60, 949.99, 1),
    (20, 'iPhone 14 Medianoche', 'Description 2', '
{"color": "Medianoche",
"images": [
        {
          "alt": "",
          "src": "static/img/IPHONE14/Medianoche/iphone-14-finish-select-202209-6-1inch-midnight.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Medianoche/iphone-14-finish-select-202209-6-1inch-midnight_AV1.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Medianoche/iphone-14-finish-select-202209-6-1inch-midnight_AV2.jpeg"
        }
    ]
}', 75, 949.99, 1),
    (21, 'iPhone 14 Blanco estelar', 'Description 2', '
{"color": "Blanco estelar",
"images": [
        {
          "alt": "",
          "src": "static/img/IPHONE14/Blanco estelar/iphone-14-finish-select-202209-6-1inch-starlight.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Blanco estelar/iphone-14-finish-select-202209-6-1inch-starlight_AV1.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/Blanco estelar/iphone-14-finish-select-202209-6-1inch-starlight_AV2.jpeg"
        }
    ]
}', 75, 949.99, 1),
    (22, 'iPhone 14 RED', 'Description 2', '
{"color": "RED",
"images": [
        {
          "alt": "",
          "src": "static/img/IPHONE14/RED/iphone-14-finish-select-202209-6-1inch-product-red.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/RED/iphone-14-finish-select-202209-6-1inch-product-red_AV1.jpeg"
        },
        {
          "alt": "",
          "src": "static/img/IPHONE14/RED/iphone-14-finish-select-202209-6-1inch-product-red_AV2.jpeg"
        }
    ]
}', 75, 949.99, 1);

-- Creación de la tabla raw_materials_partners (relación muchos a muchos entre raw_materials y partners)
CREATE TABLE raw_materials_partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raw_material_id INT,
    partner_id INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id) ON DELETE CASCADE,
    FOREIGN KEY (partner_id) REFERENCES partners(id) ON DELETE CASCADE
);

-- Datos de prueba para la tabla raw_materials_partners
INSERT INTO raw_materials_partners (raw_material_id, partner_id, props, enabled)
VALUES
    (1, 1, '{"key": "value1"}', 1),
    (2, 2, '{"key": "value2"}', 1),
    (3, 3, '{"key": "value3"}', 1);

-- Creación de la tabla bom (Bill of Materials)
CREATE TABLE bom (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    raw_material_id INT,
    quantity INT,
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (raw_material_id) REFERENCES raw_materials(id) ON DELETE CASCADE
);

-- Datos de prueba para la tabla bom
INSERT INTO bom (product_id, raw_material_id, quantity, props, enabled)
VALUES
    (1, 1, 5, '{"key": "value1"}', 1),
    (1, 2, 3, '{"key": "value2"}', 1),
    (2, 3, 4, '{"key": "value3"}', 1);

-- Creación de la tabla sales
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    total DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN
);

-- Datos de prueba para la tabla sales
INSERT INTO sales (date, total, props, enabled)
VALUES
    ('2023-01-15', 500.00, '{"key": "value1"}', 1),
    ('2023-02-20', 750.50, '{"key": "value2"}', 1),
    ('2023-03-25', 300.25, '{"key": "value3"}', 1);

-- Creación de la tabla products_sales (relación muchos a muchos entre products y sales)
CREATE TABLE products_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    sale_id INT,
    quantity INT,
    subtotal DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE
);

-- Datos de prueba para la tabla products_sales
INSERT INTO products_sales (product_id, sale_id, quantity, subtotal, props, enabled)
VALUES
    (1, 1, 2, 100.00, '{"key": "value1"}', 1),
    (1, 2, 3, 150.75, '{"key": "value2"}', 1),
    (2, 3, 1, 75.25, '{"key": "value3"}', 1);


-- Tabla de roles
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255) NOT NULL,
    enabled BOOLEAN DEFAULT TRUE
);


-- Valores de prueba para la tabla "roles"
INSERT INTO roles (role_name) VALUES
    ('Administrador'),
    ('Editor'),
    ('Usuario');


-- Tabla de usuarios
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role_id INT,
    cart JSON,
    props JSON,
    enabled BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);


-- Valores de prueba para la tabla "usuarios"
INSERT INTO users (username, password, email, role_id) VALUES
    ('admin', 'hashed_password_admin', 'admin@example.com', 1),
    ('editor', 'hashed_password_editor', 'editor@example.com', 2),
    ('usuario1', 'hashed_password_user1', 'usuario1@example.com', 3),
    ('usuario2', 'hashed_password_user2', 'usuario2@example.com', 3);


CREATE TABLE user_cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    props JSON,
    enabled BOOLEAN DEFAULT TRUE,
    UNIQUE KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Creación de la tabla purchases
CREATE TABLE purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    raw_materials_partners_id INT,
    date DATE,
    total DECIMAL(10, 2),
    props JSON,
    enabled BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (raw_materials_partners_id) REFERENCES raw_materials_partners(id) ON DELETE CASCADE
);
