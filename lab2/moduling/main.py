import http.client


class MethodsForCat:
    """:param= None
        return a method http"""
    def __init__(self):
        self.conn = http.client.HTTPSConnection("192.168.1.105", 3128)
        self.headers = {'x-api-key': "04d7aefe-8b4f-4c91-8e58-89ff6861f04a"}

    def post_vote(self, minus_plus):
        """add vote or minus vote"""
        self.conn.set_tunnel("api.thecatapi.com")

        payload = "{\"image_id\":\"asf2\",\"sub_id\":\"my-user-1234\",\"value\":%d}" % minus_plus
        headers = {
            "x-api-key": "04d7aefe-8b4f-4c91-8e58-89ff6861f04a",
            "content-type": "application/json"
        }

        self.conn.request("POST", "/v1/votes", payload, headers)

        res = self.conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    def get_cats_list(self):
        """return list of cats"""
        self.conn.set_tunnel("api.thecatapi.com")
        self.conn.request("GET", "/v1/breeds?attach_breed=0", headers=self.headers)

        res = self.conn.getresponse()
        data = res.read()
        y = data.decode("utf-8")
        return y

    def delete_vote(self, voteId):
        """delete a vote from a cat"""
        self.conn.request("DELETE", "/v1/votes/{}".format(voteId), headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


# x = MethodsForCat().get_cats_list()
# print(x)
# y = MethodsForCat().post_vote(1)
# print("return of post method = {}".format(y))
# d = MethodsForCat().delete_vote(31098)
# print(d)

