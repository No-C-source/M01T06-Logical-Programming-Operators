#Pseudocode
# Design a programme that determines the award per person in triathlon
# Assign user input for the times in minutes for all three triathlon events (swimming, cycling, running)
# Calculate the total time taken to complete the triathlon (as an output)
# Determine the award based on the total time taken to complete the triathlon
# Determine the award based on the following criteria:
# Award_provincial_colours = 0-100 #within qualifying time
# Award_provincial_half_colours = 101-105 #five minutes off from the qualifying time
# Award_provincial_scroll = 106-110 #10 minutes off from the qualifying time
# No_award = 111+ #more than 10 minutes off from the qualifying time

# Python code
time_swimming = float(input("Enter the time taken to complete the swimming event in minutes: "))
time_cycling = float(input("Enter the time taken to complete the cycling event in minutes: "))
time_running = float(input("Enter the time taken to complete the running event in minutes: "))
total_time = time_swimming + time_cycling + time_running
print(f"Total time taken to complete the triathlong: {total_time} in minutes")
if (total_time >= 0) and (total_time <= 100):
    print("Award: Provincial Colours")
elif (total_time >= 101) and (total_time <= 105):
    print("Award: Provincial Half Colours")
elif (total_time >= 106) and (total_time <= 110):
    print("Award: Provincial Scroll")
else:
    print("Award: No Award")