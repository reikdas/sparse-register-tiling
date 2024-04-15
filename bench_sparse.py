import subprocess
import os
import pathlib

FILEPATH = pathlib.Path(__file__).resolve().parent
BASE_PATH = os.path.join(FILEPATH, "..", "..")

if __name__ == "__main__":
    for threads in [1]:
        with open(os.path.join("results", "bench_executor_"+str(threads)+"thrds_rel.csv"), "w") as f:
            VBR_PATH = f"{BASE_PATH}/SABLE/Generated_MMarket_Sparse"
            for filename in os.listdir(VBR_PATH):
                assert(filename.endswith(".mtx"))
                f.write(f"{filename[:-4]}")
                print(f"Running {filename[:-4]} with {threads} threads")
                output = subprocess.check_output(["python3", "run_matrix.py", "-m", os.path.join(VBR_PATH, filename), "-t", str(threads), "-b", "512", "-o", "temp.csv"]).decode("utf-8").split("\n")
                start = -7
                for i in range(5):
                    print(f"{i}: {output[start+i]}")
                    f.write(","+output[start+i])
                f.write("\n")
