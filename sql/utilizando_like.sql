-- Consulta na Tabela
SELECT * FROM Treinamento;

-- Utilizando o comando LIKE
SELECT * FROM Treinamento
WHERE curso = 'O poder';

SELECT * FROM Treinamento
WHERE curso LIKE 'O poder%';

SELECT * FROM Treinamento
WHERE curso LIKE '%realizar%';

SELECT * FROM Colaboradores
WHERE nome LIKE 'Isadora%';
