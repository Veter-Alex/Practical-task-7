import sqlite3


def create_tables():
    """Используя команду CREATE DATABASE,
    создайте новую базу данных с названием,
    которое отражает ее цель (например, SchoolDB для базы данных школы).

    Используя команду CREATE TABLE,
    создайте несколько таблиц
    (например, таблицы Students, Courses, Enrollments).
    Укажите основные поля, такие как id, name
    и необходимые типы данных.
    """

    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()
    # создаем таблицу студентов
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Gender TEXT NOT NULL,
            EnrollmentDate TEXT NOT NULL
        )"""
    )

    # создаем таблицу курсов
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
            CourseName TEXT NOT NULL,
            DurationWeeks INTEGER NOT NULL,
            StartDate TEXT NOT NULL
        )"""
    )

    # создаем таблицу связи студентов и курсов
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Enrollments (
            EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
            StudentID INTEGER NOT NULL,
            CourseID INTEGER NOT NULL,
            EnrollmentDate TEXT NOT NULL,
            FOREIGN KEY (StudentID) REFERENCES Students (StudentID),
            FOREIGN KEY (CourseID) REFERENCES Courses (CourseID)
        )"""
    )

    conn.commit()
    conn.close()


def insert_sample_data():
    """Используйте команду INSERT INTO,
    чтобы добавить несколько записей в каждую из созданных таблиц.
    """

    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()
    # вставляем данные в таблицу студентов
    cursor.executemany(
        "INSERT INTO Students (Name, Age, Gender, EnrollmentDate) VALUES (?, ?, ?, ?)",
        [
            ("Alice", 20, "Female", "2022-01-01"),
            ("Bob", 20, "Male", "2022-02-01"),
            ("Charlie", 22, "Female", "2022-03-01"),
            ("David", 20, "Male", "2022-04-01"),
            ("Eva", 24, "Female", "2022-05-01"),
        ],
    )

    # вставляем данные в таблицу курсов
    cursor.executemany(
        "INSERT INTO Courses (CourseName, DurationWeeks, StartDate) VALUES (?, ?, ?)",
        [
            ("Math", 12, "2022-01-01"),
            ("English", 12, "2022-02-01"),
            ("Science", 12, "2022-03-01"),
            ("History", 8, "2022-04-01"),
            ("Art", 6, "2022-05-01"),
        ],
    )

    # вставляем данные в таблицу связи студентов и курсов
    cursor.executemany(
        "INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate) VALUES (?, ?, ?)",
        [
            (1, 1, "2022-01-01"),  # студент 1 записался на курс 1
            (1, 2, "2022-02-01"),  # студент 1 записался на курс 2
            (1, 3, "2022-02-01"),  # студент 1 записался на курс 3
            (2, 2, "2022-02-01"),
            (2, 4, "2022-03-01"),
            (3, 3, "2022-03-01"),
            (3, 4, "2022-04-01"),
            (4, 4, "2022-04-01"),
            (4, 5, "2022-05-01"),
            (5, 5, "2022-05-01"),
            (5, 1, "2022-01-01"),
        ],
    )

    conn.commit()

    # выводим данные о студентах
    print("\nСтуденты:")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def select_data():
    """
    Используя команду SELECT, извлеките данные из одной из таблиц
    (например, все записи из таблицы Students).
    Используйте команду WHERE, чтобы отфильтровать данные по определенному условию
    (например, извлеките студентов с определенным возрастом или из конкретного города).
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # выводим данные о студентах
    print("\nСтуденты:")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    # выводим данные о студентах имя и возраст
    print("\nСтуденты (Имя, Возраст):")
    cursor.execute("SELECT Name, Age FROM Students")
    for row in cursor.fetchall():
        print(row)

    # выводим данные о студентах имя и возраст, где возраст больше 23
    print("\nСтуденты (Имя, Возраст > 23):")
    cursor.execute("SELECT * FROM Students WHERE Age > 23")
    for row in cursor.fetchall():
        print(row)

    # выводим данные о студентах имя, где имя равно David
    print("\nСтуденты (Имя = 'Charlie'):")
    cursor.execute("SELECT * FROM Students WHERE Name LIKE 'Charlie'")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def update_data():
    """
    Используя команды UPDATE, обновите определенные записи в таблице (например, измените возраст студента).
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # обновляем данные о Charlie (возраст 22)
    cursor.execute("UPDATE Students SET Age = 22 WHERE Name = 'Charlie'")
    conn.commit()

    # выводим данные о Charlie
    print("\nСтуденты ('Charlie', возраст 22):")
    cursor.execute("SELECT * FROM Students WHERE Name LIKE 'Charlie'")
    for row in cursor.fetchall():
        print(row)

    # обновляем данные о Charlie (возраст 21)
    cursor.execute("UPDATE Students SET Age = 21 WHERE Name = 'Charlie'")
    conn.commit()

    # выводим данные о Charlie
    print("\nСтуденты ('Charlie', возраст 21):")
    cursor.execute("SELECT * FROM Students WHERE Name LIKE 'Charlie'")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def delete_data():
    """
    Используя команды DELETE, удалите ненужные записи.
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # выводим данные о студентах
    print("\nСтуденты (с 'Charlie'):")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    # удаляем данные о Charlie
    cursor.execute("DELETE FROM Students WHERE Name = 'Charlie'")
    conn.commit()

    # выводим данные о студентах после удаления
    print("\nСтуденты (после удаления 'Charlie'):")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    # вставляем Charlie назад
    cursor.executemany(
        "INSERT INTO Students (Name, Age, Gender, EnrollmentDate) VALUES (?, ?, ?, ?)",
        [
            ("Charlie", 22, "Female", "2022-03-01"),
        ],
    )
    conn.commit()
    conn.close()


