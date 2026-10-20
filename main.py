from pyscript import display, document

def bagongM (e):
    document.getElementById('output1').innerHTML = ""
    group1 = {"Joy Manawari", "Hector Samala", "Emman Azarcon", "Anthony Cruz"}
    group2 = {"Troy Bolton", "Gabriella Montez", "Sharpay Evans", "Ryan Evans"} 
    group3 = {"Mark Cohen", "Roger Davis", "Mimi Márquez", "Maureen Johnson"}
    group4 = {"Alexander Hamilton", "Eliza Schuyler", "Angelica Schuyler", "Peggy Schuyler"}

    # Curly brackets indicate that we want to push the code to beconme a set
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    # Assigns the value to set variables
    new_member = {fname + " " + lname}

    all_members = group1 | group2 | group3 | group4 | new_member

    total_members = len(group1 | group2 | group3 | group4 | new_member)

    member_list = "<br>".join(sorted(all_members))

    # Display
    document.getElementById('output1').innerHTML = f'Lahat ng Miyembro: <br> {member_list}'
    display(f'Bilang ng Miyembro: {total_members}', target="output1")

