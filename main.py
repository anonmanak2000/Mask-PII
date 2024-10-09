from mask import Mask

if __name__ == "__main__":
    mask_pii = Mask()
    try:
        masked_text = mask_pii.mask_file('file.txt')
        print("Masked Text: " + masked_text)
    except:
        print('Unexpected error!!')