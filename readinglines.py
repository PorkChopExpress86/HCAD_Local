line_num = 0
with open(r"extracted_data\real_acct.txt") as f:
    for line in f:
        if line_num != 0:
            line_list = line.split("\t")
            line_num += 1
            if len(line_list) != 71:
                print(f"There are {len(line_list)} at line number {line_num}")
        else:
            line_num += 1
