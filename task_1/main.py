import pathlib

current_dir = pathlib.Path(__file__).parent

def total_salary(filename: str) -> tuple[int, int]:
    try:
        with open(current_dir / filename, "r") as file:
            salaries = [int(line.strip().split(",")[1]) for line in file]
            total_sum = sum(salaries)
            average_salary = total_sum // len(salaries)
            return total_sum, average_salary
    except FileNotFoundError:
        print("file is not exists") 
        return 0, 0


total, average = total_salary('salaries.txt')
print(f"Total sum of salaries: {total}, Average salary: {average}")
