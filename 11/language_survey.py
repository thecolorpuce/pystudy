from survey import AnonymousSurvey as AS

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AS(question)

# Show the qquestion, and store responses to the question.  

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show survey results.
print("\nThank you to everyone that participated in this survey")
my_survey.show_results()