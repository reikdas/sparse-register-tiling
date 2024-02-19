import subprocess
import os
import re

def extract_number(input_string)->str:
    match = re.search(r"\d+\.\d+", input_string)
    if match:
        return match.group()  # Returns the matched group (the number) as a string
    else:
        return None

if __name__ == "__main__":
    for threads in [1, 16]:
        with open(os.path.join("results", "bench_"+str(threads)+"thrds.txt"), "w") as f:
            VBR_PATH = "/home/tgrogers-raid/a/das160/VBR-SpMV/Generated_MMarket"
            for filename in os.listdir(VBR_PATH):
                assert(filename.endswith(".mtx"))
                f.write(f"{filename[:-4]}")
                print(f"Running {filename[:-4]} with {threads} threads")
                output = subprocess.check_output(["python3", "run_matrix.py", "-m", os.path.join(VBR_PATH, filename), "-t", str(threads), "-b", "512", "-o", "temp.csv"]).decode("utf-8").split("\n")[-2]
                f.write(","+extract_number(output))
                print(f"{extract_number(output)}")
                f.write("\n")