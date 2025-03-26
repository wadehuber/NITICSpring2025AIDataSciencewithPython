# Our training data
data = [
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'Yes'},
    {'Hot': 'Yes', 'Money': 'No',  'Free': 'No',  'Spam': 'Yes'},
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'No'},
    {'Hot': 'Yes', 'Money': 'Yes', 'Free': 'No',  'Spam': 'Yes'},
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'No'}
]

# Step 1: Count spam and non-spam emails
total_emails = len(data)
spam_count = sum(1 for email in data if email['Spam'] == 'Yes')  # Number of spam emails
not_spam_count = total_emails - spam_count  # Number of non-spam emails

# Prior probabilities
p_spam_yes = spam_count / total_emails  # P(Spam = "Yes")
p_spam_no = not_spam_count / total_emails  # P(Spam = "No")

# Step 2: Function to calculate likelihoods for a word
def calc_likelihood(word, value, spam_label):
    # Count how many times word=value appears in emails with given spam_label
    count = sum(1 for email in data if email[word] == value and email['Spam'] == spam_label)
    total = spam_count if spam_label == "Yes" else not_spam_count
    # Laplace smoothing: add 1 to count, 2 to total (for binary Yes/No)
    return (count + 1) / (total + 2)

# Step 3: Test example
test_email = {'Hot': 'Yes', 'Money': 'No', 'Free': 'Yes'}

# Calculate probabilities for Spam = "Yes"
spam_yes_score = p_spam_yes
spam_yes_score *= calc_likelihood('Hot', test_email['Hot'], 'Yes')
spam_yes_score *= calc_likelihood('Money', test_email['Money'], 'Yes')
spam_yes_score *= calc_likelihood('Free', test_email['Free'], 'Yes')

# Calculate probabilities for Spam = "No"
spam_no_score = p_spam_no
spam_no_score *= calc_likelihood('Hot', test_email['Hot'], 'No')
spam_no_score *= calc_likelihood('Money', test_email['Money'], 'No')
spam_no_score *= calc_likelihood('Free', test_email['Free'], 'No')

# Step 4: Print results and predict
print(f"Spam Yes Score: {spam_yes_score:.4f}")
print(f"Spam No Score: {spam_no_score:.4f}")

if spam_yes_score > spam_no_score:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")