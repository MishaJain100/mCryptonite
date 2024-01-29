<font size = '4'>
<p align = "center">
<b>
Resources Used 
</b>
</p>
</font>

<br>
<font size = '3'>

- https://expressjs.com/en/starter/hello-world.html
- https://www.codecademy.com/article/what-is-crud
- https://expressjs.com/en/guide/database-integration.html
- https://stackoverflow.com/questions/39870867/what-does-app-usebodyparser-json-do
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://planetscale.com/blog/how-to-prevent-sql-injection-attacks-in-node-js
- https://stackoverflow.com/questions/41677815/how-to-loop-through-node-js-array
- https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript

Error:<br>
- ReferenceError: title is not defined<br>
Solution: https://stackoverflow.com/questions/37732986/ejs-js-referenceerror-title-not-defined<br><br>

<b>Rewriting code to prevent SQL Injection:</b><br>
<br>
Original code for updating record:

    const bID = parseInt(req.params.id);

    const { title, author } = req.body;

    const updateData = [];

    const lettersAndNumbersPattern = /^[A-Za-z0-9]+$/;

    if (title) updateData.push(`title = '${title}'`);
    if (author) updateData.push(`author = '${author}'`);

    query = `UPDATE books SET ${updateData.join(', ')} WHERE id = ?`;

New code for updating record:

    const bID = parseInt(req.params.id);

    const { title, author } = req.body;

    const updateData = [];

    const lettersAndNumbersPattern = /^[A-Za-z0-9]+$/;

    // Added code to check for special characters to prevent sqli
    if(!title.match(lettersAndNumbersPattern) || !author.match(lettersAndNumbersPattern)) {
        return res.status(400).json({ err: "No special characters please!"});
    }

    if (title) updateData.push(`title = '${title}'`);
    if (author) updateData.push(`author = '${author}'`);

    query = `UPDATE books SET ${updateData.join(', ')} WHERE id = ?`;

<br><br><br>

Updating code to prevent SQL Injection using placeholders:

New code:

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

</font>