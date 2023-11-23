from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime
import pandas as pd

root = Tk()
root.title("Add refugee")
root.geometry("450x500")

'''
# Create a csv file to store information of refugees
info = {
    "refugeeID": [],
    "familySize": [],
    "firstName": [],
    "lastName": [],
    "phoneNumber": [],
    "minor": [],
    "senior": [],
    "pregnancy": [],
    "arrivalDate": [],
    "departureDate": [],
    "status": [],
    "healthCondition": [],
    "description": []
}
df = pd.DataFrame(info)
df.to_csv('/Users/bixueying/Desktop/Volunteer/CAMP_1_REFUGEES.csv', index=False)
'''
df = pd.read_csv('/Users/bixueying/Desktop/Volunteer/CAMP_1_REFUGEES.csv')

def check_family_size(event):
    # Verify whether the user input for family size is a valid integer when the user clicks the add button.
    family_size_error_label.config(text="")
    user_input = family_size.get()
    try:
        value = int(user_input)
        if 1 <= value <= 15:
            # family_size_error_label.grid_forget()
            return True
        else:
            family_size_error_label.config(text="Please enter an integer between 1 and 15.")
    except ValueError:
        family_size_error_label.config(text="Please enter a valid integer.")
    return False

def check_first_name(event):
    # Verify whether the user input for first name alraedy in file when the user clicks the add button.
    f_name_error_label.config(text="")
    user_input = f_name.get()
    try:
      user_data = pd.read_csv('/Users/bixueying/Desktop/Volunteer/CAMP_1_REFUGEES.csv')
      if user_input in user_data["firstName"].values:
       print(f_name_error_label.config(text="Error. First name already existsed."))
      else:
       return True
    except:      
        return False

def check_phone_number(event):
    # Verify whether the phone number is in correct format.
    phone_number_error_label.config(text = "")
    PN = phone_number.get()
    try:
        value = str(int(PN))
        if len(value) >= 7 and len(value )<= 14:
            return True
        else:
            phone_number_error_label.config(text="Error. Please enter in 7-digit to 14-digit format.")
    except ValueError:
        phone_number_error_label.config(text = "Please enter numbers.")
        
 
def check_description(value):
    # Verify whether the description is within max characters.
 
    description_error_label.config(text = "")
    description_input = description.get("1.0","end-1c")
    breaks = description_input.count('\n')
    char_count = len(description_input) - breaks
    description_error_label.config(text="Total Characters: " + str(char_count) + "; Maximum Characters: 100")
    if char_count > 99:
            description.delete('end-2c')

def add():
     if check_family_size(None):
        global df
        if df.empty:
            refugee_id = 1         
        else:
            refugee_id = df['refugeeID'].max() + 1

        new_refugee = pd.Series({
            'refugeeID': refugee_id,
            'familySize': int(family_size.get()),
            'firstName': f_name.get(),
            'lastName': l_name.get(),
            'phoneNumber': phone_number.get(),
            'arrivalDate': arr_date.get(),
            'description': description.get("1.0", "end-1c")
            })

            
        df = pd.concat([df, pd.DataFrame([new_refugee])], ignore_index=True)
        df.to_csv('/Users/bixueying/Desktop/Volunteer/CAMP_1_REFUGEES.csv', index=False)
        root.destroy()
        return
    



# Create text boxes and label widgets for displaying error messages
family_size = Spinbox(root, from_=1, to=10, width=23)
family_size.grid(row=0, column=1, padx=10, pady=(10, 0))
family_size.bind('<FocusOut>', check_family_size)
family_size_required_label = Label(root, text="* Required.", font=("Helvetica", 10), fg="red", padx=10)
family_size_required_label.grid(row=1, column=1, sticky="w")
family_size_error_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
family_size_error_label.grid(row=2, column=1, sticky="w")

f_name = Entry(root, width=25)
f_name.grid(row=3, column=1, padx=10)
f_name.bind('<FocusOut>', check_first_name)
f_name_required_label = Label(root, text="* Required.", font=("Helvetica", 10), fg="red", padx=10)
f_name_required_label.grid(row=4, column=1, sticky="w")
f_name_error_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
f_name_error_label.grid(row=5, column=1, sticky="w")

l_name = Entry(root, width=25)
l_name.grid(row=6, column=1, padx=10)
l_name_required_label = Label(root, text="* Required.", font=("Helvetica", 10), fg="red", padx=10)
l_name_required_label.grid(row=7, column=1, sticky="w")
l_name_error_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
l_name_error_label.grid(row=8, column=1, sticky="w")

phone_number = Entry(root, width=25)
phone_number.grid(row=9, column=1, padx=10)
phone_number.bind('<FocusOut>', check_phone_number)
phone_number_required_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
phone_number_required_label.grid(row=10, column=1, sticky="w")
phone_number_error_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
phone_number_error_label.grid(row=11, column=1, sticky="w")

# Create a text box for the arrival date with the default set to the current date
current_date = datetime.now().strftime('%Y-%m-%d')
arr_date = Entry(root, width=25)
arr_date.insert(0, current_date)
arr_date.grid(row=12, column=1, padx=10)
arr_date_required_label = Label(root, text="* Required. e.g. 2023-11-12", font=("Helvetica", 10), fg="red", padx=10)
arr_date_required_label.grid(row=13, column=1, sticky="w")
arr_date_error_label = Label(root, text="Format should be YYYY-MM-DD.", font=("Helvetica", 10), fg="red", padx=10)
arr_date_error_label.grid(row=14, column=1, sticky="w")

description = Text(root, wrap="word", width=30, height=10)
description.grid(row=15, column=1, padx=10)
description.bind('<KeyRelease>', check_description)
description_required_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
description_required_label.grid(row=16, column=1, sticky="w")
description_error_label = Label(root, text="", font=("Helvetica", 10), fg="red", padx=10)
description_error_label.grid(row=17, column=1, sticky="w")

# Create Text Box Labels
family_size_label = Label(root, text="Family size")
family_size_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(root, text="First name")
f_name_label.grid(row=3, column=0)
l_name_label = Label(root, text="Last name")
l_name_label.grid(row=6, column=0)
phone_number_label = Label(root, text="Contact phone number", padx=10)
phone_number_label.grid(row=9, column=0)
arr_date_label = Label(root, text="Date of arrival")
arr_date_label.grid(row=12, column=0)
description_label = Label(root, text="Description")
description_label.grid(row=15, column=0, sticky="n")

# Create Submit Button
add_btn = Button(root, text="Add", command=add)
add_btn.grid(row=18, column=0, columnspan=2, padx=10)

root.mainloop()