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

    # may not have to include this

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


def processDiamond(graphPoints):
    
    # Create the scatter plot
    
    plt.scatter(graphPoints[1], graphPoints[0]) # x,y. Remember that our Z's behave like X's and our X's behave like Y's
    plt.scatter(graphPoints[3], graphPoints[2])
    plt.scatter(graphPoints[5], graphPoints[4])
    plt.scatter(graphPoints[7], graphPoints[6])
    plt.scatter(graphPoints[9], graphPoints[8])
    plt.scatter(graphPoints[11], graphPoints[10])
    plt.scatter(graphPoints[13], graphPoints[12])

    plt.scatter(0, 0, color='red') # home plate (catcher)
    
    plt.title('Baseball Diamond')
    
    # Display the plot
    plt.show()

def main():

    df203, df204 = loadData()

    graphPoints = computePoints(df203, df204)

    processDiamond(graphPoints)

if __name__ == "__main__":
    main()