import os
def config_file_path():
    results_folder = os.path.join(os.path.dirname(__file__), "Result")
    os.makedirs(results_folder, exist_ok=True)
    file_path = os.path.join(results_folder, "clean_results.txt")
    return file_path