class NaiveBayesClassifier:
    def __init__(self, data):
        """Initialize with training data."""
        self.data = data
        self.total_emails = len(data)
        # Count spam and non-spam emails
        self.spam_count = sum(1 for email in data if email['Spam'] == 'Yes')
        self.not_spam_count = self.total_emails - self.spam_count
        # Calculate prior probabilities
        self.p_spam_yes = self.spam_count / self.total_emails
        self.p_spam_no = self.not_spam_count / self.total_emails

    def calc_likelihood(self, word, value, spam_label):
        """Calculate P(word=value | Spam=spam_label) with smoothing."""
        count = sum(1 for email in self.data if email[word] == value and email['Spam'] == spam_label)
        total = self.spam_count if spam_label == "Yes" else self.not_spam_count
        # Laplace smoothing: add 1 to count, 2 to total (for binary Yes/No)
        return (count + 1) / (total + 2)
    
    def predict(self, email):
        """Predict if an email is spam based on its words."""
        # Start with prior probabilities
        spam_yes_score = self.p_spam_yes
        spam_no_score = self.p_spam_no

        # Multiply by likelihoods for each word
        for word in ['Hot', 'Money', 'Free']:
            spam_yes_score *= self.calc_likelihood(word, email[word], 'Yes')
            spam_no_score *= self.calc_likelihood(word, email[word], 'No')

        # Print scores for learning purposes
        print(f"Spam Yes Score: {spam_yes_score:.4f}")
        print(f"Spam No Score: {spam_no_score:.4f}")

        # Return prediction
        return "Spam" if spam_yes_score > spam_no_score else "Not Spam"
    
# Our training data
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
