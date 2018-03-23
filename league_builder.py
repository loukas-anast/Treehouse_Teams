import csv

def main():
    with open("soccer_players.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        result = {"Sharks": [], "Dragons": [], "Raptors": []}
        i = 1
        j = 1

        for row in reader:
            #add experienced players evenly
            if "YES" in row:
                if i % 3 != 0 and i % 2 != 0:
                    result["Sharks"].append(", ".join(row))
                elif i % 3 == 0:
                    result["Raptors"].append(", ".join(row))
                else:
                    result["Dragons"].append(", ".join(row))

                i += 1
            #add  the rest of the players
            elif "NO" in row:
                if j % 3 != 0 and j % 2 != 0:
                    result["Sharks"].append(", ".join(row))
                elif j % 3 == 0:
                    result["Raptors"].append(", ".join(row))
                else:
                    result["Dragons"].append(", ".join(row))

                j += 1

            with open("teams.txt", "w+") as file:
                file.write("Sharks\n")

                for p in result["Sharks"]:
                    file.write(p + "\n")

                file.write("\nDragons\n")

                for p in result["Dragons"]:
                    file.write(p + "\n")

                file.write("\nRaptors\n")

                for p in result["Raptors"]:
                    file.write(p + "\n")

        file.close()
        print(result)

if __name__ == "__main__":
    main()