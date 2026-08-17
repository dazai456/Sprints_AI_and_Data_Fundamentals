-- Create the Bookstore database
CREATE DATABASE IfNotExists Bookstore; 

-- Create the Authors table
CREATE TABLE Authors(author_id PK, name, birth_year); 

-- Create the Books table
CREATE TABLE Books(book_id PK, title, author_id FK, price); 

-- Create the Sales table
CREATE TABLE Sales(sale_id PK, book_id FK, sale_date, quantity).

-- insert sample data into the Sales table
INSERT INTO Sales(sale_id, book_id, sale_date, quantity) VALUES 
    (1, 1, '2023-01-15', 2),
    (2, 2, '2023-02-20', 1),
    (3, 3, '2023-03-10', 3),
    (4, 1, '2023-04-05', 1),
    (5, 2, '2023-05-12', 2)
    ;

-- insert sample data into the Books table
INSERT INTO Books(book_id, title, author_id, price) VALUES 
    (1, 'Harry Potter and the Sorcerer''s Stone', 1, 19.99),
    (2, 'A Game of Thrones', 2, 24.99),
    (3, 'The Hobbit', 3, 14.99),
    (4, 'Harry Potter and the Chamber of Secrets', 1, 21.99),
    (5, 'A Clash of Kings', 2, 22.99),
    (6, 'The Lord of the Rings', 3, 29.99),
    (7, 'Murder on the Orient Express', 4, 16.99)
    ;

-- insert sample data into the Authors table
INSERT INTO Authors(author_id, name, birth_year) VALUES 
    (1, 'J.K. Rowling', 1965),
    (2, 'George R.R. Martin', 1948),
    (3, 'J.R.R. Tolkien', 1892),
    (4, 'Agatha Christie', 1890),
    (5, 'Stephen King', 1947)
    ;

-- execute a query to count the number of authors with NULL author_id
SELECT COUNT(*) FROM Authors WHERE author_id IS NULL;

-- fetch the result of the query
SELECT B.title, A.name FROM Books B JOIN Authors A ON B.author_id = A.author_id;

SELECT book_id, SUM(quantity) AS total_sold FROM Sales GROUP BY book_id;

SELECT B.title, S.sale_date, S.quantity FROM Books B INNER JOIN Sales S ON B.book_id = S.book_id;