import { readDatabase } from '../utils';

class StudentsController {
    static async getAllStudents(req, res) {
        const dbPath = process.argv[2];

        try {
            const students = await readDatabase(dbPath);
            let responseText = 'This is the list of our students\n';

            const sortedFields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
            sortedFields.forEach((field) => {
                const studentNames = students[field];
                responseText += `Number of students in ${field}: ${studentNames.length}. List: ${studentNames.join(', ')}\n`;
            });

            res.status(200).send(responseText.trim());
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const dbPath = process.argv[2];
        const { major } = req.params;

        if (major !== 'CS' && major !== 'SWE') {
            res.status(500).send('Major parameter must be CS or SWE');
            return;
        }

        try {
            const students = await readDatabase(dbPath);
            const studentNames = students[major] || [];
            res.status(200).send(`List: ${studentNames.join(', ')}`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}

export default StudentsController;
