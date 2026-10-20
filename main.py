from pyscript import display, document

def add_brand (e):
    document.getElementById('output1').innerHTML = ""
    members1 = {"Joy Manawari", "Hector Samala", "Emman Azarcon", "Anthony Cruz"}
    members2 = {"Troy Bolton", "Gabriella Montez", "Sharpay Evans", "Ryan Evans"} 
    members3 = {"Mark Cohen", "Roger Davis", "Mimi Márquez", "Maureen Johnson"}
    members4 = {"Alexander Hamilton", "Eliza Schuyler", "Angelica Schuyler", "Peggy Schuyler"}

   
     # Curly brackets indicate that we want to push the code to beconme a set
    fname = (document.getElementById("fname").value)
    lname = (document.getElementById("lname").value)
    # Assigns the value to set variables
    new_member = fname + " " + lname

    all_members = brands | new_brand_set

    total_members = len(members | new_member)

    member_list = "<br>".join(sorted(all_members))

    # Display
    document.getElementById('output1').innerHTML = f'All members: <br> {member_list}'
    display(f'Total members: {total_members}', target="output1")
