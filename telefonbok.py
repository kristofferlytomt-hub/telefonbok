telefonbok = []
person1 = {
    "navn" : "gabriel",
    "nummer" : "41311273"
}
person2 = {
    "navn" : "sebastian",
    "nummer" : "47955824"
}
telefonbok.append(person1)
telefonbok.append(person2)

def vis_alle():
    for human_being in telefonbok:
        print(human_being["navn"], ": ", human_being["nummer"])
vis_alle()