const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();
const port = 2220;

app.use(bodyParser.json());

let query;

// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Connect to DB
const db = new sqlite3.Database('C:\\Users\\misha\\Desktop\\Important Stuff\\Databases\\CRUD.db', sqlite3.OPEN_READWRITE);

// console.log is used for printing in terminal
// Browsers can only use get requests

//Homepage
app.get('/', (req, res) => {
    console.log ('Reached Hompage');
    res.send ('Homepage');
});

// Creating a record
app.post('/books', (req, res) => {

    const { title, author } = req.body;

    if (!title && !author) {
        return res.status(400).send('Title and Author are required');
    }

    query = 'INSERT INTO books (id, title, author) VALUES (NULL, ?, ?)';

    db.run(query, [title, author], (err) => {
        if (err) {
            console.error(err.message);
            return res.status(500).send('Error creating book record');
        }

        console.log ("Book added");
        res.status(200).send('Book added successfully');
    });
});

// Searching
app.post('/books/search', (req, res) => {
    
    var { q } = req.body;
    console.log(q);

    if (!q) {
        return res.status(400).send('Title or Author required');
    }
    q = '%' + q + '%';

    query = "SELECT * FROM BOOKS WHERE title LIKE ? or author LIKE ?"; 

    db.all (query, [q, q], (err, rows) => {
        if (err) {
            console.error(err.message);
            return res.status(500).send('Error retrieving book record');
        }

        console.log ("Books retrieved", rows);
        res.status(200);
        res.json(rows);
    });

});

// Reading all records
app.get('/books', (req, res) => {
    query = 'SELECT * FROM BOOKS';
    db.all(query, (err, rows) => {
        if (err) {
            console.error(err.message);
            return res.status(500).send('Error displaying book records');
        }

        console.log ("Displayed all rows");
        res.status(200);
        res.json(rows);
    });
});

// Update record
app.put('/books/:id', (req, res) => {

    const bID = parseInt(req.params.id);

    const { title, author } = req.body;

    if (title) {
        query = `UPDATE books SET title = ? WHERE id = ?`;
        db.run (query, [title, bID], (err) => {
            if (err) {
                console.error(err.message);
                return res.status(500).send('Error updating book record');
            }
    
            console.log(`Book title updated`);
        });
    }

    if (author) {
        query = `UPDATE books SET author = ? WHERE id = ?`;
        db.run (query, [author, bID], (err) => {
            if (err) {
                console.error(err.message);
                return res.status(500).send('Error updating book record');
            }
    
            console.log(`Book author updated`);
        });
    }

    res.status(200).send('Book updated successfully');
});

// Delete record
app.delete ('/books/:id', (req, res) => {
    
    const bID = parseInt(req.params.id);
    query = 'DELETE FROM books WHERE id = ?';

    db.run (query, [bID], (err) => {
        if (err) {
            console.error(err.message);
            return res.status(500).send('Error deleting book record');
        }

        console.log('Book deleted');
        res.status(200).send('Book deleted successfully');
    });
});

app.listen(port, () => {
    console.log(`Server running on port: http://localhost:${port}`);
});