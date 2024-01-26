import sys

def process_temperatures(temperatures):
    if not temperatures:
        print("No temperature values provided.")
        return

    try:
        temperatures = [float(temp) for temp in temperatures]
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)

        print(f"Maximum Temperature: {max_temp}")
        print(f"Minimum Temperature: {min_temp}")
        print(f"Mean Temperature: {mean_temp}")

    except ValueError:
        print("Invalid temperature values provided. Please enter valid numbers.")

if __name__ == "__main__":
    # Extract temperature values from command-line arguments (excluding script name)
    temperature_values = sys.argv[1:]
    process_temperatures(temperature_values)
