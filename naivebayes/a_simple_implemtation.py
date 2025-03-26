# Our training data
data = [
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'Yes'},
    {'Hot': 'Yes', 'Money': 'No',  'Free': 'No',  'Spam': 'Yes'},
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'No'},
    {'Hot': 'Yes', 'Money': 'Yes', 'Free': 'No',  'Spam': 'Yes'},
    {'Hot': 'No',  'Money': 'Yes', 'Free': 'Yes', 'Spam': 'No'}
]

# Hardcoded probabilities (calculated above)
p_spam_yes = 0.6  # P(Spam = "Yes")
p_spam_no = 0.4   # P(Spam = "No")

# Likelihoods
p_hot_yes_spam_yes = 2/3
p_hot_no_spam_yes = 1/3
p_hot_yes_spam_no = 0    # Would be small with smoothing
p_hot_no_spam_no = 1.0

p_money_yes_spam_yes = 2/3
p_money_no_spam_yes = 1/3
p_money_yes_spam_no = 1.0
p_money_no_spam_no = 0    # Would be small with smoothing

p_free_yes_spam_yes = 1/3
p_free_no_spam_yes = 2/3
p_free_yes_spam_no = 1.0
p_free_no_spam_no = 0     # Would be small with smoothing

# Test example: Hot = Yes, Money = No, Free = Yes
hot = "Yes"
money = "No"
free = "Yes"

# Calculate P(Spam = Yes | Hot = Yes, Money = No, Free = Yes)
spam_yes_score = (p_spam_yes * 
                  p_hot_yes_spam_yes * 
                  p_money_no_spam_yes * 
                  p_free_yes_spam_yes)

# Calculate P(Spam = No | Hot = Yes, Money = No, Free = Yes)
spam_no_score = (p_spam_no * 
                 p_hot_yes_spam_no * 
                 p_money_no_spam_no * 
                 p_free_yes_spam_no)

# Print results
print(f"Spam Yes Score: {spam_yes_score}")
print(f"Spam No Score: {spam_no_score}")

# Decide
if spam_yes_score > spam_no_score:
    print("Prediction: Spam")
else:
    print("Prediction: Not Spam")