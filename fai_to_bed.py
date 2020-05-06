import sys

if __name__ == "__main__":

    finame = sys.argv[1]

    print("Getting names from " + finame)
    bname = finame.rstrip(".fai").rstrip(".fasta").rstrip(".fna").rstrip(".fa")

    with open(finame, "r") as ifi, \
    open(bname + ".chrom.names.txt", "w") as namefi, \
    open(bname + ".chrom.bed", "w") as bedfi:
        for line in ifi:
            tokens = line.strip().split("\t")
            namefi.write(tokens[0] + "\n")
            bedfi.write("\t".join([tokens[0], "0", tokens[1]]) + "\n")


