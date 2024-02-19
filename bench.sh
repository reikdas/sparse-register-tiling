#!/bin/bash

# Function to extract number from a string
extract_number() {
    local input_string="$1"
    # Using grep and sed to extract the first occurrence of a floating point number
    echo "$input_string" | grep -oE "\d+\.\d+" | head -1
}

VBR_PATH="/home/tgrogers-raid/a/das160/VBR-SpMV/Generated_MMarket"

# Loop through 1 and 16 threads
for threads in 1 16; do
    # Prepare the output file path
    output_file="results/bench_${threads}thrds.txt"
    # Ensure the directory exists
    mkdir -p $(dirname "$output_file")
    # Open the output file for writing
    exec 3>"$output_file"

    # Loop through .mtx files in the VBR_PATH
    # for filename in "$VBR_PATH"/*.mtx; do
    for filename in "$VBR_PATH"/"Matrix_10000_10000_50_50_500_0_uniform.mtx"; do
        # Extract the base name without the .mtx extension
        base_name=$(basename "$filename" .mtx)
        echo "Running $base_name with $threads threads"
        # Write the base name to the file
        echo -n "${base_name}," >&3

        # Run the matrix operation and capture the output
        output=$(python3 run_matrix.py -m "$filename" -t "$threads" -b 512 -o temp.csv)
        # Extract the last but one line from the output, which is assumed to contain the number
        last_but_one_line=$(echo "$output" | tail -2 | head -1)
        echo "HOHO"
        echo "$last_but_one_line"
        echo "HAHA"
        # Extract the number from the line
        number=$(extract_number "$last_but_one_line")
        echo "$number"
        # Write the number to the file
        echo "$number" >&3
    done

    # Close the output file descriptor
    exec 3>&-
done