def join_data():
    """
    Используя команду JOIN, соедините две таблицы (например, Students и Enrollments),
    чтобы получить данные о студентах и курсах, на которые они записаны.
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    print("\nСтуденты и курсы на которые они записаны (JOIN):")
    cursor.execute(
        """
        SELECT Students.Name, Courses.CourseName FROM Students
        JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
        JOIN Courses ON Enrollments.CourseID = Courses.CourseID
        """
    )
    for row in cursor.fetchall():
        print(row)

    conn.close()


def groupe_by_data():
    """
    Используя команду GROUP BY, сгруппируйте данные по определенному критерию
    (например, количество студентов на каждом курсе).
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    print("\nКоличество студентов на каждом курсе (GROUP BY):")
    cursor.execute(
        """
        SELECT Courses.CourseName, COUNT(*) FROM Students
        JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
        JOIN Courses ON Enrollments.CourseID = Courses.CourseID
        GROUP BY Courses.CourseName
        """
    )
    for row in cursor.fetchall():
        print(row)

    conn.close()


def count_sum_avg_data():
    """
    Используйте команды COUNT, SUM, AVG и другие агрегатные функции
    для выполнения вычислений над сгруппированными данными
    (например, подсчитайте средний возраст студентов на каждом курсе).
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    print("\nСредний возраст студентов на каждом курсе (AVG):")
    cursor.execute(
        """
        SELECT Courses.CourseName, AVG(Students.Age) FROM Students
        JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
        JOIN Courses ON Enrollments.CourseID = Courses.CourseID
        GROUP BY Courses.CourseName
        """
    )
    for row in cursor.fetchall():
        print(row)

    conn.close()


def select_select_data():
    """
    Используя подзапрос (например, SELECT внутри SELECT),
    выберите данные из одной таблицы на основе условия,
    заданного в другой таблице
    (например, выберите студентов, которые записаны на определенный курс).
    """

    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # выводим данные о студентах
    print("\nСтуденты:")
    cursor.execute(
        """
        SELECT * FROM students
        WHERE StudentID IN (SELECT StudentID
                    FROM Enrollments
                    WHERE CourseID IN (SELECT CourseID
                        FROM Courses
                        WHERE CourseName = 'Math'))
        """
    )
    for row in cursor.fetchall():
        print(row)

    conn.close()


def begin_rollback_commit():
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # Начало транзакции
    cursor.execute("BEGIN TRANSACTION")

    try:
        # выводим данные о студентах
        print("\nСтуденты до изменения и удаления:")
        cursor.execute("SELECT * FROM Students")
        for row in cursor.fetchall():
            print(row)

        # Обновление данных
        print("\n коменда: UPDATE students SET age = 25 WHERE name = 'Bob'")
        cursor.execute("UPDATE students SET age = 25 WHERE name = 'Bob'")

        # Удаление данных
        print("\n коменда: DELETE FROM students WHERE age = 22")
        cursor.execute("DELETE FROM students WHERE age = 22")

        # Фиксация транзакции
        cursor.execute("COMMIT")

        # выводим данные о студентах
        print("\nСтуденты после изменения и удаления:")
        cursor.execute("SELECT * FROM Students")
        for row in cursor.fetchall():
            print(row)

        print("\nТранзакция успешно завершена.")

        # Возвращаем данные в исходное состояние
        cursor.execute("UPDATE students SET age = 20 WHERE name = 'Bob'")
        cursor.executemany(
            "INSERT INTO Students (Name, Age, Gender, EnrollmentDate) VALUES (?, ?, ?, ?)",
            [
                ("Charlie", 22, "Female", "2022-03-01"),
            ],
        )
        conn.commit()
        print("\nДанные возвращены в исходное состояние.")
    except sqlite3.Error as e:
        # Откат транзакции в случае ошибки
        cursor.execute("ROLLBACK")
        print(f"\nОшибка при выполнении транзакции: {e}")
    finally:
        # Закрытие подключения
        conn.close()


if __name__ == "__main__":
    # create_tables()
    # insert_sample_data()
    # select_data()
    # update_data()
    # delete_data()
    # join_data()
    # groupe_by_data()
    # count_sum_avg_data()
    select_select_data()
    begin_rollback_commit()
