from mask import Mask

if __name__ == "__main__":
    mask_pii = Mask()
    try:
        # Mask Json Data
        masked_json = mask_pii.mask(input_data='{"phone" : "(988) 888 9821"}',format='json')
        print("Masked Json: " + masked_json)

        # Mask text
        masked_text = mask_pii.mask(input_data='My name is John Doe and I live in Canada.')
        print("Masked Text: " + masked_text)
    except Exception as e:
        print(e)