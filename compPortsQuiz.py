# Quiz yourself on common ports and their corresponding protocols
import random
import sys

def portNumQuestions():
    # Port number quiz
    print()
    score = 0
    # score keeps track of correct answers
    incorrectAnswers = []
    # list of answers that were incorrect for further studying
    QnA = [["FTP (enter answer as port1/port2)", "20/21"], ["SSH", "22"], ["Telnet","23"], ["SMTP", "25"], ["DNS", "53"], ["DHCP (enter answer as port1/port2)", "67/68"], ["HTTP","80"],
    ["POP3", "110"],["NTP", "123"],["IMAP", "143"], ["SNMP", "161"], ["LDAP", "389"], ["SSL/TLS(HTTPS)", "443"], ["SMB", "445"],["Syslog", "514"],["MySQL", "3306"], ["RDP", "3389"]]
    print("For the given protocol, answer with the correct port number(s)")
    random.shuffle(QnA)
    # questions are randomized to prevent memorizing the order rather than the port/protocol
    for Q in range(0, len(QnA)):
        print(QnA[Q][0])
        A = input("Enter the correct port number: ")
        if A == QnA[Q][1]:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            incorrectAnswers.append(QnA[Q])
        print()
    print("Final Score:", score)
    if len(incorrectAnswers) != 0:
        print("Incorrect Answers:")
        for wrong in range(0, len(incorrectAnswers)):
            print(incorrectAnswers[wrong][0], incorrectAnswers[wrong][1])
    print()


def protocolQuestions():
    # Protocol quiz, follows the same format as the port number function
    print()
    score = 0
    incorrectAnswers = []
    QnA = [["20/21","FTP"], ["22","SSH"], ["23","TELNET"], ["25","SMTP"], ["53", "DNS"], ["67/68", "DHCP"], ["80","HTTP"],["110", "POP3"],
    ["123", "NTP"],["143", "IMAP"], ["161","SNMP"], ["389","LDAP"], ["443","HTTPS"], ["445","SMB"],["514", "Syslog"],["3306", "MySQL"], ["3389","RDP"]]
    print("For the given port number, answer with the correct protocol")
    random.shuffle(QnA)
    for Q in range(0, len(QnA)):
        print(QnA[Q][0])
        A = input("Enter the correct protocol: ")
        if A.upper() == QnA[Q][1]:
            print("Correct")
            score += 1
        elif A.upper() != QnA[Q][1]:
            print("Incorrect")
            incorrectAnswers.append(QnA[Q])
        print()
    print("Final Score:", score)
    if len(incorrectAnswers) != 0:
        print("Incorrect Answers:")
        for wrong in range(0, len(incorrectAnswers)):
            print(incorrectAnswers[wrong][0], incorrectAnswers[wrong][1])
    print()


def main():
    options = ["A) Port Numbers", "B) Protocols", "Q) Quit"]
    print()
    print("Welcome to the port and protocol quiz!")
    print()
    choice = ''
    while choice.lower() != 'q':
        # display options menu and take valid input until user chooses to quit program
        for option in options:
            print(option)
        choice = input("Please choose from the above options: ")
        if choice.lower() == 'q':
            print("Goodbye!")
            sys.exit()
        elif choice.lower() == 'a':
            portNumQuestions()
        elif choice.lower() == 'b':
            protocolQuestions()
        else:
            print("That is not a valid option")
            print()


if __name__ == '__main__':
main()
