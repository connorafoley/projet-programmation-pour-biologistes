#!/usr/bin/env python3
import re

print("Python Slurm Script Builder")

TIME_RE = re.compile(
    r"^(?:\d+|\d{1,6}:\d{2}|\d{1,6}:\d{2}:\d{2}|\d+-\d{1,2}(?::\d{2}(?::\d{2})?)?)$"
)

def writeslurm(name,qos,chronos,email,cpus=32,mail_type='ALL',nodes=1):
    if not TIME_RE.fullmatch(str(chronos).strip()):
        raise ValueError(
            "Invalid time format. Use MM, MM:SS, HH:MM:SS, D-HH, D-HH:MM, or D-HH:MM:SS."
        )

    if "-" in str(chronos):
        hour_part = str(chronos).split("-", 1)[1].split(":", 1)[0]
        if int(hour_part) > 23:
            raise ValueError("Invalid day-hour format: HH must be 0-23.")
    
    lines = [
        "#!/usr/bin/env bash\n",
        f"#SBATCH --job-name={name}\n",
        "#SBATCH --partition=comp01\n",
        f"#SBATCH --nodes={nodes}\n",
        f"#SBATCH --qos={qos}\n",
        f"#SBATCH --cpus-per-task={cpus}\n",
        f"#SBATCH --time={chronos}\n",
        "#SBATCH --output=%x.%j.out\n",
        "#SBATCH --error=%x.%j.err\n",
        f"#SBATCH --mail-type={mail_type}\n",
        f"#SBATCH --mail-user={email}\n",
    ]

    #def commands():

    fname = f"{name}.slurm"
    with open(fname, "w", encoding="utf-8") as file:
        file.writelines(lines)


if __name__ == "__main__":
    man = int(input("Defining mail type, cpus, nodes? If so, answer 1; if not, answer 0: "))
    if man == 0:
        writeslurm(
            name = input("Job Name: "),
            qos = input("Queue Name: "),
            chronos = input("Run time. Use MM, MM:SS, HH:MM:SS, D-HH, D-HH:MM, or D-HH:MM:SS. "),
            email = input("email: ")
        )
    elif man == 1:
        writeslurm(
            name = input("Job Name: "),
            qos = input("Queue Name: "),
            chronos = input("Run time. Use MM, MM:SS, HH:MM:SS, D-HH, D-HH:MM, or D-HH:MM:SS. "),
            email = input("email: "),
            mail_type = input("Emailtype: "),
            cpus = input("Num cpus to use per task: "),
            nodes = input("number of nodes: ")
        )
    else:
        print("You didn't answer 0 or 1!")