questions_read = open("questions.txt", "r")

all_questions = [q.strip() for q in questions_read.readlines()]

questions_read.close()

count_corr_ans = 0

for each_question in all_questions:
    quest_ans = each_question.split("=")
    ques = quest_ans[0]
    answer_sheet = quest_ans[1]
    print(f"Question: {ques} ?")
    user_answer = input("Please type your answer for above question: ")

    if user_answer == answer_sheet:
        count_corr_ans = count_corr_ans + 1

num_ques = len(all_questions)
msg = "Your final score is {}/{}".format(count_corr_ans, num_ques)
print(msg)


user_results_write = open("result_exercise14.txt", "w")
user_results_write.write(msg)
user_results_write.close()
#print(all_questions)