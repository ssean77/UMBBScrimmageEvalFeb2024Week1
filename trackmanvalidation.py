import pandas as pd
import matplotlib.pyplot as plt

def loadData():
    df203 = pd.read_csv('TrackmanValidation/20240203-UofMiami-Private-1_unverified_playerpositioning.csv', usecols=['PlayID', '1B_PositionAtReleaseX', '1B_PositionAtReleaseZ', '2B_PositionAtReleaseX', '2B_PositionAtReleaseZ', 
                                                                                                '3B_PositionAtReleaseX', '3B_PositionAtReleaseZ', 'SS_PositionAtReleaseX', 'SS_PositionAtReleaseZ', 'LF_PositionAtReleaseX', 
                                                                                                'LF_PositionAtReleaseZ', 'CF_PositionAtReleaseX', 'CF_PositionAtReleaseZ', 'RF_PositionAtReleaseX', 'RF_PositionAtReleaseZ'])
    df204 = pd.read_csv('TrackmanValidation/20240204-UofMiami-Private-1_unverified_playerpositioning.csv', usecols=['PlayID', '1B_PositionAtReleaseX', '1B_PositionAtReleaseZ', '2B_PositionAtReleaseX', '2B_PositionAtReleaseZ', 
                                                                                                '3B_PositionAtReleaseX', '3B_PositionAtReleaseZ', 'SS_PositionAtReleaseX', 'SS_PositionAtReleaseZ', 'LF_PositionAtReleaseX', 
                                                                                                'LF_PositionAtReleaseZ', 'CF_PositionAtReleaseX', 'CF_PositionAtReleaseZ', 'RF_PositionAtReleaseX', 'RF_PositionAtReleaseZ'])
    
    return df203, df204

def computePoints(df203, df204):

    userChoiceOfDay = input("\nFor what day would you like the player visualization for: Feb3 or Feb4? ")

    if userChoiceOfDay == "Feb3":
        
        firstBase203X = df203['1B_PositionAtReleaseX'].tolist() # converts the column into a list
        firstBase203Z = df203['1B_PositionAtReleaseZ'].tolist()
        
        secondBase203X = df203['2B_PositionAtReleaseX'].tolist()
        secondBase203Z = df203['2B_PositionAtReleaseZ'].tolist()
        
        shortstop203X = df203['SS_PositionAtReleaseX'].tolist()
        shortstop203Z = df203['SS_PositionAtReleaseZ'].tolist()
        
        thirdBase203X = df203['3B_PositionAtReleaseX'].tolist()
        thirdBase203Z = df203['3B_PositionAtReleaseZ'].tolist()
        
        rightField203X = df203['RF_PositionAtReleaseX'].tolist()
        rightField203Z = df203['RF_PositionAtReleaseZ'].tolist()
        
        centerField203X = df203['CF_PositionAtReleaseX'].tolist()
        centerField203Z = df203['CF_PositionAtReleaseZ'].tolist()
        
        leftField203X = df203['LF_PositionAtReleaseX'].tolist()
        leftField203Z = df203['LF_PositionAtReleaseZ'].tolist()
        
        graphPoints = [firstBase203X, firstBase203Z, secondBase203X, secondBase203Z, 
                   shortstop203X, shortstop203Z, thirdBase203X, thirdBase203Z, leftField203X, 
                   leftField203Z, centerField203X, centerField203Z, rightField203X, rightField203Z]
        
        return graphPoints

    elif userChoiceOfDay == "Feb4":

        firstBase204X = df204['1B_PositionAtReleaseX'].tolist() # converts the column into a list
        firstBase204Z = df204['1B_PositionAtReleaseZ'].tolist()
        
        secondBase204X = df204['2B_PositionAtReleaseX'].tolist()
        secondBase204Z = df204['2B_PositionAtReleaseZ'].tolist()
        
        shortstop204X = df204['SS_PositionAtReleaseX'].tolist()
        shortstop204Z = df204['SS_PositionAtReleaseZ'].tolist()
        
        thirdBase204X = df204['3B_PositionAtReleaseX'].tolist()
        thirdBase204Z = df204['3B_PositionAtReleaseZ'].tolist()
        
        rightField204X = df204['RF_PositionAtReleaseX'].tolist()
        rightField204Z = df204['RF_PositionAtReleaseZ'].tolist()
        
        centerField204X = df204['CF_PositionAtReleaseX'].tolist()
        centerField204Z = df204['CF_PositionAtReleaseZ'].tolist()
        
        leftField204X = df204['LF_PositionAtReleaseX'].tolist()
        leftField204Z = df204['LF_PositionAtReleaseZ'].tolist()
        
        graphPoints = [firstBase204X, firstBase204Z, secondBase204X, secondBase204Z, 
                   shortstop204X, shortstop204Z, thirdBase204X, thirdBase204Z, leftField204X, 
                   leftField204Z, centerField204X, centerField204Z, rightField204X, rightField204Z]
        
        return graphPoints
    
    else: 
        continueOption = input("\nInvalid date entered. Would you like to try again (Y/N)? ")
        
        if continueOption == 'N':
            return 0
        else:
            computePoints(df203, df204)


def processDiamond(graphPoints):
    
    # Create the scatter plot
    
    plt.scatter(graphPoints[1], graphPoints[0]) # x,y. Remember that our Z's behave like X's and our X's behave like Y's
    plt.scatter(graphPoints[3], graphPoints[2])
    plt.scatter(graphPoints[5], graphPoints[4])
    plt.scatter(graphPoints[7], graphPoints[6])
    plt.scatter(graphPoints[9], graphPoints[8])
    plt.scatter(graphPoints[11], graphPoints[10])
    plt.scatter(graphPoints[13], graphPoints[12])

    plt.scatter(0, 0, color='black') # home plate (catcher)
    
    plt.title('Baseball Diamond')
    
    # Display the plot
    plt.show()

def main():

    df203, df204 = loadData()

    graphPoints = computePoints(df203, df204)

    if graphPoints == 0:
        return

    processDiamond(graphPoints)

if __name__ == "__main__":
    main()