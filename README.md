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

To use the `Mask` class, create an instance and call the `mask` method with your input text and desired format. The default format is `txt`, so you don't need to pass format parameter if input data is simple text:

```python
masker = Mask()
# Mask Json Data
masked_json = masker.mask(input_data='{"phone" : "(988) 888 9821"}',format='json')
print("Masked Json: " + masked_json)

# Mask text
masked_text = masker.mask(input_data='My name is John Doe and I live in Canada.')
print("Masked Text: " + masked_text)
```
