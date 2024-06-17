import fs from 'fs/promises';

export async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf8');
        const lines = data.split('\n').filter(line => line.trim() !== '');

        const students = {};

        lines.slice(1).forEach((line) => {
            const [firstName, , , field] = line.split(',');

            if (field && firstName) {
                const fieldName = field.trim();
                if (!students[fieldName]) {
                    students[fieldName] = [];
                }
                students[fieldName].push(firstName.trim());
            }
        });

        return students;
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}
