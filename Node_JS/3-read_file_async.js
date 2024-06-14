const fs = require('fs');

function countStudents(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n').filter(line => line.trim() !== '');

            const studentCount = lines.length - 1;
            console.log(`Number of students: ${studentCount}`);

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

            console.log(`Number of students in CS: ${fieldCounts.CS.length}. List: ${fieldCounts.CS.join(', ')}`);
            console.log(`Number of students in SWE: ${fieldCounts.SWE.length}. List: ${fieldCounts.SWE.join(', ')}`);

            resolve(studentCount);
        });
    });
}

module.exports = countStudents;
