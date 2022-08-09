import cs50

def final_score(quaf, didCatch):
    if didCatch == 1:
        return (quaf*10) + 150
    else:
        return (quaf*10)

def main():
    goalNum = cs50.get_int("Number of times your chasers got the quaffle through a hoop: ")
    snitchCaught = cs50.get_int("Did your team's seeker catch the snitch? Enter 1 if true, 0 otherwise: ")
    score = final_score(goalNum, snitchCaught)
    print("Your team's final score is: " + str(score))

if __name__ == "__main__":
    main()
