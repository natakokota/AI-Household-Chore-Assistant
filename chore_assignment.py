members = ''
chores  = ''
frequencyOfChores = ''
preferences = ''
availability = ''

chore0days = [0,0,0,0,0,0,0]
chore1days = [0,0,0,0,0,0,0]
chore2days = [0,0,0,0,0,0,0]
assignedMember = ["","",""] 

choresOrder = sorted(range(len(frequencyOfChores)), key=lambda i: frequencyOfChores[i])

for choreIndex in choresOrder:
    freq = frequencyOfChores[choreIndex]

    bestCandidate = -1
    bestCandidatePreferenceRank = 999

    for memberIndex in range(3):
        totalAvail = 0
        for d in range(7):
            totalAvail += availability[memberIndex][d]
        
        if totalAvail < freq:
            continue

        rank = 0
        for i in range(3):
            if preferences[memberIndex][i] == choreIndex:
                rank = i
                break

        if rank < bestCandidatePreferenceRank:
            bestCandidate = memberIndex
            bestCandidatePreferenceRank = rank

    assignedMember[choreIndex] = members[bestCandidate]

    chosenDays = []
    if freq == 7:
        for d in range(7):
            if availability[bestCandidate][d] == 1:
                chosenDays.append(d)
    else:
        for d in range(7):
            if availability[bestCandidate][d] == 1:
                chosenDays.append(d)
                if len(chosenDays) == freq:
                    break
    
    if choreIndex == 0:
        for day in chosenDays:
            chore0days[day] = 1
    elif choreIndex == 1:
        for day in chosenDays:
            chore1days[day] = 1
    else:
        for day in chosenDays:
            chore2days[day] = 1

result = {'Chore0Days': chore0days,
          'Chore1Days': chore1days,
          'Chore2Days': chore2days,
          'Assigned_Members': assignedMember}
result