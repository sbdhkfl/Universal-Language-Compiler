import argparse
from core.translator import translate
from core.errors import TranslationError
from targets import NAMES

def main():
    parser=argparse.ArgumentParser(description="Universal Language Compiler")
    sub=parser.add_subparsers(dest="command",required=True)
    t=sub.add_parser("translate",help="Translate a natural-language instruction")
    t.add_argument("text")
    t.add_argument("--target",required=True,choices=sorted(set(NAMES)))
    args=parser.parse_args()
    try: print(translate(args.text,args.target),end="")
    except (TranslationError,ValueError) as exc: parser.error(str(exc))

if __name__=="__main__": main()
