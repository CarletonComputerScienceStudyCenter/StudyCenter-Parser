2804 = Course.create(
    title: 'Discrete Structures II',
    code: 'COMP 2804',
    description: 'A second course in discrete mathematics and discrete structures. Topics include: counting, sequences and sums, discrete probability, basic statistics, recurrence relations, randomized algorithms. Material is illustrated through examples from computing.'
)

midterm = Quiz.create(
    title: "Midterm Fall 2018",
    description: "This is a the midterm from Fall 2018.",
    course_id: 2804.id
)

# -----
