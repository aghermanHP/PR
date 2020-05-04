import argparse
from modules import index

parser = argparse.ArgumentParser(description='Process http methods')
parser.add_argument("-getCats", action="store_true", help="getCats Method")
parser.add_argument("-getVotes", action="store_true", help="get Votes of cats")
parser.add_argument("-options", action="store_true", help="options of cats")
parser.add_argument("-head", action="store_true", help="HEAD of cats")
parser.add_argument("-delete", type=int, help="delete an vote -d [voteId]")
parser.add_argument("-post", nargs='+', help="-post [image_id] [0 or 1] \n 0 for minus vot 1 for + vote")
args = parser.parse_args()
methods = index.MethodsForCat()

if args.getCats:
    x = methods.get_cats()
    print(x)
elif args.getVotes:
    x = methods.get_votes()
    print(x)
elif args.options:
    x = methods.options_cats()
    print(x)
elif args.delete:
    x = methods.delete_vote(int(args.delete))
    print(x)
elif args.head:
    x = methods.head_votes()
    print(x)
elif args.post:
    x = methods.post_vote(args.post[0], int(args.post[1]))
    print(x)



