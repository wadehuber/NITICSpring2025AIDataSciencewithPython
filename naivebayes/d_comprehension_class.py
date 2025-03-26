class NaiveBayesClassifier:
    def __init__(self, data):
        """Set up the classifier with training data."""
        self.data = data
        self.total_emails = len(data)
        
        # Count spam and non-spam emails
        self.spam_count = 0
        self.not_spam_count = 0
        for email in data:
            if email['Spam'] == 'Yes':
                self.spam_count += 1
            else:
                self.not_spam_count += 1
        
        # Calculate prior probabilities
        self.p_spam_yes = self.spam_count / self.total_emails
        self.p_spam_no = self.not_spam_count / self.total_emails

    def calc_likelihood(self, word, value, spam_label):
        """Figure out how likely a word is in spam or non-spam emails."""
        # Count how many emails match our word and spam label
        matching_count = 0
        for email in self.data:
            # Check if this email has the word=value AND the right spam label
            if email[word] == value and email['Spam'] == spam_label:
                matching_count += 1
        
        # Decide total based on spam or non-spam
        if spam_label == "Yes":
            total_emails_in_group = self.spam_count
        else:
            total_emails_in_group = self.not_spam_count
        
        # Use Laplace smoothing: add 1 to count and 2 to total
        smoothed_count = matching_count + 1
        smoothed_total = total_emails_in_group + 2
        
        # Calculate the probability
        probability = smoothed_count / smoothed_total
        return probability

    def predict(self, email):
        """Guess if a new email is spam or not."""
        # Start with the basic chances of spam or not
        spam_yes_score = self.p_spam_yes
        spam_no_score = self.p_spam_no
        
        # Check each word and update scores
        words_to_check = ['Hot', 'Money', 'Free']
        for word in words_to_check:
            # Get the value of this word in the new email (Yes or No)
            word_value = email[word]
            # Multiply by the likelihood for spam and non-spam
            spam_yes_score = spam_yes_score * self.calc_likelihood(word, word_value, 'Yes')
            spam_no_score = spam_no_score * self.calc_likelihood(word, word_value, 'No')
        
        # Show the scores
        print(f"Spam Yes Score: {spam_yes_score:.4f}")
        print(f"Spam No Score: {spam_no_score:.4f}")
        
        # Decide which is more likely
        if spam_yes_score > spam_no_score:
            return "Spam"
        else:
            return "Not Spam"

# Training data
data = [
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'Yes'},
    {'Hot': 'Yes', 'Money': 'No',  'Free': 'No',  'Spam': 'Yes'},
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'No'},
    {'Hot': 'Yes', 'Money': 'Yes', 'Free': 'No',  'Spam': 'Yes'},
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'No'}
]

# Create and use the classifier
classifier = NaiveBayesClassifier(data)

# Test some emails
test_email = {'Hot': 'Yes', 'Money': 'No', 'Free': 'Yes'}
prediction = classifier.predict(test_email)
print(f"Prediction: {prediction}")

test_email2 = {'Hot': 'No', 'Money': 'Yes', 'Free': 'No'}
prediction2 = classifier.predict(test_email2)
print(f"Prediction: {prediction2}")
