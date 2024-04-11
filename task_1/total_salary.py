def total_salary(path: str) -> tuple[int, int]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [int(line.strip().split(",")[1]) for line in file]
            total_sum = sum(salaries)
            average_salary = total_sum // len(salaries)
            return total_sum, average_salary
    except FileNotFoundError:
        print("file does not exist") 
        return 0, 0


total, average = total_salary('task_1\salaries.txt')
print(f"Total sum of salaries: {total}, Average salary: {average}")
