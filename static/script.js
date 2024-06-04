<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Evaluation</title>
    <script>
        const questions = [
            {
                id: 1,
                question: "What is the primary purpose of programming languages?",
                options: [
                    "To enable computers to understand human emotions",
                    "To enable humans to communicate instructions to computers",
                    "To enhance graphics and sound in video games",
                    "To design computer hardware"
                ],
                answer: 1
            },
            {
                id: 2,
                question: "Which language was the earliest form of programming used to communicate directly with a computer's hardware?",
                options: [
                    "Assembly Language",
                    "High-Level Language",
                    "Machine Language",
                    "Fourth-Generation Language"
                ],
                answer: 2
            },
            {
                id: 3,
                question: "What is an example of a high-level programming language developed for scientific computing in 1957?",
                options: [
                    "COBOL",
                    "FORTRAN",
                    "Python",
                    "JavaScript"
                ],
                answer: 1
            },
            {
                id: 4,
                question: "Which type of programming language emerged in the 1970s and 1980s and is designed to be closer to natural human language?",
                options: [
                    "Machine Language",
                    "Assembly Language",
                    "Fourth-Generation Languages",
                    "Low-Level Languages"
                ],
                answer: 2
            },
            {
                id: 5,
                question: "Which programming paradigm is based on the concept of objects, which are instances of classes encapsulating data and behavior?",
                options: [
                    "Procedural Languages",
                    "Functional Languages",
                    "Object-Oriented Languages",
                    "Scripting Languages"
                ],
                answer: 2
            },
            {
                id: 6,
                question: "Which of the following is NOT a component of programming languages?",
                options: [
                    "Syntax",
                    "Semantics",
                    "Compilers",
                    "Control Structures"
                ],
                answer: 2
            },
            {
                id: 7,
                question: "Which language is known for its high-level, interpreted nature and is extensively used in data analysis and machine learning?",
                options: [
                    "C++",
                    "JavaScript",
                    "Python",
                    "Ruby"
                ],
                answer: 2
            },
            {
                id: 8,
                question: "Which language was designed by Apple for performance and safety, specifically for iOS and macOS app development?",
                options: [
                    "C#",
                    "Swift",
                    "Ruby",
                    "Kotlin"
                ],
                answer: 1
            },
            {
                id: 9,
                question: "What is a trend in programming languages that focuses on supporting multiple programming paradigms for greater flexibility?",
                options: [
                    "Development of Quantum Computing Languages",
                    "Rise of Multi-Paradigm Languages",
                    "Improved Performance and Efficiency",
                    "Low-Code and No-Code Platforms"
                ],
                answer: 1
            },
            {
                id: 10,
                question: "Which language is gaining traction due to its emphasis on memory safety and prevention of common programming errors that lead to security vulnerabilities?",
                options: [
                    "Rust",
                    "C",
                    "Prolog",
                    "SQL"
                ],
                answer: 0
            }
        ];

        function evaluateAnswers(userAnswers) {
            let score = 0;
            questions.forEach((question, index) => {
                if (userAnswers[index] === question.answer) {
                    score++;
                }
            });
            return score;
        }

        function submitQuiz() {
            const userAnswers = [];
            questions.forEach((question, index) => {
                const selectedOption = document.querySelector(`input[name="question${question.id}"]:checked`);
                if (selectedOption) {
                    userAnswers.push(parseInt(selectedOption.value));
                } else {
                    userAnswers.push(null);  // No answer selected
                }
            });
            const score = evaluateAnswers(userAnswers);
            alert(`Your score is ${score} out of ${questions.length}`);
        }
    </script>
</head>
<body>
    <h1>Quiz</h1>
    <form id="quizForm">
        <div id="quizContainer"></div>
        <button type="button" onclick="submitQuiz()">Submit</button>
    </form>
    <script>
        const quizContainer = document.getElementById('quizContainer');
        questions.forEach(question => {
            const questionDiv = document.createElement('div');
            questionDiv.innerHTML = `
                <p>${question.question}</p>
                ${question.options.map((option, index) => `
                    <label>
                        <input type="radio" name="question${question.id}" value="${index}">
                        ${option}
                    </label><br>
                `).join('')}
            `;
            quizContainer.appendChild(questionDiv);
        });
    </script>
</body>
</html>
