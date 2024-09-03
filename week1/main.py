from datasets import load_dataset

# Load dataset
dataset = load_dataset("coastalcph/tydi_xor_rc")

# Summarize basic statistics
def summarize_statistics(lang):
    train_data = dataset['train'].filter(lambda x: x['language'] == lang)
    val_data = dataset['validation'].filter(lambda x: x['language'] == lang)
    
    # Training data stats
    num_train = len(train_data)
    num_unanswerable_train = sum(train_data['is_impossible'])
    avg_question_len_train = sum(len(q.split()) for q in train_data['question']) / num_train
    avg_context_len_train = sum(len(c.split()) for c in train_data['context']) / num_train

    # Validation data stats
    num_val = len(val_data)
    num_unanswerable_val = sum(val_data['is_impossible'])
    avg_question_len_val = sum(len(q.split()) for q in val_data['question']) / num_val
    avg_context_len_val = sum(len(c.split()) for c in val_data['context']) / num_val

    print(f"Language: {lang}")
    print(f"Train: {num_train} examples, {num_unanswerable_train} unanswerable, Avg. Q len: {avg_question_len_train}, Avg. C len: {avg_context_len_train}")
    print(f"Validation: {num_val} examples, {num_unanswerable_val} unanswerable, Avg. Q len: {avg_question_len_val}, Avg. C len: {avg_context_len_val}")

for lang in ['fi', 'ja', 'ru']:
    summarize_statistics(lang)

