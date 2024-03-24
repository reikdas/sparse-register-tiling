import subprocess
import os

if __name__ == "__main__":
    for threads in [1, 2, 4, 8, 16]:
        with open(os.path.join("results", "bench_executor_"+str(threads)+"thrds.csv"), "w") as f:
            VBR_PATH = "/home/tgrogers-raid/a/das160/VBR-SpMV/Generated_MMarket"
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
