import re

import os
 
# Get the list of all files and directories
path = "./forms/"
dir_list = os.listdir(path)

def read_python_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# code_block = """
# if slot == "ask_followup_question":
#     if trail_count is None:
#         trail_count = 0
#         dispatcher.utter_template("utter_follow_up_for_health_issue_affirm_"+variation+loan_category+emi_flow+"_static"+SRP+bot_gender, tracker,monthly_emi = emi_amount,monthly_emi_date = due_date)
#         send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_id="PDR")
#     else:
#         dispatcher.utter_template("utter_follow_up_for_health_issue_affirm_"+variation+loan_category+emi_flow+"_static"+SRP+bot_gender, tracker,monthly_emi = emi_amount,monthly_emi_date = due_date)
#         send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG)
#     return [
#         FollowupAction("action_listen"),
#         SlotSet(REQUESTED_SLOT, slot),
#         SlotSet("timestamp", time.time()),
#         SlotSet("trail_count", trail_count + 1),
#     ]
# """

# Define the regex pattern
pattern = r'"utter_[^"]*"'
output_file_path = "./response_forms.txt"



# Recursively go through all subfolders and files
for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            code_block = read_file(file_path)

            # Find all utter patterns
            matches = re.findall(pattern, code_block)
            unique_matches = sorted(set(matches))

            # Write to output file
            with open(output_file_path, 'a') as output_file:
                for match in unique_matches:
                    print(match)
                    output_file.write(match + '\n')
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")



#  Read the file inside a folder
# for file in dir_list:
#     o_path = os.path.join(path, file)
#     code_block = read_python_file(o_path)

#     # Find all matches
#     matches = re.findall(pattern, code_block)
#     unique_matches = sorted(set(matches)) 


#     # Print the unique_matches
#     for match in unique_matches:
#         print(match)
#         match = match + '\n'
#         with open(output_file_path, 'a') as output_file:
#             output_file.write(match)
