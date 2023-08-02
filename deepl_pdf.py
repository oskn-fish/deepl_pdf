import deepl
import argparse
import subprocess
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")    
    parser.add_argument("-o", "--output")
    parser.add_argument("-l", "--language")
    args = parser.parse_args()
    if not args.language:
        args.language = "JA"
    if not args.output:
        to_ext, ext = os.path.splitext(args.input)
        args.output = to_ext+"_"+args.language.lower()+ext
    return args


def main():
    with open("./auth_key.txt") as f:
        auth_key = f.read()
    
    translator = deepl.Translator(auth_key)
    args = get_args()
    
    try:
        with open(args.input, "rb") as in_file, open(args.output, "wb") as out_file:
            translator.translate_document(in_file, out_file, target_lang=args.language, formality="more")
        subprocess.run(f"open \"{args.output}\"")
            
    except deepl.DocumentTranslationException as error:
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
        
    except deepl.DeepLException as error:
        print(error)


if __name__ == "__main__":
    main()