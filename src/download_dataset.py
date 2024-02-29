from datasets import load_dataset

cv_13 = load_dataset("mozilla-foundation/common_voice_13_0", "ru",
                     split="test", use_auth_token=True)
cv_13.save_to_disk('../data/test')
