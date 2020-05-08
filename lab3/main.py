import argparse
import requests
from modules import index
from modules import facebook

parser = argparse.ArgumentParser(description='Process http methods')
parser.add_argument('-email', type=str, help='Email address')
parser.add_argument('-password', type=str, help='Login password')
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
elif args.email and args.password:
    proxies = {
        'http': '192.168.1.105:3128',
        'https': '192.168.1.105:3128',
    }
    session = requests.session()
    session.proxies = proxies
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
    })

    fb_dtsg, user_id, xs = facebook.login(session, args.email, args.password)

    if user_id:
        print('Facebook:{0}:{1}:{2}'.format(fb_dtsg, user_id, xs))
    else:
        print('Login Failed')



