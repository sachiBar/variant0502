class TimesTable:
    @staticmethod
    def print_times_table():
        for i in range(1, 13):
            for j in range(1, 13):
                print(f"{i} x {j} = {i*j}")
            print()

# Example usage
TimesTable.print_times_table()