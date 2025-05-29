CREATE DATABASE rd_cafe;
USE rd_cafe;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Menu Items table
CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    image VARCHAR(255)
);

-- Orders table
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT,
    user_id INT,
    menu_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (menu_id) REFERENCES menu_items(id)
);

-- Members table
CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    join_date DATE DEFAULT CURRENT_DATE
);

-- Admin table
CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(100)
);

-- Insert menu items
INSERT INTO menu_items (name, price, image) VALUES
('Chocolate Lava Cake', 250, 'lava_cake.jpg'),
('New York Cheesecake', 300, 'cheesecake.jpg'),
('Strawberry Shortcake', 280, 'shortcake.jpg'),
('Red Velvet Slice', 270, 'red_velvet.jpg'),
('Tiramisu Cup', 320, 'tiramisu.jpg'),
('Fresh Orange Juice', 120, 'orange_juice.jpg'),
('Mixed Berry Smoothie', 150, 'berry_smoothie.jpg'),
('Lemon Mint Cooler', 130, 'lemon_mint.jpg'),
('Mango Shake', 160, 'mango_shake.jpg'),
('Detox Green Juice', 180, 'detox_juice.jpg'),
('RD House Red Wine (Glass)', 350, 'red_wine.jpg'),
('RD Signature White Wine', 380, 'white_wine.jpg'),
('Nepali Aaila Premium Shot', 220, 'aaila.jpg'),
('Imported Sake – Japanese Rice Wine', 420, 'sake.jpg'),
('Classic Whiskey Glass', 400, 'whiskey.jpg');