/* eslint-disable comma-dangle */
const fs = require('fs');

const countStudents = (path) => {
  let content;

  try {
    content = fs.readFileSync(path);
  } catch (e) {
    throw new Error('Cannot load the database');
  }

  content = content.toString().split('\n');

  let students = content.filter((student) => student);

  students = students.map((student) => student.split(','));

  const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;

  console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);

  const fields = {};
  for (const student of students) {
    if (!fields[student[3].replace('\r', '')]) {
      fields[student[3].replace('\r', '')] = [];
    }
    fields[student[3].replace('\r', '')].push(student[0]);
  }

  delete fields.field;

  for (const key of Object.keys(fields)) {
    console.log(
      `Number of students in ${key}: ${fields[key].length}. List: ${fields[
        key
      ].join(', ')}`
    );
  }
};

module.exports = countStudents;