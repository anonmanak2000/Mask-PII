# PII Masking Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Spacy](https://img.shields.io/badge/Spacy-3.0%2B-green.svg)
![Re](https://img.shields.io/badge/Regex-Enabled-yellow.svg)

## Overview

The PII Masking Tool is designed to help mask Personally Identifiable Information (PII) such as phone numbers, email addresses, and IP addresses in text documents. It uses regular expressions and the SpaCy library for Named Entity Recognition (NER) to identify and redact sensitive information.

## Installation

To get started with the PII Masking Tool, ensure you have Python 3.8 or higher installed. Then, install the required libraries:

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Example

To use the `Mask` class, create an instance and call the `mask_text` method with your input text:

```python
masker = Mask()
masked_text = masker.mask_text("Contact me at john.doe@example.com or call me at (555) 123-4567.")
print(masked_text)
```
## Using the `mask_file` Method

The `mask_file` method allows you to read a text file, mask any PII present, and return the masked content. Here’s how to use it:

### Example

1. Create a text file (e.g., `example.txt`) with the following content:
```bash
Please reach out to me at jane.doe@example.com or at (555) 987-6543.
```
2. Use the `mask_file` method to mask the PII in the file:

```python
masker = Mask()
masked_file_text = masker.mask_file("example.txt")
print(masked_file_text)
```

