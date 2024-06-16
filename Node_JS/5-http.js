const fs = require('fs').promises;
const http = require('http');

async function countStudents(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.split('\n').filter(line => line.trim() !== '');

        const studentCount = lines.length - 1;
        const fieldCounts = {
            CS: [],
            SWE: [],
        };

        for (let i = 1; i < lines.length; i++) {
            const row = lines[i].split(',');
            const firstName = row[0].trim();
            const field = row[3] ? row[3].trim() : '';

            if (field === 'CS') {
                fieldCounts.CS.push(firstName);
            } else if (field === 'SWE') {
                fieldCounts.SWE.push(firstName);
            }
        }

        let result = 'This is the list of our students\n';
        result += `Number of students: ${studentCount}\n`;
        result += `Number of students in CS: ${fieldCounts.CS.length}. List: ${fieldCounts.CS.join(', ')}\n`;
        result += `Number of students in SWE: ${fieldCounts.SWE.length}. List: ${fieldCounts.SWE.join(', ')}`;

        return result;
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

const app = http.createServer(async (req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        try {
            const theData = await countStudents(process.argv[2]);
            res.end(theData);
        } catch (error) {
            res.end(`${error.message}`);
        }
    }
});

app.listen(1245);

module.exports = app;
